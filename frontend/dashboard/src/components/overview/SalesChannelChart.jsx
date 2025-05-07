import React from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  Legend,
  Cell,
} from 'recharts';

// Styled Components
const ChartWrapper = styled(motion.div)`
  background-color: ${({ theme }) => theme.bgSecondary || 'rgba(31, 41, 55, 0.5)'};
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.5rem;
  border: 1px solid ${({ theme }) => theme.borderColor || '#374151'};
`;

const ChartTitle = styled.h2`
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: ${({ theme }) => theme.textPrimary || '#f3f4f6'};
`;

const ChartContainer = styled.div`
  height: 20rem;
  @media (max-width: 640px) {
  height: 16rem;
  }
`;

const COLORS = ['#8B5CF6', '#3B82F6', '#22C55E', '#F59E0B', '#F43F5E'];

// Props-based chart for reusability
const SalesChannelChart = ({ title = "Sales Channel", data = [], colors = COLORS }) => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      role="region"
      aria-label="Bar chart showing sales distribution"
    >
      <ChartTitle>{title}</ChartTitle>
      <ChartContainer>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#4B5563" />
            <XAxis dataKey="name" stroke="#9ca3af" />
            <YAxis stroke="#9ca3af" />
            <Tooltip
              contentStyle={{
                backgroundColor: 'rgba(31,41,55,0.8)',
                borderColor: '#4B5563',
              }}
              itemStyle={{ color: '#E5E7EB' }}
            />
            <Legend />
            <Bar
              dataKey="value"
              isAnimationActive={true}
              animationDuration={600}
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={colors[index % colors.length]} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </ChartContainer>
    </ChartWrapper>
  );
};

// Default dataset for fallback
SalesChannelChart.defaultProps = {
  data: [
    { name: 'Website', value: 45600 },
    { name: 'Mobile App', value: 38200 },
    { name: 'Social Media', value: 18700 },
  ],
};

export default SalesChannelChart;