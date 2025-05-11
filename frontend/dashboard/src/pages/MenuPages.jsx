import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import Header from '../components/common/Header';
import { AlertTriangle, DollarSign, TrendingUp, Package, Plus } from 'lucide-react';
import StatsCard from '../components/common/StatsCard';
import MenuTable from '../components/menu/MenuTable';
import SalesTrendChart from '../components/menu/SalesTrendChart';
import CategoryDistributionChart from '../components/overview/CategoryDistributionChart';
import AddMenuModal from '../components/menu/AddMenuModal';
import ModifyMenuModal from '../components/menu/ModifyMenuModal';
import Snackbar from '../components/common/Snackbar';



// Styled Components
const PageWrapper = styled.div`
  flex: 1;
  overflow: auto;
  position: relative;
  z-index: 10;
  background-color: #111827;
  color: #f9fafb;
`;

const Main = styled.main`
  max-width: ${({ theme }) => theme.sizes?.container || '1280px'};
  margin: 0 auto;
  padding: ${({ theme }) => theme.spacing?.mainPadding || '1.5rem 1rem'};

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

const ChartsContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-top: 2rem;

  @media (min-width: 1024px) {
    flex-direction: row;
    & > * {
      flex: 1;
    }
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

const MenuPages = () => {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [isModifyModalOpen, setIsModifyModalOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState(null);
  const [snackbar, setSnackbar] = useState({
    isVisible: false,
    message: '',
    type: 'success'
  });

  const handleAddClick = () => {
    setIsAddModalOpen(true);
  };

  const handleCloseAddModal = () => {
    setIsAddModalOpen(false);
  };

  const handleCloseModifyModal = () => {
    setIsModifyModalOpen(false);
    setSelectedItem(null);
  };

  const handleAddMenu = (newItem) => {
    // Here you would typically make an API call to add the item
    console.log('New menu item:', newItem);
    setSnackbar({
      isVisible: true,
      message: 'Added successfully'
    });
    setIsAddModalOpen(false);
  };

  const handleModifyMenu = (modifiedItem) => {
    // Here you would typically make an API call to update the item
    console.log('Modified menu item:', modifiedItem);
    setSnackbar({
      isVisible: true,
      message: 'Menu item modified successfully'
    });
    setIsModifyModalOpen(false);
    setSelectedItem(null);
  };

  const handleEditClick = (item) => {
    setSelectedItem(item);
    setIsModifyModalOpen(true);
  };

  const handleDeleteMenu = (id) => {
    // Here you would typically make an API call to delete the item
    console.log('Deleting menu item:', id);
    setSnackbar({
      isVisible: true,
      message: 'Menu item deleted successfully',
      type: 'success'
    });
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, isVisible: false }));
  };

  return (
    <PageWrapper>
      <Header title="Menu" />

      <Main>
        <StatsGrid
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <StatsCard name="Total Products" icon={Package} value="1234" color="#6366F1" />
          <StatsCard name="Top Selling" icon={TrendingUp} value="89" color="#8B5CF6" />
          <StatsCard name="Low Stock" icon={AlertTriangle} value="23" color="#EC4899" />
          <StatsCard name="Total Revenue" icon={DollarSign} value="$543,210" color="#10B981" />
        </StatsGrid>

        <MenuTable 
          onEditClick={handleEditClick} 
          onDeleteClick={handleDeleteMenu}
        />
        <AddButton onClick={handleAddClick}>
          <Plus size={20} />
        </AddButton>

        <ChartsContainer>
          <SalesTrendChart />
          <CategoryDistributionChart />
        </ChartsContainer>

        <AddMenuModal
          isOpen={isAddModalOpen}
          onClose={handleCloseAddModal}
          onSubmit={handleAddMenu}
        />

        <ModifyMenuModal
          isOpen={isModifyModalOpen}
          onClose={handleCloseModifyModal}
          onSubmit={handleModifyMenu}
          item={selectedItem}
        />

        <Snackbar
          isVisible={snackbar.isVisible}
          message={snackbar.message}
          type={snackbar.type}
          onClose={handleCloseSnackbar}
        />
      </Main>
    </PageWrapper>
  );
};

export default MenuPages;
