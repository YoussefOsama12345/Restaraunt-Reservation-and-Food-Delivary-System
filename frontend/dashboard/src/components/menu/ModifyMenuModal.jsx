import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { X } from 'lucide-react';

// Reuse the same styled components from AddMenuModal
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
  max-width: 600px;
  max-height: 80vh;
  position: relative;
  border: 1px solid #374151;
  overflow-y: auto;

  /* Custom scrollbar styling */
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

  &::-webkit-scrollbar-thumb:hover {
    background: #6b7280;
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
    color: #f9fafb;
  }
`;

const Title = styled.h2`
  color: #f9fafb;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 600;
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
  color: #f9fafb;
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

const TextArea = styled.textarea`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;
  min-height: 100px;
  resize: vertical;
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

const Select = styled.select`
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
`;

const IngredientsInput = styled.div`
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
`;

const IngredientTag = styled.span`
  background-color: #374151;
  color: #9ca3af;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.25rem;
`;

const RemoveIngredientButton = styled.button`
  background: transparent;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;

  &:hover {
    color: #f87171;
  }
`;

const AddIngredientButton = styled.button`
  background-color: #374151;
  color: #9ca3af;
  border: 1px dashed #4b5563;
  border-radius: 0.375rem;
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #4b5563;
    color: #f9fafb;
  }
`;

const SubmitButton = styled.button`
  background-color: #818cf8;
  color: white;
  border: none;
  border-radius: 0.5rem;
  padding: 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 1rem;

  &:hover {
    background-color: #6366f1;
  }

  &:disabled {
    background-color: #4b5563;
    cursor: not-allowed;
  }
`;

const ModifyMenuModal = ({ isOpen, onClose, onSubmit, item }) => {
  const [formData, setFormData] = useState({
    name: '',
    category: '',
    price: '',
    description: '',
    ingredients: [],
    productimage: '',
    available: true,
    sales: 0
  });

  const [newIngredient, setNewIngredient] = useState('');

  useEffect(() => {
    if (item) {
      setFormData({
        ...item,
        price: item.price.toString()
      });
    }
  }, [item]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleAddIngredient = () => {
    if (newIngredient.trim() && !formData.ingredients.includes(newIngredient.trim())) {
      setFormData(prev => ({
        ...prev,
        ingredients: [...prev.ingredients, newIngredient.trim()]
      }));
      setNewIngredient('');
    }
  };

  const handleRemoveIngredient = (ingredient) => {
    setFormData(prev => ({
      ...prev,
      ingredients: prev.ingredients.filter(i => i !== ingredient)
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      price: parseFloat(formData.price)
    });
    onClose();
  };

  if (!isOpen) return null;

  return (
    <ModalOverlay
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      onClick={onClose}
    >
      <ModalContent
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.9, opacity: 0 }}
        onClick={e => e.stopPropagation()}
      >
        <CloseButton onClick={onClose}>
          <X size={20} />
        </CloseButton>
        <Title>Modify Menu Item</Title>
        <Form onSubmit={handleSubmit}>
          <FormGroup>
            <Label>Name</Label>
            <Input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter item name"
              required
            />
          </FormGroup>

          <FormGroup>
            <Label>Category</Label>
            <Select
              name="category"
              value={formData.category}
              onChange={handleChange}
              required
            >
              <option value="">Select a category</option>
              <option value="Baked">Baked</option>
              <option value="Sushi">Sushi</option>
              <option value="Pasta">Pasta</option>
              <option value="Meat">Meat</option>
              <option value="Chicken">Chicken</option>
            </Select>
          </FormGroup>

          <FormGroup>
            <Label>Price</Label>
            <Input
              type="number"
              name="price"
              value={formData.price}
              onChange={handleChange}
              placeholder="Enter price"
              step="0.01"
              min="0"
              required
            />
          </FormGroup>

          <FormGroup>
            <Label>Description</Label>
            <TextArea
              name="description"
              value={formData.description}
              onChange={handleChange}
              placeholder="Enter item description"
              required
            />
          </FormGroup>

          <FormGroup>
            <Label>Image URL</Label>
            <Input
              type="text"
              name="productimage"
              value={formData.productimage}
              onChange={handleChange}
              placeholder="Enter image URL"
              required
            />
          </FormGroup>

          <FormGroup>
            <Label>Ingredients</Label>
            <IngredientsInput>
              {formData.ingredients.map((ingredient, index) => (
                <IngredientTag key={index}>
                  {ingredient}
                  <RemoveIngredientButton
                    type="button"
                    onClick={() => handleRemoveIngredient(ingredient)}
                  >
                    <X size={14} />
                  </RemoveIngredientButton>
                </IngredientTag>
              ))}
              <Input
                type="text"
                value={newIngredient}
                onChange={(e) => setNewIngredient(e.target.value)}
                placeholder="Add ingredient"
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    e.preventDefault();
                    handleAddIngredient();
                  }
                }}
              />
              <AddIngredientButton type="button" onClick={handleAddIngredient}>
                Add
              </AddIngredientButton>
            </IngredientsInput>
          </FormGroup>

          <FormGroup>
            <Label>Availability</Label>
            <Select
              name="available"
              value={formData.available}
              onChange={handleChange}
              required
            >
              <option value={true}>Available</option>
              <option value={false}>Unavailable</option>
            </Select>
          </FormGroup>

          <SubmitButton type="submit">Save Changes</SubmitButton>
        </Form>
      </ModalContent>
    </ModalOverlay>
  );
};

export default ModifyMenuModal; 