import React, { useState } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FcGoogle } from 'react-icons/fc';
import { AiFillApple, AiFillGithub } from 'react-icons/ai';

const LoginContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
  overflow: hidden;
`;

const LoginCard = styled(motion.div)`
  background: white;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: ${({ theme }) => theme.colors.secondary};
  }
`;

const Title = styled.h2`
  color: ${({ theme }) => theme.colors.primary};
  margin-bottom: 1.5rem;
  font-size: 2rem;
  text-align: center;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
`;

const InputGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  color: ${({ theme }) => theme.colors.textLight};
  font-size: 0.9rem;
`;

const Input = styled.input`
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
  background-color: white;
  color: #1f2937;

  &:focus {
    outline: none;
    border-color: ${({ theme }) => theme.colors.secondary};
    box-shadow: 0 0 0 2px rgba(249, 115, 22, 0.2);
  }

  &::placeholder {
    color: #9ca3af;
  }
`;

const SubmitButton = styled.button`
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

const LinkText = styled.p`
  text-align: center;
  color: ${({ theme }) => theme.colors.textLight};
  font-size: 0.9rem;
  margin-top: 1rem;

  a {
    color: ${({ theme }) => theme.colors.secondary};
    text-decoration: none;
    font-weight: 500;

    &:hover {
      text-decoration: underline;
    }
  }
`;

const Divider = styled.div`
  display: flex;
  align-items: center;
  text-align: center;
  margin: 1.5rem 0;
  color: #6b7280;
  font-size: 0.875rem;

  &::before,
  &::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #e5e7eb;
  }

  &::before {
    margin-right: 1rem;
  }

  &::after {
    margin-left: 1rem;
  }
`;

const SocialButton = styled.button`
  width: 100%;
  padding: 0.75rem 1.5rem;
  background-color: white;
  color: #374151;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;

  &:hover {
    border-color: #f97316;
    color: #f97316;
  }

  svg {
    width: 1.25rem;
    height: 1.25rem;
  }

  &.apple {
    background-color: black;
    color: white;
    border: none;

    &:hover {
      background-color: #1a1a1a;
    }
  }

  &.github {
    background-color: #24292e;
    color: white;
    border: none;

    &:hover {
      background-color: #2f363d;
    }
  }
`;

const SocialButtonsContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement login logic
    console.log('Login attempt:', formData);
  };

  const handleSocialLogin = (provider) => {
    // TODO: Implement social login logic
    console.log(`Login with ${provider}`);
  };

  return (
    <LoginContainer>
      <LoginCard
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Title>Welcome to <span>Food Hub</span></Title>
        <Form onSubmit={handleSubmit}>
          <InputGroup>
            <Label htmlFor="email">Email</Label>
            <Input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </InputGroup>
          <InputGroup>
            <Label htmlFor="password">Password</Label>
            <Input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </InputGroup>
          <LinkText>
            <Link to="/forgot-password">Forgot your password?</Link>
          </LinkText>
          <SubmitButton type="submit">Log In</SubmitButton>
        </Form>

        <Divider>Or continue with</Divider>

        <SocialButtonsContainer>
          <SocialButton onClick={() => handleSocialLogin('google')}>
            <FcGoogle />
            Sign in with Google
          </SocialButton>
          <SocialButton className="apple" onClick={() => handleSocialLogin('apple')}>
            <AiFillApple />
            Sign in with Apple
          </SocialButton>
          <SocialButton className="github" onClick={() => handleSocialLogin('github')}>
            <AiFillGithub />
            Sign in with GitHub
          </SocialButton>
        </SocialButtonsContainer>

        <LinkText>
          Don't have an account? <Link to="/register">Sign up</Link>
        </LinkText>
      </LoginCard>
    </LoginContainer>
  );
};

export default Login; 