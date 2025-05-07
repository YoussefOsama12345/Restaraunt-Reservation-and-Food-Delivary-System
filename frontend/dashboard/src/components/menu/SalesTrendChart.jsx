import React from "react";
import styled from "styled-components";
import { motion } from "framer-motion";
import {
	LineChart,
	Line,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	ResponsiveContainer,
} from "recharts";

const salesData = [
	{ name: "Jan", sales: 4000 },
	{ name: "Feb", sales: 3000 },
	{ name: "Mar", sales: 5000 },
	{ name: "Apr", sales: 4500 },
	{ name: "May", sales: 6000 },
	{ name: "Jun", sales: 5500 },
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

const SalesTrendChart = () => {
	return (
		<ChartWrapper
		initial={{ opacity: 0, y: 20 }}
		animate={{ opacity: 1, y: 0 }}
		transition={{ delay: 0.2 }}
		role="region"
		aria-label="Sales trend line chart"
		>
		<ChartTitle>Sales Trend</ChartTitle>
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
					stroke="rgb(34, 197, 94)"
					strokeWidth={3}
					dot={{ fill: "rgb(34, 197, 94)", strokeWidth: 2, r: 6 }}
					activeDot={{ r: 8, strokeWidth: 2 }}
				/>
				</LineChart>
				</ResponsiveContainer>
			</ChartContainer>
			</ChartWrapper>
		);
};

export default SalesTrendChart;