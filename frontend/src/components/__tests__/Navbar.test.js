import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Navbar from '../Navbar';

describe('Navbar Component', () => {
  const renderNavbar = () => {
    render(
      <BrowserRouter>
        <Navbar />
      </BrowserRouter>
    );
  };

  test('renders restaurant name', () => {
    renderNavbar();
    expect(screen.getByText('Food Hub')).toBeInTheDocument();
  });

  test('renders all navigation links', () => {
    renderNavbar();
    expect(screen.getByText('Home')).toBeInTheDocument();
    expect(screen.getByText('Menu')).toBeInTheDocument();
    expect(screen.getByText('Reservation')).toBeInTheDocument();
    expect(screen.getByText('Delivery')).toBeInTheDocument();
  });

  test('all links have correct href attributes', () => {
    renderNavbar();
    expect(screen.getByText('Home').closest('a')).toHaveAttribute('href', '/');
    expect(screen.getByText('Menu').closest('a')).toHaveAttribute('href', '/menu');
    expect(screen.getByText('Reservation').closest('a')).toHaveAttribute('href', '/reservation');
    expect(screen.getByText('Delivery').closest('a')).toHaveAttribute('href', '/delivery');
  });
}); 