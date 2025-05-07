import { motion } from "framer-motion";
import { DollarSign, Users, ShoppingBag, Eye, ArrowDownRight, ArrowUpRight } from "lucide-react";
import styled from "styled-components";

// Data structure for dashboard overview cards
const overviewData = [
  { name: "Revenue", value: "$1,234,567", change: 12.5, icon: DollarSign },
  { name: "Users", value: "45,678", change: 8.3, icon: Users },
  { name: "Orders", value: "9,876", change: -3.2, icon: ShoppingBag },
  { name: "Page Views", value: "1,234,567", change: 15.7, icon: Eye },
];

// Styled container for all cards
const Grid = styled.div`
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(1, 1fr);

  @media (min-width: 640px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(4, 1fr);
  }

  margin-bottom: 2rem;
`;

// Styled single card container
const Card = styled(motion.div)`
  background-color: rgba(31, 41, 55, 0.6);
  backdrop-filter: blur(12px);
  border: 1px solid #374151;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease;
  &:hover {
    transform: translateY(-4px);
  }
`;

// Styled icon wrapper
const IconWrapper = styled.div`
  width: 22px ;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  border-radius: 16px;
  background-color: ${({ isPositive }) =>
    isPositive ? "rgba(34, 197, 94, 0.2)" : "rgba(239, 68, 68, 0.2)"};
`;

// Styled change indicator
const ChangeWrapper = styled.div`
  margin-top: 1rem;
  display: flex;
  align-items: center;
  color: ${({ isPositive }) => (isPositive ? "#22C55E" : "#EF4444")};
`;

// Styled text elements
const Title = styled.h3`
  font-size: 0.875rem;
  font-weight: 500;
  color: #9ca3af;
`;

const Value = styled.p`
  margin-top: 0.25rem;
  font-size: 1.25rem;
  font-weight: 600;
  color: #f3f4f6;
`;

const Percentage = styled.span`
  margin-left: 0.25rem;
  font-size: 0.875rem;
  font-weight: 500;
`;

const Comparison = styled.span`
  margin-left: 0.5rem;
  font-size: 0.875rem;
  color: #9ca3af;
`;

const OverviewCards = () => {
  return (
    <Grid>
      {overviewData.map((item, index) => {
        const Icon = item.icon;
        const isPositive = item.change >= 0;

        return (
          <Card
            key={item.name}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            role="region"
            aria-label={`${item.name} summary`}
          >
            {/* Card Header */}
            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <div>
                <Title>{item.name}</Title>
                <Value>{item.value}</Value>
              </div>
              <IconWrapper isPositive={isPositive}>
                <Icon size={24} color={isPositive ? "#22C55E" : "#EF4444"} />
              </IconWrapper>
            </div>

            {/* Change Indicator */}
            <ChangeWrapper isPositive={isPositive}>
              {isPositive ? <ArrowUpRight size={20} /> : <ArrowDownRight size={20} />}
              <Percentage>{Math.abs(item.change)}%</Percentage>
              <Comparison>vs last period</Comparison>
            </ChangeWrapper>
          </Card>
        );
      })}
    </Grid>
  );
};

export default OverviewCards;
