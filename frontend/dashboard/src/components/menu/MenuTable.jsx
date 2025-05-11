import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Edit, Search, Trash2, ChevronDown } from 'lucide-react';
import ConfirmModal from '../common/ConfirmModal';

// Sample data
const PRODUCT_DATA = [
  { id: 1, productimage:"./menuImg/Neapolitan Pizza Dough.jpg", name: "Naepolitana Pizza Dough", category: "Baked", price: 59.99, sales: 1200, description: "Traditional Italian pizza dough made with high-quality.", available: true, ingredients: ["Flour", "Yeast", "Salt", "Water", "Olive Oil"] },
  { id: 2, productimage:"./menuImg/asian.jpeg" , name: "Leather Wallet", category: "Sushi", price: 39.99, sales: 800, description: "Handcrafted genuine leather wallet", available: true, ingredients: ["Rice", "Salmon", "Nori", "Cucumber", "Avocado", "Wasabi"] },
  { id: 3, productimage:"./menuImg/creamy shrimp fettuccine pasta with homemade alfredo sauce -.jpeg", name: "shrimp pasta", category: "Electronics", price: 199.99, sales: 650, description: "Advanced smartwatch with health monitoring", available: false, ingredients: ["Fettuccine", "Shrimp", "Heavy Cream", "Parmesan", "Garlic", "Butter"] },
  { id: 4, productimage:"./menuImg/Garlic Butter Steak Bites and Mash.jpg", name: "meat balls", category: "Fitness", price: 29.99, sales: 950, description: "Premium non-slip yoga mat with perfect thickness", available: true, ingredients: ["Ground Beef", "Breadcrumbs", "Eggs", "Onion", "Garlic", "Herbs"] },
  { id: 5, productimage:"./menuImg/Slow-Cooked Garlic Butter Chicken & Ribeye with….jpeg", name: "chicken", category: "Home", price: 79.99, sales: 720, description: "Programmable coffee maker", available: false, ingredients: ["Chicken", "Garlic", "Butter", "Herbs", "Lemon", "Olive Oil"] },
];

// Styled Components
const TableWrapper = styled(motion.div)`
  background-color: #1f2937;
  padding: 1.5rem;
  border-radius: 1rem;
  border: 1px solid #374151;
  backdrop-filter: blur(6px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  margin-bottom: 2rem;
  color: #f9fafb;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  align-items: center;
`;

const SearchInputWrapper = styled.div`
  position: relative;
`;

const SearchInput = styled.input`
  padding: 0.5rem 0.5rem 0.5rem 2.5rem;
  background-color: #374151;
  color: white;
  border-radius: 0.5rem;
  border: none;
  outline: none;

  &::placeholder {
    color: #9ca3af;
  }
`;

const SearchIcon = styled(Search)`
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
`;

const StyledTable = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const Th = styled.th`
  padding: 0.75rem 1rem;
  text-align: left;
  text-transform: uppercase;
  font-size: 0.75rem;
  color: #9ca3af;
  font-weight: 500;
  border-bottom: 1px solid #374151;
`;

const Td = styled.td`
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  color: #d1d5db;
`;

const ProductImage = styled.img`
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  margin-right: 0.75rem;
`;

const ActionButton = styled.button`
  background: transparent;
  border: none;
  cursor: pointer;
  margin-right: 0.5rem;
  color: ${({ color }) => color || '#60a5fa'};
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.375rem;
  transition: all 0.2s;
  padding: 0.25rem;

  &:last-child {
    margin-right: 0;
  }

  &:hover {
    opacity: 0.8;
    transform: translateY(-1px);
  }

  &:active {
    transform: translateY(0);
  }
`;

const ActionButtonsWrapper = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
`;

const DescriptionCell = styled.div`
  max-width: 300px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #9ca3af;
  font-size: 0.875rem;
`;

const StatusBadge = styled.span`
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  background-color: ${props => props.available ? '#10B981' : '#EF4444'};
  color: white;
  text-transform: uppercase;
`;

const StatusDot = styled.span`
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 6px;
  background-color: white;
`;

const IngredientsDropdown = styled.div`
  position: relative;
  display: inline-block;
`;

const DropdownButton = styled.button`
  background-color: #374151;
  color: #9ca3af;
  padding: 0.5rem 1rem;
  border: 1px solid #4b5563;
  border-radius: 0.375rem;
  cursor: pointer;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;

  &:hover {
    background-color: #4b5563;
    color: #f9fafb;
  }
`;

const DropdownContent = styled.div`
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #1f2937;
  min-width: 200px;
  border: 1px solid #374151;
  border-radius: 0.375rem;
  padding: 0.5rem;
  z-index: 1000;
  margin-top: 0.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
`;

const IngredientItem = styled.div`
  padding: 0.5rem;
  color: #9ca3af;
  font-size: 0.875rem;
  cursor: pointer;
  border-radius: 0.25rem;
  transition: all 0.2s;

  &:hover {
    background-color: #374151;
    color: #f9fafb;
  }
`;

const MenuTable = ({ onEditClick, onDeleteClick }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(PRODUCT_DATA);
  const [openDropdown, setOpenDropdown] = useState(null);
  const [deleteModalOpen, setDeleteModalOpen] = useState(false);
  const [itemToDelete, setItemToDelete] = useState(null);

  // Filter products based on search
  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = PRODUCT_DATA.filter(product => 
      product.name.toLowerCase().includes(term) || 
      product.category.toLowerCase().includes(term) ||
      product.description.toLowerCase().includes(term) ||
      product.ingredients.some(ingredient => ingredient.toLowerCase().includes(term))
    );
    setFilteredProducts(filtered);
  };

  const handleDeleteClick = (id) => {
    setItemToDelete(id);
    setDeleteModalOpen(true);
  };

  const handleConfirmDelete = () => {
    if (itemToDelete) {
      setFilteredProducts(prev => prev.filter(product => product.id !== itemToDelete));
      onDeleteClick(itemToDelete);
      setDeleteModalOpen(false);
      setItemToDelete(null);
    }
  };

  const handleCloseDeleteModal = () => {
    setDeleteModalOpen(false);
    setItemToDelete(null);
  };

  const toggleDropdown = (id) => {
    setOpenDropdown(openDropdown === id ? null : id);
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (openDropdown && !event.target.closest('.ingredients-dropdown')) {
        setOpenDropdown(null);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [openDropdown]);

  return (
    <TableWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <Header>
        <h2>Menu List</h2>
        <SearchInputWrapper>
          <SearchInput
            type="text"
            placeholder="Search products..."
            onChange={handleSearch}
            value={searchTerm}
          />
          <SearchIcon size={20} />
        </SearchInputWrapper>
      </Header>

      <StyledTable>
        <thead>
          <tr>
            <Th>Name</Th>
            <Th>Category</Th>
            <Th>Price</Th>
            <Th>Sales</Th>
            <Th>Description</Th>
            <Th>Ingredients</Th>
            <Th>Availability</Th>
            <Th>Actions</Th>
          </tr>
        </thead>
        <tbody>
          {filteredProducts.map(product => (
            <motion.tr
              key={product.id}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3 }}
            >
              <Td>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <ProductImage src={product.productimage} alt={product.name} />
                  {product.name}
                </div>
              </Td>
              <Td>{product.category}</Td>
              <Td>${product.price.toFixed(2)}</Td>
              <Td>{product.sales}</Td>
              <Td>
                <DescriptionCell title={product.description}>
                  {product.description}
                </DescriptionCell>
              </Td>
              <Td>
                <IngredientsDropdown className="ingredients-dropdown">
                  <DropdownButton onClick={() => toggleDropdown(product.id)}>
                      Ingredients
                    <ChevronDown size={16} />
                  </DropdownButton>
                  {openDropdown === product.id && (
                    <DropdownContent>
                      {product.ingredients.map((ingredient, index) => (
                        <IngredientItem key={index}>
                          {ingredient}
                        </IngredientItem>
                      ))}
                    </DropdownContent>
                  )}
                </IngredientsDropdown>
              </Td>
              <Td>
                <StatusBadge available={product.available}>
                  <StatusDot />
                  {product.available ? 'Available' : 'Unavailable'}
                </StatusBadge>
              </Td>
              <Td>
                <ActionButtonsWrapper>
                  <ActionButton color="#818cf8" onClick={() => onEditClick(product)}>
                    <Edit size={16} />
                  </ActionButton>
                  <ActionButton color="#f87171" onClick={() => handleDeleteClick(product.id)}>
                    <Trash2 size={16} />
                  </ActionButton>
                </ActionButtonsWrapper>
              </Td>
            </motion.tr>
          ))}
        </tbody>
      </StyledTable>

      <ConfirmModal
        isOpen={deleteModalOpen}
        onClose={handleCloseDeleteModal}
        onConfirm={handleConfirmDelete}
        title="Delete Menu Item"
        message="Are you sure you want to delete this menu item? This action cannot be undone."
      />
    </TableWrapper>
  );
};

export default MenuTable;
