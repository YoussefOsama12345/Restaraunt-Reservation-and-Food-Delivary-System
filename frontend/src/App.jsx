import React from 'react';
import { Routes, Route } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import Home from './pages/Home';
import Menu from './pages/Menu';
import Cart from './pages/Cart';
import Reservation from './pages/Reservation';
import Delivery from './pages/Delivery';
import Login from './pages/Login';
import Dashboard from './pages/admin/Dashboard';
import ProtectedRoute from './components/ProtectedRoute';
import { CartProvider } from './context/CartContext';
import { RestaurantProvider } from './context/RestaurantContext';
import './assets/styles/App.css';

function App() {
  return (
    <div className="App">
      <RestaurantProvider>
        <CartProvider>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/admin/dashboard" element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            } />
            <Route path="/" element={<MainLayout />}>
              <Route index element={<Home />} />
              <Route path="menu" element={<Menu />} />
              <Route path="cart" element={<Cart />} />
              <Route path="reservation" element={<Reservation />} />
              <Route path="delivery" element={<Delivery />} />
            </Route>
          </Routes>
        </CartProvider>
      </RestaurantProvider>
    </div>
  );
}

export default App; 