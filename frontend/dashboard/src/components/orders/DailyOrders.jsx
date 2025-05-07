import { motion } from "framer-motion";
import styled from "styled-components";
import {
	LineChart,
	Line,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	Legend,
	ResponsiveContainer
} from "recharts";

// 📊 Sample daily orders data
const dailyOrdersData = [
	{ date: "07/01", orders: 45 },
	{ date: "07/02", orders: 52 },
	{ date: "07/03", orders: 49 },
	{ date: "07/04", orders: 60 },
	{ date: "07/05", orders: 55 },
	{ date: "07/06", orders: 58 },
	{ date: "07/07", orders: 62 }
];

/* ------------------------- Styled Components ------------------------- */

// Container for the chart card
const ChartCard = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.8); 
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
	border-radius: 1rem;
	padding: 1.5rem;
	border: 1px solid #374151;
`;

// Chart title
const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #f3f4f6;
	margin-bottom: 1rem;
`;

// Wrapper for the chart height/width
const ChartWrapper = styled.div`
	width: 100%;
	height: 300px;
`;

/* ------------------------- Component ------------------------- */

const DailyOrders = () => {
	return (
		<ChartCard
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			transition={{ delay: 0.2 }}
		>
			<Title>Daily Orders</Title>

			<ChartWrapper>
				<ResponsiveContainer>
					<LineChart data={dailyOrdersData}>
						<CartesianGrid strokeDasharray="3 3" stroke="#374151" />
						<XAxis dataKey="date" stroke="#9CA3AF" />
						<YAxis stroke="#9CA3AF" />
						<Tooltip
							contentStyle={{
								backgroundColor: "rgba(31, 41, 55, 0.8)",
								borderColor: "#4B5563"
							}}
							itemStyle={{ color: "#E5E7EB" }}
						/>
						<Legend />
						<Line
							type="monotone" dataKey="orders" stroke="rgb(255, 128, 66)" strokeWidth={2}
						/>
					</LineChart>
				</ResponsiveContainer>
			</ChartWrapper>
		</ChartCard>
	);
};

export default DailyOrders;
