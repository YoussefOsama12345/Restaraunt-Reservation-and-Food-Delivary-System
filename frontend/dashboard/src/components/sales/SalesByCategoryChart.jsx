import { motion } from "framer-motion";
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer
} from "recharts";
import styled from "styled-components";

// Sample sales data by category
const salesByCategory = [
	{ name: "Electronics", value: 400 },
	{ name: "Clothing", value: 300 },
	{ name: "Home & Garden", value: 200 },
	{ name: "Books", value: 100 },
	{ name: "Others", value: 150 }
];

// Define a color palette for pie slices
const COLORS = ["#6366F1", "#10B981", "#F59E0B", "#EF4444", "#3B82F6"];

// Styled wrapper with modern UI effects
const ChartContainer = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.5);
	backdrop-filter: blur(12px);
	border: 1px solid #374151;
	border-radius: 1rem;
	box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
	padding: 1.75rem;
	width: 100%;
	height: auto;
	display: flex;
	flex-direction: column;
	transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;

	&:hover {
		transform: translateY(-2px);
		box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
	}
`;

// Styled title for the chart
const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #f3f4f6;
	margin-bottom: 2rem;
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding-bottom: 1rem;
	border-bottom: 1px solid rgba(55, 65, 81, 0.5);
`;

const TotalValue = styled.span`
	font-size: 0.875rem;
	color: #9ca3af;
	font-weight: normal;
	background-color: rgba(55, 65, 81, 0.3);
	padding: 0.25rem 0.75rem;
	border-radius: 9999px;
`;

// Wrapper to control chart size
const ChartWrapper = styled.div`
	width: 100%;
	height: 24rem;
	display: flex;
	flex-direction: column;
	justify-content: center;
	position: relative;
	margin-top: 0.5rem;
`;

const SalesByCategoryChart = () => {
	// Calculate total sales
	const totalSales = salesByCategory.reduce((sum, item) => sum + item.value, 0);

	// Custom tooltip component
	const CustomTooltip = ({ active, payload }) => {
		if (active && payload && payload.length) {
			const data = payload[0].payload;
			const percentage = ((data.value / totalSales) * 100).toFixed(1);
			
			return (
				<div style={{
					backgroundColor: 'rgba(31, 41, 55, 0.95)',
					padding: '12px',
					border: '1px solid #374151',
					borderRadius: '8px',
					boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
				}}>
					<p style={{ color: '#f3f4f6', margin: '0 0 4px 0', fontWeight: '600' }}>{data.name}</p>
					<p style={{ color: '#9ca3af', margin: '0 0 4px 0' }}>Value: ${data.value.toLocaleString()}</p>
					<p style={{ color: '#10B981', margin: '0' }}>Share: {percentage}%</p>
				</div>
			);
		}
		return null;
	};

	return (
		<ChartContainer
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			transition={{ delay: 0.3 }}
		>
			<Title>
				Sales by Category
				<TotalValue>Total: ${totalSales.toLocaleString()}</TotalValue>
			</Title>

			<ChartWrapper>
				<ResponsiveContainer>
					<PieChart>
						<Pie
							data={salesByCategory}
							cx="50%"
							cy="50%"
							outerRadius={110}
							innerRadius={55}
							dataKey="value"
							label={({ name, percent }) =>
								`${name} ${(percent * 100).toFixed(0)}%`
							}
							labelLine={false}
							animationBegin={0}
							animationDuration={1000}
						>
							{salesByCategory.map((entry, index) => (
								<Cell
									key={`cell-${index}`}
									fill={COLORS[index % COLORS.length]}
									stroke="#111827"
									strokeWidth={2}
								/>
							))}
						</Pie>

						<Tooltip content={<CustomTooltip />} />
						<Legend
							verticalAlign="bottom"
							height={36}
							iconType="circle"
							align="center"
							wrapperStyle={{
								paddingTop: "1.5rem",
								color: "#f3f4f6"
							}}
						/>
					</PieChart>
				</ResponsiveContainer>
			</ChartWrapper>
		</ChartContainer>
	);
};

export default SalesByCategoryChart;
