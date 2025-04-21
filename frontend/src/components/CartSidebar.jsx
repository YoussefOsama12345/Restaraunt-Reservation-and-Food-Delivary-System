// Enhanced CartSidebar with styled controls and clean image previews
import styled, { keyframes } from 'styled-components';
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Minus, Plus } from 'lucide-react';

// Animations
const slideIn = keyframes`
  from { transform: translateX(100%) scale(0.98); }
  to { transform: translateX(0) scale(1); }
`;
const slideOut = keyframes`
  from { transform: translateX(0) scale(1); }
  to { transform: translateX(100%) scale(0.98); }
`;
const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;
const fadeOut = keyframes`
  from { opacity: 1; }
  to { opacity: 0; }
`;

// Styled Components
const Overlay = styled.div`
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(2px);
  animation: ${props => props.isClosing ? fadeOut : fadeIn} 0.3s ease;
  z-index: 1000;
`;

const SidebarContainer = styled.div`
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
  max-width: 420px;
  height: 100vh;
  background: linear-gradient(to bottom right, #ffffff, #fff8f1);
  z-index: 1001;
  box-shadow: -8px 0 20px rgba(0, 0, 0, 0.08);
  animation: ${props => props.isClosing ? slideOut : slideIn} 0.35s ease;
  border-top-left-radius: 2rem;
  border-bottom-left-radius: 2rem;
  display: flex;
  flex-direction: column;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.6rem 2rem;
  background: linear-gradient(to right, #fff8f1, #ffffff);
  border-bottom: 1px solid #f3f4f6;
`;

const Title = styled.h2`
  font-size: 1.6rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
`;

const CloseButton = styled.button`
  background: none;
  border: none;
  color: #9ca3af;
  border-radius: 50%;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  transition: all 0.2s ease;

  &:hover {
    background-color: #fef3c7;
    color: #f97316;
    transform: scale(1.1);
  }

  svg {
    width: 1.6rem;
    height: 1.6rem;
  }
`;

const CartContent = styled.div`
  flex: 1;
  padding: 2rem;
  background-color: #fff;
  overflow-y: auto;

  &::-webkit-scrollbar {
    width: 6px;
  }
  &::-webkit-scrollbar-thumb {
    background: #f97316;
    border-radius: 4px;
  }
`;

const CartItem = styled(motion.div)`
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 0;
  border-bottom: 1px solid #f3f4f6;
`;

const ItemImage = styled.img`
  width: 64px;
  height: 64px;
  object-fit: cover;
  border-radius: 14px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.05);
  }
`;

const ItemDetails = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;

  h4 {
    font-size: 1rem;
    margin: 0;
    color: #111827;
  }

  span {
    font-size: 0.9rem;
    color: #6b7280;
  }
`;

const QuantityControlWrapper = styled.div`
  display: flex;
  gap: 0.8rem;
  align-items: center;

  button {
    width: 44px;
    height: 44px;
    background: linear-gradient(to bottom right, #f97316, #fb923c);
    color: #fff;
    border: none;
    border-radius: 50%;
    font-size: 1.3rem;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 6px 14px rgba(249, 115, 22, 0.3);
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    justify-content: center;

    svg {
      width: 20px;
      height: 20px;
      stroke-width: 2.5;
    }

    &:hover {
      background: linear-gradient(to bottom right, #ea580c, #facc15);
      transform: scale(1.07);
      box-shadow: 0 8px 20px rgba(234, 88, 12, 0.3);
    }

    &:active {
      transform: scale(0.95);
      box-shadow: 0 4px 10px rgba(234, 88, 12, 0.2);
    }
  }

  span {
    font-size: 1.2rem;
    font-weight: 600;
    min-width: 36px;
    text-align: center;
    color: #1f2937;
  }
`;

const RemoveButton = styled.button`
  background: none;
  border: none;
  color: #ef4444;
  font-size: 1.2rem;
  cursor: pointer;
  margin-left: 0.3rem;

  &:hover {
    transform: scale(1.15);
  }
`;

const EmptyCart = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #6b7280;
  padding: 3rem 1rem;
  gap: 1.25rem;

  svg {
    width: 4.5rem;
    height: 4.5rem;
    color: #f97316;
  }

  p {
    font-size: 1.1rem;
    font-weight: 500;
  }
`;

const TotalRow = styled.div`
  display: flex;
  justify-content: space-between;
  font-size: 1.1rem;
  font-weight: 600;
  margin-top: 1rem;
`;

const Footer = styled.div`
  padding: 1.75rem 2rem;
  background: linear-gradient(to top, #fff8f1, #ffffff);
  border-top: 1px solid #f3f4f6;
  box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.04);
`;

const CheckoutButton = styled.button`
  width: 100%;
  padding: 1rem;
  background: linear-gradient(to right, #f97316, #ea580c);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 14px rgba(249, 115, 22, 0.2);

  &:hover {
    background: linear-gradient(to right, #ea580c, #facc15);
    transform: translateY(-1px);
  }

  &:disabled {
    background: #d1d5db;
    color: #fff;
    cursor: not-allowed;
  }
`;

const QuantityControl = ({ quantity, onIncrease, onDecrease }) => (
  <QuantityControlWrapper>
    <button onClick={onDecrease}><Minus /></button>
    <span>{quantity}</span>
    <button onClick={onIncrease}><Plus /></button>
  </QuantityControlWrapper>
);

const CartSidebar = ({ isOpen, onClose }) => {
  const [cart, setCart] = useState([
    { id: 1, name: 'Cheeseburger', price: 50, quantity: 1, image: 'https://i.imgur.com/5Aqgz7o.jpg' },
    { id: 2, name: 'Fries', price: 25, quantity: 2, image: 'https://i.imgur.com/e3tK00z.jpg' },
  ]);
  const [isClosing, setIsClosing] = useState(false);

  const updateQuantity = (id, change) => {
    setCart(cart =>
      cart.map(item =>
        item.id === id ? { ...item, quantity: Math.max(1, item.quantity + change) } : item
      )
    );
  };

  const total = cart.reduce((sum, item) => sum + item.quantity * item.price, 0);

  const handleClose = () => {
    setIsClosing(true);
    setTimeout(() => {
      setIsClosing(false);
      onClose();
    }, 300);
  };

  if (!isOpen && !isClosing) return null;

  return (
    <>
      <Overlay isClosing={isClosing} onClick={handleClose} />
      <SidebarContainer isClosing={isClosing}>
        <Header>
          <Title>Your Cart</Title>
          <CloseButton onClick={handleClose}>
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </CloseButton>
        </Header>

        <CartContent>
          {cart.length === 0 ? (
            <EmptyCart>
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.3 2.3c-.6.6-.2 1.7.7 1.7H17m0 0a2 2 0 100 4 2 2 0 000-4m-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              <p>Your cart is empty</p>
            </EmptyCart>
          ) : (
            <AnimatePresence>
              {cart.map(item => (
                <CartItem
                  key={item.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: 20 }}
                  transition={{ duration: 0.25 }}
                >
                  <ItemImage src={item.image} alt={item.name} />
                  <ItemDetails>
                    <h4>{item.name}</h4>
                    <span>EGP {item.price}</span>
                  </ItemDetails>
                  <QuantityControl
                    quantity={item.quantity}
                    onIncrease={() => updateQuantity(item.id, 1)}
                    onDecrease={() => updateQuantity(item.id, -1)}
                  />
                </CartItem>
              ))}
              <TotalRow>
                <span>Total:</span>
                <span>EGP {total}</span>
              </TotalRow>
            </AnimatePresence>
          )}
        </CartContent>

        <Footer>
          <CheckoutButton disabled={cart.length === 0}>
            Proceed to Checkout
          </CheckoutButton>
        </Footer>
      </SidebarContainer>
    </>
  );
};

export default CartSidebar;
