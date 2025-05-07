import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { motion } from "framer-motion";
import styled from "styled-components";

// Data for the product performance bar chart
const productPerformanceData = [
  { name: "Product A", sales: 4000, revenue: 2400, profit: 2400 },
  { name: "Product B", sales: 3000, revenue: 1398, profit: 2210 },
  { name: "Product C", sales: 2000, revenue: 9800, profit: 2290 },
  { name: "Product D", sales: 2780, revenue: 3908, profit: 2000 },
  { name: "Product E", sales: 1890, revenue: 4800, profit: 2181 },
];

// Styled component for the chart wrapper
const ChartWrapper = styled(motion.div)`
  background-color: #1F2937;
  background-opacity: 0.5;
  backdrop-filter: blur(8px);
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #4a5568;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
`;

// Styled component for the title of the chart section
const Title = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #e5e7eb;
  margin-bottom: 16px;
`;

// Styled component for the chart container
const ChartContainer = styled.div`
  width: 100%;
  height: 300px;
  
`;

const ProductPerformance = () => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.4 }}
    >
      {/* Title for the chart */}
      <Title>Product Performance</Title>

      {/* Chart container */}
      <ChartContainer>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={productPerformanceData}>
            {/* Cartesian Grid for grid lines */}
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
            
            {/* X and Y Axis */}
            <XAxis dataKey="name" stroke="#9CA3AF" />
            <YAxis stroke="#9CA3AF" />
            
            {/* Tooltip with custom styles */}
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(31, 41, 55, 0.8)",
                borderColor: "#4B5563",
              }}
              itemStyle={{ color: "#E5E7EB" }}
            />
            
            {/* Legend to display the bar keys */}
            <Legend />
            
            {/* Different bars representing sales, revenue, and profit */}
            <Bar dataKey="sales" fill="#8B5CF6" />
            <Bar dataKey="revenue" fill="#10B981" />
            <Bar dataKey="profit" fill="#F59E0B" />
          </BarChart>
        </ResponsiveContainer>
      </ChartContainer>
    </ChartWrapper>
  );
};

export default ProductPerformance;
