import styled from 'styled-components'
import { Link } from 'react-router-dom'

const FooterContainer = styled.footer`
  background-color: white;
  color: #1e293b;
  padding: 3rem 1rem 2rem;
  width: 100%;
`

const FooterTop = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding-bottom: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);

  @media (min-width: 768px) {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
`

const Branding = styled.div`
  max-width: 500px;
`

const Logo = styled.h2`
  font-size: 2rem;
  font-weight: 800;
  background: linear-gradient(90deg, #f97316, #ea580c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
`

const Tagline = styled.p`
  color: #374151;
  font-size: 0.95rem;
  line-height: 1.5;
`

const SocialLinks = styled.div`
  display: flex;
  gap: 0.75rem;
`

const SocialIcon = styled.a`
  width: 2.5rem;
  height: 2.5rem;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: all 0.3s ease;

  &:hover {
    background: #f97316;
    transform: scale(1.05) translateY(-2px);
  }

  svg {
    width: 1.25rem;
    height: 1.25rem;
  }
`

const FooterGrid = styled.div`
  max-width: 1200px;
  margin: 2rem auto 0;
  display: grid;
  gap: 2rem;

  @media (min-width: 768px) {
    grid-template-columns: repeat(3, 1fr);
  }
`

const FooterColumn = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
`

const ColumnTitle = styled.h4`
  color: #f97316;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
`

const FooterLink = styled(Link)`
  color: #374151;
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.2s ease;

  &:hover {
    color: #f97316;
  }
`

const FooterText = styled.p`
  color: #374151;
  font-size: 0.95rem;
  line-height: 1.5;
`

const Copyright = styled.div`
  text-align: center;
  font-size: 0.875rem;
  color: #374151;
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
`

const Footer = () => {
  const year = new Date().getFullYear()

  return (
    <FooterContainer>
      <FooterTop>
        <Branding>
          <Logo>Food Hub</Logo>
          <Tagline>
            Delivering delicious food to your doorstep with love, speed, and quality.
          </Tagline>
        </Branding>
        <SocialLinks>
          <SocialIcon href="https://facebook.com" target="_blank" aria-label="Facebook">
            <svg fill="currentColor" viewBox="0 0 24 24">
              <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z" />
            </svg>
          </SocialIcon>
          <SocialIcon href="https://instagram.com" target="_blank" aria-label="Instagram">
            <svg fill="currentColor" viewBox="0 0 24 24">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
              <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z" />
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
            </svg>
          </SocialIcon>
          <SocialIcon href="https://twitter.com" target="_blank" aria-label="Twitter">
            <svg fill="currentColor" viewBox="0 0 24 24">
              <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z" />
            </svg>
          </SocialIcon>
        </SocialLinks>
      </FooterTop>

      <FooterGrid>
        <FooterColumn>
          <ColumnTitle>Quick Links</ColumnTitle>
          <FooterLink to="/">Home</FooterLink>
          <FooterLink to="/menu">Menu</FooterLink>
          <FooterLink to="/about">About Us</FooterLink>
          <FooterLink to="/contact">Contact</FooterLink>
        </FooterColumn>

        <FooterColumn>
          <ColumnTitle>Contact Info</ColumnTitle>
          <FooterText><strong>Address:</strong> 123 Food Street, Cuisine City</FooterText>
          <FooterText><strong>Phone:</strong> +20 123 456 7890</FooterText>
          <FooterText><strong>Email:</strong> info@foodhub.com</FooterText>
        </FooterColumn>

        <FooterColumn>
          <ColumnTitle>Opening Hours</ColumnTitle>
          <FooterText><strong>Mon - Fri:</strong> 10:00 AM - 10:00 PM</FooterText>
          <FooterText><strong>Sat - Sun:</strong> 11:00 AM - 11:00 PM</FooterText>
        </FooterColumn>
      </FooterGrid>

      <Copyright>
        &copy; {year} Food Hub. All rights reserved.
      </Copyright>
    </FooterContainer>
  )
}

export default Footer
