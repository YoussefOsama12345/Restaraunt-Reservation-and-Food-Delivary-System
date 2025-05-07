import styled from 'styled-components';
import { motion } from 'framer-motion';
import { UsersIcon, UserPlus, UserCheck, UserX } from 'lucide-react';

import Header from '../components/common/Header';
import StatsCard from '../components/common/StatsCard';
import UsersTable from '../components/users/UsersTable';
import UserGrowthChart from '../components/users/UserGrowthChart';
import UserActivityHeatmap from '../components/users/UserActivityHeatmap';
import UserDemographicsChart from '../components/users/UserDemographicsChart';

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

// UsersPage component definition
const UsersPage = () => {
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
        <UsersTable />

        {/* Charts grid for activity, demographics, and growth */}
        <ChartsGrid>
          <UserGrowthChart />
          <UserActivityHeatmap />
          <UserDemographicsChart />
        </ChartsGrid>
      </MainContent>
    </PageWrapper>
  );
};

export default UsersPage;
