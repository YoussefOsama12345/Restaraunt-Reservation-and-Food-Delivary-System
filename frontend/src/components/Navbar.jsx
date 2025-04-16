import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import CartIcon from './CartIcon';

const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: white;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
`;

const Logo = styled(Link)`
  color: #ff6b6b;
  text-decoration: none;
  font-size: 1.8rem;
  font-weight: bold;
  display: flex;
  align-items: center;
  
  span {
    color: #ff6b6b;
  }
`;

const NavLinks = styled.div`
  display: flex;
  gap: 2rem;
  align-items: center;
`;

const NavLink = styled(Link)`
  color: #333;
  text-decoration: none;
  font-weight: 500;
  position: relative;
  padding: 0.5rem;
  
  &:after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: #ff6b6b;
    transition: width 0.3s ease;
  }
  
  &:hover:after {
    width: 100%;
  }
  
  &.active {
    color: #ff6b6b;
    
    &:after {
      width: 100%;
    }
  }
`;

const RightSection = styled.div`
  display: flex;
  align-items: center;
  gap: 1.5rem;
`;

const CartButton = styled(Link)`
  position: relative;
  padding: 0.5rem;
  color: #ff6b6b;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  
  .cart-count {
    position: absolute;
    top: -5px;
    right: -5px;
    background-color: #ff6b6b;
    color: white;
    font-size: 0.8rem;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  svg {
    width: 24px;
    height: 24px;
  }
`;

const LoginButton = styled(Link)`
  padding: 0.8rem 1.5rem;
  background-color: #ff6b6b;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  
  &:hover {
    background-color: #ff5252;
    transform: translateY(-2px);
  }
  
  svg {
    width: 16px;
    height: 16px;
  }
`;

function Navbar() {
  return (
    <Nav>
      <Logo to="/">
        F<span>oodi</span>
      </Logo>
      <NavLinks>
        <NavLink to="/" className="active">Home</NavLink>
        <NavLink to="/menu">Menu</NavLink>
        <NavLink to="/delivery">Delivery</NavLink>
        <NavLink to="/reservation">Reservation</NavLink>
      </NavLinks>
      <RightSection>
        <CartButton to="/cart">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z" />
            <path d="M3 6h18" />
            <path d="M16 10a4 4 0 01-8 0" />
          </svg>
          <span className="cart-count">0</span>
        </CartButton>
        <LoginButton to="/login">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M13.8 12H3" />
          </svg>
          Login
        </LoginButton>
      </RightSection>
    </Nav>
  );
}

export default Navbar; 