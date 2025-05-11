import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Edit, Search, Trash2 } from 'lucide-react';

const PRODUCT_DATA = [
    { id: 1, productimage:"./menuImg/Neapolitan Pizza Dough.jpg", name: "Naepolitana Pizza Dough", category: "Baked", stock: 143, sales: 1200 },
    { id: 2, productimage:"./menuImg/asian.jpeg" , name: "Leather Wallet", category: "Accessories", stock: 89, sales: 800 },
    { id: 3, productimage:"./menuImg/creamy shrimp fettuccine pasta with homemade alfredo sauce -.jpeg", name: "Smart Watch", category: "Electronics",  stock: 56, sales: 650 },
    { id: 4, productimage:"./menuImg/Garlic Butter Steak Bites and Mash.jpg", name: "Yoga Mat", category: "Fitness",  stock: 210, sales: 950 },
    { id: 5, productimage:"./menuImg/Slow-Cooked Garlic Butter Chicken & Ribeye with….jpeg", name: "Coffee Maker", category: "Home", stock: 78, sales: 720 },
  ];

  
  const TableWrapper = styled(motion.div)`
  background-color: #1f2937;
  padding: 1.5rem;
  border-radius: 1rem;
  border: 1px solid #374151;
  backdrop-filter: blur(6px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
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

const CenteredTd = styled(Td)`
  text-align: center;
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
  margin-right: 0.25rem;
  color: ${({ color }) => color || '#60a5fa'};
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.375rem;
  transition: all 0.2s;
  padding: 0.25rem;

  &:hover {
    opacity: 0.8;
  }

  &:last-child {
    margin-right: 0;
  }
`;

const CategoryTable = ({ products, onDeleteClick, onModifyClick }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(products);

  // Update filtered products when products prop changes
  React.useEffect(() => {
    setFilteredProducts(products);
  }, [products]);

  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = products.filter(product => 
      product.name.toLowerCase().includes(term) || 
      product.category.toLowerCase().includes(term)
    );
    setFilteredProducts(filtered);
  };

  const handleDelete = (product) => {
    onDeleteClick(product);
  };

  const handleModify = (product) => {
    onModifyClick(product);
  };

  return (
    <TableWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <Header>
        <h2>Categories Table</h2>
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
            <Th style={{ textAlign: 'center' }}>Items number</Th>
            <Th>Total Sales</Th>
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
              <CenteredTd>{product.stock}</CenteredTd>
              <Td>{product.sales}</Td>
              <Td>
                <ActionButton 
                  color="#818cf8"
                  onClick={() => handleModify(product)}
                  title="Edit item"
                >
                  <Edit size={16} />
                </ActionButton>
                <ActionButton 
                  color="#f87171" 
                  onClick={() => handleDelete(product)}
                  title="Delete item"
                >
                  <Trash2 size={16} />
                </ActionButton>
              </Td>
            </motion.tr>
          ))}
        </tbody>
      </StyledTable>
    </TableWrapper>
  );
};

export default CategoryTable;