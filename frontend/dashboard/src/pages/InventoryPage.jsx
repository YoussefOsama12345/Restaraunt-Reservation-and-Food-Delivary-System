import React from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import Header from '../components/common/Header';
import { AlertTriangle, DollarSign, TrendingUp, Package } from 'lucide-react';
import StatsCard from '../components/common/StatsCard';
import InventoryTable from '../components/inventory/InventoryTable';



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

const InventoryPage = () => {
return (
    <PageWrapper>
        <Header title="Inventory" />

    <Main>
        <StatsGrid
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1 }}
        >
            <StatsCard name="Total Items" icon={Package} value="1234" color="#6366F1" />
            <StatsCard name="Top Consumption" icon={TrendingUp} value="89" color="#8B5CF6" />
            <StatsCard name="Low Stock" icon={AlertTriangle} value="23" color="#EC4899" />
            <StatsCard name="Total Revenue" icon={DollarSign} value="$543,210" color="#10B981" />
        </StatsGrid>

        <InventoryTable />

    </Main>
    </PageWrapper>
);
};

export default InventoryPage;