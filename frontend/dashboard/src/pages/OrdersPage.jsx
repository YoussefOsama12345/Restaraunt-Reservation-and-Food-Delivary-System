import { CheckCircle, Clock, DollarSign, ShoppingBag } from "lucide-react";
import { motion } from "framer-motion";
import styled from "styled-components";

import Header from "../components/common/Header";
import StatsCard from "../components/common/StatsCard";
import DailyOrders from "../components/orders/DailyOrders";
import OrderDistribution from "../components/orders/OrderDistribution";
import OrdersTable from "../components/orders/OrdersTable";

// 📊 Sample order statistics data
const orderStats = {
	totalOrders: "1,234",
	pendingOrders: "56",
	completedOrders: "1,178",
	totalRevenue: "$98,765"
};

/* ------------------------- Styled Components ------------------------- */

// Main wrapper for scrollable content
const PageWrapper = styled.div`
	flex: 1;
	position: relative;
	z-index: 10;
	overflow: auto;
	background-color: #111827;
`;

// Main content container
const MainContent = styled.main`
	max-width: 80rem; // 1280px
	margin: 0 auto;
	padding: 1.5rem 1rem;

	@media (min-width: 1024px) {
		padding: 1.5rem 2rem;
	}
`;

// Grid for the stats cards
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

// Grid for the two main order charts
const ChartsGrid = styled.div`
	display: grid;
	grid-template-columns: 1fr;
	gap: 2rem;
	margin-bottom: 2rem;

	@media (min-width: 1024px) {
		grid-template-columns: repeat(2, 1fr);
	}
`;

/* ------------------------- Component ------------------------- */

const OrdersPage = () => {
	return (
		<PageWrapper>
			{/* 🧭 Page Header */}
			<Header title="Orders" />

			{/* 📦 Main Section */}
			<MainContent>
				{/* 📊 Statistics Cards */}
				<StatsGrid
					initial={{ opacity: 0, y: 20 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 1 }}
				>
					<StatsCard name="Total Orders" icon={ShoppingBag} value={orderStats.totalOrders} color="#6366F1" />
					<StatsCard name="Pending Orders" icon={Clock} value={orderStats.pendingOrders} color="#F59E0B" />
					<StatsCard name="Completed Orders" icon={CheckCircle} value={orderStats.completedOrders} color="#10B981" />
					<StatsCard name="Total Revenue" icon={DollarSign} value={orderStats.totalRevenue} color="#EF4444" />
				</StatsGrid>

				{/* 📈 Order Charts */}
				<ChartsGrid>
					<DailyOrders />
					<OrderDistribution />
				</ChartsGrid>

				{/* 📋 Orders Table */}
				<OrdersTable />
			</MainContent>
		</PageWrapper>
	);
};

export default OrdersPage;
