import React from 'react';
import styled from 'styled-components';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

const CartContainer = styled.div`
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
`;

const Title = styled.h1`
  color: #8B4513;
  margin-bottom: 2rem;
  text-align: center;
`;

const CartItems = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const CartItem = styled.div`
  display: flex;
  align-items: center;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  gap: 1rem;
`;

const ItemImage = styled.img`
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
`;

const ItemDetails = styled.div`
  flex: 1;
`;

const ItemName = styled.h3`
  color: #8B4513;
  margin-bottom: 0.5rem;
`;

const ItemPrice = styled.p`
  color: #666;
  font-weight: bold;
`;

const QuantityControl = styled.div`
  display: flex;
  align-items: center;
  gap: 1rem;
`;

const QuantityButton = styled.button`
  background: #8B4513;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-weight: bold;

  &:hover {
    background: #6B3410;
  }

  &:disabled {
    background: #ccc;
    cursor: not-allowed;
  }
`;

const RemoveButton = styled.button`
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;

  &:hover {
    background: #c0392b;
  }
`;

const EmptyCart = styled.div`
  text-align: center;
  padding: 3rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const CartSummary = styled.div`
  margin-top: 2rem;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Total = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-top: 1px solid #eee;
  font-size: 1.2rem;
  font-weight: bold;
`;

const CheckoutButton = styled(Link)`
  display: block;
  width: 100%;
  padding: 1rem;
  background: #8B4513;
  color: white;
  text-align: center;
  text-decoration: none;
  border-radius: 4px;
  margin-top: 1rem;
  font-weight: bold;
  transition: background 0.3s ease;

  &:hover {
    background: #6B3410;
  }
`;

const ContinueShopping = styled(Link)`
  display: inline-block;
  margin-top: 1rem;
  color: #8B4513;
  text-decoration: none;
  font-weight: 500;

  &:hover {
    text-decoration: underline;
  }
`;

function Cart() {
  const { cartItems, removeFromCart, updateQuantity } = useCart();

  const calculateTotal = () => {
    return cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
  };

  if (!cartItems || cartItems.length === 0) {
    return (
      <CartContainer>
        <Title>Your Cart</Title>
        <EmptyCart>
          <h2>Your cart is empty</h2>
          <p>Looks like you haven't added anything to your cart yet.</p>
          <ContinueShopping to="/menu">Continue Shopping</ContinueShopping>
        </EmptyCart>
      </CartContainer>
    );
  }

  return (
    <CartContainer>
      <Title>Your Cart</Title>
      <CartItems>
        {cartItems.map(item => (
          <CartItem key={item.id}>
            <ItemImage src={item.image} alt={item.name} />
            <ItemDetails>
              <ItemName>{item.name}</ItemName>
              <ItemPrice>${(item.price * item.quantity).toFixed(2)}</ItemPrice>
            </ItemDetails>
            <QuantityControl>
              <QuantityButton
                onClick={() => updateQuantity(item.id, item.quantity - 1)}
                disabled={item.quantity <= 1}
              >
                -
              </QuantityButton>
              <span>{item.quantity}</span>
              <QuantityButton
                onClick={() => updateQuantity(item.id, item.quantity + 1)}
              >
                +
              </QuantityButton>
            </QuantityControl>
            <RemoveButton onClick={() => removeFromCart(item.id)}>
              Remove
            </RemoveButton>
          </CartItem>
        ))}
      </CartItems>

      <CartSummary>
        <Total>
          <span>Total:</span>
          <span>${calculateTotal().toFixed(2)}</span>
        </Total>
        <CheckoutButton to="/checkout">Proceed to Checkout</CheckoutButton>
      </CartSummary>

      <div style={{ textAlign: 'center', marginTop: '2rem' }}>
        <ContinueShopping to="/menu">
          ← Continue Shopping
        </ContinueShopping>
      </div>
    </CartContainer>
  );
}

export default Cart; 