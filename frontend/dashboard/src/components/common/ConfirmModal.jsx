import React from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { AlertTriangle } from 'lucide-react';

const Overlay = styled(motion.div)`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
`;

const ModalContent = styled(motion.div)`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  position: relative;
  border: 1px solid #374151;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
`;

const Title = styled.h2`
  color: #f9fafb;
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
`;

const Message = styled.p`
  color: #d1d5db;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
`;

const ButtonGroup = styled.div`
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
`;

const Button = styled.button`
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    transform: translateY(-1px);
  }

  &:active {
    transform: translateY(0);
  }
`;

const CancelButton = styled(Button)`
  background-color: #374151;
  color: #f9fafb;
  border: 1px solid #4b5563;

  &:hover {
    background-color: #4b5563;
  }
`;

const ConfirmButton = styled(Button)`
  background-color: #ef4444;
  color: white;
  border: none;

  &:hover {
    background-color: #dc2626;
  }
`;

const ConfirmModal = ({ isOpen, onClose, onConfirm, title, message }) => {
  if (!isOpen) return null;

  return (
    <Overlay
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      onClick={onClose}
    >
      <ModalContent
        initial={{ scale: 0.95, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.95, opacity: 0 }}
        onClick={e => e.stopPropagation()}
      >
        <Title>
          <AlertTriangle size={20} color="#ef4444" />
          {title}
        </Title>
        <Message>{message}</Message>
        <ButtonGroup>
          <CancelButton onClick={onClose}>
            Cancel
          </CancelButton>
          <ConfirmButton onClick={onConfirm}>
            Delete
          </ConfirmButton>
        </ButtonGroup>
      </ModalContent>
    </Overlay>
  );
};

export default ConfirmModal; 