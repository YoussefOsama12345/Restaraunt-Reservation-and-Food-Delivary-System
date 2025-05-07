import styled from "styled-components";
import Header from "../components/common/Header";
import OverviewCards from "../components/analytics/OverviewCards";
import RevenueChart from "../components/analytics/RevenueChart";
import ChannelPerformance from "../components/analytics/ChannelPerformance";
import ProductPerformance from "../components/analytics/ProductPerformance";
import UserRetention from "../components/analytics/UserRetention";
import CustomerSegmentation from "../components/analytics/CustomerSegmentation";

// Styled container for the whole page
const PageContainer = styled.div`
  flex: 1;
  overflow: auto;
  position: relative;
  z-index: 10;
  background-color: #111827; // Tailwind's bg-gray-900
`;

// Main content wrapper with max width and padding
const MainContent = styled.main`
  max-width: 1280px;
  margin: 0 auto;
  padding: 1.5rem 1rem;

  @media (min-width: 1024px) {
    padding: 1.5rem 2rem;
  }
`;

// Responsive grid for analytical sections
const GridTwoCol = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-bottom: 2rem;

  @media (min-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
  }
`;

const AnalyticsPage = () => {
  return (
    <PageContainer>
      {/* Dashboard Header */}
      <Header title="Analytics Dashboard" />

      <MainContent>
        {/* Overview section with metrics/stat cards */}
        <OverviewCards />

        {/* Revenue trend line or bar chart */}
        <RevenueChart />

        {/* Two-column grid section for various performance and analytics charts */}
        <GridTwoCol>
            <ChannelPerformance />
            <ProductPerformance />
            <UserRetention />
            <CustomerSegmentation />
        </GridTwoCol>
      </MainContent>
    </PageContainer>
  );
};

export default AnalyticsPage;
