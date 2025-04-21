import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { motion, useInView } from 'framer-motion';
import { useRef, useEffect } from 'react';

const themed = (light, dark) => ({ theme }) => theme.mode === 'dark' ? dark : light;

const Section = styled.section`
  width: 100%;
  padding: 5rem 1.5rem;
  background-color: #fdf2ec;
  overflow-x: hidden;
`;

const Container = styled.div`
  max-width: 1240px;
  margin: 0 auto;
`;

const Grid = styled.div`
  display: grid;
  gap: 3rem;
  align-items: center;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
  }
`;

const TextBlock = styled(motion.div)`
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
`;

const Heading = styled(motion.h1)`
  font-family: 'Playfair Display', serif;
  font-size: 2.75rem;
  font-weight: 800;
  color: ${themed('#1f2937', '#fff')};
  line-height: 1.3;

  @media (min-width: 768px) {
    font-size: 3.5rem;
  }

  span {
    color: #f97316;
    background: linear-gradient(90deg, #f97316, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
`;

const Description = styled.p`
  font-size: 1.1rem;
  font-family: 'Inter', sans-serif;
  line-height: 1.8;
  color: ${themed('#4b5563', '#d1d5db')};
  max-width: 550px;
`;

const ButtonGroup = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
`;

const PrimaryButton = styled.button`
  background: linear-gradient(to right, #f97316, #ea580c);
  color: white;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 1.05rem;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(234, 88, 12, 0.25);
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(to right, #ea580c, #facc15);
    transform: translateY(-2px);
  }

  &:active {
    transform: scale(0.96);
  }
`;

const SecondaryButton = styled(Link)`
  padding: 0.75rem 2rem;
  border: 2px solid #f97316;
  color: #f97316;
  border-radius: 9999px;
  background-color: transparent;
  font-weight: 500;
  font-size: 1.05rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;

  &:hover {
    background-color: #fef3c7;
    color: #b45309;
    border-color: #facc15;
  }
`;

const ImageWrapper = styled(motion.div)`
  position: relative;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  padding-bottom: 2rem;
`;

const Decoration = styled.div`
  position: absolute;
  top: -2rem;
  right: -2rem;
  width: 20rem;
  height: 20rem;
  background: #facc15;
  border-radius: 9999px;
  z-index: 1;
`;

const DotDecoration = styled.div`
  position: absolute;
  bottom: -1rem;
  left: -1rem;
  width: 6rem;
  height: 6rem;
  background-image: radial-gradient(#fcd34d 1px, transparent 1px);
  background-size: 10px 10px;
  z-index: 0;
`;

const HeroImage = styled.img`
  position: relative;
  z-index: 10;
  width: 100%;
  height: auto;
  object-fit: cover;
  transition: transform 0.5s ease;

  &:hover {
    transform: scale(1.05); // Smooth zoom-in on hover
  }
`;

const fadeUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 },
};

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
};

const Hero = () => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  useEffect(() => {
    document.fonts?.load('1em Playfair Display');
  }, []);

  return (
    <Section ref={ref}>
      <Container>
        <Grid>
          <TextBlock
            initial={{ opacity: 0, y: 40 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.8, ease: 'easeOut' }}
          >
            <Heading>
              Dive into Delights<br />
              Of Delectable <span>Food</span>
            </Heading>
            <Description>
              Savor the best food delivery in town! Journey through a world of flavors,
              delivered right to your doorstep with unmatched quality and freshness.
            </Description>
            <ButtonGroup>
              <PrimaryButton aria-label="Order Now">Order Now</PrimaryButton>
              <SecondaryButton to="/menu" aria-label="View Menu">View Menu</SecondaryButton>
            </ButtonGroup>
          </TextBlock>

          <ImageWrapper
            initial={{ opacity: 0, scale: 0.95 }}
            animate={isInView ? { opacity: 1, scale: 1 } : {}}
            transition={{ duration: 0.8, ease: 'easeOut', delay: 0.3 }}
          >
            <Decoration />
            <DotDecoration />
            <HeroImage
              src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
              alt="Delicious Food"
            />
          </ImageWrapper>
        </Grid>
      </Container>
    </Section>
  );
};

export default Hero;