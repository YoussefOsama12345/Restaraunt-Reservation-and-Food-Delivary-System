import React, { useRef, useEffect } from 'react';
import styled from 'styled-components';
import Hero from '../components/Hero';
import Categories from '../components/Categories';
import FeaturedDishes from '../components/FeaturedDishes';
import Testimonials from '../components/Testimonials';
import About from '../components/About';
import Contact from '../components/Contact';
import Reservation from '../components/Reservation';

const Section = styled.section`
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.8s ease, transform 0.8s ease;
  margin: 2rem 0;
  will-change: opacity, transform;

  &.visible {
    opacity: 1;
    transform: translateY(0);
  }

  &.hidden {
    opacity: 0;
    transform: translateY(50px);
  }
`;

const Home = () => {
  const sectionRefs = useRef([]);

  useEffect(() => {
    const observerOptions = {
      root: null,
      rootMargin: '-10% 0px',  // Trigger slightly before element enters/leaves viewport
      threshold: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  // Multiple thresholds for smoother transitions
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        // Get the element's position relative to the viewport
        const rect = entry.boundingClientRect;
        const windowHeight = window.innerHeight;
        const isScrollingDown = rect.top < windowHeight / 2;

        if (entry.isIntersecting) {
          // Element is entering the viewport
          entry.target.classList.remove('hidden');
          entry.target.classList.add('visible');
        } else {
          // Element is leaving the viewport
          if (isScrollingDown) {
            // Scrolling down, element moves up and out
            entry.target.classList.remove('visible');
            entry.target.classList.add('hidden');
          } else {
            // Scrolling up, element moves down and out
            entry.target.classList.remove('visible');
            entry.target.classList.add('hidden');
          }
        }
      });
    }, observerOptions);

    sectionRefs.current.forEach(ref => {
      if (ref) {
        observer.observe(ref);
        // Initially hide all sections
        ref.classList.add('hidden');
      }
    });

    return () => {
      sectionRefs.current.forEach(ref => {
        if (ref) observer.unobserve(ref);
      });
    };
  }, []);

  return (
    <>
      <Section ref={el => sectionRefs.current[0] = el}>
        <Hero />
      </Section>
      <Section ref={el => sectionRefs.current[1] = el}>
        <Categories />
      </Section>
      <Section ref={el => sectionRefs.current[2] = el} id="featured-dishes">
        <FeaturedDishes />
      </Section>
      <Section ref={el => sectionRefs.current[3] = el}>
        <Reservation />
      </Section>
      <Section ref={el => sectionRefs.current[4] = el}>
        <Testimonials />
      </Section>
      <Section ref={el => sectionRefs.current[5] = el} id="about">
        <About />
      </Section>
      <Section ref={el => sectionRefs.current[6] = el} id="contact">
        <Contact />
      </Section>
    </>
  );
};

export default Home; 