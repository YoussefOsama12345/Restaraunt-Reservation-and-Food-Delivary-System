import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import styled, { ThemeProvider } from 'styled-components';
import { useEffect, useRef, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

import GlobalStyle from './styles/GlobalStyle';

import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Categories from './components/Categories';
import FeaturedDishes from './components/FeaturedDishes';
import Testimonials from './components/Testimonials';
import Contact from './components/Contact';
import Footer from './components/Footer';
import Team from './components/Team';
import Values from './components/Values';
import Mission from './components/Mission';
import Reservation from './components/Reservation';
import Gallery from './components/Gallary';
import Story from './components/Story';
import Faqs from './components/Faqs';

import Login from './pages/Login';
import ForgotPassword from './pages/ForgotPassword';
import ReservationPage from './pages/Reservation';
import Menu from './pages/Menu';
import Register from './pages/Register';

import { CartProvider } from './context/CartContext';

const theme = {
  colors: {
    primary: '#8B4513',
    secondary: '#f97316',
    background: '#fff5f1',
    backgroundDark: '#fff0e8',
    text: '#333333',
    textLight: '#666666',
    accent: '#d4af37'
  },
  fonts: {
    body: "'Poppins', sans-serif",
    heading: "'Playfair Display', serif"
  },
  borderRadius: {
    small: '0.25rem',
    medium: '0.5rem',
    large: '1rem'
  },
  shadows: {
    small: '0 2px 4px rgba(139, 69, 19, 0.05)',
    medium: '0 4px 6px rgba(139, 69, 19, 0.07)',
    large: '0 10px 15px rgba(139, 69, 19, 0.1)'
  }
};

const AppWrapper = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #fdf2ec;
  color: ${({ theme }) => theme.colors.text};
  font-family: ${({ theme }) => theme.fonts.body};
`;

const Main = styled.main`
  flex: 1;
  padding-top: 100px;
`;

const Section = styled.section`
  transition: opacity 0.8s ease, transform 0.8s ease;
  margin: 2rem 0;
`;

const ScrollTopButton = styled(motion.button)`
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: ${({ theme }) => theme.colors.secondary};
  color: white;
  border: none;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  font-size: 1.2rem;
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;

  &:hover {
    background: ${({ theme }) => theme.colors.primary};
    transform: scale(1.1) translateY(-2px);
    box-shadow: 0 18px 30px rgba(0, 0, 0, 0.25);
  }

  &::before {
    content: 'Back to Top';
    position: absolute;
    bottom: 130%;
    left: 50%;
    transform: translateX(-50%);
    background: ${({ theme }) => theme.colors.text};
    color: white;
    font-size: 0.75rem;
    padding: 5px 10px;
    border-radius: 6px;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease;
  }

  &:hover::before {
    opacity: 1;
  }

  svg {
    width: 34px;
    height: 34px;
    transition: transform 0.3s ease;
  }

  &:hover svg {
    transform: translateY(-2px);
  }
`;

function App() {
  const sectionRefs = useRef([]);
  const [showScrollTop, setShowScrollTop] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setShowScrollTop(window.scrollY > 3000);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const HomePage = (
    <AppWrapper>
      <Navbar sectionRefs={sectionRefs} />
      <Main>
        <Section ref={(el) => (sectionRefs.current[0] = el)} id="hero"><Hero /></Section>
        <Section ref={(el) => (sectionRefs.current[1] = el)} id="featured"><FeaturedDishes /></Section>
        <Section ref={(el) => (sectionRefs.current[2] = el)} id="categories"><Categories /></Section>
        <Section ref={(el) => (sectionRefs.current[3] = el)} id="reservation"><Reservation /></Section>
        <Section ref={(el) => (sectionRefs.current[4] = el)} id="gallery"><Gallery /></Section>
        <Section ref={(el) => (sectionRefs.current[5] = el)} id="story"><Story /></Section>
        <Section ref={(el) => (sectionRefs.current[6] = el)} id="mission"><Mission /></Section>
        <Section ref={(el) => (sectionRefs.current[7] = el)} id="values"><Values /></Section>
        <Section ref={(el) => (sectionRefs.current[8] = el)} id="team"><Team /></Section>
        <Section ref={(el) => (sectionRefs.current[9] = el)} id="testimonials"><Testimonials /></Section>
        <Section ref={(el) => (sectionRefs.current[10] = el)} id="faqs"><Faqs /></Section>
        <Section ref={(el) => (sectionRefs.current[11] = el)} id="contact"><Contact /></Section>
      </Main>

      <AnimatePresence>
        {showScrollTop && (
          <ScrollTopButton
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            whileTap={{ scale: 0.9 }}
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M18 15l-6-6-6 6" />
            </svg>
          </ScrollTopButton>
        )}
      </AnimatePresence>

      <Footer />
    </AppWrapper>
  );

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <CartProvider>
        <Router>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />
            <Route path="/reservation" element={<ReservationPage />} />
            <Route path="/menu" element={<Menu />} />
            <Route path="/" element={HomePage} />
          </Routes>
        </Router>
      </CartProvider>
    </ThemeProvider>
  );
}

export default App;
