import React, { createContext, useContext, useState } from 'react';

// Create Context
const CartContext = createContext();

// Provider
export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);
  const [isCartOpen, setIsCartOpen] = useState(false);

  // Add item to cart
  const addToCart = (item) => {
    setCartItems((prev) => {
      const exists = prev.find((x) => x.id === item.id);
      return exists
        ? prev.map((x) =>
            x.id === item.id ? { ...x, quantity: x.quantity + 1 } : x
          )
        : [...prev, { ...item, quantity: 1 }];
    });
  };

  // Remove item from cart
  const removeFromCart = (id) =>
    setCartItems((prev) => prev.filter((item) => item.id !== id));

  // Increase item quantity
  const increaseQuantity = (id) =>
    setCartItems((prev) =>
      prev.map((item) =>
        item.id === id ? { ...item, quantity: item.quantity + 1 } : item
      )
    );

  // Decrease item quantity
  const decreaseQuantity = (id) =>
    setCartItems((prev) =>
      prev.map((item) =>
        item.id === id
          ? { ...item, quantity: Math.max(item.quantity - 1, 1) }
          : item
      )
    );

  // Clear cart
  const clearCart = () => setCartItems([]);

  // Toggle cart visibility
  const openCart = () => setIsCartOpen(true);
  const closeCart = () => setIsCartOpen(false);

  return (
    <CartContext.Provider
      value={{
        cartItems,
        addToCart,
        removeFromCart,
        increaseQuantity,
        decreaseQuantity,
        clearCart,
        openCart,
        closeCart,
        isCartOpen,
        cartCount: cartItems.reduce((acc, item) => acc + item.quantity, 0), // 🆕 total count
        cartTotal: cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0), // 🆕 total price
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

// Custom hook
export const useCart = () => useContext(CartContext);
