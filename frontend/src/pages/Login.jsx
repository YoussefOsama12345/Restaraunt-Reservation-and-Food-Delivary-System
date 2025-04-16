import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate, Link } from 'react-router-dom';

const LoginContainer = styled.div`
  padding: 2rem;
  max-width: 500px;
  margin: 0 auto;
  background-color: #fff5ee;
  min-height: calc(100vh - 70px);
  display: flex;
  flex-direction: column;
  justify-content: center;
`;

const Title = styled.h1`
  color: #8B4513;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.5rem;
`;

const Form = styled.form`
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
`;

const FormGroup = styled.div`
  margin-bottom: 1.5rem;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 0.5rem;
  color: #8B4513;
  font-weight: 500;
`;

const Input = styled.input`
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  
  &:focus {
    outline: none;
    border-color: #8B4513;
  }
`;

const Button = styled.button`
  width: 100%;
  padding: 1rem;
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
  
  &:hover {
    background-color: #6b3410;
  }

  &.secondary {
    background-color: transparent;
    border: 2px solid #8B4513;
    color: #8B4513;
    margin-top: 1rem;

    &:hover {
      background-color: #fff5ee;
    }
  }
`;

const ErrorMessage = styled.div`
  background-color: #f8d7da;
  color: #721c24;
  padding: 1rem;
  border-radius: 5px;
  margin-top: 1rem;
  text-align: center;
`;

const Divider = styled.div`
  display: flex;
  align-items: center;
  text-align: center;
  margin: 1.5rem 0;
  color: #666;

  &::before,
  &::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #ddd;
  }

  &::before {
    margin-right: .5em;
  }

  &::after {
    margin-left: .5em;
  }
`;

const ForgotPassword = styled(Link)`
  display: block;
  text-align: right;
  color: #8B4513;
  text-decoration: none;
  font-size: 0.9rem;
  margin-top: -1rem;
  margin-bottom: 1rem;

  &:hover {
    text-decoration: underline;
  }
`;

function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    name: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    setError(''); // Clear error when user types
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!isLogin && formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    if (isLogin) {
      // Login logic
      if (formData.email === 'admin@foodhub.com' && formData.password === 'admin123') {
        localStorage.setItem('isAuthenticated', 'true');
        navigate('/admin/dashboard');
      } else {
        setError('Invalid email or password');
      }
    } else {
      // Registration logic
      // Here you would typically make an API call to register the user
      console.log('Registration data:', formData);
      // For demo purposes, automatically switch to login after registration
      setIsLogin(true);
      setFormData(prev => ({
        ...prev,
        confirmPassword: '',
        name: ''
      }));
    }
  };

  return (
    <LoginContainer>
      <Title>{isLogin ? 'Login' : 'Create Account'}</Title>
      <Form onSubmit={handleSubmit}>
        {!isLogin && (
          <FormGroup>
            <Label>Full Name</Label>
            <Input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required={!isLogin}
              placeholder="Enter your full name"
            />
          </FormGroup>
        )}

        <FormGroup>
          <Label>Email</Label>
          <Input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            placeholder="Enter your email"
          />
        </FormGroup>
        
        <FormGroup>
          <Label>Password</Label>
          <Input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            placeholder={isLogin ? "Enter your password" : "Create a password"}
          />
        </FormGroup>

        {!isLogin && (
          <FormGroup>
            <Label>Confirm Password</Label>
            <Input
              type="password"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              required={!isLogin}
              placeholder="Confirm your password"
            />
          </FormGroup>
        )}

        {isLogin && (
          <ForgotPassword to="/forgot-password">Forgot Password?</ForgotPassword>
        )}
        
        <Button type="submit">
          {isLogin ? 'Login' : 'Create Account'}
        </Button>
        
        {error && <ErrorMessage>{error}</ErrorMessage>}

        <Divider>OR</Divider>

        <Button 
          type="button" 
          className="secondary"
          onClick={() => {
            setIsLogin(!isLogin);
            setError('');
            setFormData(prev => ({
              ...prev,
              confirmPassword: '',
              name: ''
            }));
          }}
        >
          {isLogin ? 'Create New Account' : 'Already have an account? Login'}
        </Button>
      </Form>
    </LoginContainer>
  );
}

export default Login; 