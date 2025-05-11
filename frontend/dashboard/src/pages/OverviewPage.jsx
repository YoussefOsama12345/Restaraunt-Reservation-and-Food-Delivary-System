import React from 'react';
import styled, { ThemeProvider } from 'styled-components';
import { Zap, Users, BarChart, ShoppingBag } from 'lucide-react';
import SalesOverView from '../components/overview/SalesOverView.jsx';
import CategoryDistributionChart from '../components/overview/CategoryDistributionChart';
import SalesChannelChart from '../components/overview/SalesChannelChart';
import StatsCard from '../components/common/StatsCard';
import Header from '../components/common/Header';
import { motion } from 'framer-motion';

const lightTheme = {
  background: '#ffffff',
  text: '#111827',
};

const darkTheme = {
  background: '#111827',
  text: '#f9fafb',
};

const PageWrapper = styled.div`
  flex: 1;
  overflow: auto;
  position: relative;
  z-index: 10;
  background-color: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.text};
  min-height: 100vh;
  width: 100%;
`;

const Main = styled.main.attrs(() => ({ role: 'main', 'aria-label': 'Overview content section' }))`
  max-width: 1280px;
  margin: 0 auto;
  padding: 1.5rem 1rem;
  width: 100%;
  box-sizing: border-box;

  @media (min-width: 640px) {
    padding: 1.5rem 1.5rem;
  }

  @media (min-width: 1024px) {
    padding: 2rem 2rem;
  }

  @media (min-width: 1280px) {
    padding: 2.5rem 2rem;
  }
`;

const StatsGrid = styled(motion.div)`
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin-bottom: 2rem;
  width: 100%;

  @media (min-width: 480px) {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
  }
`;

const ChartsGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  width: 100%;

  @media (min-width: 768px) {
    gap: 2rem;
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
      "sales sales"
      "category channel";
    gap: 2rem;
  }

  & > *:nth-child(1) {
    grid-area: sales;
    min-height: 400px;
  }

  & > *:nth-child(2) {
    grid-area: category;
    min-height: 350px;
  }

  & > *:nth-child(3) {
    grid-area: channel;
    min-height: 350px;
  }

  @media (max-width: 1023px) {
    & > * {
      min-height: 350px;
    }
  }

  @media (max-width: 639px) {
    & > * {
      min-height: 300px;
    }
  }
`;

const OverviewPage = () => {
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  return (
    <ThemeProvider theme={prefersDark ? darkTheme : lightTheme}>
      <PageWrapper>
        <Header title="Overview" />

        <Main>
          <StatsGrid
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
          >
            <StatsCard 
              name="Total Sales" 
              icon={Zap} 
              value="$12,345" 
              color="#6366F1" 
            />
            <StatsCard 
              name="New Users" 
              icon={Users} 
              value="1,234" 
              color="#8B5CF6" 
            />
            <StatsCard 
              name="Total Products" 
              icon={ShoppingBag} 
              value="567" 
              color="#EC4899" 
            />
            <StatsCard 
              name="Conversion Rate" 
              icon={BarChart} 
              value="12.5%" 
              color="#10B981" 
            />
          </StatsGrid>

          <ChartsGrid>
            <SalesOverView />
            <CategoryDistributionChart />
            <SalesChannelChart />
          </ChartsGrid>
        </Main>
      </PageWrapper>
    </ThemeProvider>
  );
};

export default OverviewPage;