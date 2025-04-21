import styled, { keyframes } from 'styled-components'

// 🔄 Subtle float animation for background circle
const float = keyframes`
  0% { transform: translateY(-50%) translateX(0); }
  50% { transform: translateY(-50%) translateX(10px); }
  100% { transform: translateY(-50%) translateX(0); }
`

const Section = styled.section`
  width: 100%;
  padding: 5rem 1rem;
  background: ${({ theme }) => theme.colors?.background || '#fff'};
`

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`

const Grid = styled.div`
  display: grid;
  gap: 3rem;
  align-items: center;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
  }
`

const ImageWrapper = styled.div`
  position: relative;
`

const CircleDecoration = styled.div`
  position: absolute;
  left: -2rem;
  top: 50%;
  transform: translateY(-50%);
  width: 9rem;
  height: 9rem;
  background-color: #4ade80;
  border-radius: 50%;
  opacity: 0.1;
  animation: ${float} 5s ease-in-out infinite;
`

const ChefImage = styled.img`
  position: relative;
  z-index: 10;
  width: 100%;
  height: 500px;
  object-fit: cover;
  border-radius: 1.5rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
`

const TextContent = styled.div`
  display: flex;
  flex-direction: column;
  gap: 2rem;
`

const Title = styled.h2`
  font-size: 2.25rem;
  font-weight: 800;
  line-height: 1.3;
  color: ${({ theme }) => theme.colors?.primary || '#111827'};

  @media (min-width: 768px) {
    font-size: 2.5rem;
  }
`

const Paragraph = styled.p`
  font-size: 1.1rem;
  line-height: 1.8;
  color: ${({ theme }) => theme.colors?.textSecondary || '#6b7280'};
`

const Card = styled.div`
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(8px);
  border-radius: 1.25rem;
  padding: 2rem;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  transition: transform 0.4s ease;

  &:hover {
    transform: translateY(-5px);
  }
`

const Stars = styled.div`
  display: flex;
  gap: 0.3rem;
  font-size: 1.25rem;

  span {
    background: linear-gradient(to right, #facc15, #fbbf24);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
`

const Quote = styled.p`
  font-size: 1rem;
  font-style: italic;
  color: #4b5563;
  line-height: 1.7;
`

const CustomerInfo = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
`

const Avatar = styled.div`
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
`

const CustomerDetails = styled.div`
  flex: 1;

  h4 {
    font-size: 0.95rem;
    font-weight: 600;
    color: #111827;
  }

  p {
    font-size: 0.8rem;
    color: #6b7280;
  }
`

const Dots = styled.div`
  display: flex;
  gap: 0.3rem;

  div {
    width: 0.6rem;
    height: 0.6rem;
    border-radius: 999px;
    background-color: #e5e7eb;

    &:first-child {
      background-color: #4ade80;
    }
  }
`

const Testimonials = () => {
  return (
    <Section>
      <Container>
        <Grid>
          <ImageWrapper>
            <CircleDecoration />
            <ChefImage
              src="https://images.unsplash.com/photo-1622021142947-da7dedc7c39a?auto=format&fit=crop&w=800&q=80"
              alt="Our Chef"
            />
          </ImageWrapper>

          <TextContent>
            <Title>
              What Our Customers<br />Say About Us
            </Title>
            <Paragraph>
              We pride ourselves on authentic, fresh, and delicious food. But don't just take our word for it — here’s what our customers have to say!
            </Paragraph>

            <Card>
              <Stars>
                {[...Array(5)].map((_, i) => (
                  <span key={i}>★</span>
                ))}
              </Stars>
              <Quote>
                “The food is absolutely amazing! Fresh ingredients, authentic recipes, and the delivery is always on time. This is my go-to place for ordering food!”
              </Quote>
              <CustomerInfo>
                <Avatar>
                  <img
                    src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=100&q=80"
                    alt="Customer"
                  />
                </Avatar>
                <CustomerDetails>
                  <h4>Sarah Johnson</h4>
                  <p>Regular Customer</p>
                </CustomerDetails>
                <Dots>
                  {[...Array(4)].map((_, i) => (
                    <div key={i} />
                  ))}
                </Dots>
              </CustomerInfo>
            </Card>
          </TextContent>
        </Grid>
      </Container>
    </Section>
  )
}

export default Testimonials
