import React, { useState } from 'react';
import styled from 'styled-components';

const DeliveryContainer = styled.div`
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  background-color: #fff5ee;
  min-height: calc(100vh - 70px);
`;

const Title = styled.h1`
  color: #8B4513;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.5rem;
`;

const ContentWrapper = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`;

const InfoSection = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
`;

const InfoTitle = styled.h2`
  color: #8B4513;
  margin-bottom: 1rem;
  font-size: 1.8rem;
`;

const InfoText = styled.p`
  color: #666;
  line-height: 1.6;
  margin-bottom: 1.5rem;
`;

const InfoList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const InfoItem = styled.li`
  color: #666;
  margin-bottom: 0.8rem;
  padding-left: 1.5rem;
  position: relative;
  
  &:before {
    content: "✓";
    color: #8B4513;
    position: absolute;
    left: 0;
  }
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

const TextArea = styled.textarea`
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  min-height: 100px;
  
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
`;

const SuccessMessage = styled.div`
  background-color: #d4edda;
  color: #155724;
  padding: 1rem;
  border-radius: 5px;
  margin-top: 1rem;
  text-align: center;
`;

function Delivery() {
  const [formData, setFormData] = useState({
    name: '',
    address: '',
    phone: '',
    email: '',
    orderDetails: ''
  });
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would typically send the data to your backend
    console.log('Delivery order submitted:', formData);
    setIsSubmitted(true);
    setFormData({
      name: '',
      address: '',
      phone: '',
      email: '',
      orderDetails: ''
    });
  };

  return (
    <DeliveryContainer>
      <Title>Food Delivery</Title>
      <ContentWrapper>
        <InfoSection>
          <InfoTitle>Delivery Information</InfoTitle>
          <InfoText>
            Enjoy our delicious food in the comfort of your home. We offer fast and reliable delivery service 
            to your doorstep.
          </InfoText>
          <InfoList>
            <InfoItem>Free delivery for orders above $30</InfoItem>
            <InfoItem>Delivery time: 30-45 minutes</InfoItem>
            <InfoItem>Available 7 days a week</InfoItem>
            <InfoItem>Contactless delivery option</InfoItem>
            <InfoItem>Real-time order tracking</InfoItem>
          </InfoList>
          <InfoText>
            For any special requests or dietary requirements, please mention them in the order details section.
          </InfoText>
        </InfoSection>

        <Form onSubmit={handleSubmit}>
          <FormGroup>
            <Label>Full Name</Label>
            <Input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </FormGroup>
          
          <FormGroup>
            <Label>Delivery Address</Label>
            <Input
              type="text"
              name="address"
              value={formData.address}
              onChange={handleChange}
              required
            />
          </FormGroup>
          
          <FormGroup>
            <Label>Phone Number</Label>
            <Input
              type="tel"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </FormGroup>
          
          <FormGroup>
            <Label>Email</Label>
            <Input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </FormGroup>
          
          <FormGroup>
            <Label>Order Details</Label>
            <TextArea
              name="orderDetails"
              value={formData.orderDetails}
              onChange={handleChange}
              placeholder="Please list the items you'd like to order and any special instructions"
              required
            />
          </FormGroup>
          
          <Button type="submit">Place Order</Button>
          
          {isSubmitted && (
            <SuccessMessage>
              Your order has been submitted successfully! We'll contact you shortly to confirm the details.
            </SuccessMessage>
          )}
        </Form>
      </ContentWrapper>
    </DeliveryContainer>
  );
}

export default Delivery; 