import { useState } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';

// Animation variant
const fadeIn = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 },
};

// Layout Styling
const Section = styled.section`
  background-color: #fef4f0;
  padding: 4rem 1rem;
  min-height: 100vh;
  display: flex;
  align-items: center;
`;

const Container = styled.div`
  max-width: 1100px;
  margin: auto;
  display: grid;
  gap: 3rem;
  grid-template-columns: 1fr;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
  }
`;

const InfoBox = styled(motion.div)`
  background: #fff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
`;

const Title = styled.h2`
  font-size: 2rem;
  font-weight: bold;
  color: #1e293b;
  margin-bottom: 1rem;
`;

const Text = styled.p`
  font-size: 1rem;
  color: #6b7280;
  margin-bottom: 1.5rem;
`;

const ContactDetail = styled.div`
  margin-bottom: 1.25rem;
  line-height: 1.6;

  strong {
    display: block;
    font-weight: 600;
    color: #f97316;
    margin-bottom: 0.25rem;
  }

  span {
    color: #374151;
  }
`;

const FormBox = styled(motion.form)`
  background: #fff;
  padding: 2rem;
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
`;

const Input = styled.input`
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border: 2px solid #e2e8f0;
  font-size: 1rem;
  background-color: #ffffff;
  color: #1e293b;
  transition: all 0.3s ease;

  &::placeholder {
    color: #94a3b8;
  }

  &:focus {
    border-color: #f97316;
    box-shadow: 0 0 0 3px rgba(249, 115, 22, 0.15);
    outline: none;
  }

  &:hover {
    border-color: #f97316;
  }
`;

const TextArea = styled.textarea`
  padding: 0.75rem 1rem;
  min-height: 120px;
  border-radius: 0.5rem;
  border: 2px solid #e2e8f0;
  font-size: 1rem;
  background-color: #ffffff;
  color: #1e293b;
  resize: none;
  transition: all 0.3s ease;

  &::placeholder {
    color: #94a3b8;
  }

  &:focus {
    border-color: #f97316;
    box-shadow: 0 0 0 3px rgba(249, 115, 22, 0.15);
    outline: none;
  }

  &:hover {
    border-color: #f97316;
  }
`;

const Button = styled.button`
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;

  &:hover {
    transform: translateY(-2px);
  }
`;

// Modal Styles
const ModalOverlay = styled(motion.div)`
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 50;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
`;

const ModalContent = styled(motion.div)`
  background: white;
  padding: 2.5rem 2rem;
  border-radius: 1.25rem;
  text-align: center;
  max-width: 420px;
  width: 100%;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);

  &::before {
    content: '';
    position: absolute;
    top: -40%;
    left: -30%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(249, 115, 22, 0.05), transparent 70%);
    z-index: -1;
  }
`;

const ModalTitle = styled.h3`
  font-size: 1.8rem;
  font-weight: 800;
  background: linear-gradient(135deg, #f97316, #ea580c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
`;

const ModalIcon = styled.div`
  width: 60px;
  height: 60px;
  background: #f97316;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.25rem;

  svg {
    color: white;
    width: 30px;
    height: 30px;
  }
`;

const ModalText = styled.p`
  font-size: 1rem;
  color: #475569;
  margin-bottom: 1.75rem;
`;

const ModalButton = styled.button`
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: background 0.3s ease;

  &:hover {
    background: linear-gradient(135deg, #ea580c, #c2410c);
  }
`;

// Component
const RestaurantContact = () => {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });
  const [showModal, setShowModal] = useState(false);

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
    setFormData({ name: '', email: '', message: '' });
    setShowModal(true);
  };

  const handleModalClose = () => {
    setShowModal(false); // stays on the same page
  };

  return (
    <Section id="contact">
      <Container>
        <InfoBox
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          variants={fadeIn}
        >
          <Title>Contact Our Restaurant</Title>
          <Text>
            We'd love to hear from you. Whether it's a reservation, catering, or general inquiry – we're here to help.
          </Text>
          <ContactDetail>
            <strong>Phone</strong>
            <span>+20 123 456 7890</span>
          </ContactDetail>
          <ContactDetail>
            <strong>Email</strong>
            <span>info@foodhub.com</span>
          </ContactDetail>
          <ContactDetail>
            <strong>Location</strong>
            <span>123 Food Street, Cairo, Egypt</span>
          </ContactDetail>
        </InfoBox>

        <FormBox
          onSubmit={handleSubmit}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
          variants={fadeIn}
        >
          <Input
            type="text"
            name="name"
            placeholder="Your Name"
            value={formData.name}
            onChange={handleChange}
            required
          />
          <Input
            type="email"
            name="email"
            placeholder="Your Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <TextArea
            name="message"
            placeholder="Your Message"
            value={formData.message}
            onChange={handleChange}
            required
          />
          <Button type="submit">Send Message</Button>
        </FormBox>
      </Container>

      {/* Modal */}
      <AnimatePresence>
        {showModal && (
          <ModalOverlay
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <ModalContent
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.9, opacity: 0 }}
              transition={{ duration: 0.3 }}
            >
              <ModalIcon>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </ModalIcon>
              <ModalTitle>Message Sent!</ModalTitle>
              <ModalText>Your message has been successfully submitted. We'll get back to you shortly.</ModalText>
              <ModalButton onClick={handleModalClose}>OK</ModalButton>
            </ModalContent>
          </ModalOverlay>
        )}
      </AnimatePresence>
    </Section>
  );
};

export default RestaurantContact;
