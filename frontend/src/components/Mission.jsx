import styled from 'styled-components'
import { motion } from 'framer-motion'

// 🌟 Styled Components
const MissionSection = styled(motion.section)`
  background: ${({ theme }) =>
    theme.mode === 'dark'
      ? 'linear-gradient(135deg, #1f2937, #111827)'
      : 'linear-gradient(135deg, #fffaf3, #fef6ee)'};
  padding: 3rem 2rem;
  border-radius: 1.5rem;
  margin: 4rem auto;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  max-width: 1920px;
  transition: background 0.3s ease-in-out;
`

const MissionTitle = styled.h2`
  font-size: 2.5rem;
  font-weight: 700;
  color: ${({ theme }) => theme.colors?.primary || '#111827'};
  margin-bottom: 2rem;
  position: relative;
  font-family: ${({ theme }) => theme.fonts?.heading || 'inherit'};

  &::after {
    content: '';
    position: absolute;
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #f97316, #ea580c);
    border-radius: 999px;
  }
`

const MissionText = styled.p`
  font-size: 1.15rem;
  line-height: 1.8;
  color: ${({ theme }) => theme.colors?.textSecondary || '#4b5563'};
  max-width: 850px;
  margin: 0 auto;
  font-weight: 400;

  strong {
    color: ${({ theme }) => theme.colors?.secondary || '#f97316'};
    font-weight: 600;
  }
`

// 💫 Animation Variants
const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 }
}

// 🚀 Mission Component
const Mission = () => {
  return (
    <MissionSection
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
      variants={fadeInUp}
      transition={{ duration: 0.6 }}
    >
      <MissionTitle>Our Mission</MissionTitle>
      <MissionText>
        At <strong>Food Hub</strong>, our mission is to revolutionize the food delivery experience
        by offering exceptional quality, unmatched convenience, and outstanding customer service. We
        strive to connect food lovers with the best culinary creations while supporting local
        restaurants and promoting sustainable practices.
      </MissionText>
    </MissionSection>
  )
}

export default Mission
