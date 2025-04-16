import React, { createContext, useState, useContext } from 'react';

const RestaurantContext = createContext();

export function RestaurantProvider({ children }) {
  const [menuItems, setMenuItems] = useState([
    {
      id: 1,
      name: "Creamy Pasta Carbonara",
      description: "Classic Italian pasta with creamy sauce, pancetta, and parmesan cheese",
      price: 250,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1612874742237-6526221588e3?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 2,
      name: "Margherita Pizza",
      description: "Traditional pizza with fresh mozzarella, tomatoes, and basil",
      price: 180,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 3,
      name: "Mediterranean Salad",
      description: "Fresh greens with feta cheese, olives, and balsamic dressing",
      price: 120,
      category: "Appetizers",
      image: "https://images.unsplash.com/photo-1540420773420-3366772f4999?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 4,
      name: "Chocolate Lava Cake",
      description: "Warm chocolate cake with a molten center, served with vanilla ice cream",
      price: 90,
      category: "Desserts",
      image: "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 5,
      name: "Grilled Salmon",
      description: "Fresh Atlantic salmon with lemon butter sauce and seasonal vegetables",
      price: 320,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1485921325833-c519f76c4927?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 6,
      name: "Beef Tenderloin",
      description: "Premium beef tenderloin with red wine reduction and truffle mashed potatoes",
      price: 450,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1600891964092-4316c288032e?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 7,
      name: "Mushroom Risotto",
      description: "Creamy Arborio rice with wild mushrooms and parmesan cheese",
      price: 200,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1476124369491-e7addf5db371?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 8,
      name: "Bruschetta",
      description: "Toasted bread topped with fresh tomatoes, garlic, and basil",
      price: 80,
      category: "Appetizers",
      image: "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 9,
      name: "Caesar Salad",
      description: "Romaine lettuce, parmesan cheese, croutons, and Caesar dressing",
      price: 110,
      category: "Appetizers",
      image: "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 10,
      name: "Tiramisu",
      description: "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream",
      price: 95,
      category: "Desserts",
      image: "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 11,
      name: "Cheesecake",
      description: "New York style cheesecake with berry compote",
      price: 85,
      category: "Desserts",
      image: "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 12,
      name: "Minestrone Soup",
      description: "Traditional Italian vegetable soup with pasta and beans",
      price: 75,
      category: "Appetizers",
      image: "https://images.unsplash.com/photo-1547592166-23ac45744acd?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 13,
      name: "Chicken Alfredo",
      description: "Grilled chicken breast with creamy Alfredo sauce and fettuccine",
      price: 220,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?q=80&w=800&auto=format&fit=crop",
      available: true
    },
    {
      id: 14,
      name: "Vegetable Lasagna",
      description: "Layers of pasta, vegetables, and cheese in tomato sauce",
      price: 190,
      category: "Main Course",
      image: "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?q=80&w=800&auto=format&fit=crop",
      available: true
    }
  ]);

  const [orders, setOrders] = useState([
    {
      id: 1,
      customer: "John Doe",
      items: [
        { id: 1, quantity: 2 },
        { id: 3, quantity: 1 }
      ],
      total: 620,
      status: "Delivered",
      date: "2024-04-20",
      time: "19:30"
    },
    {
      id: 2,
      customer: "Jane Smith",
      items: [
        { id: 2, quantity: 1 },
        { id: 4, quantity: 2 }
      ],
      total: 360,
      status: "In Progress",
      date: "2024-04-21",
      time: "20:15"
    }
  ]);

  const [reservations, setReservations] = useState([
    {
      id: 1,
      name: "Sarah Wilson",
      email: "sarah@example.com",
      phone: "123-456-7890",
      date: "2024-04-20",
      time: "19:00",
      guests: 4,
      status: "Confirmed",
      specialRequests: "Window seat preferred"
    },
    {
      id: 2,
      name: "David Brown",
      email: "david@example.com",
      phone: "987-654-3210",
      date: "2024-04-21",
      time: "20:30",
      guests: 2,
      status: "Pending",
      specialRequests: "Allergic to nuts"
    }
  ]);

  const addMenuItem = (item) => {
    const newItem = {
      ...item,
      id: menuItems.length + 1,
      available: true
    };
    setMenuItems([...menuItems, newItem]);
  };

  const updateMenuItem = (id, updates) => {
    setMenuItems(menuItems.map(item => 
      item.id === id ? { ...item, ...updates } : item
    ));
  };

  const deleteMenuItem = (id) => {
    setMenuItems(menuItems.filter(item => item.id !== id));
  };

  const addOrder = (order) => {
    const newOrder = {
      ...order,
      id: orders.length + 1,
      date: new Date().toISOString().split('T')[0],
      time: new Date().toTimeString().split(' ')[0].substring(0, 5),
      status: "Pending"
    };
    setOrders([...orders, newOrder]);
  };

  const updateOrderStatus = (id, status) => {
    setOrders(orders.map(order => 
      order.id === id ? { ...order, status } : order
    ));
  };

  const addReservation = (reservation) => {
    const newReservation = {
      ...reservation,
      id: reservations.length + 1,
      status: "Pending"
    };
    setReservations([...reservations, newReservation]);
  };

  const updateReservationStatus = (id, status) => {
    setReservations(reservations.map(reservation => 
      reservation.id === id ? { ...reservation, status } : reservation
    ));
  };

  const value = {
    menuItems,
    orders,
    reservations,
    addMenuItem,
    updateMenuItem,
    deleteMenuItem,
    addOrder,
    updateOrderStatus,
    addReservation,
    updateReservationStatus
  };

  return (
    <RestaurantContext.Provider value={value}>
      {children}
    </RestaurantContext.Provider>
  );
}

export function useRestaurant() {
  const context = useContext(RestaurantContext);
  if (!context) {
    throw new Error('useRestaurant must be used within a RestaurantProvider');
  }
  return context;
} 