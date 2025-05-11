import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Flame, DollarSign, TrendingUp, Package, Plus } from 'lucide-react';
import StatsCard from '../components/common/StatsCard';
import Header from '../components/common/Header';
import CategoryTable from '../components/category/categoryTable';
import ConfirmModal from '../components/common/ConfirmModal';
import Snackbar from '../components/common/Snackbar';
import AddCategoryModal from '../components/category/AddCategoryModal';
import ModifyCategoryModal from '../components/category/ModifyCategoryModal';

// Styled Components
const PageWrapper = styled.div`
    flex: 1;
    overflow: auto;
    position: relative;
    z-index: 10;
    background-color: #111827;
    color: #f9fafb;
    min-height: 100vh;
`;

const Main = styled.main`
    max-width: ${({ theme }) => theme.sizes?.container || '1280px'};
    margin: 0 auto;
    padding: ${({ theme }) => theme.spacing?.mainPadding || '1.5rem 1rem'};

    @media (min-width: 1024px) {
        padding: 2rem;
    }

    @media (min-width: 1280px) {
        padding: 2.5rem;
    }
`;


const StatsGrid = styled(motion.div)`
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
    margin-bottom: 2.5rem;

    @media (min-width: 640px) {
        grid-template-columns: repeat(2, 1fr);
    }

    @media (min-width: 1024px) {
        grid-template-columns: repeat(4, 1fr);
    }
`;

const ContentSection = styled.section`
    background-color: #1f2937;
    border-radius: 1rem;
    border: 1px solid #374151;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
`;

const AddButton = styled(motion.button)`
  position: relative;
  margin-top: 1.5rem;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 10px;
  background-color: #818cf8;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: all 0.2s;

  &:hover {
    background-color: #6366f1;
    transform: scale(1.05);
  }

  &:active {
    transform: scale(0.95);
  }
`;

const PRODUCT_DATA = [
    { id: 1, productimage:"./menuImg/Neapolitan Pizza Dough.jpg", name: "Naepolitana Pizza Dough", category: "Baked", stock: 143, sales: 1200 },
    { id: 2, productimage:"./menuImg/asian.jpeg" , name: "Leather Wallet", category: "Accessories", stock: 89, sales: 800 },
    { id: 3, productimage:"./menuImg/creamy shrimp fettuccine pasta with homemade alfredo sauce -.jpeg", name: "Smart Watch", category: "Electronics",  stock: 56, sales: 650 },
    { id: 4, productimage:"./menuImg/Garlic Butter Steak Bites and Mash.jpg", name: "Yoga Mat", category: "Fitness",  stock: 210, sales: 950 },
    { id: 5, productimage:"./menuImg/Slow-Cooked Garlic Butter Chicken & Ribeye with….jpeg", name: "Coffee Maker", category: "Home", stock: 78, sales: 720 },
];

const CategoryPage = () => {
    const [products, setProducts] = useState(PRODUCT_DATA);
    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
    const [isAddModalOpen, setIsAddModalOpen] = useState(false);
    const [isModifyModalOpen, setIsModifyModalOpen] = useState(false);
    const [itemToDelete, setItemToDelete] = useState(null);
    const [itemToModify, setItemToModify] = useState(null);
    const [snackbar, setSnackbar] = useState({
        isVisible: false,
        message: '',
        type: 'success'
    });

    const handleAddClick = () => {
        setIsAddModalOpen(true);
    };

    const handleAddClose = () => {
        setIsAddModalOpen(false);
    };

    const handleAddSubmit = (newCategory) => {
        setProducts(prevProducts => [...prevProducts, newCategory]);
        setSnackbar({
            isVisible: true,
            message: 'Category added successfully',
            type: 'success'
        });
        setIsAddModalOpen(false);
    };

    const handleModifyClick = (item) => {
        setItemToModify(item);
        setIsModifyModalOpen(true);
    };

    const handleModifyClose = () => {
        setIsModifyModalOpen(false);
        setItemToModify(null);
    };

    const handleModifySubmit = (modifiedCategory) => {
        console.log('Modifying category:', modifiedCategory); // Debug log
        setProducts(prevProducts => {
            const updatedProducts = prevProducts.map(product => {
                if (product.id === modifiedCategory.id) {
                    console.log('Updating product:', product.id); // Debug log
                    return {
                        ...product,
                        name: modifiedCategory.name,
                        category: modifiedCategory.category,
                        stock: modifiedCategory.stock,
                        sales: modifiedCategory.sales,
                        productimage: modifiedCategory.productimage
                    };
                }
                return product;
            });
            console.log('Updated products:', updatedProducts); // Debug log
            return updatedProducts;
        });

        setSnackbar({
            isVisible: true,
            message: 'Category modified successfully',
            type: 'success'
        });
        setIsModifyModalOpen(false);
        setItemToModify(null);
    };

    const handleDeleteClick = (item) => {
        setItemToDelete(item);
        setIsDeleteModalOpen(true);
    };

    const handleConfirmDelete = () => {
        setProducts(prevProducts => prevProducts.filter(product => product.id !== itemToDelete.id));
        setSnackbar({
            isVisible: true,
            message: 'Item deleted successfully',
            type: 'success'
        });
        setIsDeleteModalOpen(false);
        setItemToDelete(null);
    };

    const handleCloseDeleteModal = () => {
        setIsDeleteModalOpen(false);
        setItemToDelete(null);
    };

    const handleCloseSnackbar = () => {
        setSnackbar(prev => ({ ...prev, isVisible: false }));
    };

    return (
        <PageWrapper>
            <Header title="Categories" />
            <Main>
                <StatsGrid
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.1 }}
                >
                    <StatsCard
                        icon={Flame}
                        name="Top Sales"
                        value="Napolitana"
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

                <ContentSection>
                    <CategoryTable 
                        products={products}
                        onDeleteClick={handleDeleteClick}
                        onModifyClick={handleModifyClick}
                    />
                </ContentSection>

                <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                    <AddButton
                        onClick={handleAddClick}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                    >
                        <Plus size={20} />
                    </AddButton>
                </div>

                <ConfirmModal
                    isOpen={isDeleteModalOpen}
                    onClose={handleCloseDeleteModal}
                    onConfirm={handleConfirmDelete}
                    title="Delete Item"
                    message={`Are you sure you want to delete ${itemToDelete?.name}? This action cannot be undone.`}
                />

                <AddCategoryModal
                    isOpen={isAddModalOpen}
                    onClose={handleAddClose}
                    onSubmit={handleAddSubmit}
                />

                <ModifyCategoryModal
                    isOpen={isModifyModalOpen}
                    onClose={handleModifyClose}
                    onSubmit={handleModifySubmit}
                    category={itemToModify}
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

export default CategoryPage;