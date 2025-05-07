import React from "react";
import styled from "styled-components";
import { motion } from "framer-motion";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,} from "recharts";

const salesData = [
	{ name: "Jan", sales: 1000 },
	{ name: "Feb", sales: 1500 },
	{ name: "Mar", sales: 2000 },
	{ name: "Apr", sales: 3000 },
	{ name: "May", sales: 4000 },
	{ name: "Jun", sales: 5000 },
];

const ChartWrapper = styled(motion.div)`
	background-color: rgba(31, 41, 55, 0.5);
	backdrop-filter: blur(10px);
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	border-radius: 1rem;
	padding: 1.5rem;
	border: 1px solid #374151;
`;

const ChartTitle = styled.h2`
	font-size: 1.125rem;
	font-weight: 500;
	margin-bottom: 1rem;
	color: #f3f4f6;
`;

const ChartContainer = styled.div`
  	height: 20rem;
`;

const UserGrowthChart = () => {
	return (
		<ChartWrapper
		initial={{ opacity: 0, y: 20 }}
		animate={{ opacity: 1, y: 0 }}
		transition={{ delay: 0.2 }}
		role="region"
		aria-label="Sales overview line chart"
		>
		<ChartTitle>Users Growth</ChartTitle>
		<ChartContainer>
			<ResponsiveContainer width="100%" height="100%">
			<LineChart data={salesData}>
				<CartesianGrid strokeDasharray="3 3" stroke="#4B5563" />
				<XAxis dataKey="name" stroke="#9ca3af" />
				<YAxis stroke="#9ca3af" />
				<Tooltip
				contentStyle={{
					backgroundColor: "rgba(31, 41, 55, 0.8)",
					borderColor: "#4B5563",
				}}
					itemStyle={{ color: "#E5E7EB" }}
				/>
				<Line
					type="monotone"  
					dataKey="sales"
					stroke="rgb(236, 72, 153)"
					strokeWidth={3}
					dot={{ fill: "rgb(236, 72, 153)", strokeWidth: 2, r: 6 }}
					activeDot={{ r: 8, strokeWidth: 2 }}
				/>
				</LineChart>
				</ResponsiveContainer>
			</ChartContainer>
			</ChartWrapper>
		);
};

export default UserGrowthChart;