import { motion } from "framer-motion";
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from "recharts";
import styled from "styled-components";

// Data for the channel performance pie chart
const channelData = [
  { name: "Organic Search", value: 4000 },
  { name: "Paid Search", value: 3000 },
  { name: "Direct", value: 2000 },
  { name: "Social Media", value: 2780 },
  { name: "Referral", value: 1890 },
  { name: "Email", value: 2390 },
];

// Define color palette for each channel segment
const COLORS = [
  "#8884d8", "#82ca9d", "#ffc658", "#ff8042", "#0088FE", "#00C49F"
];

// Styled component for the wrapper of the chart section
const ChartWrapper = styled(motion.div)`
  background-color: #1F2937;
  background-opacity: 0.5;
  backdrop-filter: blur(8px);
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #4a5568;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
`;

// Styled component for the title
const Title = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #e5e7eb;
  margin-bottom: 16px;
`;

// Styled component for the pie chart container
const ChartContainer = styled.div`
  width: 100%;
  height: 300px;
  background-color: rgba(31, 41, 55, 0.5);
`;

const ChannelPerformance = () => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.3 }}
    >
      {/* Title for the chart section */}
      <Title>Channel Performance</Title>

      {/* Responsive container for the pie chart */}
      <ChartContainer>
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            {/* Pie chart representing the channel data */}
            <Pie
              data={channelData}
              cx="50%"
              cy="50%"
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
            >
              {/* Mapping each segment to a color from COLORS array */}
              {channelData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>

            {/* Tooltip customization */}
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(31, 41, 55, 0.5)",
                borderColor: "#4B5563",
              }}
              itemStyle={{ color: "#E5E7EB" }}
            />

            {/* Legend for identifying the different channel names */}
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </ChartContainer>
    </ChartWrapper>
  );
};

export default ChannelPerformance;
