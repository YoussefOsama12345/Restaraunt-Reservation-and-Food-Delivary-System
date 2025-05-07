import React, { useState } from 'react';
import { BarChart2, ShoppingCart, TrendingUp, Users, DollarSign, Menu, NotepadText, SquareMenu, User, Component } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { Link } from 'react-router-dom';
import styled from 'styled-components';


const SIDEBAR_ITEMS = [
    { name: "Overview", icon: BarChart2, color: "#6366f1", href: "/" },
    { name: "Menu", icon: SquareMenu, color: "#3B82F6", href: "/menu" },
    { name: "Users", icon: Users, color: "#fe4899", href: "/users" },
    { name: "Sales", icon: DollarSign, color: "#10b981", href: "/sales" },
    { name: "Orders", icon: ShoppingCart, color: "#FFFF00", href: "/orders" },
    { name: "Analytics", icon: TrendingUp, color: "#8b5cf6", href: "/analytics" },
    { name: "Inventory", icon: NotepadText, color: "#3B8C8C", href: "/inventory" },
    { name: "Category", icon: Component, color: "#4CAF50", href: "/category" },
    { name: "Staff", icon: User, color: "#FFA500", href: "/staff" },
];

const SidebarWrapper = styled(motion.div)`
    position: relative;
    z-index: 10;
    flex-shrink: 0;
    transition: all 0.3s ease-in-out;
    width: ${({ isOpen }) => (isOpen ? '256px' : '80px')};

    @media (max-width: 768px) {
        position: absolute;
        top: 0;
        left: 0;
        height: 100vh;
        background-color: ${({ theme }) => theme.background || 'rgba(31, 41, 55, 0.85)'};
    }
`;

const SidebarInner = styled.div`
    height: 100%;
    background-color: ${({ theme }) => theme.sidebarBg || 'rgba(31, 41, 55, 0.5)'};
    backdrop-filter: blur(10px);
    padding: 1rem;
    display: flex;
    flex-direction: column;
    border-right: 1px solid ${({ theme }) => theme.borderColor || '#374151'};
`;

const ToggleButton = styled(motion.button)`
    padding: 0.5rem;
    border-radius: 9999px;
    background: none;
    border: none;
    color: ${({ theme }) => theme.iconColor || 'white'};
    cursor: pointer;
    transition: background-color 0.2s;
    max-width: fit-content;

    &:hover {
        background-color: ${({ theme }) => theme.hoverBg || '#374151'};
    }

    &:focus-visible {
        outline: 2px solid ${({ theme }) => theme.accent || '#22c55e'};
        outline-offset: 2px;
    }
`;

const Nav = styled.nav`
    margin-top: 2rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
`;

const NavItem = styled(motion.div)`
    display: flex;
    align-items: center;
    padding: 0.85rem;
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background-color 0.2s;
    color: ${({ theme }) => theme.text || 'white'};

    &:hover {
        background-color: ${({ theme }) => theme.hoverBg || '#374151'};
    }
`;

const Label = styled(motion.span)`
    margin-left: 1rem;
    white-space: nowrap;
    overflow: hidden;
    color: ${({ theme }) => theme.text || 'white'};
`;

const Sidebar = () => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);

    return (
        <SidebarWrapper
        isOpen={isSidebarOpen}
        animate={{ width: isSidebarOpen ? 256 : 80 }}
        >
        <SidebarInner>
            <ToggleButton
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            aria-label="Toggle sidebar"
            >
            <Menu size={24} />
            </ToggleButton>

            <Nav role="navigation" aria-label="Main Navigation">
            {SIDEBAR_ITEMS.map((item) => (
                <Link key={item.href} to={item.href} style={{ textDecoration: 'none' }}>
                <NavItem>
                    <item.icon size={20} style={{ color: item.color, minWidth: '20px' }} />
                    <AnimatePresence>
                    {isSidebarOpen && (
                        <Label
                        initial={{ opacity: 0, width: 0 }}
                        animate={{ opacity: 1, width: 'auto' }}
                        exit={{ opacity: 0.2, width: 0 }}
                        transition={{ duration: 0.2}}
                        >
                        {item.name}
                        </Label>
                    )}
                    </AnimatePresence>
                </NavItem>
                </Link>
            ))}
            </Nav>
        </SidebarInner>
        </SidebarWrapper>
    );
};

export default Sidebar;