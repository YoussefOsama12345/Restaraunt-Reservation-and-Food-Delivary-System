import React, { useState } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';

const ModalOverlay = styled(motion.div)`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
`;

const ModalContent = styled(motion.div)`
  background: #fff;
  direction: ${({ theme }) => theme.direction || 'ltr'};
  width: 92%;
  max-width: 520px;
  max-height: 92vh;
  overflow-y: auto;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  position: relative;
  border-top-left-radius: 1.5rem;
  border-bottom-left-radius: 1.5rem;
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
  transition: border-radius 0.5s ease;

  &::-webkit-scrollbar {
    width: 8px;
    background: transparent;
  }
  &::-webkit-scrollbar-track {
    background: #f3f4f6;
    border-radius: 0 10px 10px 0;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #f97316;
    border-radius: 0 10px 10px 0;
    border: 2px solid #fff;
    transition: background 0.3s ease;
  }
  &:hover::-webkit-scrollbar-thumb {
    background: linear-gradient(to bottom, #ea580c, #facc15);
  }

  scrollbar-width: thin;
  scrollbar-color: #f97316 #f3f4f6;

  ${({ theme }) => theme.direction === 'rtl' && `
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
    &::-webkit-scrollbar-track {
      border-radius: 10px 0 0 10px;
    }
    &::-webkit-scrollbar-thumb {
      border-radius: 10px 0 0 10px;
    }
  `}
`;

const CloseButton = styled.button`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #9ca3af;
  outline: none;
  transition: color 0.3s ease;

  &:hover {
    color: #ef4444;
  }
`;

const Content = styled.div`
  padding: 2rem;
`;

const ImageContainer = styled.div`
  width: 100%;
  height: 240px;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
`;

const Title = styled.h2`
  font-size: 2rem;
  font-weight: 800;
  color: #111827;
  margin-bottom: 0.75rem;
  position: relative;
  display: inline-block;

  &::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 0;
    height: 3px;
    width: 100%;
    background: linear-gradient(to right, #f97316, #ea580c);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s ease;
  }

  &:hover::after {
    transform: scaleX(1);
  }
`;

const Description = styled.p`
  color: #6b7280;
  margin-bottom: 1.25rem;
  font-size: 1rem;
`;

const Price = styled.div`
  font-size: 1.25rem;
  font-weight: 600;
  color: #8B4513;
  margin-bottom: 1rem;
`;

const QuantityControls = styled.div`
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.75rem;
  padding: 0.6rem 1.2rem;
  background: #f3f4f6;
  border-radius: 9999px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
`;

const QuantityButton = styled.button`
  background: #f97316;
  color: #fff;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 9999px;
  font-size: 1.2rem;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  outline: none;

  &:hover {
    background: #ea580c;
    transform: scale(1.05);
  }
  &:active {
    transform: scale(0.95);
  }
`;

const QuantityText = styled.span`
  font-size: 1.25rem;
  font-weight: 700;
  color: #374151;
`;

const AdditionsSection = styled.div` margin-bottom: 2rem; `;
const AdditionsTitle = styled.h3`
  font-size: 1.15rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #1f2937;
`;
const AdditionsGroup = styled.div` margin-bottom: 1.5rem; `;
const GroupLabel = styled.div`
  font-size: 0.95rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
  color: #4b5563;
`;
const AdditionItem = styled(motion.label)`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 1rem;
  border: 2px solid transparent;
  border-radius: 0.6rem;
  background: #f9fafb;
  cursor: pointer;
  margin-bottom: 0.6rem;
  transition: all 0.25s ease;
  outline: none;

  &:hover {
    background: #fff;
    border-color: #f97316;
    transform: scale(1.02);
  }
`;
const CheckboxIcon = styled(motion.div)`
  width: 20px;
  height: 20px;
  border-radius: 6px;
  border: 2px solid ${({ active }) => (active ? '#f97316' : '#d1d5db')};
  background-color: ${({ active }) => (active ? '#f97316' : '#fff')};
  display: flex;
  align-items: center;
  justify-content: center;
`;

const AddToCartButton = styled.button`
  background: linear-gradient(to right, #f97316, #ea580c);
  color: #fff;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.75rem;
  font-weight: 600;
  font-size: 1rem;
  width: 100%;
  cursor: pointer;
  outline: none;
  transition: background 0.3s ease;

  &:hover {
    background: linear-gradient(to right, #ea580c, #facc15);
  }
`;

const AddToCartModal = ({ isOpen, onClose, item, onAddToCart }) => {
  const [quantity, setQuantity] = useState(1);
  const [selectedAdditions, setSelectedAdditions] = useState([]);

  const additions = [
    { id: 1, name: 'Extra Cheese', price: 10 },
    { id: 2, name: 'Spicy Sauce', price: 5 },
    { id: 3, name: 'Garlic Topping', price: 0 },
    { id: 4, name: 'Pickles', price: 0 },
    { id: 5, name: 'Bacon Crumbles', price: 15 },
    { id: 6, name: 'Fried Onions', price: 5 },
    { id: 7, name: 'Mushrooms', price: 7 },
  ];

  const calculateAddonsTotal = () =>
    selectedAdditions.reduce((acc, id) => {
      const addition = additions.find((a) => a.id === id);
      return addition ? acc + addition.price : acc;
    }, 0);

  const totalPrice = (item.price + calculateAddonsTotal()) * quantity;

  const toggleAddition = (addition) => {
    setSelectedAdditions((prev) =>
      prev.includes(addition.id)
        ? prev.filter((id) => id !== addition.id)
        : [...prev, addition.id]
    );
  };

  const handleAddToCart = () => {
    onAddToCart({ ...item, quantity, additions: selectedAdditions, totalPrice });
    onClose();
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <ModalOverlay
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
        >
          <ModalContent
            initial={{ scale: 0.95, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.95, opacity: 0 }}
            onClick={(e) => e.stopPropagation()}
          >
            <CloseButton onClick={onClose}>×</CloseButton>
            <ImageContainer>
              <img src={item.image} alt={item.name} />
            </ImageContainer>
            <Content>
              <Title>{item.name}</Title>
              <Description>{item.description}</Description>
              <Price>EGP {item.price}</Price>

              <QuantityControls>
                <QuantityButton onClick={() => setQuantity(Math.max(1, quantity - 1))}>-</QuantityButton>
                <QuantityText>{quantity}</QuantityText>
                <QuantityButton onClick={() => setQuantity(quantity + 1)}>+</QuantityButton>
              </QuantityControls>

              <AdditionsSection>
                <AdditionsTitle>Customize Your Dish</AdditionsTitle>

                {[0, 1].map((group) => (
                  <AdditionsGroup key={group}>
                    <GroupLabel>{group === 0 ? 'Free Add-ons' : 'Premium Add-ons'}</GroupLabel>
                    {additions
                      .filter((a) => (group === 0 ? a.price === 0 : a.price > 0))
                      .map((addition) => (
                        <AdditionItem
                          key={addition.id}
                          whileHover={{ scale: 1.02 }}
                          onClick={() => toggleAddition(addition)}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                            <CheckboxIcon active={selectedAdditions.includes(addition.id)}>
                              {selectedAdditions.includes(addition.id) && (
                                <motion.svg
                                  width="12"
                                  height="12"
                                  viewBox="0 0 20 20"
                                  fill="none"
                                  initial={{ scale: 0 }}
                                  animate={{ scale: 1 }}
                                  xmlns="http://www.w3.org/2000/svg"
                                >
                                  <path
                                    d="M5 10.5L8.5 14L15 7"
                                    stroke="#fff"
                                    strokeWidth="2"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                  />
                                </motion.svg>
                              )}
                            </CheckboxIcon>
                            <motion.span whileHover={{ color: '#111827' }}>{addition.name}</motion.span>
                          </div>
                          <span className="price-tag">
                            {addition.price > 0 ? `+EGP ${addition.price}` : 'Free'}
                          </span>
                        </AdditionItem>
                      ))}
                  </AdditionsGroup>
                ))}
              </AdditionsSection>

              <AddToCartButton onClick={handleAddToCart}>
                Add to Cart – EGP {totalPrice}
              </AddToCartButton>
            </Content>
          </ModalContent>
        </ModalOverlay>
      )}
    </AnimatePresence>
  );
};

export default AddToCartModal;
