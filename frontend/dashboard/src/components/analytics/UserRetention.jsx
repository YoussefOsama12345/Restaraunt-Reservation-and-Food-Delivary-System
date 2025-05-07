import { useState, useMemo } from "react";
import { motion } from "framer-motion";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";
import styled from "styled-components";

// Sample Data for User Retention
const userRetentionData = [
  { name: "Week 1", retention: 100 },
  { name: "Week 2", retention: 75 },
  { name: "Week 3", retention: 60 },
  { name: "Week 4", retention: 50 },
  { name: "Week 5", retention: 45 },
  { name: "Week 6", retention: 40 },
  { name: "Week 7", retention: 38 },
];

// Styled-components for the container
const ChartContainer = styled(motion.div)`
  background-color: #1f2937;
  background-opacity: 0.5;
  backdrop-filter: blur(20px);
  border-radius: 1rem;
  padding: 1.5rem;
  border: 1px solid #374151;
`;

// Component for User Retention Chart
const UserRetention = () => {
  // State to manage animation delay (if needed for future enhancements)
  const [animationDelay] = useState(0.5);

  // Memoize the chart data for optimization (avoid unnecessary re-renders)
  const chartData = useMemo(() => userRetentionData, []);

  return (
    <ChartContainer
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: animationDelay }}
    >
      {/* Title */}
      <h2 style={{ color: '#E5E7EB', fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>User Retention</h2>

      {/* Chart Container */}
      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <LineChart data={chartData}>
            {/* Grid Lines */}
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
            
            {/* X and Y Axis */}
            <XAxis dataKey="name" stroke="#9CA3AF" />
            <YAxis stroke="#9CA3AF" />
            
            {/* Tooltip for Interactivity */}
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(31, 41, 55, 0.8)",
                borderColor: "#4B5563",
              }}
              itemStyle={{ color: "#E5E7EB" }}
            />
            
            {/* Legend to Display Key Information */}
            <Legend />
            
            {/* Line representing User Retention */}
            <Line type="monotone" dataKey="retention" stroke="rgb(0, 136, 254)" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </ChartContainer>
  );
};

export default UserRetention;
