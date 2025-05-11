import styled from 'styled-components';
import { motion } from 'framer-motion';
import { UsersIcon, UserPlus, UserCheck, UserX, Plus } from 'lucide-react';
import { useState } from 'react';

import Header from '../components/common/Header';
import StatsCard from '../components/common/StatsCard';
import UsersTable from '../components/users/UsersTable';
import UserGrowthChart from '../components/users/UserGrowthChart';
import UserActivityHeatmap from '../components/users/UserActivityHeatmap';
import UserDemographicsChart from '../components/users/UserDemographicsChart';
import AddUserModal from '../components/users/AddUserModal';
import ModifyUserModal from '../components/users/ModifyUserModal';
import ConfirmModal from '../components/common/ConfirmModal';
import Snackbar from '../components/common/Snackbar';

// Styled component for the outer container of the page
const PageWrapper = styled.div`
  flex: 1;
  overflow: auto;
  position: relative;
  z-index: 10;
  background-color: #111827;
`;

// Main content area with responsive padding
const MainContent = styled.main`
  max-width: 1120px;
  margin: 0 auto;
  padding: 1.5rem 1rem;

  @media (min-width: 1024px) {
    padding: 1.5rem 2rem;
  }
`;

// Grid for statistics cards (Total Users, Active Users, etc.)
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

// Grid layout for data visualizations/charts
const ChartsGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin-top: 2rem;

  @media (min-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
      "growth activity"
      "demographics demographics";
  }

  & > *:nth-child(1) {
    grid-area: growth;
  }

  & > *:nth-child(2) {
    grid-area: activity;
  }

  & > *:nth-child(3) {
    grid-area: demographics;
  }
`;

// User statistics data (this could come from an API in the future)
const userStats = {
  totalUsers: 152845,
  newUsersToday: 243,
  activeUsers: 98520,
  churnRate: '2.4%',
};

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

// UsersPage component definition
const UsersPage = () => {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [isModifyModalOpen, setIsModifyModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);
  const [userToDelete, setUserToDelete] = useState(null);
  const [users, setUsers] = useState([
    { id: 1, name: "John Doe", userId: 2245, email: "john@example.com", role: "Customer", status: "Active" },
    { id: 2, name: "Jane Smith", userId: 2246, email: "jane@example.com", role: "Admin", status: "Active" },
    { id: 3, name: "Bob Johnson", userId: 2247, email: "bob@example.com", role: "Customer", status: "Inactive" },
    { id: 4, name: "Alice Brown", userId: 2248, email: "alice@example.com", role: "Customer", status: "Active" },
    { id: 5, name: "Charlie Wilson", userId: 2249, email: "charlie@example.com", role: "Moderator", status: "Active" }
  ]);
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
    setSelectedUser(null);
  };

  const handleAddUser = (newUser) => {
    // Here you would typically make an API call to add the user
    console.log('New user:', newUser);
    setSnackbar({
      isVisible: true,
      message: 'User added successfully',
      type: 'success'
    });
    setIsAddModalOpen(false);
  };

  const handleModifyUser = (modifiedUser) => {
    // Here you would typically make an API call to update the user
    console.log('Modified user:', modifiedUser);
    setSnackbar({
      isVisible: true,
      message: 'User modified successfully',
      type: 'success'
    });
    setIsModifyModalOpen(false);
    setSelectedUser(null);
  };

  const handleEditClick = (user) => {
    setSelectedUser(user);
    setIsModifyModalOpen(true);
  };

  const handleDeleteClick = (user) => {
    setUserToDelete(user);
    setIsDeleteModalOpen(true);
  };

  const handleConfirmDelete = () => {
    // Remove the user from the users array
    setUsers(prevUsers => prevUsers.filter(user => user.id !== userToDelete.id));
    
    setSnackbar({
      isVisible: true,
      message: 'User deleted successfully',
      type: 'success'
    });
    setIsDeleteModalOpen(false);
    setUserToDelete(null);
  };

  const handleCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setUserToDelete(null);
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, isVisible: false }));
  };

  return (
    <PageWrapper>
      {/* Page title/header */}
      <Header title="Users" />

      <MainContent>
        {/* Animated statistics cards grid */}
        <StatsGrid
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <StatsCard
            name="Total Users"
            icon={UsersIcon}
            value={userStats.totalUsers.toLocaleString()}
            color="#6366F1"
          />
          <StatsCard
            name="New Users Today"
            icon={UserPlus}
            value={userStats.newUsersToday}
            color="#10B981"
          />
          <StatsCard
            name="Active Users"
            icon={UserCheck}
            value={userStats.activeUsers.toLocaleString()}
            color="#F59E0B"
          />
          <StatsCard
            name="Churn Rate"
            icon={UserX}
            value={userStats.churnRate}
            color="#EF4444"
          />
        </StatsGrid>

        {/* Table of users */}
        <UsersTable 
          users={users}
          onEditClick={handleEditClick}
          onDeleteClick={handleDeleteClick}
        />

        <AddButton onClick={handleAddClick}>
          <Plus size={20} />
        </AddButton>

        {/* Charts grid for activity, demographics, and growth */}
        <ChartsGrid>
          <UserGrowthChart />
          <UserActivityHeatmap />
          <UserDemographicsChart />
        </ChartsGrid>

        <AddUserModal
          isOpen={isAddModalOpen}
          onClose={handleCloseAddModal}
          onSubmit={handleAddUser}
        />

        <ModifyUserModal
          isOpen={isModifyModalOpen}
          onClose={handleCloseModifyModal}
          onSubmit={handleModifyUser}
          user={selectedUser}
        />

        <ConfirmModal
          isOpen={isDeleteModalOpen}
          onClose={handleCloseDeleteModal}
          onConfirm={handleConfirmDelete}
          title="Delete User"
          message={`Are you sure you want to delete ${userToDelete?.name}? This action cannot be undone.`}
        />

        <Snackbar
          isVisible={snackbar.isVisible}
          message={snackbar.message}
          type={snackbar.type}
          onClose={handleCloseSnackbar}
        />
      </MainContent>
    </PageWrapper>
  );
};

export default UsersPage;
