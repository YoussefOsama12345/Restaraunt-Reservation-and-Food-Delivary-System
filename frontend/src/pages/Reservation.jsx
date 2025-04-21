import React, { useState, useRef, useEffect } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import {
  FaUser, FaEnvelope, FaPhone, FaCalendarAlt,
  FaClock, FaUsers, FaGlassCheers
} from 'react-icons/fa';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const PageContainer = styled.div`
  min-height: 100vh;
  background: #fff7ed;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 180px 20px 40px;

  @media (max-width: 768px) {
    padding: 140px 16px 40px;
  }
`;

const ContentWrapper = styled.div`
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
`;

const Card = styled(motion.div)`
  display: flex;
  flex-direction: row;
  border: 3px solid #f97316;
  border-radius: 20px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  background: white;
  transition: all 0.4s ease;

  &:hover {
    transform: scale(1.01);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.12);
  }

  @media (max-width: 968px) {
    flex-direction: column;
  }
`;

const FormSection = styled.div`
  padding: 40px;
  background: white;
  width: 60%;

  @media (max-width: 968px) {
    width: 100%;
    padding: 24px;
  }
`;

const Title = styled.h1`
  color: #1f2937;
  font-size: 2.2rem;
  margin-bottom: 1rem;

  @media (max-width: 480px) {
    font-size: 1.75rem;
  }
`;

const Subtitle = styled.p`
  color: #6b7280;
  margin-bottom: 1.5rem;
  font-size: 1rem;

  @media (max-width: 480px) {
    font-size: 0.95rem;
  }
`;

const Form = styled.form`
  display: grid;
  gap: 20px;
`;

const FormGroup = styled.div`
  display: grid;
  gap: 8px;
  position: relative;
`;

const FormRow = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;

  @media (max-width: 640px) {
    grid-template-columns: 1fr;
  }
`;

const LeftIcon = styled.div`
  position: absolute;
  left: 12px;
  color: #f97316;
  display: flex;
  align-items: center;

  svg {
    width: 18px;
    height: 18px;
  }
`;

const RightIcon = styled.div`
  position: absolute;
  right: 12px;
  color: #f97316;
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 8px;

  svg {
    width: 18px;
    height: 18px;
  }
`;

const InputWrapper = styled.div`
  position: relative;
  display: flex;
  align-items: center;
`;

const Label = styled.label`
  color: #4b5563;
  font-weight: 500;
`;

const RegularInput = styled.input`
  width: 100%;
  padding: 12px 12px 12px 40px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  background-color: white;
  color: #1f2937;
`;

const DateTimeInput = styled(RegularInput)`
  padding-right: 40px;
`;

const Select = styled.select`
  width: 100%;
  padding: 12px 40px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  background-color: white;
  color: #1f2937;
`;

const SubmitButton = styled(motion.button)`
  background-color: #f97316;
  color: white;
  padding: 14px 20px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;

  @media (max-width: 480px) {
    font-size: 0.95rem;
    padding: 12px;
  }
`;

const ImageSection = styled.div`
  position: relative;
  width: 40%;
  height: auto;
  max-height: 800px;
  overflow: hidden;

  @media (max-width: 968px) {
    order: -1;
    width: 100%;
    height: 300px;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
`;

// Modal Styles
const ModalOverlay = styled(motion.div)`
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(3px);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const ModalContent = styled(motion.div)`
  background: white;
  padding: 2.5rem 2rem;
  border-radius: 1rem;
  max-width: 400px;
  width: 90%;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  text-align: center;
`;

const ModalIcon = styled.div`
  background-color: #f97316;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin: 0 auto 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;

  svg {
    color: white;
    width: 28px;
    height: 28px;
  }
`;

const ModalTitle = styled.h3`
  font-size: 1.75rem;
  color: #f97316;
  font-weight: bold;
  margin-bottom: 0.75rem;
`;

const ModalText = styled.p`
  font-size: 1rem;
  color: #4b5563;
  line-height: 1.5;
`;

const ReservationPage = () => {
  const [formData, setFormData] = useState({
    name: '', email: '', phone: '', date: '', time: '', guests: '2', occasion: 'regular'
  });
  const [showSuccess, setShowSuccess] = useState(false);
  const navigate = useNavigate();
  const dateInputRef = useRef(null);
  const timeInputRef = useRef(null);

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  const handleIconClick = (ref) => ref?.current?.showPicker?.();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setShowSuccess(true);
    setTimeout(() => {
      setShowSuccess(false);
      navigate('/');
    }, 2000);
  };

  return (
    <>
      <Navbar />
      <PageContainer>
        <ContentWrapper>
          <motion.div initial={{ opacity: 0, y: 40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <Card>
              <FormSection>
                <Title>Reserve Your Table</Title>
                <Subtitle>Book your dining experience with us and enjoy a memorable meal.</Subtitle>
                <Form onSubmit={handleSubmit}>
                  <FormGroup>
                    <Label htmlFor="name">Full Name</Label>
                    <InputWrapper>
                      <LeftIcon><FaUser /></LeftIcon>
                      <RegularInput type="text" id="name" name="name" placeholder="Enter your name" value={formData.name} onChange={handleChange} required />
                    </InputWrapper>
                  </FormGroup>

                  <FormGroup>
                    <Label htmlFor="email">Email Address</Label>
                    <InputWrapper>
                      <LeftIcon><FaEnvelope /></LeftIcon>
                      <RegularInput type="email" id="email" name="email" placeholder="Enter your email" value={formData.email} onChange={handleChange} required />
                    </InputWrapper>
                  </FormGroup>

                  <FormGroup>
                    <Label htmlFor="phone">Phone Number</Label>
                    <InputWrapper>
                      <LeftIcon><FaPhone /></LeftIcon>
                      <RegularInput type="tel" id="phone" name="phone" placeholder="Enter your phone" value={formData.phone} onChange={handleChange} required />
                    </InputWrapper>
                  </FormGroup>

                  <FormRow>
                    <FormGroup>
                      <Label htmlFor="date">Date</Label>
                      <InputWrapper>
                        <DateTimeInput type="date" id="date" name="date" value={formData.date} onChange={handleChange} ref={dateInputRef} required />
                        <RightIcon onClick={() => handleIconClick(dateInputRef)}><FaCalendarAlt /></RightIcon>
                      </InputWrapper>
                    </FormGroup>

                    <FormGroup>
                      <Label htmlFor="time">Time</Label>
                      <InputWrapper>
                        <DateTimeInput type="time" id="time" name="time" value={formData.time} onChange={handleChange} ref={timeInputRef} required />
                        <RightIcon onClick={() => handleIconClick(timeInputRef)}><FaClock /></RightIcon>
                      </InputWrapper>
                    </FormGroup>
                  </FormRow>

                  <FormRow>
                    <FormGroup>
                      <Label htmlFor="guests">Guests</Label>
                      <InputWrapper>
                        <LeftIcon><FaUsers /></LeftIcon>
                        <Select id="guests" name="guests" value={formData.guests} onChange={handleChange}>
                          {[1, 2, 3, 4, 5, 6, 7, 8].map(num => (
                            <option key={num} value={num}>{num} {num === 1 ? 'Guest' : 'Guests'}</option>
                          ))}
                        </Select>
                      </InputWrapper>
                    </FormGroup>

                    <FormGroup>
                      <Label htmlFor="occasion">Occasion</Label>
                      <InputWrapper>
                        <LeftIcon><FaGlassCheers /></LeftIcon>
                        <Select id="occasion" name="occasion" value={formData.occasion} onChange={handleChange}>
                          <option value="regular">Regular Dining</option>
                          <option value="birthday">Birthday</option>
                          <option value="anniversary">Anniversary</option>
                          <option value="business">Business</option>
                          <option value="special">Special Occasion</option>
                        </Select>
                      </InputWrapper>
                    </FormGroup>
                  </FormRow>

                  <SubmitButton type="submit" whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                    Book Table
                  </SubmitButton>
                </Form>
              </FormSection>

              <ImageSection>
                <img
                  src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1400&q=80"
                  alt="Restaurant Interior"
                />
              </ImageSection>
            </Card>
          </motion.div>
        </ContentWrapper>
      </PageContainer>

      <AnimatePresence>
        {showSuccess && (
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
                <svg fill="none" stroke="currentColor" strokeWidth="3" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              </ModalIcon>
              <ModalTitle>Message Sent!</ModalTitle>
              <ModalText>Your message has been successfully submitted.<br />We'll get back to you shortly.</ModalText>
            </ModalContent>
          </ModalOverlay>
        )}
      </AnimatePresence>

      <Footer />
    </>
  );
};

export default ReservationPage;
