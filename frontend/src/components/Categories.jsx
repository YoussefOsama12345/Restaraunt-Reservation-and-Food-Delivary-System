import styled from 'styled-components'
import { motion } from 'framer-motion'

// 🌙 Helper for light/dark mode
const themed = (light, dark) => ({ theme }) => theme.mode === 'dark' ? dark : light

// 🔲 Wrapper Section
const Section = styled.section`
  width: 100%;
  padding: 4rem 1rem;
  background-color: transparent;
`

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`

const Title = styled.h2`
  font-size: 2.5rem;
  font-weight: 800;
  color: ${themed('#111827', '#f9fafb')};
  text-align: center;
  margin-bottom: 3rem;
  position: relative;

  &::after {
    content: '';
    position: absolute;
    bottom: -14px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    height: 4px;
    background: linear-gradient(90deg, #f97316, #ea580c);
    border-radius: 999px;
  }
`

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 2rem;

  @media (min-width: 768px) {
    gap: 2.5rem;
  }
`

const CategoryCard = styled(motion.div)`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.8rem 1rem;
  border-radius: 1.25rem;
  backdrop-filter: blur(10px);
  background: ${({ theme }) =>
    theme.mode === 'dark'
      ? 'rgba(255, 255, 255, 0.05)'
      : 'rgba(255, 255, 255, 0.7)'};
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: ${({ theme }) => theme.shadows.medium};
  text-align: center;
  transition: all 0.4s ease;
  cursor: pointer;

  &:hover {
    transform: translateY(-8px) scale(1.02);
    background: linear-gradient(145deg, #fef3c7, #fde68a);
    border-color: #f59e0b;
  }
`

const IconWrapper = styled.div`
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background-color: ${({ theme }) => theme.colors.background};
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin-bottom: 1rem;
  transition: transform 0.3s ease;

  ${CategoryCard}:hover & {
    transform: scale(1.2) rotate(6deg);
  }
`

const CategoryName = styled.h3`
  font-weight: 600;
  font-size: 1.125rem;
  color: ${({ theme }) => theme.colors.text};
  margin-top: 0.25rem;
`

// 🧭 Category Data
const categories = [
  { id: 1, name: 'Fast Food', icon: '🍔' },
  { id: 2, name: 'Breakfast', icon: '🍳' },
  { id: 3, name: 'Dessert', icon: '🍰' },
  { id: 4, name: 'Dinner Kit', icon: '🍽️' }
]

// 🎬 Motion Animation
const animation = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
}

// 🚀 Component
const Categories = () => (
  <Section>
    <Container>
      <Title>Popular Categories</Title>
      <Grid>
        {categories.map((category, index) => (
          <CategoryCard
            key={category.id}
            variants={animation}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
            transition={{ duration: 0.4, delay: index * 0.15 }}
            aria-label={`Category: ${category.name}`}
            role="button"
          >
            <IconWrapper>
              <span role="img" aria-label={category.name}>{category.icon}</span>
            </IconWrapper>
            <CategoryName>{category.name}</CategoryName>
          </CategoryCard>
        ))}
      </Grid>
    </Container>
  </Section>
)

export default Categories
