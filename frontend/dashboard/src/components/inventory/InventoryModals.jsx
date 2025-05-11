import React from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { X, CheckCircle2, AlertTriangle, Trash2 } from 'lucide-react';

const ModalOverlay = styled(motion.div)`
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
  max-width: 500px;
  position: relative;
  border: 1px solid #374151;
`;

const CloseButton = styled.button`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.375rem;
  transition: all 0.2s;

  &:hover {
    color: #e5e7eb;
    background-color: #374151;
  }
`;

const Title = styled.h2`
  color: #f9fafb;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  color: #e5e7eb;
  font-size: 0.875rem;
`;

const Input = styled.input`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;

  &:focus {
    outline: none;
    border-color: #60a5fa;
  }

  &::placeholder {
    color: #9ca3af;
  }
`;

const Select = styled.select`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;

  &:focus {
    outline: none;
    border-color: #60a5fa;
  }
`;

const SubmitButton = styled.button`
  padding: 0.75rem;
  background-color: #60a5fa;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 1rem;

  &:hover {
    background-color: #3b82f6;
  }

  &:disabled {
    background-color: #374151;
    cursor: not-allowed;
  }
`;

const ErrorMessage = styled.span`
  color: #ef4444;
  font-size: 0.75rem;
  margin-top: 0.25rem;
`;

const SuccessModalOverlay = styled(motion.div)`
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

const SuccessModalContent = styled(motion.div)`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  position: relative;
  border: 1px solid #374151;
  text-align: center;
`;

const SuccessIcon = styled(CheckCircle2)`
  color: #10b981;
  width: 48px;
  height: 48px;
  margin-bottom: 1rem;
`;

const SuccessTitle = styled.h2`
  color: #f9fafb;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
`;

const SuccessMessage = styled.p`
  color: #9ca3af;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
`;

const SuccessButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #059669;
  }
`;

const DeleteModalOverlay = styled(motion.div)`
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

const DeleteModalContent = styled(motion.div)`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  position: relative;
  border: 1px solid #374151;
  text-align: center;
`;

const WarningIcon = styled(AlertTriangle)`
  color: #f87171;
  width: 48px;
  height: 48px;
  margin-bottom: 1rem;
`;

const DeleteTitle = styled.h2`
  color: #f9fafb;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
`;

const DeleteMessage = styled.p`
  color: #9ca3af;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: 1rem;
  justify-content: center;
`;

const CancelButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #374151;
  color: #e5e7eb;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #4b5563;
  }
`;

const DeleteButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #ef4444;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #dc2626;
  }
`;

const DeleteSuccessModalOverlay = styled(motion.div)`
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

const DeleteSuccessModalContent = styled(motion.div)`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  position: relative;
  border: 1px solid #374151;
  text-align: center;
`;

const DeleteSuccessIcon = styled(Trash2)`
  color: #10b981;
  width: 48px;
  height: 48px;
  margin-bottom: 1rem;
`;

const DeleteSuccessTitle = styled.h2`
  color: #f9fafb;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
`;

const DeleteSuccessMessage = styled.p`
  color: #9ca3af;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
`;

const DeleteSuccessButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #059669;
  }
`;

const ModifySuccessModalOverlay = styled(motion.div)`
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

const ModifySuccessModalContent = styled(motion.div)`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  position: relative;
  border: 1px solid #374151;
  text-align: center;
`;

const ModifySuccessIcon = styled(CheckCircle2)`
  color: #10b981;
  width: 48px;
  height: 48px;
  margin-bottom: 1rem;
`;

const ModifySuccessTitle = styled.h2`
  color: #f9fafb;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
`;

const ModifySuccessMessage = styled.p`
  color: #9ca3af;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
`;

const ModifySuccessButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #059669;
  }
`;

const SnackbarContainer = styled(motion.div)`
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background-color: #10b981;
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  z-index: 1000;
`;

const SnackbarIcon = styled(CheckCircle2)`
  width: 20px;
  height: 20px;
  flex-shrink: 0;
`;

const SnackbarMessage = styled.p`
  margin: 0;
  font-size: 0.875rem;
  font-weight: 500;
`;

const SnackbarCloseButton = styled.button`
  background: none;
  border: none;
  color: white;
  padding: 0.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.5rem;
  opacity: 0.8;
  transition: opacity 0.2s;

  &:hover {
    opacity: 1;
  }
`;

const AddItemModal = ({ isOpen, onClose, onSubmit, formData, setFormData, errors }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(e);
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
            onClick={e => e.stopPropagation()}
          >
            <CloseButton onClick={onClose}>
              <X size={20} />
            </CloseButton>
            <Title>Add New Item</Title>
            <Form onSubmit={handleSubmit}>
              <FormGroup>
                <Label htmlFor="name">Item Name</Label>
                <Input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Enter item name"
                />
                {errors.name && <ErrorMessage>{errors.name}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="itemId">Item ID</Label>
                <Input
                  type="text"
                  id="itemId"
                  name="itemId"
                  value={formData.itemId}
                  onChange={handleChange}
                  placeholder="Enter item ID"
                />
                {errors.itemId && <ErrorMessage>{errors.itemId}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="category">Category</Label>
                <Select
                  id="category"
                  name="category"
                  value={formData.category}
                  onChange={handleChange}
                >
                  <option value="">Select a category</option>
                  <option value="Baked">Baked</option>
                  <option value="Pasta">Pasta</option>
                  <option value="Meat">Meat</option>
                  <option value="Vegetables">Vegetables</option>
                  <option value="Dairy">Dairy</option>
                </Select>
                {errors.category && <ErrorMessage>{errors.category}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="cost">Cost (per unit)</Label>
                <Input
                  type="number"
                  id="cost"
                  name="cost"
                  value={formData.cost}
                  onChange={handleChange}
                  placeholder="Enter cost"
                  step="0.01"
                  min="0"
                />
                {errors.cost && <ErrorMessage>{errors.cost}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="quantity">Quantity</Label>
                <Input
                  type="number"
                  id="quantity"
                  name="quantity"
                  value={formData.quantity}
                  onChange={handleChange}
                  placeholder="Enter quantity"
                  min="0"
                />
                {errors.quantity && <ErrorMessage>{errors.quantity}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="expireDate">Expire Date</Label>
                <Input
                  type="date"
                  id="expireDate"
                  name="expireDate"
                  value={formData.expireDate}
                  onChange={handleChange}
                />
                {errors.expireDate && <ErrorMessage>{errors.expireDate}</ErrorMessage>}
              </FormGroup>

              <SubmitButton type="submit">Add Item</SubmitButton>
            </Form>
          </ModalContent>
        </ModalOverlay>
      )}
    </AnimatePresence>
  );
};

const SuccessModal = ({ isOpen, onClose }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <SuccessModalOverlay
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
        >
          <SuccessModalContent
            initial={{ scale: 0.95, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.95, opacity: 0 }}
            onClick={e => e.stopPropagation()}
          >
            <SuccessIcon />
            <SuccessTitle>Item Added Successfully</SuccessTitle>
            <SuccessMessage>The new item has been added to your inventory.</SuccessMessage>
            <SuccessButton onClick={onClose}>Close</SuccessButton>
          </SuccessModalContent>
        </SuccessModalOverlay>
      )}
    </AnimatePresence>
  );
};

const DeleteConfirmationModal = ({ isOpen, onClose, onConfirm, itemName }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <DeleteModalOverlay
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
        >
          <DeleteModalContent
            initial={{ scale: 0.95, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.95, opacity: 0 }}
            onClick={e => e.stopPropagation()}
          >
            <WarningIcon />
            <DeleteTitle>Delete Item</DeleteTitle>
            <DeleteMessage>
              Are you sure you want to delete "{itemName}"? This action cannot be undone.
            </DeleteMessage>
            <ButtonGroup>
              <CancelButton onClick={onClose}>Cancel</CancelButton>
              <DeleteButton onClick={onConfirm}>Delete</DeleteButton>
            </ButtonGroup>
          </DeleteModalContent>
        </DeleteModalOverlay>
      )}
    </AnimatePresence>
  );
};

const EditItemModal = ({ isOpen, onClose, onSubmit, formData, setFormData, errors }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(e);
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
            onClick={e => e.stopPropagation()}
          >
            <CloseButton onClick={onClose}>
              <X size={20} />
            </CloseButton>
            <Title>Edit Item</Title>
            <Form onSubmit={handleSubmit}>
              <FormGroup>
                <Label htmlFor="name">Item Name</Label>
                <Input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Enter item name"
                />
                {errors.name && <ErrorMessage>{errors.name}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="itemId">Item ID</Label>
                <Input
                  type="text"
                  id="itemId"
                  name="itemId"
                  value={formData.itemId}
                  onChange={handleChange}
                  placeholder="Enter item ID"
                  disabled
                />
                {errors.itemId && <ErrorMessage>{errors.itemId}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="category">Category</Label>
                <Select
                  id="category"
                  name="category"
                  value={formData.category}
                  onChange={handleChange}
                >
                  <option value="">Select a category</option>
                  <option value="Baked">Baked</option>
                  <option value="Pasta">Pasta</option>
                  <option value="Meat">Meat</option>
                  <option value="Vegetables">Vegetables</option>
                  <option value="Dairy">Dairy</option>
                </Select>
                {errors.category && <ErrorMessage>{errors.category}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="cost">Cost (per unit)</Label>
                <Input
                  type="number"
                  id="cost"
                  name="cost"
                  value={formData.cost}
                  onChange={handleChange}
                  placeholder="Enter cost"
                  step="0.01"
                  min="0"
                />
                {errors.cost && <ErrorMessage>{errors.cost}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="quantity">Quantity</Label>
                <Input
                  type="number"
                  id="quantity"
                  name="quantity"
                  value={formData.quantity}
                  onChange={handleChange}
                  placeholder="Enter quantity"
                  min="0"
                />
                {errors.quantity && <ErrorMessage>{errors.quantity}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label htmlFor="expireDate">Expire Date</Label>
                <Input
                  type="date"
                  id="expireDate"
                  name="expireDate"
                  value={formData.expireDate}
                  onChange={handleChange}
                />
                {errors.expireDate && <ErrorMessage>{errors.expireDate}</ErrorMessage>}
              </FormGroup>

              <SubmitButton type="submit">Save Changes</SubmitButton>
            </Form>
          </ModalContent>
        </ModalOverlay>
      )}
    </AnimatePresence>
  );
};

const ModifySuccessModal = ({ isOpen, onClose, itemName }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <ModifySuccessModalOverlay
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
        >
          <ModifySuccessModalContent
            initial={{ scale: 0.95, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.95, opacity: 0 }}
            onClick={e => e.stopPropagation()}
          >
            <ModifySuccessIcon />
            <ModifySuccessTitle>Item Modified Successfully</ModifySuccessTitle>
            <ModifySuccessMessage>
              "{itemName}" has been updated in your inventory.
            </ModifySuccessMessage>
            <ModifySuccessButton onClick={onClose}>Close</ModifySuccessButton>
          </ModifySuccessModalContent>
        </ModifySuccessModalOverlay>
      )}
    </AnimatePresence>
  );
};

const Snackbar = ({ isOpen, onClose, message }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <SnackbarContainer
          initial={{ opacity: 0, y: 20, scale: 0.95 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          exit={{ opacity: 0, y: 20, scale: 0.95 }}
          transition={{ duration: 0.2 }}
        >
          <SnackbarIcon />
          <SnackbarMessage>{message}</SnackbarMessage>
          <SnackbarCloseButton onClick={onClose}>
            <X size={16} />
          </SnackbarCloseButton>
        </SnackbarContainer>
      )}
    </AnimatePresence>
  );
};

export {
  AddItemModal,
  SuccessModal,
  DeleteConfirmationModal,
  EditItemModal,
  ModifySuccessModal,
  Snackbar
}; 