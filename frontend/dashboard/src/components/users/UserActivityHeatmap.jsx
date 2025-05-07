import { motion } from 'framer-motion';
import styled from 'styled-components';
import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

// Sample user activity data by time block and day
const userActivityData = [
  { name: 'Mon', '0-4': 20, '4-8': 40, '8-12': 60, '12-16': 80, '16-20': 100, '20-24': 30 },
  { name: 'Tue', '0-4': 30, '4-8': 50, '8-12': 70, '12-16': 90, '16-20': 110, '20-24': 40 },
  { name: 'Wed', '0-4': 40, '4-8': 60, '8-12': 80, '12-16': 100, '16-20': 120, '20-24': 50 },
  { name: 'Thu', '0-4': 50, '4-8': 70, '8-12': 90, '12-16': 110, '16-20': 130, '20-24': 60 },
  { name: 'Fri', '0-4': 60, '4-8': 80, '8-12': 100, '12-16': 120, '16-20': 140, '20-24': 70 },
  { name: 'Sat', '0-4': 70, '4-8': 90, '8-12': 110, '12-16': 130, '16-20': 150, '20-24': 80 },
  { name: 'Sun', '0-4': 80, '4-8': 100, '8-12': 120, '12-16': 140, '16-20': 160, '20-24': 90 },
];

// Styled components for layout and styling
// This component wraps the entire chart with a blurred background and shadow effect.
const ChartWrapper = styled(motion.div)`
  background-color: rgba(31, 41, 55, 0.5); // Gray-800 with opacity for background
  backdrop-filter: blur(12px); // Applies a blur effect on the background
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2); // Shadow to make the chart stand out
  border-radius: 1rem; // Rounded corners for a softer look
  padding: 1.5rem; // Adds spacing around the chart content
  border: 1px solid #374151; // Gray-700 border for subtle distinction
`;

// Title for the chart with some styling
const Title = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #f3f4f6; // Gray-100 for text color
  margin-bottom: 1rem; // Spacing below the title
`;

const UserActivityHeatmap = () => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }} // Initial animation properties: fading in and sliding up
      animate={{ opacity: 1, y: 0 }} // Final animation properties: fully visible and in place
      transition={{ delay: 0.4 }} // Delays the animation for a smoother effect
    >
      <Title>User Activity Heatmap</Title> {/* The title of the chart */}
      
      {/* Responsive container ensures the chart resizes correctly based on available space */}
      <div style={{ width: '100%', height: 300 }}>
        <ResponsiveContainer>
          <BarChart data={userActivityData}>
            {/* Adds a grid background with a dashed pattern */}
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
            
            {/* X-axis displaying the day of the week */}
            <XAxis dataKey="name" stroke="#9CA3AF" />
            
            {/* Y-axis to represent the user activity count */}
            <YAxis stroke="#9CA3AF" />
            
            {/* Tooltip for displaying data on hover */}
            <Tooltip
              contentStyle={{
                backgroundColor: 'rgba(31, 41, 55, 0.8)', // Dark background for tooltip
                borderColor: '#4B5563', // Gray border for tooltip
              }}
              itemStyle={{ color: '#E5E7EB' }} // Light text color for items inside the tooltip
            />
            
            {/* Legend to identify each time block */}
            <Legend />
            
            {/* Stacked bar segments per time period */}
            <Bar dataKey="0-4" stackId="a" fill="#6366F1" /> {/* Activity from 0-4 hours */}
            <Bar dataKey="4-8" stackId="a" fill="#8B5CF6" /> {/* Activity from 4-8 hours */}
            <Bar dataKey="8-12" stackId="a" fill="#EC4899" /> {/* Activity from 8-12 hours */}
            <Bar dataKey="12-16" stackId="a" fill="#10B981" /> {/* Activity from 12-16 hours */}
            <Bar dataKey="16-20" stackId="a" fill="#F59E0B" /> {/* Activity from 16-20 hours */}
            <Bar dataKey="20-24" stackId="a" fill="#3B82F6" /> {/* Activity from 20-24 hours */}
          </BarChart>
        </ResponsiveContainer>
      </div>
    </ChartWrapper>
  );
};

export default UserActivityHeatmap;
