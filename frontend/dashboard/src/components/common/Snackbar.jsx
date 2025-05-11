import React, { useEffect } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { CheckCircle2 } from 'lucide-react';

const SnackbarContainer = styled(motion.div)`
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background-color: #10B981;
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  z-index: 1000;
`;

const Message = styled.span`
  font-size: 0.875rem;
  font-weight: 500;
`;

const Snackbar = ({ message, isVisible, onClose }) => {
  useEffect(() => {
    if (isVisible) {
      const timer = setTimeout(() => {
        onClose();
      }, 3000);

      return () => clearTimeout(timer);
    }
  }, [isVisible, onClose]);

  return (
    <AnimatePresence>
      {isVisible && (
        <SnackbarContainer
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 50 }}
          transition={{ duration: 0.2 }}
        >
          <CheckCircle2 size={20} />
          <Message>{message}</Message>
        </SnackbarContainer>
      )}
    </AnimatePresence>
  );
};

export default Snackbar; 