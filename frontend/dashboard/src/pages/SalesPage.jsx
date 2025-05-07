import { motion } from 'framer-motion';
import { DollarSign, ShoppingCart, TrendingUp, CreditCard } from 'lucide-react';
import styled from 'styled-components';

import Header from '../components/common/Header';
import SalesOverviewChart from '../components/sales/SalesOverviewChart';
import SalesByCategoryChart from '../components/sales/SalesByCategoryChart';
import DailySalesTrend from '../components/sales/DailySalesTrend';
import StatsCard from '../components/common/StatsCard';

// Static sales stats - consider making this dynamic in the future
const salesStats = {
	totalRevenue: "$1,234,567",
	averageOrderValue: "$78.90",
	conversionRate: "3.45%",
	salesGrowth: "12.3%",
};

// Styled container for the entire page
const PageContainer = styled.div`
	flex: 1;
	overflow: auto;
	position: relative;
	z-index: 10;
	background-color: #111827; /* Dark background to match topbar */
`;

// Main content area with responsive padding
const ContentWrapper = styled.main`
	max-width: 1280px;
	margin: 0 auto;
	padding: 1.5rem 1rem;

	@media (min-width: 1024px) {
		padding: 1.5rem 2rem;
	}
`;

// Grid for the stat cards
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

// Grid for the two charts at the bottom
const ChartsGrid = styled.div`
	display: grid;
	grid-template-columns: 1fr;
	gap: 3rem;
	margin-bottom: 2rem;

	@media (min-width: 1024px) {
		grid-template-columns: repeat(2, 1fr);
		gap: 5rem;
	}
`;

const SalesPage = () => {
	return (
		<PageContainer>
			{/* Page Header */}
			<Header title='Sales Dashboard' />

			<ContentWrapper>
				{/* 📊 Statistic Cards */}
				<StatsGrid
					initial={{ opacity: 0, y: 20 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 1 }}
				>
					<StatsCard
						name='Total Revenue'
						icon={DollarSign}
						value={salesStats.totalRevenue}
						color='#6366F1' // Indigo
					/>
					<StatsCard
						name='Avg. Order Value'
						icon={ShoppingCart}
						value={salesStats.averageOrderValue}
						color='#10B981' // Emerald
					/>
					<StatsCard
						name='Conversion Rate'
						icon={TrendingUp}
						value={salesStats.conversionRate}
						color='#F59E0B' // Amber
					/>
					<StatsCard
						name='Sales Growth'
						icon={CreditCard}
						value={salesStats.salesGrowth}
						color='#EF4444' // Red
					/>
				</StatsGrid>

				{/* 📈 Overview Chart */}
				<SalesOverviewChart />

				{/* 📊 Additional Charts */}
				<ChartsGrid>
					<SalesByCategoryChart />
					<DailySalesTrend />
				</ChartsGrid>
			</ContentWrapper>
		</PageContainer>
	);
};

export default SalesPage;
