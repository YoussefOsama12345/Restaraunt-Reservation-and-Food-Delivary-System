"""
Database utility functions to handle async/sync context issues in SQLAlchemy operations.
"""

import functools
from typing import Any, Callable, TypeVar, cast
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

T = TypeVar('T')

def handle_missing_greenlet(async_func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator to handle MissingGreenlet errors in async SQLAlchemy operations.
    If an async operation fails with a MissingGreenlet error, it will fall back to
    a synchronous implementation.
    
    Usage:
        @handle_missing_greenlet
        async def my_async_db_function(db, ...):
            # Your async implementation
            
        # The decorator will automatically create a sync fallback
    """
    @functools.wraps(async_func)
    async def wrapper(*args, **kwargs):
        try:
            return await async_func(*args, **kwargs)
        except Exception as e:
            error_str = str(e)
            if "MissingGreenlet" in error_str or "greenlet_spawn has not been called" in error_str:
                print(f"Warning: Falling back to sync implementation due to: {error_str}")
                
                # Extract parameters
                db = None
                order_id = None
                user_id = None
                item_id = None
                
                # Extract db from args or kwargs
                if args and isinstance(args[0], AsyncSession):
                    db = args[0]
                    args = args[1:]
                elif 'db' in kwargs and isinstance(kwargs['db'], AsyncSession):
                    db = kwargs.pop('db')
                
                # Extract other common parameters
                if 'order_id' in kwargs:
                    order_id = kwargs['order_id']
                elif len(args) > 0 and async_func.__name__ in ['list_order_items', 'add_order_item']:
                    order_id = args[0]
                    args = args[1:]
                
                if 'user_id' in kwargs:
                    user_id = kwargs['user_id']
                elif len(args) > 0 and 'user_id' in str(async_func.__annotations__):
                    user_id = args[0]
                    args = args[1:]
                
                if 'item_id' in kwargs:
                    item_id = kwargs['item_id']
                elif len(args) > 0 and async_func.__name__ in ['get_order_item', 'update_order_item', 'delete_order_item']:
                    item_id = args[0]
                    args = args[1:]
                
                # Create a synchronous session
                sync_db = SessionLocal()
                try:
                    # Try to find a sync implementation with the same name pattern
                    module_name = async_func.__module__
                    func_name = async_func.__name__
                    
                    # First, try to find a module-specific sync implementation
                    try:
                        # Try to import the _sync version of the module
                        sync_module_name = module_name.replace('service', 'service_sync')
                        import importlib
                        sync_module = importlib.import_module(sync_module_name)
                        sync_func_name = f"{func_name}_sync" if not func_name.endswith('_sync') else func_name
                        
                        if hasattr(sync_module, sync_func_name):
                            sync_func = getattr(sync_module, sync_func_name)
                            
                            # Determine which parameters to pass based on function name
                            if func_name == 'list_order_items':
                                return sync_func(order_id, user_id)
                            elif func_name == 'get_order_item':
                                return sync_func(item_id, user_id)
                            elif func_name == 'get_order':
                                return sync_func(order_id, user_id)
                            else:
                                # For other functions, pass all extracted parameters
                                params = {}
                                if order_id is not None:
                                    params['order_id'] = order_id
                                if user_id is not None:
                                    params['user_id'] = user_id
                                if item_id is not None:
                                    params['item_id'] = item_id
                                
                                # Add any remaining kwargs
                                params.update(kwargs)
                                
                                return sync_func(**params)
                    except (ImportError, AttributeError) as import_error:
                        print(f"Could not import sync implementation: {import_error}")
                    
                    # If we get here, try to find a function in the same module with _sync suffix
                    try:
                        import importlib
                        module = importlib.import_module(module_name)
                        sync_func_name = f"{func_name}_sync"
                        
                        if hasattr(module, sync_func_name):
                            sync_func = getattr(module, sync_func_name)
                            
                            # Call with appropriate parameters based on function name
                            if func_name == 'list_order_items':
                                return sync_func(order_id, user_id)
                            elif func_name in ['get_order_item', 'get_order']:
                                return sync_func(item_id or order_id, user_id)
                            else:
                                # Pass all parameters
                                return sync_func(sync_db, *args, **kwargs)
                    except (ImportError, AttributeError) as import_error:
                        print(f"Could not find sync implementation in same module: {import_error}")
                    
                    # If no specific sync implementation exists, use a generic implementation
                    return generic_sync_implementation(sync_db, async_func, order_id, user_id, item_id, *args, **kwargs)
                finally:
                    sync_db.close()
            # Re-raise the original exception if it's not a MissingGreenlet error
            raise
    return wrapper

def generic_sync_implementation(sync_db: Session, async_func: Callable, order_id: int = None, user_id: int = None, item_id: int = None, *args, **kwargs) -> Any:
    """
    Generic synchronous implementation for async database functions.
    This is used when a specific sync implementation is not available.
    
    The implementation handles common patterns for order and order item operations.
    """
    import inspect
    from sqlalchemy import select as sync_select
    from sqlalchemy.ext.asyncio import AsyncSession
    
    # Get the function name to determine what kind of operation we're doing
    func_name = async_func.__name__
    
    # Handle common order and order item operations
    if func_name == 'list_order_items' and order_id is not None and user_id is not None:
        from app.db.models.order_item import OrderItem
        from app.db.models.order import Order
        
        # First verify the order exists and belongs to the user
        order = sync_db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
        if not order:
            from fastapi import HTTPException, status
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or unauthorized")
        
        # Then get the order items
        items = sync_db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
        
        # Convert to dictionary format
        return [{c.name: getattr(item, c.name) for c in OrderItem.__table__.columns} 
                for item in items]
    
    elif func_name == 'get_order' and order_id is not None and user_id is not None:
        from app.db.models.order import Order
        from app.db.models.order_item import OrderItem
        
        # Get the order
        order = sync_db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
        if not order:
            from fastapi import HTTPException, status
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or unauthorized")
        
        # Convert order to dictionary
        order_dict = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
        
        # Add payment_method if present
        if hasattr(order, 'payment_method') and order.payment_method is not None:
            order_dict['payment_method'] = order.payment_method
        else:
            order_dict['payment_method'] = 'unknown'
        
        # Get order items separately
        items = sync_db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
        
        # Add items to the order dictionary
        order_dict['items'] = [
            {c.name: getattr(item, c.name) for c in OrderItem.__table__.columns}
            for item in items
        ]
        
        return order_dict
    
    elif func_name == 'get_order_item' and item_id is not None and user_id is not None:
        from app.db.models.order_item import OrderItem
        from app.db.models.order import Order
        
        # Get the order item
        order_item = sync_db.query(OrderItem).join(Order).filter(
            OrderItem.id == item_id, Order.user_id == user_id
        ).first()
        
        if not order_item:
            from fastapi import HTTPException, status
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found or unauthorized")
        
        # Convert to dictionary
        return {c.name: getattr(order_item, c.name) for c in OrderItem.__table__.columns}
    
    # If we couldn't determine a specific implementation, try a more generic approach
    # Get the source code of the async function to analyze its structure
    try:
        source = inspect.getsource(async_func)
        
        # Look for common patterns in the source code
        if "OrderItem" in source and "select(" in source and ".where(" in source:
            from app.db.models.order_item import OrderItem
            from app.db.models.order import Order
            
            # Try to build a query based on available parameters
            if order_id is not None:
                items = sync_db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
                return [{c.name: getattr(item, c.name) for c in OrderItem.__table__.columns} for item in items]
            elif item_id is not None:
                item = sync_db.query(OrderItem).filter(OrderItem.id == item_id).first()
                if item:
                    return {c.name: getattr(item, c.name) for c in OrderItem.__table__.columns}
    except Exception as e:
        print(f"Error in generic implementation analysis: {e}")
    
    # If we couldn't determine a specific implementation, raise an error
    raise NotImplementedError(
        f"No synchronous implementation available for {async_func.__name__}. "
        f"Please create a {async_func.__name__}_sync function."
    )
