// Enhanced Navbar with Modern Design, Sidebar, and Close Button

import { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import styled, { keyframes } from 'styled-components';
import CartSidebar from './CartSidebar';
import { useCart } from '../context/CartContext';
import { FaShoppingCart } from 'react-icons/fa';
import { HiMenu, HiX } from 'react-icons/hi';

/* Animations */
const slideIn = keyframes`
  from { transform: translateX(-100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
`;

const slideOut = keyframes`
  from { transform: translateX(0); opacity: 1; }
  to { transform: translateX(-100%); opacity: 0; }
`;

/* Styled Components */
const NavbarContainer = styled.nav`
  background-color: ${({ isScrolled }) =>
    isScrolled ? 'rgba(255, 255, 255, 0.85)' : 'rgba(255, 255, 255, 0.7)'};
  backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: ${({ isScrolled }) => (isScrolled ? '0.75rem 0' : '1.25rem 0')};
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.03);
  transition: all 0.3s ease-in-out;
`;

const Container = styled.div`
  max-width: 1200px;
  padding: 1rem;
  margin: 0 auto;
`;

const FlexWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Brand = styled(Link)`
  font-size: 1.75rem;
  font-weight: 700;
  color: #f97316;
  letter-spacing: -0.5px;
  text-decoration: none;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: color 0.3s ease;

  &:hover {
    color: #ea580c;
  }

  @media (max-width: 768px) {
    display: none;
  }
`;

const NavLinks = styled.nav`
  display: flex;
  gap: 2rem;
  align-items: center;

  @media (max-width: 768px) {
    display: none;
  }
`;

const StyledLink = styled.a`
  all: unset;
  color: #374151;
  cursor: pointer;
  font-weight: 500;
  position: relative;
  padding-bottom: 2px;
  transition: color 0.3s ease;

  &::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 0%;
    height: 2px;
    background: #f97316;
    transition: width 0.3s ease;
  }

  &:hover {
    color: #f97316;
  }

  &:hover::after {
    width: 100%;
  }
`;

const OrderButton = styled.button`
  background: linear-gradient(to right, #f97316, #ea580c);
  color: white;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.95rem;
  letter-spacing: 0.2px;
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.25);
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(to right, #ea580c, #facc15);
    transform: scale(1.03);
  }

  &.full-width {
    width: 100%;
  }
`;

const MobileToggle = styled.div`
  display: flex;
  align-items: center;
  gap: 0.75rem;

  @media (min-width: 769px) {
    display: none;
  }
`;

const MobileBrand = styled.span`
  font-size: 1.25rem;
  font-weight: 600;
  color: #f97316;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
`;

const MobileButton = styled.button`
  background: none;
  border: none;
  color: #374151;
  cursor: pointer;
  padding: 0;
  transition: transform 0.3s ease;

  svg {
    width: 1.75rem;
    height: 1.75rem;
  }

  &:hover {
    transform: scale(1.1);
  }
`;

const CartIcon = styled.button`
  background: none;
  border: none;
  color: #374151;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.3s ease;

  &:hover {
    color: #f97316;
  }

  svg {
    width: 1.5rem;
    height: 1.5rem;
  }

  @media (max-width: 768px) {
    display: none;
  }
`;

const MobileCartIcon = styled(CartIcon)`
  display: none;

  @media (max-width: 768px) {
    display: flex;
    margin-right: 0.75rem;
  }
`;

const Overlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 1090;
`;

const SidebarLogo = styled.div`
  font-size: 1.5rem;
  font-weight: 700;
  color: #f97316;
  margin-bottom: 1rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
`;

const MobileMenu = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 270px;
  background: #fff;
  box-shadow: 4px 0 16px rgba(0, 0, 0, 0.07);
  padding: 2rem 1.25rem;
  z-index: 1100;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  animation: ${({ isClosing }) => isClosing ? slideOut : slideIn} 0.3s ease-in-out;

  @media (min-width: 769px) {
    display: none;
  }

  &::before {
    content: '';
    width: 100%;
    height: 1px;
    background: #eee;
    margin-bottom: 1rem;
  }
`;

const SidebarCloseButton = styled.button`
  align-self: flex-end;
  background: none;
  border: none;
  color: #4b5563;
  cursor: pointer;
  padding: 0;
  margin-bottom: 1rem;

  svg {
    width: 1.8rem;
    height: 1.8rem;
  }

  &:hover {
    color: #f97316;
    transform: rotate(90deg) scale(1.1);
  }

  transition: color 0.3s ease, transform 0.3s ease;
`;

const MobileLinkList = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const FloatingCTA = styled(Link)`
  position: fixed;
  bottom: 1.25rem;
  right: 1.25rem;
  z-index: 999;
  background: linear-gradient(to right, #f97316, #ea580c);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  box-shadow: 0 10px 30px rgba(249, 115, 22, 0.3);
  transition: transform 0.3s ease;

  &:hover {
    background: linear-gradient(to right, #ea580c, #facc15);
    transform: scale(1.05);
  }

  @media (min-width: 768px) {
    display: none;
  }
`;

// Add inside JSX under <SidebarCloseButton>:
// <SidebarLogo>Food Hub</SidebarLogo>

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isClosing, setIsClosing] = useState(false);
  const { isCartOpen, openCart, closeCart } = useCart();
  const location = useLocation();
  const navigate = useNavigate();
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const closeMobileMenu = () => {
    setIsClosing(true);
    setTimeout(() => {
      setIsOpen(false);
      setIsClosing(false);
    }, 300);
  };

  const scrollToTop = (e) => {
    e.preventDefault();
    if (location.pathname !== '/') {
      window.location.href = '/';
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    closeMobileMenu();
  };

  const scrollToSection = (sectionId) => {
    if (location.pathname !== '/') {
      window.location.href = `/#${sectionId}`;
    } else {
      const element = document.getElementById(sectionId);
      if (element) {
        const navbarHeight = document.querySelector('nav').offsetHeight;
        const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
        window.scrollTo({ top: elementPosition - navbarHeight, behavior: 'smooth' });
      }
    }
    closeMobileMenu();
  };

  return (
    <>
      <NavbarContainer isScrolled={isScrolled}>
        <Container>
          <FlexWrapper>
            <Brand to="/" onClick={scrollToTop}>Food Hub</Brand>
            <NavLinks>
              <StyledLink as={Link} to="/" onClick={scrollToTop}>Home</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('featured-dishes')}>Menu</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('about')}>About</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('contact')}>Contact</StyledLink>
              <CartIcon onClick={openCart}><FaShoppingCart /></CartIcon>
              <Link to="/login" style={{ textDecoration: 'none' }}>
                <OrderButton>Login</OrderButton>
              </Link>
            </NavLinks>
            <MobileToggle>
              <MobileCartIcon onClick={openCart}><FaShoppingCart /></MobileCartIcon>
              <MobileButton onClick={() => setIsOpen(true)}>
                {isOpen && !isClosing ? <HiX /> : <HiMenu />}
              </MobileButton>
            </MobileToggle>
          </FlexWrapper>
        </Container>
      </NavbarContainer>

      {isOpen && (
        <>
          <Overlay onClick={closeMobileMenu} />
          <MobileMenu isClosing={isClosing}>
            <SidebarCloseButton onClick={closeMobileMenu}>
              <HiX />
            </SidebarCloseButton>
            <MobileLinkList>
              <StyledLink as="button" onClick={scrollToTop}>Home</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('featured-dishes')}>Menu</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('about')}>About</StyledLink>
              <StyledLink as="button" onClick={() => scrollToSection('contact')}>Contact</StyledLink>
              <Link to="/login" style={{ textDecoration: 'none' }}>
                <OrderButton className="full-width">Login</OrderButton>
              </Link>
            </MobileLinkList>
          </MobileMenu>
        </>
      )}

      <FloatingCTA to="/menu">Order Now</FloatingCTA>
      <CartSidebar isOpen={isCartOpen} onClose={closeCart} />
    </>
  );
};

export default Navbar;