import { motion } from "framer-motion";
import styled from "styled-components";
import {
	ResponsiveContainer,
	Radar,
	RadarChart,
	PolarGrid,
	PolarAngleAxis,
	PolarRadiusAxis,
	Legend,
	Tooltip,
} from "recharts";

// Sample data for customer segmentation
const customerSegmentationData = [
	{ subject: "Engagement", A: 120, B: 110, fullMark: 150 },
	{ subject: "Loyalty", A: 98, B: 130, fullMark: 150 },
	{ subject: "Satisfaction", A: 86, B: 130, fullMark: 150 },
	{ subject: "Spend", A: 99, B: 100, fullMark: 150 },
	{ subject: "Frequency", A: 85, B: 90, fullMark: 150 },
	{ subject: "Recency", A: 65, B: 85, fullMark: 150 },
];

// Styled-components for container and chart styles
const StyledContainer = styled(motion.div)`
	background-color: #1f2937;
	background-opacity: 0.5;
	backdrop-filter: blur(10px);
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	border-radius: 12px;
	padding: 24px;
	border: 1px solid #4b5563;
`;

const Title = styled.h2`
	font-size: 1.25rem;
	font-weight: 600;
	color: #e5e7eb;
	margin-bottom: 16px;
`;

const ChartWrapper = styled.div`
	width: 100%;
	height: 300px;
`;

const CustomTooltip = styled(Tooltip)`
	background-color: rgba(31, 41, 55, 0.8) !important;
	border-color: #4b5563 !important;
	color: #e5e7eb;
`;

const CustomerSegmentation = () => {
	return (
		// Apply motion for animation effects on the chart container
		<StyledContainer
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			transition={{ delay: 0.6 }}
		>
			{/* Title of the chart */}
			<Title>Customer Segmentation</Title>

			{/* Chart container */}
			<ChartWrapper>
				<ResponsiveContainer>
					{/* Radar chart for segmentation data */}
					<RadarChart cx="50%" cy="50%" outerRadius="80%" data={customerSegmentationData}>
						{/* Polar grid for chart */}
						<PolarGrid stroke="#374151" />

						{/* Axis for each segment */}
						<PolarAngleAxis dataKey="subject" stroke="#9CA3AF" />
						<PolarRadiusAxis angle={30} domain={[0, 150]} stroke="#9CA3AF" />

						{/* Radar for each segment (A and B) */}
						<Radar name="Segment A" dataKey="A" stroke="#8B5CF6" fill="#8B5CF6" fillOpacity={0.6} />
						<Radar name="Segment B" dataKey="B" stroke="#10B981" fill="#10B981" fillOpacity={0.6} />

						{/* Legend to display chart information */}
						<Legend />

						{/* Custom Tooltip for styling the chart tooltips */}
						<CustomTooltip
							contentStyle={{
								backgroundColor: "rgba(31, 41, 55, 0.8)",
								borderColor: "#4B5563",
							}}
							itemStyle={{ color: "#E5E7EB" }}
						/>
					</RadarChart>
				</ResponsiveContainer>
			</ChartWrapper>
		</StyledContainer>
	);
};

export default CustomerSegmentation;
