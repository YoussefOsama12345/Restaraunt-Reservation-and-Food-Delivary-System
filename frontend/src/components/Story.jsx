import styled from 'styled-components'
import { motion } from 'framer-motion'

// 💡 Container for the entire section
const StorySection = styled(motion.section)`
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  margin: 0 auto 4rem;
  max-width: 1200px;
  padding: 2rem;
  border-radius: 1.5rem;
  background: ${({ theme }) =>
    theme.mode === 'dark'
      ? 'linear-gradient(135deg, #1f2937, #111827)'
      : 'linear-gradient(135deg, #fffaf0, #fef6e4)'};
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: background 0.3s ease;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
    align-items: center;
    padding: 3rem;
  }
`

// 📝 Text Content
const StoryContent = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
  padding: 1rem;
`

const StoryTitle = styled.h2`
  font-size: 2.5rem;
  font-weight: 800;
  color: ${({ theme }) => theme.colors?.primary || '#111827'};
  position: relative;
  margin-bottom: 1rem;
  line-height: 1.2;

  &::after {
    content: '';
    position: absolute;
    bottom: -12px;
    left: 0;
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #f97316, #ea580c);
    border-radius: 999px;
  }
`

const StoryText = styled.p`
  font-size: 1.125rem;
  line-height: 1.85;
  color: ${({ theme }) => theme.colors?.textSecondary || '#4b5563'};

  strong {
    color: ${({ theme }) => theme.colors?.secondary || '#f97316'};
    font-weight: 600;
  }
`

// 🗼️ Image Container
const StoryImage = styled(motion.div)`
  position: relative;
  width: 100%;
  height: 400px;
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  transition: transform 0.4s ease;

  &:hover img {
    transform: scale(1.05);
  }

  &::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(45deg, rgba(249, 115, 22, 0.08), rgba(249, 115, 22, 0.2));
    z-index: 1;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: relative;
    z-index: 2;
    border-radius: inherit;
    transition: transform 0.3s ease;
  }
`

// 🎞️ Animation Variant
const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 },
}

// 📦 Component
const Story = () => {
  return (
    <StorySection
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
      variants={fadeInUp}
      transition={{ duration: 0.6 }}
    >
      <StoryContent>
        <StoryTitle>How It All Started</StoryTitle>
        <StoryText>
          <strong>Food Hub</strong> was born from a simple idea: to make delicious, high-quality
          food accessible to everyone. Founded in 2020, our journey began with a small team of food
          enthusiasts passionate about bringing world-class cuisine directly to your home.
        </StoryText>
        <StoryText>
          What started as a local concept quickly grew into a trusted delivery network, connecting
          communities with the finest restaurants and chefs in the city. Our secret? A relentless
          focus on quality, speed, and customer care.
        </StoryText>
        <StoryText>
          Today, we're proud to serve thousands of happy customers — yet we’re just getting started.
          Great food. Anywhere. Anytime.
        </StoryText>
      </StoryContent>

      <StoryImage
        variants={fadeInUp}
        transition={{ duration: 0.4, delay: 0.2 }}
      >
        <img
          src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&w=800&q=80"
          alt="Food Hub kitchen"
          loading="lazy"
        />
      </StoryImage>
    </StorySection>
  )
}

export default Story