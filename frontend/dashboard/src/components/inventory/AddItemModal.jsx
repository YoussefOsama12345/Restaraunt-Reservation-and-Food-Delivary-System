import React, { useState } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { X } from 'lucide-react';

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
  background: transparent;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.5rem;
  
  &:hover {
    color: #d1d5db;
  }
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
  color: #d1d5db;
  font-size: 0.875rem;
`;

const Input = styled.input`
  padding: 0.5rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.375rem;
  color: white;
  font-size: 0.875rem;

  &:focus {
    outline: none;
    border-color: #818cf8;
  }
`;

const SubmitButton = styled.button`
  background-color: #818cf8;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  font-weight: 500;
  margin-top: 1rem;

  &:hover {
    background-color: #6366f1;
  }

  &:disabled {
    background-color: #4b5563;
    cursor: not-allowed;
  }
`;

const ErrorMessage = styled.span`
  color: #ef4444;
  font-size: 0.75rem;
  margin-top: 0.25rem;
`;

const AddItemModal = ({ isOpen, onClose, onAdd }) => {
  const [formData, setFormData] = useState({
    name: '',
    itemId: '',
    category: '',
    cost: '',
    quantity: '',
    sales: '',
    expireDate: '',
    productimage: ''
  });
  const [errors, setErrors] = useState({});

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};
    Object.keys(formData).forEach(key => {
      if (!formData[key]) {
        newErrors[key] = 'This field is required';
      }
    });
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      const newProduct = {
        id: Date.now(), // Generate a unique ID
        ...formData,
        cost: parseFloat(formData.cost),
        quantity: parseInt(formData.quantity),
        sales: parseInt(formData.sales)
      };
      onAdd(newProduct);
      onClose();
      setFormData({
        name: '',
        itemId: '',
        category: '',
        cost: '',
        quantity: '',
        sales: '',
        expireDate: '',
        productimage: ''
      });
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <ModalOverlay
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <ModalContent
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.9, opacity: 0 }}
          >
            <CloseButton onClick={onClose}>
              <X size={20} />
            </CloseButton>
            <h2 style={{ color: '#f9fafb', marginBottom: '1.5rem' }}>Add New Item</h2>
            <Form onSubmit={handleSubmit}>
              <FormGroup>
                <Label>Name</Label>
                <Input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  placeholder="Enter product name"
                />
                {errors.name && <ErrorMessage>{errors.name}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Item ID</Label>
                <Input
                  type="text"
                  name="itemId"
                  value={formData.itemId}
                  onChange={handleInputChange}
                  placeholder="Enter item ID"
                />
                {errors.itemId && <ErrorMessage>{errors.itemId}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Category</Label>
                <Input
                  type="text"
                  name="category"
                  value={formData.category}
                  onChange={handleInputChange}
                  placeholder="Enter category"
                />
                {errors.category && <ErrorMessage>{errors.category}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Cost (per unit)</Label>
                <Input
                  type="number"
                  name="cost"
                  value={formData.cost}
                  onChange={handleInputChange}
                  placeholder="Enter cost"
                  step="0.01"
                />
                {errors.cost && <ErrorMessage>{errors.cost}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Quantity</Label>
                <Input
                  type="number"
                  name="quantity"
                  value={formData.quantity}
                  onChange={handleInputChange}
                  placeholder="Enter quantity"
                />
                {errors.quantity && <ErrorMessage>{errors.quantity}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Sales</Label>
                <Input
                  type="number"
                  name="sales"
                  value={formData.sales}
                  onChange={handleInputChange}
                  placeholder="Enter sales"
                />
                {errors.sales && <ErrorMessage>{errors.sales}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Expiration Date</Label>
                <Input
                  type="date"
                  name="expireDate"
                  value={formData.expireDate}
                  onChange={handleInputChange}
                />
                {errors.expireDate && <ErrorMessage>{errors.expireDate}</ErrorMessage>}
              </FormGroup>

              <FormGroup>
                <Label>Product Image URL</Label>
                <Input
                  type="text"
                  name="productimage"
                  value={formData.productimage}
                  onChange={handleInputChange}
                  placeholder="Enter image URL"
                />
                {errors.productimage && <ErrorMessage>{errors.productimage}</ErrorMessage>}
              </FormGroup>

              <SubmitButton type="submit">Add Item</SubmitButton>
            </Form>
          </ModalContent>
        </ModalOverlay>
      )}
    </AnimatePresence>
  );
};

export default AddItemModal; 