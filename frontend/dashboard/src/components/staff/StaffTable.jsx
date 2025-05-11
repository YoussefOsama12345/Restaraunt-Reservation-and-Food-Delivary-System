import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Edit, Search, Trash2 } from 'lucide-react';
import ModifyStaffModal from './ModifyStaffModal';
import Snackbar from '../common/Snackbar';
import ConfirmModal from '../common/ConfirmModal';

const PRODUCT_DATA = [
    { id: 1, staffId: "STF001", productimage:"./menuImg/Neapolitan Pizza Dough.jpg", name: "Naepolitana Pizza Dough", age: 28, phone: "01035226990", address: "123 Main St, Cairo", salary: 8000, shift: { type: "Morning", from: "08:00am", to: "4:00pm" }, role: "Chef" },
    { id: 2, staffId: "STF002", productimage:"./menuImg/asian.jpeg" , name: "Leather Wallet", age: 32, phone: "01158746985", address: "456 Park Ave, Alexandria", salary: 9500, shift: { type: "Evening", from: "4:00pm ", to: "12:00am" }, role: "Manager" },
    { id: 3, staffId: "STF003", productimage:"./menuImg/creamy shrimp fettuccine pasta with homemade alfredo sauce -.jpeg", name: "Smart Watch", age: 25, phone: "01059874644", address: "789 Nile Rd, Giza", salary: 7500, shift: { type: "Night", from: "12:00am", to: "08:00am" }, role: "Waiter" },
    { id: 4, staffId: "STF004", productimage:"./menuImg/Garlic Butter Steak Bites and Mash.jpg", name: "Yoga Mat", age: 35, phone:"01236445569", address: "321 Garden City, Cairo", salary: 12000, shift: { type: "Morning", from: "08:00am", to: "4:00pm" }, role: "Chef assistant" },
    { id: 5, staffId: "STF005", productimage:"./menuImg/Slow-Cooked Garlic Butter Chicken & Ribeye with….jpeg", name: "Coffee Maker", age: 30, phone:"01105588963", address: "654 Heliopolis, Cairo", salary: 8500, shift: { type: "Evening", from: "4:00pm", to: "12:00am" }, role: "Bartender" },
];

// Styled Components
const TableWrapper = styled(motion.div)`
  background-color: #1f2937;
  padding: 1.5rem;
  border-radius: 1rem;
  border: 1px solid #374151;
  backdrop-filter: blur(6px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  margin-bottom: 5rem;
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

  &:hover {
    opacity: 0.8;
  }
`;

const ShiftCell = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
`;

const ShiftType = styled.span`
  font-weight: 500;
  color: #60a5fa;
`;

const ShiftTime = styled.span`
  font-size: 0.75rem;
  color: #9ca3af;
`;

const RoleBadge = styled.span`
  background-color: #374151;
  color: #60a5fa;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 500;
  text-transform: uppercase;
`;

const StaffTable = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(PRODUCT_DATA);
  const [isModifyModalOpen, setIsModifyModalOpen] = useState(false);
  const [selectedStaff, setSelectedStaff] = useState(null);
  const [snackbar, setSnackbar] = useState({
    isVisible: false,
    message: '',
    type: 'success'
  });
  const [deleteConfirmModal, setDeleteConfirmModal] = useState({
    isOpen: false,
    staffToDelete: null
  });

  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = PRODUCT_DATA.filter(product => 
      product.name.toLowerCase().includes(term) || 
      product.staffId.toLowerCase().includes(term) ||
      product.phone.includes(term) ||
      product.address.toLowerCase().includes(term) ||
      product.salary.toString().includes(term) ||
      product.shift.type.toLowerCase().includes(term) ||
      product.role.toLowerCase().includes(term)
    );
    setFilteredProducts(filtered);
  };

  const handleDeleteClick = (staff) => {
    setDeleteConfirmModal({
      isOpen: true,
      staffToDelete: staff
    });
  };

  const handleDeleteConfirm = () => {
    const { staffToDelete } = deleteConfirmModal;
    setFilteredProducts(prev => prev.filter(product => product.id !== staffToDelete.id));
    setSnackbar({
      isVisible: true,
      message: `${staffToDelete.name} has been deleted successfully`,
      type: 'success'
    });
    setDeleteConfirmModal({ isOpen: false, staffToDelete: null });
  };

  const handleDeleteCancel = () => {
    setDeleteConfirmModal({ isOpen: false, staffToDelete: null });
  };

  const handleModify = (staff) => {
    setSelectedStaff(staff);
    setIsModifyModalOpen(true);
  };

  const handleModifySubmit = (modifiedStaff) => {
    setFilteredProducts(prev => 
      prev.map(staff => 
        staff.id === selectedStaff.id ? { ...staff, ...modifiedStaff } : staff
      )
    );
    setSnackbar({
      isVisible: true,
      message: `${modifiedStaff.name} has been modified successfully`,
      type: 'success'
    });
    setIsModifyModalOpen(false);
  };

  const handleAddStaff = (newStaff) => {
    const newId = Math.max(...filteredProducts.map(p => p.id)) + 1;
    const staffWithId = { 
      ...newStaff, 
      id: newId,
      staffId: `STF${String(newId).padStart(3, '0')}`,
      age: parseInt(newStaff.age) || 0,
      salary: parseInt(newStaff.salary) || 0,
      shift: {
        type: newStaff.shiftType || 'Morning',
        from: newStaff.shiftFrom || '08:00am',
        to: newStaff.shiftTo || '4:00pm'
      }
    };
    setFilteredProducts(prev => [...prev, staffWithId]);
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, isVisible: false }));
  };

  return (
    <TableWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <Header>
        <h2>Staff List</h2>
        <SearchInputWrapper>
          <SearchInput
            type="text"
            placeholder="Search staff..."
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
            <Th>Staff ID</Th>
            <Th>Role</Th>
            <Th>Age</Th>
            <Th>Phone</Th>
            <Th>Address</Th>
            <Th>Salary</Th>
            <Th>Shift</Th>
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
              <Td>{product.staffId}</Td>
              <Td><RoleBadge>{product.role}</RoleBadge></Td>
              <Td>{product.age}</Td>
              <Td>{product.phone}</Td>
              <Td>{product.address}</Td>
              <Td>${product.salary.toLocaleString()}</Td>
              <Td>
                <ShiftCell>
                  <ShiftType>{product.shift.type}</ShiftType>
                  <ShiftTime>{product.shift.from} - {product.shift.to}</ShiftTime>
                </ShiftCell>
              </Td>
              <Td>
                <ActionButton color="#818cf8" onClick={() => handleModify(product)}>
                  <Edit size={16} />
                </ActionButton>
                <ActionButton color="#f87171" onClick={() => handleDeleteClick(product)}>
                  <Trash2 size={16} />
                </ActionButton>
              </Td>
            </motion.tr>
          ))}
        </tbody>
      </StyledTable>

      <ModifyStaffModal
        isOpen={isModifyModalOpen}
        onClose={() => setIsModifyModalOpen(false)}
        onModify={handleModifySubmit}
        staffData={selectedStaff}
      />

      <ConfirmModal
        isOpen={deleteConfirmModal.isOpen}
        onClose={handleDeleteCancel}
        onConfirm={handleDeleteConfirm}
        title="Delete Staff Member"
        message={`Are you sure you want to delete ${deleteConfirmModal.staffToDelete?.name}? This action cannot be undone.`}
      />

      <Snackbar
        isVisible={snackbar.isVisible}
        message={snackbar.message}
        type={snackbar.type}
        onClose={handleCloseSnackbar}
      />
    </TableWrapper>
  );
};

export default StaffTable;