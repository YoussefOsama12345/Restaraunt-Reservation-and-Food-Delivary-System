import styled from 'styled-components'
import { motion } from 'framer-motion'

// 🔶 Styled Section Wrapper
const ValuesSection = styled(motion.section)`
  margin-bottom: 4rem;
  padding: 2rem;
  border-radius: 1.5rem;
  box-shadow: 0 10px 40px rgba(249, 115, 22, 0.05);
`

// 🔶 Title with underline
const ValuesTitle = styled.h2`
  font-size: 2.25rem;
  font-weight: 700;
  color: #111827;
  text-align: center;
  margin-bottom: 3rem;
  position: relative;

  &::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    height: 4px;
    background: linear-gradient(90deg, #f97316, #ea580c);
    border-radius: 999px;
  }
`

// 🔶 Grid with centered layout
const ValuesGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;

  @media (min-width: 640px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(4, 1fr);
  }
`

// 🔶 Individual Value Card
const ValueCard = styled(motion.div)`
  background: white;
  border-radius: 1rem;
  padding: 1.25rem;
  text-align: center;
  transition: all 0.4s ease;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
  border: 1px solid transparent;
  min-height: 220px;

  &:hover {
    transform: translateY(-6px);
    border-color: #f97316;
    box-shadow: 0 16px 30px rgba(249, 115, 22, 0.1);
  }
`

// 🔶 Icon styling
const ValueIcon = styled.div`
  width: 50px;
  height: 50px;
  margin: 0 auto 0.75rem;
  background-color: #fff7ed;
  color: #f97316;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;

  svg {
    width: 20px;
    height: 20px;
  }

  ${ValueCard}:hover & {
    background-color: #fef3c7;
    color: #ea580c;
  }
`

const ValueTitle = styled.h3`
  font-size: 1.15rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.5rem;
`

const ValueText = styled.p`
  font-size: 0.9rem;
  color: #4b5563;
  line-height: 1.6;
`

// 🔶 Animation Variant
const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 }
}

// 🔶 Data for Values
const values = [
  {
    title: 'Quality',
    text: 'We never compromise on the quality of food and service we provide to our customers.',
    icon: (
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
      </svg>
    )
  },
  {
    title: 'Speed',
    text: 'We understand the value of your time and ensure prompt delivery of your orders.',
    icon: (
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    )
  },
  {
    title: 'Passion',
    text: 'Our love for food drives us to continuously improve and innovate our services.',
    icon: (
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
      </svg>
    )
  },
  {
    title: 'Community',
    text: 'We believe in building strong relationships with our customers and restaurant partners.',
    icon: (
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
      </svg>
    )
  }
]

// 🔶 Final Component
const Values = () => (
  <ValuesSection
    initial="hidden"
    whileInView="visible"
    viewport={{ once: true, amount: 0.3 }}
    transition={{ duration: 0.6 }}
  >
    <ValuesTitle>Our Values</ValuesTitle>
    <ValuesGrid>
      {values.map((val, index) => (
        <ValueCard key={val.title} variants={fadeInUp} transition={{ duration: 0.4, delay: 0.1 * index }}>
          <ValueIcon>{val.icon}</ValueIcon>
          <ValueTitle>{val.title}</ValueTitle>
          <ValueText>{val.text}</ValueText>
        </ValueCard>
      ))}
    </ValuesGrid>
  </ValuesSection>
)

export default Values
