import React from 'react'
import styled from 'styled-components'
import { motion } from 'framer-motion'
import PropTypes from 'prop-types'

// 🌟 Styled motion card container
const Card = styled(motion.div)`
    background-color: rgba(31, 41, 55, 0.5); /* gray-800 + opacity */
    backdrop-filter: blur(10px);
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    border-radius: 1rem;
    border: 1px solid #374151;
    outline: none;

    &:focus {
        box-shadow: 0 0 0 2px #22c55e;
    }
`

const CardInner = styled.div`
    padding: 1.25rem;

    @media (min-width: 640px) {
        padding: 1.5rem;
    }
`

const Label = styled.span`
    display: flex;
    align-items: center;
    font-size: 0.875rem;
    font-weight: 500;
    color: ${({ theme }) => theme.colors?.gray400 || '#9ca3af'};
`

const Value = styled.p`
    margin-top: 0.25rem;
    font-size: clamp(1.75rem, 2vw, 2rem);
    font-weight: 600;
    color: ${({ theme }) => theme.colors?.gray100 || '#f3f4f6'};
`

const IconWrapper = styled.span`
    display: inline-flex;
    align-items: center;
    margin-right: 0.5rem;
`

const StatsCard = ({ name, icon: Icon, value, color }) => {
    return (
        <Card
        tabIndex="0"
        whileHover={{ y: -5, boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)' }}
        role="region"
        aria-label={`Statistic card for ${name}`}
        >
        <CardInner>
            <Label>
            <IconWrapper>
                {Icon && <Icon size={20} style={{ color }} aria-hidden="true" />}
            </IconWrapper>
            {name}
            </Label>
            <Value>{value}</Value>
        </CardInner>
        </Card>
    )
}

// PropTypes validation
StatsCard.propTypes = {
    name: PropTypes.string.isRequired,
    icon: PropTypes.elementType,
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    color: PropTypes.string
}

export default StatsCard
