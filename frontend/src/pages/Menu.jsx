import React, { useState } from 'react';
import { useRestaurant } from '../context/RestaurantContext';
import { useCart } from '../context/CartContext';
import styled from 'styled-components';
import './Menu.css';

const AddedToCartMessage = styled.div`
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background-color: #4CAF50;
  color: white;
  padding: 1rem 2rem;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  animation: slideIn 0.3s ease-out;
  z-index: 1000;

  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
`;

const MenuContainer = styled.div`
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
`;

const MenuTitle = styled.h1`
  color: #8B4513;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.5rem;
`;

const CategoryFilters = styled.div`
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
`;

const CategoryButton = styled.button`
  padding: 0.5rem 1.5rem;
  border: 2px solid #8B4513;
  border-radius: 25px;
  background-color: ${props => props.active ? '#8B4513' : 'transparent'};
  color: ${props => props.active ? 'white' : '#8B4513'};
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background-color: #8B4513;
    color: white;
  }
`;

const MenuGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
`;

const MenuItem = styled.div`
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
`;

const ItemImage = styled.img`
  width: 100%;
  height: 200px;
  object-fit: cover;
  background-color: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #8B4513;
  font-size: 1.2rem;
  text-align: center;
  padding: 1rem;
`;

const PlaceholderText = styled.div`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #8B4513;
  font-size: 1.2rem;
  text-align: center;
  padding: 1rem;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 5px;
`;

const ItemDetails = styled.div`
  padding: 1.5rem;
`;

const ItemName = styled.h3`
  color: #8B4513;
  margin-bottom: 0.5rem;
`;

const ItemDescription = styled.p`
  color: #666;
  margin-bottom: 1rem;
  font-size: 0.9rem;
`;

const ItemFooter = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Price = styled.span`
  color: #8B4513;
  font-weight: bold;
  font-size: 1.2rem;
`;

const AddToCartButton = styled.button`
  padding: 0.5rem 1rem;
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #6b3410;
  }
`;

function Menu() {
  const { menuItems } = useRestaurant();
  const { addItem } = useCart();
  const [activeCategory, setActiveCategory] = useState('all');
  const [showAddedMessage, setShowAddedMessage] = useState(false);
  const [lastAddedItem, setLastAddedItem] = useState('');
  const [imageErrors, setImageErrors] = useState({});

  const categories = ['all', ...new Set(menuItems.map(item => item.category))];

  const filteredItems = activeCategory === 'all' 
    ? menuItems 
    : menuItems.filter(item => item.category === activeCategory);

  const handleImageError = (itemId) => {
    setImageErrors(prev => ({ ...prev, [itemId]: true }));
  };

  const handleAddToCart = (item) => {
    addItem(item);
    setLastAddedItem(item.name);
    setShowAddedMessage(true);
    setTimeout(() => {
      setShowAddedMessage(false);
    }, 2000);
  };

  return (
    <MenuContainer>
      <MenuTitle>Our Menu</MenuTitle>
      
      <CategoryFilters>
        {categories.map(category => (
          <CategoryButton
            key={category}
            active={activeCategory === category}
            onClick={() => setActiveCategory(category)}
          >
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </CategoryButton>
        ))}
      </CategoryFilters>

      <MenuGrid>
        {filteredItems.map(item => (
          <MenuItem key={item.id}>
            <div style={{ position: 'relative' }}>
              <ItemImage 
                src={item.image} 
                alt={item.name}
                onError={() => handleImageError(item.id)}
              />
              {imageErrors[item.id] && (
                <PlaceholderText>
                  {item.name}
                  <div style={{ fontSize: '0.8rem', marginTop: '0.5rem' }}>
                    Image coming soon
                  </div>
                </PlaceholderText>
              )}
            </div>
            <ItemDetails>
              <ItemName>{item.name}</ItemName>
              <ItemDescription>{item.description}</ItemDescription>
              <ItemFooter>
                <Price>EGP {item.price}</Price>
                <AddToCartButton onClick={() => handleAddToCart(item)}>
                  Add to Cart
                </AddToCartButton>
              </ItemFooter>
            </ItemDetails>
          </MenuItem>
        ))}
      </MenuGrid>

      {showAddedMessage && (
        <AddedToCartMessage>
          {lastAddedItem} added to cart!
        </AddedToCartMessage>
      )}
    </MenuContainer>
  );
}

export default Menu; 