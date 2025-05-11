import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
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
  border-radius: 1rem;
  padding: 2rem;
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  border: 1px solid #374151;

  &::-webkit-scrollbar {
    width: 8px;
  }

  &::-webkit-scrollbar-track {
    background: #374151;
    border-radius: 4px;
  }

  &::-webkit-scrollbar-thumb {
    background: #4b5563;
    border-radius: 4px;
  }
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
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.375rem;
  transition: all 0.2s;

  &:hover {
    background-color: #374151;
    color: #f3f4f6;
  }
`;

const Title = styled.h2`
  color: #f9fafb;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  padding-right: 2rem;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
`;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  color: #f3f4f6;
  font-size: 0.875rem;
  font-weight: 500;
`;

const Input = styled.input`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;
  transition: all 0.2s;

  &:focus {
    outline: none;
    border-color: #818cf8;
    box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.2);
  }

  &::placeholder {
    color: #9ca3af;
  }
`;

const ButtonGroup = styled.div`
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1rem;
`;

const Button = styled.button`
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

const CancelButton = styled(Button)`
  background-color: #374151;
  color: #f3f4f6;

  &:hover:not(:disabled) {
    background-color: #4b5563;
  }
`;

const SubmitButton = styled(Button)`
  background-color: #818cf8;
  color: white;

  &:hover:not(:disabled) {
    background-color: #6366f1;
  }
`;

const ErrorMessage = styled.span`
  color: #f87171;
  font-size: 0.75rem;
  margin-top: 0.25rem;
`;

const AddCategoryModal = ({ isOpen, onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    name: '',
    category: '',
    stock: '',
    sales: '',
    productimage: ''
  });

  const [errors, setErrors] = useState({});

  const validateForm = () => {
    const newErrors = {};
    if (!formData.name.trim()) newErrors.name = 'Name is required';
    if (!formData.category.trim()) newErrors.category = 'Category is required';
    if (!formData.stock.trim()) newErrors.stock = 'Stock is required';
    if (!formData.sales.trim()) newErrors.sales = 'Sales is required';
    if (!formData.productimage.trim()) newErrors.productimage = 'Product image is required';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
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

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      onSubmit({
        ...formData,
        id: Date.now(), // Generate a temporary ID
        stock: parseInt(formData.stock),
        sales: parseInt(formData.sales)
      });
      setFormData({
        name: '',
        category: '',
        stock: '',
        sales: '',
        productimage: ''
      });
    }
  };

  if (!isOpen) return null;

  return (
    <ModalOverlay
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <ModalContent
        initial={{ scale: 0.95, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.95, opacity: 0 }}
      >
        <CloseButton onClick={onClose}>
          <X size={20} />
        </CloseButton>
        <Title>Add New Category</Title>
        <Form onSubmit={handleSubmit}>
          <FormGroup>
            <Label htmlFor="name">Name</Label>
            <Input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter product name"
            />
            {errors.name && <ErrorMessage>{errors.name}</ErrorMessage>}
          </FormGroup>

          <FormGroup>
            <Label htmlFor="category">Category</Label>
            <Input
              type="text"
              id="category"
              name="category"
              value={formData.category}
              onChange={handleChange}
              placeholder="Enter category"
            />
            {errors.category && <ErrorMessage>{errors.category}</ErrorMessage>}
          </FormGroup>

          <FormGroup>
            <Label htmlFor="stock">Items Number</Label>
            <Input
              type="number"
              id="stock"
              name="stock"
              value={formData.stock}
              onChange={handleChange}
              placeholder="Enter items number"
            />
            {errors.stock && <ErrorMessage>{errors.stock}</ErrorMessage>}
          </FormGroup>

          <FormGroup>
            <Label htmlFor="sales">Total Sales</Label>
            <Input
              type="number"
              id="sales"
              name="sales"
              value={formData.sales}
              onChange={handleChange}
              placeholder="Enter total sales"
            />
            {errors.sales && <ErrorMessage>{errors.sales}</ErrorMessage>}
          </FormGroup>

          <FormGroup>
            <Label htmlFor="productimage">Product Image URL</Label>
            <Input
              type="text"
              id="productimage"
              name="productimage"
              value={formData.productimage}
              onChange={handleChange}
              placeholder="Enter product image URL"
            />
            {errors.productimage && <ErrorMessage>{errors.productimage}</ErrorMessage>}
          </FormGroup>

          <ButtonGroup>
            <CancelButton type="button" onClick={onClose}>
              Cancel
            </CancelButton>
            <SubmitButton type="submit">
              Add Category
            </SubmitButton>
          </ButtonGroup>
        </Form>
      </ModalContent>
    </ModalOverlay>
  );
};

export default AddCategoryModal; 