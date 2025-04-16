import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';

const DashboardContainer = styled.div`
  padding: 2rem;
  background-color: #fff5ee;
  min-height: calc(100vh - 70px);
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
`;

const Title = styled.h1`
  color: #8B4513;
  font-size: 2.5rem;
`;

const LogoutButton = styled.button`
  padding: 0.5rem 1rem;
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  
  &:hover {
    background-color: #6b3410;
  }
`;

const StatsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
`;

const StatCard = styled.div`
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
`;

const StatTitle = styled.h3`
  color: #666;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
`;

const StatValue = styled.div`
  color: #8B4513;
  font-size: 2rem;
  font-weight: bold;
`;

const Section = styled.div`
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
`;

const SectionTitle = styled.h2`
  color: #8B4513;
  margin-bottom: 1rem;
  font-size: 1.8rem;
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const TableHeader = styled.th`
  padding: 1rem;
  text-align: left;
  border-bottom: 2px solid #ddd;
  color: #8B4513;
`;

const TableRow = styled.tr`
  &:nth-child(even) {
    background-color: #f9f9f9;
  }
`;

const TableCell = styled.td`
  padding: 1rem;
  border-bottom: 1px solid #ddd;
`;

function Dashboard() {
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    totalOrders: 156,
    totalReservations: 89,
    revenue: '$12,450',
    activeUsers: 234
  });

  const [recentOrders, setRecentOrders] = useState([
    { id: 1, customer: 'John Doe', items: 'Pizza, Salad', total: '$45.99', status: 'Delivered' },
    { id: 2, customer: 'Jane Smith', items: 'Pasta, Dessert', total: '$32.50', status: 'In Progress' },
    { id: 3, customer: 'Mike Johnson', items: 'Burger, Fries', total: '$28.75', status: 'Pending' }
  ]);

  const [recentReservations, setRecentReservations] = useState([
    { id: 1, name: 'Sarah Wilson', date: '2024-04-20', time: '19:00', guests: 4, status: 'Confirmed' },
    { id: 2, name: 'David Brown', date: '2024-04-21', time: '20:30', guests: 2, status: 'Pending' },
    { id: 3, name: 'Emily Davis', date: '2024-04-22', time: '18:00', guests: 6, status: 'Confirmed' }
  ]);

  useEffect(() => {
    const isAuthenticated = localStorage.getItem('isAuthenticated');
    if (!isAuthenticated) {
      navigate('/login');
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('isAuthenticated');
    navigate('/login');
  };

  return (
    <DashboardContainer>
      <Header>
        <Title>Admin Dashboard</Title>
        <LogoutButton onClick={handleLogout}>Logout</LogoutButton>
      </Header>

      <StatsGrid>
        <StatCard>
          <StatTitle>Total Orders</StatTitle>
          <StatValue>{stats.totalOrders}</StatValue>
        </StatCard>
        <StatCard>
          <StatTitle>Total Reservations</StatTitle>
          <StatValue>{stats.totalReservations}</StatValue>
        </StatCard>
        <StatCard>
          <StatTitle>Revenue</StatTitle>
          <StatValue>{stats.revenue}</StatValue>
        </StatCard>
        <StatCard>
          <StatTitle>Active Users</StatTitle>
          <StatValue>{stats.activeUsers}</StatValue>
        </StatCard>
      </StatsGrid>

      <Section>
        <SectionTitle>Recent Orders</SectionTitle>
        <Table>
          <thead>
            <tr>
              <TableHeader>Order ID</TableHeader>
              <TableHeader>Customer</TableHeader>
              <TableHeader>Items</TableHeader>
              <TableHeader>Total</TableHeader>
              <TableHeader>Status</TableHeader>
            </tr>
          </thead>
          <tbody>
            {recentOrders.map(order => (
              <TableRow key={order.id}>
                <TableCell>#{order.id}</TableCell>
                <TableCell>{order.customer}</TableCell>
                <TableCell>{order.items}</TableCell>
                <TableCell>{order.total}</TableCell>
                <TableCell>{order.status}</TableCell>
              </TableRow>
            ))}
          </tbody>
        </Table>
      </Section>

      <Section>
        <SectionTitle>Recent Reservations</SectionTitle>
        <Table>
          <thead>
            <tr>
              <TableHeader>Reservation ID</TableHeader>
              <TableHeader>Name</TableHeader>
              <TableHeader>Date</TableHeader>
              <TableHeader>Time</TableHeader>
              <TableHeader>Guests</TableHeader>
              <TableHeader>Status</TableHeader>
            </tr>
          </thead>
          <tbody>
            {recentReservations.map(reservation => (
              <TableRow key={reservation.id}>
                <TableCell>#{reservation.id}</TableCell>
                <TableCell>{reservation.name}</TableCell>
                <TableCell>{reservation.date}</TableCell>
                <TableCell>{reservation.time}</TableCell>
                <TableCell>{reservation.guests}</TableCell>
                <TableCell>{reservation.status}</TableCell>
              </TableRow>
            ))}
          </tbody>
        </Table>
      </Section>
    </DashboardContainer>
  );
}

export default Dashboard; 