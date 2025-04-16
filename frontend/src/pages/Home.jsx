import React, { useState } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { useRestaurant } from '../context/RestaurantContext';

const HomeContainer = styled.div`
  background-color: #fff;
  width: 100%;
  min-height: 100vh;
  padding-top: 80px; /* Add space for fixed navbar */
`;

const ContentWrapper = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;

  @media (max-width: 768px) {
    padding: 1rem;
  }
`;

const HeroSection = styled.section`
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;
  margin-bottom: 4rem;
  
  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
  }
`;

const TextContent = styled.div`
  flex: 1;
  max-width: 600px;
`;

const Title = styled.h1`
  font-size: 4rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  
  span {
    color: #4CAF50;
  }
`;

const Description = styled.p`
  color: #666;
  font-size: 1.2rem;
  margin-bottom: 2.5rem;
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

const HeroImageContainer = styled.div`
  flex: 1;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const CircleBackground = styled.div`
  position: absolute;
  width: 500px;
  height: 500px;
  background-color: #4CAF50;
  border-radius: 50%;
  opacity: 0.1;
  z-index: 0;
`;

const HeroImage = styled.img`
  max-width: 100%;
  height: auto;
  position: relative;
  z-index: 1;
`;

const CategoriesSection = styled.section`
  max-width: 1200px;
  margin: 0 auto;
  padding: 6rem 2rem;
`;

const CategoryGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-top: 3rem;
  
  @media (max-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
`;

const CategoryCard = styled(Link)`
  background: #fff;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  text-decoration: none;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
`;

const CategoryIcon = styled.div`
  width: 80px;
  height: 80px;
  background-color: #e8f5e9;
  border-radius: 50%;
  margin: 0 auto 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  
  img {
    width: 40px;
    height: 40px;
  }
`;

const SectionTitle = styled.div`
  text-align: center;
  margin-bottom: 1rem;
  
  p {
    color: #4CAF50;
    text-transform: uppercase;
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 0.5rem;
  }
  
  h2 {
    font-size: 2.5rem;
    color: #000;
    font-weight: bold;
  }
`;

const SpecialDishesSection = styled.section`
  max-width: 1200px;
  margin: 0 auto;
  padding: 6rem 2rem;
  position: relative;
`;

const DishesGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`;

const DishCard = styled.div`
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
`;

const DishImage = styled.img`
  width: 100%;
  height: 250px;
  object-fit: cover;
`;

const FavoriteButton = styled.button`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #4CAF50;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: white;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;

  &:hover {
    background: #45a049;
  }
`;

const DishInfo = styled.div`
  padding: 1.5rem;
`;

const DishName = styled.h3`
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 0.5rem;
`;

const DishDescription = styled.p`
  color: #666;
  margin-bottom: 1rem;
`;

const PriceRating = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Price = styled.span`
  color: #ff6b6b;
  font-size: 1.25rem;
  font-weight: bold;
`;

const Rating = styled.span`
  color: #ffd700;
  font-size: 1.1rem;
`;

const TestimonialsSection = styled.section`
  max-width: 1200px;
  margin: 0 auto;
  padding: 6rem 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
`;

const ChefImageContainer = styled.div`
  position: relative;
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  aspect-ratio: 1;
  
  &::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: #4CAF50;
    border-radius: 50%;
    z-index: 0;
    opacity: 0.2;
  }
`;

const ChefImage = styled.img`
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 20px;
  object-fit: cover;
  z-index: 1;
`;

const ChefLabel = styled.div`
  position: absolute;
  bottom: -20px;
  right: 20px;
  background: white;
  padding: 10px 20px;
  border-radius: 25px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  
  span {
    font-weight: 500;
  }
`;

const TestimonialQuote = styled.blockquote`
  font-size: 1.5rem;
  color: #333;
  line-height: 1.6;
  margin: 2rem 0;
  font-style: italic;
`;

const CustomerFeedback = styled.div`
  margin-top: 2rem;
`;

const CustomerAvatars = styled.div`
  display: flex;
  margin-bottom: 1rem;
  
  img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid white;
    margin-right: -10px;
  }
`;

const FeedbackStats = styled.div`
  display: flex;
  align-items: center;
  gap: 1rem;
  
  .rating {
    color: #ffd700;
    font-size: 1.2rem;
    font-weight: bold;
  }
  
  .reviews {
    color: #666;
  }
`;

function Home() {
  const { menuItems } = useRestaurant();
  const [currentSlide, setCurrentSlide] = useState(0);
  
  // Calculate category counts
  const categoryCount = {
    'Main Course': menuItems.filter(item => item.category === 'Main Course').length,
    'Appetizers': menuItems.filter(item => item.category === 'Appetizers').length,
    'Desserts': menuItems.filter(item => item.category === 'Desserts').length,
    'All': menuItems.length
  };

  // Featured dishes data
  const featuredDishes = [
    {
      id: 1,
      name: "Fattoush salad",
      description: "Fresh vegetables mixed with crispy pita bread and sumac dressing",
      price: "24.00",
      rating: "4.9",
      image: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format&fit=crop"
    },
    {
      id: 2,
      name: "Vegetable salad",
      description: "Seasonal vegetables with house dressing",
      price: "26.00",
      rating: "4.6",
      image: "https://images.unsplash.com/photo-1540420773420-3366772f4999?q=80&w=800&auto=format&fit=crop"
    },
    {
      id: 3,
      name: "Egg vegi salad",
      description: "Fresh vegetables with boiled eggs and olives",
      price: "23.00",
      rating: "4.5",
      image: "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800&auto=format&fit=crop"
    }
  ];

  return (
    <HomeContainer>
      <ContentWrapper>
        <HeroSection>
          <TextContent>
            <Title>
              Delicious <span>Food</span> For Your Cravings
            </Title>
            <Description>
              We make fresh and healthy meals with different recipes
            </Description>
            <ButtonContainer>
              <Button to="/menu" className="primary">
                View Menu
              </Button>
              <Button to="/reservation" className="secondary">
                Book a Table
              </Button>
            </ButtonContainer>
          </TextContent>
          <HeroImageContainer>
            <CircleBackground />
            <img 
              src="/images/hero-food.jpg" 
              alt="Delicious hero dish"
              style={{ 
                width: '100%',
                maxWidth: '500px',
                height: 'auto',
                borderRadius: '20px',
                position: 'relative',
                zIndex: 1
              }}
            />
          </HeroImageContainer>
        </HeroSection>

        <CategoriesSection>
          <SectionTitle>
            <p>Popular Categories</p>
            <h2>Best Dishes From Our Menu</h2>
          </SectionTitle>
          <CategoryGrid>
            <CategoryCard to="/menu?category=main">
              <CategoryIcon>
                <img src="/images/icons/burger.svg" alt="Main Dish" />
              </CategoryIcon>
              <h3>Main Dish</h3>
              <p>({categoryCount['Main Course']} dishes)</p>
            </CategoryCard>
            <CategoryCard to="/menu?category=breakfast">
              <CategoryIcon>
                <img src="/images/icons/sandwich.svg" alt="Break Fast" />
              </CategoryIcon>
              <h3>Break Fast</h3>
              <p>(12 break fast)</p>
            </CategoryCard>
            <CategoryCard to="/menu?category=dessert">
              <CategoryIcon>
                <img src="/images/icons/dessert.svg" alt="Dessert" />
              </CategoryIcon>
              <h3>Dessert</h3>
              <p>({categoryCount['Desserts']} dessert)</p>
            </CategoryCard>
            <CategoryCard to="/menu">
              <CategoryIcon>
                <img src="/images/icons/juice.svg" alt="Browse All" />
              </CategoryIcon>
              <h3>Browse All</h3>
              <p>({categoryCount['All']} Items)</p>
            </CategoryCard>
          </CategoryGrid>
        </CategoriesSection>

        <SpecialDishesSection>
          <SectionTitle>
            <p>Special Dishes</p>
            <h2>Standout Dishes From Our Menu</h2>
          </SectionTitle>
          <DishesGrid>
            {featuredDishes.map((dish) => (
              <DishCard key={dish.id}>
                <DishImage src={dish.image} alt={dish.name} />
                <FavoriteButton>♥</FavoriteButton>
                <DishInfo>
                  <DishName>{dish.name}</DishName>
                  <DishDescription>{dish.description}</DishDescription>
                  <PriceRating>
                    <Price>${dish.price}</Price>
                    <Rating>★ {dish.rating}</Rating>
                  </PriceRating>
                </DishInfo>
              </DishCard>
            ))}
          </DishesGrid>
        </SpecialDishesSection>

        <TestimonialsSection>
          <ChefImageContainer>
            <ChefImage 
              src="https://images.unsplash.com/photo-1577219491135-ce391730fb2c?q=80&w=800&auto=format&fit=crop"
              alt="Our Best Chef"
            />
            <ChefLabel>
              <span>Our Best Chef</span> 👨‍🍳
            </ChefLabel>
          </ChefImageContainer>
          
          <TestimonialQuote>
            "I had the pleasure of dining at Foodi last night, and I'm still raving about the experience! 
            The attention to detail in presentation and service was impeccable"
          </TestimonialQuote>
          
          <CustomerFeedback>
            <CustomerAvatars>
              <img src="https://randomuser.me/api/portraits/women/12.jpg" alt="Customer" />
              <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Customer" />
              <img src="https://randomuser.me/api/portraits/women/23.jpg" alt="Customer" />
            </CustomerAvatars>
            
            <FeedbackStats>
              <span className="rating">★ 4.9</span>
              <span className="reviews">(18.6k Reviews)</span>
            </FeedbackStats>
          </CustomerFeedback>
        </TestimonialsSection>
      </ContentWrapper>
    </HomeContainer>
  );
}

export default Home; 