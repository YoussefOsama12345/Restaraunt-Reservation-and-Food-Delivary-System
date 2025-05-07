import React from 'react';
import { motion } from 'framer-motion';
import styled from 'styled-components';
import {PieChart, Pie, Cell, Tooltip ,Legend , ResponsiveContainer} from 'recharts';

const categoryData = [
    { name: 'Electronics', value: 4500 },
    { name: 'Clothing', value: 3200 },
    { name: 'Home & Garden', value: 2800 },
    { name: 'Books', value: 2100 },
    { name: 'Sports & Outdoors', value: 1900 }
];

const COLORS = ['#8B5CF6', '#3B82F6', '#22C55E', '#F59E0B', '#F43F5E'];


const ChartWrapper = styled(motion.div)`
    background-color: rgba(31, 41, 55, 0.5); 
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 1.5rem;
    border: 1px solid #374151; 
`;

const ChartTitle = styled.h2`
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #f3f4f6; 
`;

const ChartContainer = styled.div`
    width: 100%;
    height: 300px;
    position: relative;
`;


const CategoryDistributionChart = () => {
    return (
        <ChartWrapper
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3 }}
        >
        <ChartTitle>Category Distribution</ChartTitle>
        <ChartContainer>
            <ResponsiveContainer width="100%" height="100%">
            <PieChart>
                <Pie
                data={categoryData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                labelLine={false}
                outerRadius={80}
                fill="#8884d8"
                animationBegin={0}
                animationDuration={1500}
                animationEasing="ease-out"
                label={({ name, percent }) =>
                    `${name} (${(percent * 100).toFixed(0)}%)`
                }
                >
                {categoryData.map((entry, index) => (
                    <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                    />
                ))}
                </Pie>
                <Tooltip
                contentStyle={{
                    backgroundColor: 'rgba(31,41,55,0.8)',
                    borderColor: '#4B5563',
                    color: '#E5E7EB'
                }}
                itemStyle={{ color: '#E5E7EB' }}
                />
                <Legend />
            </PieChart>
            </ResponsiveContainer>
        </ChartContainer>
        </ChartWrapper>
    );
};

export default CategoryDistributionChart;
