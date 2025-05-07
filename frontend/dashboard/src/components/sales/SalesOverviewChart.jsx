import { motion } from 'framer-motion';
import {
	AreaChart,
	Area,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	ResponsiveContainer
} from 'recharts';
import { useState } from 'react';
import styled from 'styled-components';

// Simulated sales data by time range
const salesData = {
	'This Week': [
		{ month: 'Mon', sales: 1200 },
		{ month: 'Tue', sales: 2100 },
		{ month: 'Wed', sales: 1800 },
		{ month: 'Thu', sales: 2300 },
		{ month: 'Fri', sales: 2600 },
		{ month: 'Sat', sales: 2000 },
		{ month: 'Sun', sales: 1900 }
	],
	'This Month': [
		{ month: 'Week 1', sales: 4000 },
		{ month: 'Week 2', sales: 3000 },
		{ month: 'Week 3', sales: 5000 },
		{ month: 'Week 4', sales: 4500 }
	],
	'This Quarter': [
		{ month: 'Jan', sales: 4000 },
		{ month: 'Feb', sales: 3000 },
		{ month: 'Mar', sales: 5000 }
	],
	'This Year': [
		{ month: 'Jan', sales: 4000 },
		{ month: 'Feb', sales: 3000 },
		{ month: 'Mar', sales: 5000 },
		{ month: 'Apr', sales: 4500 },
		{ month: 'May', sales: 6000 },
		{ month: 'Jun', sales: 5500 },
		{ month: 'Jul', sales: 7000 },
		{ month: 'Aug', sales: 6200 },
		{ month: 'Sep', sales: 5800 },
		{ month: 'Oct', sales: 6100 },
		{ month: 'Nov', sales: 6900 },
		{ month: 'Dec', sales: 7200 }
	]
};

// Styled container for the whole chart
const ChartContainer = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.5); /* Semi-transparent dark bg */
	backdrop-filter: blur(12px); /* Frosted glass effect */
	border: 1px solid #374151;
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
	border-radius: 1rem;
	padding: 1.5rem;
	margin-bottom: 2rem;
`;

// Top section: title and dropdown
const HeaderRow = styled.div`
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 1.5rem;
`;

const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #f3f4f6;
`;

const TimeRangeSelect = styled.select`
	background-color: #374151;
	color: #ffffff;
	border: none;
	border-radius: 0.375rem;
	padding: 0.25rem 0.75rem;
	font-size: 0.875rem;

	&:focus {
		outline: none;
		box-shadow: 0 0 0 2px #3b82f6; /* blue ring */
	}
`;

// Chart area
const ChartWrapper = styled.div`
	width: 100%;
	height: 20rem; /* Equivalent to h-80 in Tailwind */
`;

const SalesOverviewChart = () => {
	const [selectedTimeRange, setSelectedTimeRange] = useState('This Month');

	// Select appropriate dataset based on time range
	const chartData = salesData[selectedTimeRange] || [];

	return (
		<ChartContainer
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			transition={{ delay: 0.2 }}
		>
			{/* Chart Header with Title and Filter Dropdown */}
			<HeaderRow>
				<Title>Sales Overview</Title>
				<TimeRangeSelect
					value={selectedTimeRange}
					onChange={(e) => setSelectedTimeRange(e.target.value)}
				>
					{Object.keys(salesData).map((range) => (
						<option key={range} value={range}>
							{range}
						</option>
					))}
				</TimeRangeSelect>
			</HeaderRow>

			{/* Chart Visualization */}
			<ChartWrapper>
				<ResponsiveContainer>
					<AreaChart data={chartData}>
						<CartesianGrid strokeDasharray='3 3' stroke='#374151' />
						<XAxis dataKey='month' stroke='#9CA3AF' />
						<YAxis stroke='#9CA3AF' />
						<Tooltip
							contentStyle={{
								backgroundColor: 'rgba(31, 41, 55, 0.8)',
								borderColor: '#4B5563'
							}}
							itemStyle={{ color: '#E5E7EB' }}
						/>
						<Area
							type='monotone'
							dataKey='sales'
							stroke='#8B5CF6'
							fill='#8B5CF6'
							fillOpacity={0.3}
						/>
					</AreaChart>
				</ResponsiveContainer>
			</ChartWrapper>
		</ChartContainer>
	);
};

export default SalesOverviewChart;
