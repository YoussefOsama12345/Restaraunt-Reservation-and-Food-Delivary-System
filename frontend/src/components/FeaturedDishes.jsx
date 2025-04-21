import styled from 'styled-components'
import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

const themed = (light, dark) => ({ theme }) => theme.mode === 'dark' ? dark : light

const fadeInUp = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
}

const Section = styled.section`
  width: 100%;
  padding: 5rem 1rem;
  background: transparent;
`

const Container = styled.div`
  max-width: 1280px;
  margin: 0 auto;
`

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
  flex-wrap: wrap;
  gap: 1rem;
`

const Title = styled.h2`
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.3;
  color: ${themed('#111827', '#f9fafb')};
`

const ViewAllButton = styled(Link)`
  font-size: 1rem;
  font-weight: 600;
  color: #f97316;
  display: flex;
  align-items: center;
  gap: 0.35rem;
  text-decoration: none;

  &:hover {
    color: #d97706;
  }

  svg {
    width: 1.2rem;
    height: 1.2rem;
  }
`

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
  gap: 2rem;
`

const Card = styled(motion.article)`
  background: ${({ theme }) =>
    theme.mode === 'dark'
      ? 'rgba(255,255,255,0.05)'
      : 'rgba(255, 255, 255, 0.7)'};
  backdrop-filter: blur(10px);
  border-radius: 1.25rem;
  overflow: hidden;
  border: 1px solid transparent;
  transition: all 0.4s ease;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);

  &:hover {
    transform: translateY(-6px);
    border: 1px solid #f97316;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.08);
  }
`

const ImageContainer = styled.div`
  position: relative;
  height: 240px;
  overflow: hidden;

  &:hover img {
    transform: scale(1.08);
  }
`

const DishImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
`

const RatingBadge = styled.div`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: ${themed('#ffffff', '#1f2937')};
  color: #fbbf24;
  font-weight: 700;
  padding: 0.4rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
`

const HoverOverlay = styled.div`
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(2px);
  opacity: 0;
  transition: opacity 0.3s ease;

  ${Card}:hover & {
    opacity: 1;
  }
`

const QuickViewButton = styled.button`
  background: #fff;
  color: #f97316;
  padding: 0.6rem 1.4rem;
  border-radius: 999px;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: #fef3c7;
    color: #ea580c;
  }
`

const CardContent = styled.div`
  padding: 1.5rem;
`

const DishName = styled.h3`
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  color: ${themed('#111827', '#ffffff')};
`

const DishDescription = styled.p`
  font-size: 0.95rem;
  color: ${themed('#6b7280', '#d1d5db')};
  margin-bottom: 1rem;
  line-height: 1.6;
`

const CardFooter = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`

const Price = styled.span`
  font-size: 1.125rem;
  font-weight: 700;
  color: ${themed('#111827', '#f3f4f6')};

  &::before {
    content: 'EGP ';
    font-weight: 400;
    color: #9ca3af;
  }
`

const AddButton = styled.button`
  background: linear-gradient(90deg, #f97316, #ea580c);
  color: #fff;
  padding: 0.5rem 1.1rem;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(90deg, #ea580c, #facc15);
    color: #1f2937;
  }
`

const dishes = [
  {
    id: 1,
    name: 'Chicken Salad',
    description: 'Fresh and healthy salad with grilled chicken',
    price: 120,
    image: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    rating: 4.5,
  },
  {
    id: 2,
    name: 'Vegetable Bowl',
    description: 'Mixed vegetables with quinoa and avocado',
    price: 95,
    image: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80',
    rating: 4.8,
  },
  {
    id: 3,
    name: 'Beef Stir Fry',
    description: 'Tender beef strips with seasonal vegetables',
    price: 150,
    image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
    rating: 4.7,
  },
]

const FeaturedDishes = () => {
  const { openCart } = useCart()

  return (
    <Section id="featured-dishes">
      <Container>
        <Header>
          <Title>Standout Dishes<br />From Our Menu</Title>
          <ViewAllButton to="/menu">
            View All
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </ViewAllButton>
        </Header>

        <Grid>
          {dishes.map((dish, index) => (
            <Card
              key={dish.id}
              variants={fadeInUp}
              initial="hidden"
              animate="visible"
              transition={{ duration: 0.5, delay: index * 0.15 }}
            >
              <ImageContainer>
                <DishImage src={dish.image} alt={dish.name} />
                <RatingBadge>
                  <span>★</span>
                  <span>{dish.rating}</span>
                </RatingBadge>
                <HoverOverlay>
                  <QuickViewButton>Quick View</QuickViewButton>
                </HoverOverlay>
              </ImageContainer>
              <CardContent>
                <DishName>{dish.name}</DishName>
                <DishDescription>{dish.description}</DishDescription>
                <CardFooter>
                  <Price>{dish.price}</Price>
                  <AddButton onClick={openCart}>Add to Cart</AddButton>
                </CardFooter>
              </CardContent>
            </Card>
          ))}
        </Grid>
      </Container>
    </Section>
  )
}

export default FeaturedDishes
