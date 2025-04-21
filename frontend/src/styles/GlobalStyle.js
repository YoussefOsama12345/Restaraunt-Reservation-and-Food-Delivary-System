// src/GlobalStyle.js
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  /* Reset & Base Styles */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scrollbar-width: thin;                     /* Firefox */
    scrollbar-color: #ea580c #fdf3ee;          /* Firefox */
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    font-family: ${({ theme }) => theme.fonts.body};
    line-height: 1.6;
    color: ${({ theme }) => theme.colors.text};
    background-color: ${({ theme }) => theme.colors.background};
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: ${({ theme }) => theme.fonts.heading};
    margin-bottom: 1rem;
  }

  a {
    color: ${({ theme }) => theme.colors.primary};
    text-decoration: none;
    transition: color 0.3s ease;

    &:hover {
      color: ${({ theme }) => theme.colors.secondary};
    }
  }

  button {
    cursor: pointer;
    font-family: ${({ theme }) => theme.fonts.body};
  }

  img {
    max-width: 100%;
    height: auto;
  }

  .container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  .section-title {
    text-align: center;
    margin-bottom: 3rem;

    h2 {
      font-size: 2.5rem;
      color: ${({ theme }) => theme.colors.primary};
      margin-bottom: 1rem;
    }

    p {
      color: ${({ theme }) => theme.colors.textLight};
      max-width: 600px;
      margin: 0 auto;
    }
  }

  /* Scrollbar Styling (WebKit) */
  ::-webkit-scrollbar {
    width: 12px;
  }

  ::-webkit-scrollbar-track {
    background: #fdf3ee;
  }

  ::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #f97316, #ea580c);
    border-radius: 6px;
  }

  ::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #ea580c, #c2410c);
  }
`;

export default GlobalStyle;
