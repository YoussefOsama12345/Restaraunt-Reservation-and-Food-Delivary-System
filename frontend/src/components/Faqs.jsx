import { useState } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { FiChevronDown } from 'react-icons/fi';

// Styled Components
const FAQSection = styled.section`
  padding: 4rem 1rem;
  background-color: #fdf2ec;
`;

const Container = styled.div`
  max-width: 900px;
  margin: 0 auto;
`;

const Title = styled.h2`
  font-size: 2.25rem;
  font-weight: 800;
  color: #1e293b;
  text-align: center;
  margin-bottom: 3rem;
  letter-spacing: -0.5px;
`;

const FAQItem = styled(motion.div)`
  background: #ffffff;
  border-radius: 1rem;
  overflow: hidden;
  margin-bottom: 1.25rem;
  border: 1px solid #f3f4f6;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  will-change: transform;

  &:hover {
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
    transform: translateY(-2px);
  }
`;

const Question = styled.button`
  width: 100%;
  padding: 1.25rem 1.5rem;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1.1rem;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  color: #111827;
  transition: color 0.3s ease;

  &:hover {
    color: #f97316;
  }

  &:focus {
    outline: none;
    border: none;
    box-shadow: none;
  }
`;

const AnswerWrapper = styled(motion.div)`
  padding: 0 1.5rem 1.25rem;
  background-color: #fff;
  overflow: hidden;
`;

const AnswerText = styled(motion.p)`
  color: #4b5563;
  font-size: 0.97rem;
  line-height: 1.65;
`;

const Chevron = styled(motion.div)`
  display: flex;
  align-items: center;
  justify-content: center;
  transform-origin: center;
  transition: color 0.3s ease;

  svg {
    color: #111827;
    transition: color 0.3s ease;
  }

  ${Question}:hover & svg {
    color: #f97316;
  }
`;

const answerVariants = {
  collapsed: {
    opacity: 0,
    height: 0,
    scaleY: 0.95,
    transition: {
      duration: 0.25,
      ease: [0.4, 0, 0.2, 1]
    }
  },
  open: {
    opacity: 1,
    height: 'auto',
    scaleY: 1,
    transition: {
      duration: 0.5,
      ease: [0.22, 1, 0.36, 1]
    }
  }
};

const rotateVariants = {
  open: { rotate: 180, transition: { duration: 0.3 } },
  closed: { rotate: 0, transition: { duration: 0.3 } }
};

const itemVariants = {
  hidden: { opacity: 0, y: 10 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.1, duration: 0.3, ease: 'easeOut' }
  })
};

const faqs = [
  {
    question: "What are your delivery hours?",
    answer: "We deliver daily from 10:00 AM to 10:00 PM, including weekends and holidays."
  },
  {
    question: "Do you have vegetarian or vegan options?",
    answer: "Absolutely! Our menu features a wide variety of plant-based and vegetarian dishes."
  },
  {
    question: "Can I make a reservation online?",
    answer: "Yes, you can book a table directly from our website or through our app."
  },
  {
    question: "Do you cater for events?",
    answer: "Yes, we offer full catering services for both small and large events. Contact us for custom packages."
  },
  {
    question: "What payment methods do you accept?",
    answer: "We accept cash, all major credit cards, and mobile wallets like Apple Pay and Google Pay."
  },
];

const RestaurantFAQ = () => {
  const [openIndex, setOpenIndex] = useState(null);

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <FAQSection id="faqs">
      <Container>
        <Title>Frequently Asked Questions</Title>
        {faqs.map((item, i) => (
          <FAQItem
            key={i}
            custom={i}
            initial="hidden"
            animate="visible"
            variants={itemVariants}
          >
            <Question onClick={() => toggleFAQ(i)}>
              {item.question}
              <Chevron
                variants={rotateVariants}
                animate={openIndex === i ? 'open' : 'closed'}
              >
                <FiChevronDown size={22} />
              </Chevron>
            </Question>

            <AnimatePresence initial={false}>
              {openIndex === i && (
                <AnswerWrapper
                  key="content"
                  initial="collapsed"
                  animate="open"
                  exit="collapsed"
                  variants={answerVariants}
                >
                  <AnswerText
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    transition={{ delay: 0.1, duration: 0.35 }}
                  >
                    {item.answer}
                  </AnswerText>
                </AnswerWrapper>
              )}
            </AnimatePresence>
          </FAQItem>
        ))}
      </Container>
    </FAQSection>
  );
};

export default RestaurantFAQ;