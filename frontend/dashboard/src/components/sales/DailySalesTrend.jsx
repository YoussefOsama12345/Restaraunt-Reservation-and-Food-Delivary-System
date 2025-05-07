import { motion } from "framer-motion";
import {
	BarChart,
	Bar,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	ResponsiveContainer
} from "recharts";
import styled from "styled-components";

// ✅ Sample data showing daily sales trends
const dailySalesData = [
	{ name: "Mon", sales: 1000 },
	{ name: "Tue", sales: 1200 },
	{ name: "Wed", sales: 900 },
	{ name: "Thu", sales: 1100 },
	{ name: "Fri", sales: 1300 },
	{ name: "Sat", sales: 1600 },
	{ name: "Sun", sales: 1400 }
];

/* --------------------------- Styled Components --------------------------- */

// 🔳 Container with frosted glass effect and animation
const ChartContainer = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.5);
	backdrop-filter: blur(12px);
	border: 1px solid #374151;
	border-radius: 1rem;
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
	padding: 1.75rem;
	width: auto;
	height: auto;
	min-height: 32rem;
	display: flex;
	flex-direction: column;
	transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;

	&:hover {
		transform: translateY(-2px);
		box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
	}
`;

// 📌 Title for the chart
const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #f3f4f6;
	margin-bottom: 1.5rem;
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding-bottom: 1rem;
	border-bottom: 1px solid rgba(55, 65, 81, 0.5);
`;

// 📈 Responsive wrapper for the chart
const ChartWrapper = styled.div`
	width: 100%;
	height: 24rem;
	display: flex;
	flex-direction: column;
	justify-content: center;
	position: relative;
	margin-top: 0.5rem;
`;

/* --------------------------- Component --------------------------- */

const DailySalesTrend = () => {
	return (
		<ChartContainer
			initial={{ opacity: 0, y: 20 }} // ✨ Animate from below
			animate={{ opacity: 1, y: 0 }}  // ✨ Animate into view
			transition={{ delay: 0.3 }}     // ⏱ Staggered animation delay
		>
			{/* 🔠 Section Heading */}
			<Title>Daily Sales Trend</Title>

			{/* 🧊 Bar Chart */}
			<ChartWrapper>
				<ResponsiveContainer>
					<BarChart data={dailySalesData}>
						{/* Grid lines */}
						<CartesianGrid strokeDasharray="3 3" stroke="#374151" />
						{/* X and Y axis with styled text */}
						<XAxis dataKey="name" stroke="#9CA3AF" />
						<YAxis stroke="#9CA3AF" />
						
						{/* Tooltip with dark theme */}
						<Tooltip
							contentStyle={{
								backgroundColor: "rgba(31, 41, 55, 0.8)",
								borderColor: "#4B5563"
							}}
							itemStyle={{ color: "#E5E7EB" }}
						/>

						{/* Bars with rounded corners */}
						<Bar
							dataKey="sales"
							fill="#10B981" // Emerald green
							radius={[6, 6, 0, 0]} // Rounded top corners
						/>
					</BarChart>
				</ResponsiveContainer>
			</ChartWrapper>
		</ChartContainer>
	);
};

export default DailySalesTrend;
