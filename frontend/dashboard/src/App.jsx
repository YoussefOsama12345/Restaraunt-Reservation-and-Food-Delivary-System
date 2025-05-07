import React from 'react';
import styled, { ThemeProvider, createGlobalStyle } from 'styled-components';
import { Routes, Route } from 'react-router-dom';
import Sidebar from './components/common/Sidebar';
import OverviewPage from './pages/OverviewPage';
import MenuPages from './pages/MenuPages';
import UsersPage from './pages/UsersPage';
import SalesPage from './pages/SalesPage';
import OrdersPage from './pages/OrdersPage';
import AnalyticsPage from './pages/AnalyticsPage';
import InventoryPage from './pages/InventoryPage';
import StaffPage from './pages/StaffPage';
import CategoryPage from './pages/CategoryPage';




// 🌗 Global Style
const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    background-color: ${({ theme }) => theme.bodyBg};
    color: ${({ theme }) => theme.textColor};
    font-family: 'Segoe UI', sans-serif;
  }
`;

// 🎨 Themes
const lightTheme = {
  bodyBg: '#ffffff',
  textColor: '#111827',
  gradient: 'linear-gradient(to bottom right, #ffffff, #f3f4f6, #e5e7eb)',
  blur: 'blur(4px)',
};

const darkTheme = {
  bodyBg: '#111827',
  textColor: '#f3f4f6',
  gradient: 'linear-gradient(to bottom right, #111827, #1f2937, #111827)',
  blur: 'blur(4px)',
};

// 📦 Styled Components
const AppWrapper = styled.div`
  display: flex;
  height: 100vh;
  overflow: hidden;
  position: relative;
`;

const BackgroundLayer = styled.div`
  position: fixed;
  inset: 0;
  z-index: 0;
`;

const GradientOverlay = styled.div`
  position: absolute;
  inset: 0;
  background: ${({ theme }) => theme.gradient};
  opacity: 0.8;
`;

const BlurLayer = styled.div`
  position: absolute;
  inset: 0;
  backdrop-filter: ${({ theme }) => theme.blur};
`;

const ContentArea = styled.div`
  flex: 1;
  position: relative;
  z-index: 10;
  overflow-y: auto;
`;

// 🚀 App Entry
const App = () => {
  const prefersDarkMode = window.matchMedia?.('(prefers-color-scheme: dark)').matches;
  const activeTheme = prefersDarkMode ? darkTheme : lightTheme;

  return (
    <ThemeProvider theme={activeTheme}>
      <GlobalStyle />
      <AppWrapper>
        <BackgroundLayer>
          <GradientOverlay />
          <BlurLayer />
        </BackgroundLayer>

        <Sidebar />
        <ContentArea>
          <Routes>
            <Route path="/" element={<OverviewPage />} />
            <Route path="/menu" element={<MenuPages />} />
            <Route path="/users" element={<UsersPage />} />
            <Route path="/sales" element={<SalesPage />} />
            <Route path="/orders" element={<OrdersPage />} />
            <Route path="/analytics" element={<AnalyticsPage />} />
            <Route path="/inventory" element={<InventoryPage />} /> 
            <Route path="/category" element={<CategoryPage />} />
            <Route path="/staff" element={<StaffPage />} />
          </Routes>
        </ContentArea>
      </AppWrapper>
    </ThemeProvider>
  );
};

export default App;
