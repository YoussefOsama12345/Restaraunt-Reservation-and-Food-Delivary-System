import React, { useState } from 'react';
import styled from 'styled-components';
import { motion, AnimatePresence } from 'framer-motion';
import { FiChevronLeft, FiChevronRight } from 'react-icons/fi';

// Image URLs
const images = [
    'https://images.unsplash.com/photo-1555396273-367ea4eb4db5',
    'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38',
    'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f',
    'https://images.unsplash.com/photo-1600891964599-f61ba0e24092',
    'https://images.unsplash.com/photo-1600891964599-f61ba0e24092',
    'https://images.unsplash.com/photo-1600891964599-f61ba0e24092',
];

// Styled Components
const Section = styled.section`
    padding: 4rem 2rem;
    background-color: #fdf2ec;
    text-align: center;
`;

const Title = styled.h2`
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 2rem;
    color: #1e293b;
`;

const CarouselOuter = styled.div`
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const CarouselContainer = styled.div`
    position: relative;
    width: 100%;
    max-width: 800px;
    overflow: hidden;
    border-radius: 16px;
    height: 450px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);

    @media (max-width: 768px) {
        height: 300px;
    }
`;

const Slide = styled(motion.div)`
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        border-radius: 16px;
    }
`;

const NavButton = styled.button`
    background: #f97316;
    border: none;
    padding: 0.75rem;
    border-radius: 50%;
    cursor: pointer;
    margin: 0 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;

    svg {
        color: white;
        transition: color 0.3s ease;
    }

    &:hover:not(:disabled) {
        background-color: white;

        svg {
        color: #f97316;
        }
    }

    &:disabled {
        background-color: #fcd9b6;
        cursor: not-allowed;

        svg {
        color: white;
        opacity: 0.5;
        }
    }
`;

// Framer Variants
const variants = {
    enter: (direction) => ({
        x: direction > 0 ? 300 : -300,
        opacity: 0
    }),
    center: {
        x: 0,
        opacity: 1
    },
    exit: (direction) => ({
        x: direction > 0 ? -300 : 300,
        opacity: 0
    })
};

const Gallery = () => {
    const [[current, direction], setCurrent] = useState([0, 0]);

    const paginate = (dir) => {
        const nextIndex = current + dir;

        if (nextIndex < 0 || nextIndex >= images.length) return;

        setCurrent([nextIndex, dir]);
    };

    return (
        <Section id="gallery">
        <Title>Gallery</Title>
        <CarouselOuter>
            <NavButton onClick={() => paginate(-1)} disabled={current === 0}>
            <FiChevronLeft size={24} />
            </NavButton>

            <CarouselContainer>
            <AnimatePresence initial={false} custom={direction}>
                <Slide
                key={current}
                custom={direction}
                variants={variants}
                initial="enter"
                animate="center"
                exit="exit"
                transition={{
                    x: { type: 'spring', stiffness: 300, damping: 30 },
                    opacity: { duration: 0.3 }
                }}
                >
                <img
                    src={`${images[current]}?auto=format&fit=crop&w=800&h=600&q=80`}
                    alt={`Gallery image ${current + 1}`}
                    loading="lazy"
                />
                </Slide>
            </AnimatePresence>
            </CarouselContainer>

            <NavButton onClick={() => paginate(1)} disabled={current === images.length - 1}>
            <FiChevronRight size={24} />
            </NavButton>
        </CarouselOuter>
        </Section>
    );
    };

export default Gallery;
