import React from 'react';
import styled, { useTheme } from 'styled-components';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

// Styled Components
const ReservationSection = styled.section`
  padding: 4rem 2rem;
  background: linear-gradient(to right, #fff7ed, #fffbea);
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow: hidden;
`;

const ImageContainer = styled.div`
  width: 100%;
  max-width: 1100px;
  height: 550px;
  position: relative;
  margin-bottom: 2rem;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
  transition: box-shadow 0.3s ease;

  @media (max-width: 768px) {
    height: 350px;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
    display: block;
  }

  &:hover img {
    transform: scale(1.04);
  }

  &::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.2) 0%,
      rgba(0, 0, 0, 0.3) 100%
    );
    pointer-events: none;
  }
`;

const BookButton = styled(motion(Link))`
  background-color: #f97316;
  color: white;
  padding: 1rem 2.5rem;
  border: 2px solid #f97316;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 6px 20px rgba(249, 115, 22, 0.3);
  text-decoration: none;

  &:hover {
    background-color: white;
    color: #f97316;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(249, 115, 22, 0.4);
  }
`;

const Title = styled.h2`
  color: ${({ theme }) => theme?.colors?.primary || '#1e293b'};
  font-size: 2.75rem;
  font-weight: 800;
  margin-bottom: 1rem;
  text-align: center;
  font-family: ${({ theme }) => theme?.fonts?.heading || 'inherit'};
`;

const Subtitle = styled.p`
  color: ${({ theme }) => theme?.colors?.textLight || '#6b7280'};
  font-size: 1.1rem;
  margin-bottom: 3rem;
  text-align: center;
  max-width: 640px;
  line-height: 1.6;
`;

const Reservation = () => {
  const theme = useTheme();

  return (
    <ReservationSection id="reservation">
      <Title theme={theme}>Reserve Your Table</Title>
      <Subtitle theme={theme}>
        Experience the perfect dining atmosphere with our carefully curated table settings.
      </Subtitle>

      <motion.div
        initial={{ opacity: 0, y: 60 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: 'easeOut' }}
        viewport={{ once: true }}
      >
        <ImageContainer>
          <img 
            src="https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=1100&h=550&q=80"
            alt="Beautiful table setup in a modern restaurant"
            loading="lazy"
          />
        </ImageContainer>
      </motion.div>

      <BookButton
        to="/reservation"
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        Book Now
      </BookButton>
    </ReservationSection>
  );
};

export default Reservation;
