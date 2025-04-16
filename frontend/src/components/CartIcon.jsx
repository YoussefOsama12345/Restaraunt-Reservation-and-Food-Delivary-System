import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { useCart } from '../context/CartContext';

const CartContainer = styled(Link)`
  position: relative;
  display: flex;
  align-items: center;
  color: #ff6b6b;
  text-decoration: none;
  font-size: 1.5rem;
  padding: 0.5rem;
  transition: transform 0.2s ease;

  &:hover {
    transform: scale(1.1);
  }
`;

const CartCount = styled.span`
  position: absolute;
  top: -5px;
  right: -5px;
  background-color: #4CAF50;
  color: white;
  border-radius: 50%;
  padding: 0.2rem 0.5rem;
  font-size: 0.8rem;
  font-weight: bold;
  min-width: 20px;
  text-align: center;
`;

function CartIcon() {
  const { cartItems } = useCart();
  const itemCount = cartItems ? cartItems.length : 0;

  return (
    <CartContainer to="/cart">
      <i className="fas fa-shopping-cart"></i>
      {itemCount > 0 && <CartCount>{itemCount}</CartCount>}
    </CartContainer>
  );
}

export default CartIcon; 