import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const HomeContainer = styled.div`
  padding: 2rem;
  background-color: #fff5ee;
  min-height: calc(100vh - 70px);
  position: relative;
  overflow: hidden;
`;

const ContentWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  gap: 2rem;
  
  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
  }
`;

const TextContent = styled.div`
  flex: 1;
`;

const ImagesContent = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2rem;
`;

const Title = styled.h1`
  color: #8B4513;
  font-size: 3.5rem;
  margin-bottom: 1rem;
`;

const Subtitle = styled.h2`
  color: #8B4513;
  font-size: 2rem;
  margin-bottom: 1.5rem;
`;

const Description = styled.p`
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 2rem;
  line-height: 1.6;
`;

const ButtonContainer = styled.div`
  display: flex;
  gap: 1rem;
  
  @media (max-width: 768px) {
    justify-content: center;
  }
`;

const Button = styled(Link)`
  padding: 0.8rem 2rem;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
  
  &.primary {
    background-color: #8B4513;
    color: white;
    
    &:hover {
      background-color: #6b3410;
    }
  }
  
  &.secondary {
    background-color: white;
    color: #8B4513;
    border: 2px solid #8B4513;
    
    &:hover {
      background-color: #8B4513;
      color: white;
    }
  }
`;

const FoodImage = styled.img`
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
`;

const DecorativeElement = styled.div`
  position: absolute;
  width: 100px;
  height: 100px;
  opacity: 0.1;
  background-color: #8B4513;
  
  &.top-right {
    top: 0;
    right: 0;
    transform: rotate(45deg);
  }
  
  &.bottom-left {
    bottom: 0;
    left: 0;
    transform: rotate(-45deg);
  }
`;

function Home() {
  return (
    <HomeContainer>
      <DecorativeElement className="top-right" />
      <DecorativeElement className="bottom-left" />
      <ContentWrapper>
        <TextContent>
          <Title>Welcome to Food Hub</Title>
          <Subtitle>Where Every Bite Tells a Story</Subtitle>
          <Description>
            Experience the perfect blend of flavors at Food Hub. Our chefs craft each dish with passion and precision, 
            using only the freshest ingredients. From traditional favorites to innovative creations, every meal is a 
            celebration of taste and quality. Join us for an unforgettable dining experience that will delight your 
            senses and satisfy your cravings.
          </Description>
          <ButtonContainer>
            <Button to="/reservation" className="primary">MAKE A RESERVATION</Button>
            <Button to="/menu" className="secondary">EXPLORE OUR MENU</Button>
          </ButtonContainer>
        </TextContent>
        <ImagesContent>
          <FoodImage 
            src="/images/hero-food.jpg" 
            alt="Our signature dish presentation"
          />
          <FoodImage 
            src="/images/featured-dish.jpg" 
            alt="Chef's special creation"
          />
        </ImagesContent>
      </ContentWrapper>
    </HomeContainer>
  );
}

export default Home; 