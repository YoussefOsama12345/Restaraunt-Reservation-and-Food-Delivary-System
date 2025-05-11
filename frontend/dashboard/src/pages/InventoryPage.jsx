import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import Header from '../components/common/Header';
import { AlertTriangle, DollarSign, TrendingUp, Package, Plus } from 'lucide-react';
import StatsCard from '../components/common/StatsCard';
import InventoryTable from '../components/inventory/InventoryTable';
import { AddItemModal, DeleteConfirmationModal, EditItemModal, Snackbar } from '../components/inventory/InventoryModals';

// Styled Components
const PageWrapper = styled.div`
    flex: 1;
    position: relative;
    z-index: 10;
    background-color: #111827;
    color: #f9fafb;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    width: 100%;
`;

const Main = styled.main`
    flex: 1;
    max-width: ${({ theme }) => theme.sizes?.container || '1280px'};
    margin: 0 auto;
    padding: ${({ theme }) => theme.spacing?.mainPadding || '1.5rem 1rem'};
    width: 100%;
    overflow-x: hidden;
    box-sizing: border-box;

    @media (min-width: 1024px) {
        padding-left: 2rem;
        padding-right: 2rem;
    }

    @media (min-width: 1280px) {
        padding-left: 2rem;
        padding-right: 2rem;
    }
`;

const StatsGrid = styled(motion.div)`
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
    margin-bottom: 2rem;

    @media (min-width: 640px) {
        grid-template-columns: repeat(2, 1fr);
    }

    @media (min-width: 1024px) {
        grid-template-columns: repeat(4, 1fr);
    }
`;


const AddButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: #818cf8;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  margin-top: 1rem;
  margin-left: auto;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  &:hover {
    background-color: #6366f1;
    transform: translateY(-1px);
  }

  &:active {
    transform: translateY(0);
  }
`;

const InventoryPage = () => {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [isSnackbarOpen, setIsSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [itemToDelete, setItemToDelete] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    itemId: '',
    category: '',
    cost: '',
    quantity: '',
    expireDate: ''
  });
  const [errors, setErrors] = useState({});

  const validateForm = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Name is required';
    if (!formData.itemId) newErrors.itemId = 'Item ID is required';
    if (!formData.category) newErrors.category = 'Category is required';
    if (!formData.cost) newErrors.cost = 'Cost is required';
    if (!formData.quantity) newErrors.quantity = 'Quantity is required';
    if (!formData.expireDate) newErrors.expireDate = 'Expire date is required';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const showSnackbar = (message) => {
    setSnackbarMessage(message);
    setIsSnackbarOpen(true);
    setTimeout(() => {
      setIsSnackbarOpen(false);
    }, 3000);
  };

  const handleAddSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      // Here you would typically make an API call to add the item
      console.log('Adding item:', formData);
      setIsAddModalOpen(false);
      showSnackbar(`"${formData.name}" has been added successfully`);
      // Reset form
      setFormData({
        name: '',
        itemId: '',
        category: '',
        cost: '',
        quantity: '',
        expireDate: ''
      });
      setErrors({});
    }
  };

  const handleEditClick = (item) => {
    setFormData({
      name: item.name,
      itemId: item.itemId,
      category: item.category,
      cost: item.cost,
      quantity: item.quantity,
      expireDate: item.expireDate
    });
    setIsEditModalOpen(true);
  };

  const handleEditSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      // Here you would typically make an API call to update the item
      console.log('Updating item:', formData);
      setIsEditModalOpen(false);
      showSnackbar(`"${formData.name}" has been modified successfully`);
      // Reset form
      setFormData({
        name: '',
        itemId: '',
        category: '',
        cost: '',
        quantity: '',
        expireDate: ''
      });
      setErrors({});
    }
  };

  const handleDeleteClick = (item) => {
    setItemToDelete(item);
    setIsDeleteModalOpen(true);
  };

  const handleDeleteConfirm = () => {
    if (itemToDelete) {
      // Here you would typically make an API call to delete the item
      console.log('Deleting item:', itemToDelete);
      setIsDeleteModalOpen(false);
      showSnackbar(`"${itemToDelete.name}" has been deleted successfully`);
      setItemToDelete(null);
    }
  };

  const handleCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setItemToDelete(null);
  };

  return (
    <PageWrapper>
      <Header title="Inventory"/>
      <Main>
        <StatsGrid
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          <StatsCard
            icon={AlertTriangle}
            name="Low Stock Items"
            value="5"
            color="#f87171"
          />
          <StatsCard
            icon={DollarSign}
            name="Total Value"
            value="$12,500"
            color="#34d399"
          />
          <StatsCard
            icon={TrendingUp}
            name="Monthly Sales"
            value="$3,200"
            color="#60a5fa"
          />
          <StatsCard
            icon={Package}
            name="Total Items"
            value="156"
            color="#818cf8"
          />
        </StatsGrid>

        <InventoryTable 
          onDeleteClick={handleDeleteClick}
          onEditClick={handleEditClick}
        />
        
        <AddButton onClick={() => setIsAddModalOpen(true)}>
          <Plus size={20} />
        </AddButton>

        <AddItemModal
          isOpen={isAddModalOpen}
          onClose={() => setIsAddModalOpen(false)}
          onSubmit={handleAddSubmit}
          formData={formData}
          setFormData={setFormData}
          errors={errors}
        />

        <EditItemModal
          isOpen={isEditModalOpen}
          onClose={() => {
            setIsEditModalOpen(false);
            setFormData({
              name: '',
              itemId: '',
              category: '',
              cost: '',
              quantity: '',
              expireDate: ''
            });
            setErrors({});
          }}
          onSubmit={handleEditSubmit}
          formData={formData}
          setFormData={setFormData}
          errors={errors}
        />

        <DeleteConfirmationModal
          isOpen={isDeleteModalOpen}
          onClose={handleCloseDeleteModal}
          onConfirm={handleDeleteConfirm}
          itemName={itemToDelete?.name}
        />

        <Snackbar
          isOpen={isSnackbarOpen}
          onClose={() => setIsSnackbarOpen(false)}
          message={snackbarMessage}
        />
      </Main>
    </PageWrapper>
  );
};

export default InventoryPage;