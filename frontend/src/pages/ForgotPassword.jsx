import { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { motion } from 'framer-motion';

// Reuse styled components from Login.jsx
const PageContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
  overflow: hidden;
`;

const AuthCard = styled(motion.div)`
  background: white;
  padding: 2.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
              0 10px 10px -5px rgba(0, 0, 0, 0.04);
  width: 100%;
  max-width: 420px;
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #f97316 0%, #ea580c 100%);
  }
`;

const Title = styled.h1`
  color: #1f2937;
  font-size: 1.875rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  text-align: center;
`;

const Subtitle = styled.p`
  color: #6b7280;
  font-size: 0.875rem;
  text-align: center;
  margin-bottom: 2rem;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
`;

const InputGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  color: #4b5563;
  font-size: 0.875rem;
  font-weight: 500;
`;

const Input = styled.input`
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  font-size: 1rem;
  color: #1f2937;
  transition: all 0.2s;
  background-color: white;

  &:focus {
    outline: none;
    border-color: #f97316;
    box-shadow: 0 0 0 3px rgba(249, 115, 22, 0.1);
  }

  &::placeholder {
    color: #9ca3af;
  }
`;

const Button = styled.button`
  background-color: #f97316;
  color: white;
  padding: 0.75rem 1.5rem;
  border: 2px solid #f97316;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;

  &:hover {
    background-color: white;
    color: #f97316;
    border-color: #f97316;
  }
`;

const LinkText = styled(Link)`
  color: #f97316;
  font-size: 0.875rem;
  text-decoration: none;
  text-align: center;
  
  &:hover {
    text-decoration: underline;
  }
`;

const ErrorMessage = styled.p`
  color: #ef4444;
  font-size: 0.875rem;
  margin-top: 0.25rem;
`;

const SuccessMessage = styled.div`
  background-color: #ecfdf5;
  color: #047857;
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
  text-align: center;
  font-size: 0.875rem;
`;

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const validateForm = () => {
    if (!email) {
      setError('Email is required');
      return false;
    }
    if (!/\S+@\S+\.\S+/.test(email)) {
      setError('Email is invalid');
      return false;
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsLoading(true);
    try {
      // Add your password reset logic here
      console.log('Requesting password reset for:', email);
      await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate API call
      setIsSuccess(true);
    } catch (error) {
      console.error('Password reset error:', error);
      setError('Failed to send reset instructions. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <PageContainer>
      <AuthCard
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Title>Reset Password</Title>
        <Subtitle>
          Enter your email address and we'll send you instructions to reset your password
        </Subtitle>

        {isSuccess ? (
          <>
            <SuccessMessage>
              Password reset instructions have been sent to your email address.
              Please check your inbox.
            </SuccessMessage>
            <LinkText to="/login" style={{ display: 'block', textAlign: 'center' }}>
              Return to Sign In
            </LinkText>
          </>
        ) : (
          <Form onSubmit={handleSubmit}>
            <InputGroup>
              <Label htmlFor="email">Email Address</Label>
              <Input
                type="email"
                id="email"
                placeholder="you@example.com"
                value={email}
                onChange={(e) => {
                  setEmail(e.target.value);
                  setError('');
                }}
                aria-invalid={!!error}
              />
              {error && <ErrorMessage>{error}</ErrorMessage>}
            </InputGroup>

            <Button type="submit" disabled={isLoading}>
              {isLoading ? 'Sending Instructions...' : 'Send Reset Instructions'}
            </Button>

            <div style={{ textAlign: 'center', marginTop: '1rem' }}>
              <LinkText to="/login">Back to Sign In</LinkText>
            </div>
          </Form>
        )}
      </AuthCard>
    </PageContainer>
  );
};

export default ForgotPassword; 