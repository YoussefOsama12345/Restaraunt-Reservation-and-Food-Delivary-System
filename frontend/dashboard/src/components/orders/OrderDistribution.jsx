import React from "react";
import { motion } from "framer-motion";
import styled from "styled-components";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend,
} from "recharts";

// Sample chart data
const orderStatusData = [
  { name: "Pending", value: 30 },
  { name: "Processing", value: 45 },
  { name: "Shipped", value: 60 },
  { name: "Delivered", value: 120 },
];

// Chart colors for each slice
const COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FED766", "#2AB7CA"];

// Styled components
const ChartWrapper = styled(motion.section)`
  background-color: rgba(31, 41, 55, 0.8);
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #374151;
  border-radius: 1rem;
  padding: 1.5rem;
  width: 100%;
`;

const Title = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #f9fafb;
  margin-bottom: 1rem;
`;

// Main component
const OrderDistribution = ({ data = orderStatusData, title = "Order Status Distribution" }) => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.3 }}
      aria-label="Order Status Pie Chart"
      role="region"
    >
      <Title>{title}</Title>

      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              aria-label="Order status distribution"
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(31, 41, 55, 0.9)",
                borderColor: "#4B5563",
              }}
              itemStyle={{ color: "#E5E7EB" }}
            />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </ChartWrapper>
  );
};

export default OrderDistribution;
