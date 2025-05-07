import styled from 'styled-components'

//  Styled Header Container
const HeaderWrapper = styled.header`
    width: 100%;
    background-color: #111827; 
    backdrop-filter: blur(10px);
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid #374151; /* Tailwind's gray-700 */
`

//  Responsive Inner Container
const Container = styled.div`
    max-width: 1280px;
    margin: 0 auto;
    padding: 1rem;

    @media (min-width: 640px) {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    @media (min-width: 1024px) {
        padding-left: 2rem;
        padding-right: 2rem;
    }
`

// Title with theme-aware color fallback
const Title = styled.h1`
    font-size: 1.5rem;
    font-weight: 600;
    color: ${({ theme }) => theme?.colors?.textPrimary || '#f3f4f6'};
`

// Header Component in JSX
const Header = ({ title }) => (
    <HeaderWrapper role="banner" aria-label="Main header">
        <Container>
        <Title>{title}</Title>
        </Container>
    </HeaderWrapper>
)

export default Header
