import React, { useState } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useCart } from '../context/CartContext';
import AddToCartModal from '../components/AddToCartModal';

const categoriesList = ['All', 'Starters', 'Main Dishes', 'Desserts', 'Drinks'];

const dishes = [
    {
      id: 1,
      name: 'Chicken Salad',
      category: 'Starters',
      description: 'Fresh and healthy salad with grilled chicken',
      price: 120,
      image: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
      rating: 4.5
    },
    {
      id: 2,
      name: 'Vegetable Bowl',
      category: 'Starters',
      description: 'Mixed vegetables with quinoa and avocado',
      price: 95,
      image: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 3,
      name: 'Hummus & Pita',
      category: 'Starters',
      description: 'Classic hummus served with warm pita bread',
      price: 70,
      image: 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
    {
      id: 4,
      name: 'Beef Stir Fry',
      category: 'Main Dishes',
      description: 'Tender beef strips with seasonal vegetables',
      price: 150,
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 5,
      name: 'Grilled Salmon',
      category: 'Main Dishes',
      description: 'Salmon with garlic lemon butter and asparagus',
      price: 165,
      image: 'https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=800&q=80',
      rating: 4.9
    },
    {
      id: 6,
      name: 'Chicken Alfredo Pasta',
      category: 'Main Dishes',
      description: 'Creamy pasta with grilled chicken breast',
      price: 130,
      image: 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 7,
      name: 'Tiramisu',
      category: 'Desserts',
      description: 'Classic Italian dessert with mascarpone and espresso',
      price: 60,
      image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 8,
      name: 'Panna Cotta',
      category: 'Desserts',
      description: 'Vanilla cream topped with berry coulis',
      price: 55,
      image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
    {
      id: 9,
      name: 'Chocolate Lava Cake',
      category: 'Desserts',
      description: 'Warm chocolate cake with molten center',
      price: 65,
      image: 'https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80',
      rating: 4.9
    },
    {
      id: 10,
      name: 'Fresh Lemonade',
      category: 'Drinks',
      description: 'Refreshing lemon and mint cooler',
      price: 35,
      image: 'https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?auto=format&fit=crop&w=800&q=80',
      rating: 4.4
    },
    {
      id: 11,
      name: 'Iced Coffee',
      category: 'Drinks',
      description: 'Cold brew with milk and vanilla syrup',
      price: 45,
      image: 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 12,
      name: 'Mango Smoothie',
      category: 'Drinks',
      description: 'Blended mango, banana, and yogurt',
      price: 50,
      image: 'https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
    {
      id: 13,
      name: 'Right-sized client-server Graphic Interface',
      category: 'Desserts',
      description: 'Cost course mention again side be onto leave those.',
      price: 62,
      image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 14,
      name: 'Reverse-engineered 6thgeneration model',
      category: 'Main Dishes',
      description: 'Care item well especially.',
      price: 78,
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 15,
      name: 'Organic methodical artificial intelligence',
      category: 'Desserts',
      description: 'Buy majority sort never agent worry.',
      price: 49,
      image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
      rating: 4.2
    },
    {
      id: 16,
      name: 'Streamlined web-enabled hub',
      category: 'Starters',
      description: 'Cut final ten poor behavior region summer task sign.',
      price: 82,
      image: 'https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80',
      rating: 4.4
    },
    {
      id: 17,
      name: 'Business-focused composite task-force',
      category: 'Desserts',
      description: 'Congress condition begin style forward gas responsibility like.',
      price: 72,
      image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 18,
      name: 'Balanced bottom-line forecast',
      category: 'Starters',
      description: 'Determine environment forward support impact several woman.',
      price: 48,
      image: 'https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80',
      rating: 4.4
    },
    {
      id: 19,
      name: 'Mandatory dedicated solution',
      category: 'Starters',
      description: 'Southern term majority hundred perhaps case page then.',
      price: 115,
      image: 'https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
    {
      id: 20,
      name: 'Persevering multi-tasking software',
      category: 'Main Dishes',
      description: 'Wind better deal class standard too physical.',
      price: 99,
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 21,
      name: 'Front-line contextually-based Internet solution',
      category: 'Main Dishes',
      description: 'Focus democratic behind finish age mother debate radio fast avoid.',
      price: 93,
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
    {
      id: 22,
      name: 'Multi-tiered modular interface',
      category: 'Drinks',
      description: 'Rest raise option able either agent.',
      price: 167,
      image: 'https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?auto=format&fit=crop&w=800&q=80',
      rating: 4.3
    },
    {
      id: 23,
      name: 'Strawberry Cheesecake',
      category: 'Desserts',
      description: 'Creamy cheesecake topped with fresh strawberries',
      price: 93,
      image: 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80',
      rating: 4.7
    },
    {
      id: 24,
      name: 'Baklava',
      category: 'Desserts',
      description: 'Layers of filo pastry filled with chopped nuts and honey',
      price: 105,
      image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 25,
      name: 'Bruschetta',
      category: 'Starters',
      description: 'Grilled bread with tomato, garlic, and basil',
      price: 46,
      image: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
      rating: 5.0
    },
    {
      id: 26,
      name: 'Stuffed Mushrooms',
      category: 'Starters',
      description: 'Mushrooms filled with cheese and herbs',
      price: 86,
      image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
      rating: 5.0
    },
    {
      id: 27,
      name: 'Lamb Chops',
      category: 'Main Dishes',
      description: 'Grilled lamb chops with rosemary and garlic',
      price: 118,
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
      rating: 4.9
    },
    {
      id: 28,
      name: 'Spaghetti Carbonara',
      category: 'Main Dishes',
      description: 'Pasta with eggs, cheese, pancetta, and pepper',
      price: 102,
      image: 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 29,
      name: 'Strawberry Milkshake',
      category: 'Drinks',
      description: 'Blended strawberries with milk and ice cream',
      price: 55,
      image: 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80',
      rating: 4.9
    },
    {
      id: 30,
      name: 'Espresso',
      category: 'Drinks',
      description: 'Strong and bold Italian coffee',
      price: 30,
      image: 'https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?auto=format&fit=crop&w=800&q=80',
      rating: 4.8
    },
    {
      id: 31,
      name: 'Churros',
      category: 'Desserts',
      description: 'Fried dough pastry dusted with sugar and cinnamon',
      price: 67,
      image: 'https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80',
      rating: 4.5
    },
    {
      id: 32,
      name: 'Garlic Bread',
      category: 'Starters',
      description: 'Toasted bread with garlic butter',
      price: 42,
      image: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
      rating: 4.6
    },
  
  ];
  

const fadeInUp = { hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0 } };

const Section = styled.section`
  width: 100%;
  padding: 100px 20px 60px;
  background: #fff7ed;
`;

const Container = styled.div`
  max-width: 1280px;
  margin: 0 auto;
`;

const Title = styled.h2`
  font-size: 2.8rem;
  font-weight: 800;
  color: #8B4513;
  text-align: center;
  margin-bottom: 2rem;
  font-family: 'Playfair Display', serif;
`;

const CategoriesContainer = styled.div`
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2.5rem;
`;

const CategoryButton = styled.button`
  background: ${({ active }) => (active ? '#f97316' : '#fff')};
  color: ${({ active }) => (active ? '#fff' : '#f97316')};
  border: 2px solid #f97316;
  padding: 0.6rem 1.2rem;
  border-radius: 999px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s ease;

  &:hover {
    background: #f97316;
    color: #fff;
  }
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
  gap: 2rem;
`;

const Card = styled(motion.article)`
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border-radius: 1.25rem;
  overflow: hidden;
  border: 1px solid #f97316;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
  transition: all 0.4s ease;

  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  }
`;

const ImageContainer = styled.div`
  position: relative;
  height: 220px;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }

  &:hover img {
    transform: scale(1.08);
  }
`;

const RatingBadge = styled.div`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #fff;
  color: #f97316;
  font-weight: 700;
  padding: 0.4rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
`;

const CardContent = styled.div`
  padding: 1.5rem;
`;

const DishName = styled.h3`
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: #1f2937;
`;

const DishDescription = styled.p`
  font-size: 0.95rem;
  color: #6b7280;
  margin-bottom: 1rem;
`;

const CardFooter = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Price = styled.span`
  font-size: 1.1rem;
  font-weight: 700;
  color: #8B4513;

  &::before {
    content: 'EGP ';
    font-weight: 400;
    color: #9ca3af;
  }
`;

const AddButton = styled.button`
  background: linear-gradient(90deg, #f97316, #ea580c);
  color: #fff;
  padding: 0.5rem 1.1rem;
  font-size: 0.85rem;
  font-weight: 600;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(90deg, #ea580c, #facc15);
    color: #1f2937;
  }
`;

const Menu = () => {
  const { addToCart } = useCart();
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedItem, setSelectedItem] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const filteredDishes = selectedCategory === 'All'
    ? dishes
    : dishes.filter((dish) => dish.category === selectedCategory);

  const handleAddToCartClick = (dish) => {
    setSelectedItem(dish);
    setIsModalOpen(true);
  };

  const handleModalClose = () => {
    setIsModalOpen(false);
    setSelectedItem(null);
  };

  const handleAddToCart = (itemWithDetails) => {
    addToCart(itemWithDetails);
  };

  return (
    <>
      <Navbar />
      <Section>
        <Container>
          <Title>Explore Our Menu</Title>

          <CategoriesContainer>
            {categoriesList.map((cat) => (
              <CategoryButton
                key={cat}
                active={selectedCategory === cat}
                onClick={() => setSelectedCategory(cat)}
              >
                {cat}
              </CategoryButton>
            ))}
          </CategoriesContainer>

          <Grid>
            {filteredDishes.map((dish, index) => (
              <Card
                key={dish.id}
                variants={fadeInUp}
                initial="hidden"
                animate="visible"
                transition={{ duration: 0.5, delay: index * 0.1 }}
              >
                <ImageContainer>
                  <img src={dish.image} alt={dish.name} />
                  <RatingBadge>★ {dish.rating}</RatingBadge>
                </ImageContainer>
                <CardContent>
                  <DishName>{dish.name}</DishName>
                  <DishDescription>{dish.description}</DishDescription>
                  <CardFooter>
                    <Price>{dish.price}</Price>
                    <AddButton onClick={() => handleAddToCartClick(dish)}>
                      Add to Cart
                    </AddButton>
                  </CardFooter>
                </CardContent>
              </Card>
            ))}
          </Grid>
        </Container>
      </Section>
      <Footer />

      {selectedItem && (
        <AddToCartModal
          isOpen={isModalOpen}
          onClose={handleModalClose}
          item={selectedItem}
          onAddToCart={handleAddToCart}
        />
      )}
    </>
  );
};

export default Menu;
