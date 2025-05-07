import { motion } from "framer-motion"; // Importing for animations
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from "recharts"; // Charting components
import styled from "styled-components"; // Importing styled-components for custom styles

// Colors for pie chart segments to distinguish demographic groups
const COLORS = ["#8884d8", "#82ca9d", "#ffc658", "#ff8042", "#0088FE"];

// Sample data for user demographics by age groups
const userDemographicsData = [
  { name: "18-24", value: 20 },
  { name: "25-34", value: 30 },
  { name: "35-44", value: 25 },
  { name: "45-54", value: 15 },
  { name: "55+", value: 10 },
];

// Styled component for the outer chart wrapper with a blurred background and shadow
const ChartWrapper = styled(motion.div)`
  background-color: rgba(31, 41, 55, 0.5); /* Semi-transparent dark background */
  backdrop-filter: blur(12px); /* Adds a blur effect to the background for modern UI */
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2); /* Adds depth with a subtle shadow */
  border-radius: 1rem; /* Rounded corners for a softer, modern appearance */
  padding: 1.5rem; /* Adds padding around the content */
  border: 1px solid #374151; /* Border color to match dark theme */
  display: flex;
  flex-direction: column;
  align-items: center; /* Centers the content horizontally */
  justify-content: center; /* Centers the content vertically */
`;

// Title of the chart with custom styling
const Title = styled.h2`
  font-size: 1.25rem; /* Font size for the title */
  font-weight: 600; /* Bold weight for prominence */
  color: #f3f4f6; /* Light gray color for the title */
  margin-bottom: 1rem; /* Space between the title and chart */
`;

// Styled component for the container that holds the chart, ensuring proper sizing
const ChartContainer = styled.div`
  width: 100%; /* Ensures the chart takes up the full width */
  height: 300px; /* Fixed height for the chart container */
`;

const UserDemographicsChart = () => {
  return (
    <ChartWrapper
      initial={{ opacity: 0, y: 20 }} /* Initial animation state: faded and sliding */
      animate={{ opacity: 1, y: 0 }} /* Final animation state: fully visible and in place */
      transition={{ delay: 0.5 }} /* Adds a delay for a smoother fade-in effect */
    >
      {/* Title of the chart */}
      <Title>User Demographics</Title>

      {/* Container for the pie chart, ensuring proper layout */}
      <ChartContainer>
        <ResponsiveContainer>
          <PieChart>
            {/* The Pie chart itself */}
            <Pie
              data={userDemographicsData} /* Data to be displayed */
              cx="50%" /* Center the pie horizontally */
              cy="50%" /* Center the pie vertically */
              outerRadius={100} /* Set the outer radius of the pie chart */
              fill="#8884d8" /* Default fill color (for the first segment) */
              dataKey="value" /* Key used for the data */
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`} 
              /* Label displays the demographic group and percentage */
            >
              {/* Create individual segments with different colors */}
              {userDemographicsData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            {/* Tooltip that displays more information when hovering over a segment */}
            <Tooltip
              contentStyle={{
                backgroundColor: "rgba(31, 41, 55, 0.8)", /* Dark background for tooltip */
                borderColor: "#4B5563", /* Border color for the tooltip */
              }}
              itemStyle={{ color: "#E5E7EB" }} /* Light text color for better contrast */
            />
            {/* Legend to show which color corresponds to which demographic */}
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </ChartContainer>
    </ChartWrapper>
  );
};

export default UserDemographicsChart;
