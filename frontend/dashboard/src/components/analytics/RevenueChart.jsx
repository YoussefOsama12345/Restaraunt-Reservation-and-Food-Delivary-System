import { useState } from "react";
import { motion } from "framer-motion";
import styled from "styled-components";
import {
	AreaChart,
	Area,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	Legend,
	ResponsiveContainer,
} from "recharts";

// Sample static revenue data
const revenueData = [
	{ month: "Jan", revenue: 4000, target: 3800 },
	{ month: "Feb", revenue: 3000, target: 3600 },
	{ month: "Mar", revenue: 5000, target: 4300 },
	{ month: "Apr", revenue: 4200, target: 4700 },
	{ month: "May", revenue: 6000, target: 4200 },
	{ month: "Jun", revenue: 5500, target: 5400 },
	{ month: "Jul", revenue: 7000, target: 6400 },
];

// Styled container for the entire card
const ChartContainer = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.5); /* Tailwind's gray-800 + opacity */
	backdrop-filter: blur(8px);
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
	border: 1px solid #374151; /* Tailwind's gray-700 */
	border-radius: 1rem;
	padding: 1.5rem;
	margin-bottom: 2rem;
`;

// Flex container for title and select
const Header = styled.div`
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 1.5rem;
`;

// Dropdown for time range filter
const Select = styled.select`
	background-color: #374151;
	color: #fff;
	border-radius: 0.375rem;
	padding: 0.4rem 0.75rem;
	outline: none;
	border: none;
	font-size: 0.875rem;

	&:focus {
		box-shadow: 0 0 0 2px #3b82f6; /* Tailwind's blue-500 */
	}
`;

// Title style
const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #f3f4f6; /* Tailwind's gray-100 */
`;

const RevenueChart = () => {
	const [selectedTimeRange, setSelectedTimeRange] = useState("This Month");

	// Placeholder for future: loading, empty, or dynamic chart logic
	const isLoading = false;

	return (
		<ChartContainer
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			transition={{ delay: 0.2 }}
		>
			<Header>
				<Title>Revenue vs Target</Title>

				{/* Time range filter (static for now) */}
				<Select
					aria-label='Select time range'
					value={selectedTimeRange}
					onChange={(e) => setSelectedTimeRange(e.target.value)}
				>
					<option>This Week</option>
					<option>This Month</option>
					<option>This Quarter</option>
					<option>This Year</option>
				</Select>
			</Header>

			{/* Chart Area */}
			<div style={{ width: "100%", height: 400 }}>
				{isLoading ? (
					<p style={{ color: "#9CA3AF" }}>Loading chart...</p>
				) : (
					<ResponsiveContainer>
						<AreaChart data={revenueData}>
							{/* Grid lines */}
							<CartesianGrid strokeDasharray='3 3' stroke='#374151' />

							{/* X and Y axes */}
							<XAxis dataKey='month' stroke='#9CA3AF' />
							<YAxis stroke='#9CA3AF' />

							{/* Tooltip with dark theme */}
							<Tooltip
								contentStyle={{
									backgroundColor: "rgba(31, 41, 55, 0.8)",
									borderColor: "#4B5563",
								}}
								itemStyle={{ color: "#E5E7EB" }}
							/>

							{/* Legend */}
							<Legend />

							{/* Revenue area */}
							<Area
								type='monotone'
								dataKey='revenue'
								stroke='#8B5CF6'
								fill='#8B5CF6'
								fillOpacity={0.3}
							/>

							{/* Target area */}
							<Area
								type='monotone'
								dataKey='target'
								stroke='#10B981'
								fill='#10B981'
								fillOpacity={0.3}
							/>
						</AreaChart>
					</ResponsiveContainer>
				)}
			</div>
		</ChartContainer>
	);
};

export default RevenueChart;
