import styled from 'styled-components'
import { motion } from 'framer-motion'
import { FaLinkedin, FaTwitter, FaInstagram } from 'react-icons/fa'

const TeamSection = styled(motion.section)`
  margin-bottom: 4rem;
  padding: 2rem;
  background-color: #fdf2ec;
  border-radius: 1rem;
`

const TeamTitle = styled.h2`
  font-size: 2.25rem;
  font-weight: 700;
  color: #111827;
  text-align: center;
  margin-bottom: 3rem;
  position: relative;

  &::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #f97316, #ea580c);
    border-radius: 2px;
  }
`

const Grid = styled.div`
  display: grid;
  gap: 2rem;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  max-width: 1200px;
  margin: 0 auto;
`

const TeamMember = styled(motion.div)`
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.07);
  transition: all 0.3s ease;
  min-height: 500px;
  border: 1px solid transparent;

  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    border-color: #f97316;
  }
`

const MemberImage = styled.div`
  width: 180px;
  height: 180px;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  overflow: hidden;
  position: relative;
  border: 4px solid #fff7ed;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);

  &::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(45deg, rgba(249, 115, 22, 0.1), rgba(249, 115, 22, 0.2));
    z-index: 1;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: relative;
    z-index: 2;
  }
`

const MemberName = styled.h3`
  font-size: 1.5rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 0.5rem;
`

const MemberRole = styled.p`
  font-size: 1rem;
  color: #f97316;
  margin-bottom: 1rem;
  font-weight: 500;
`

const MemberBio = styled.p`
  font-size: 0.875rem;
  color: #6b7280;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex-grow: 1;
`

const SocialLinks = styled.div`
  display: flex;
  gap: 1rem;
  justify-content: center;
`

const SocialLink = styled.a`
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #fff7ed;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #f97316;
  transition: all 0.3s ease;

  &:hover {
    background: #f97316;
    color: white;
    transform: translateY(-2px);
  }
`

const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0 },
}

const members = [
  {
    name: 'Sarah Johnson',
    role: 'Founder & CEO',
    image: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=300&q=80',
    bio: 'With over 15 years of experience in the food industry, Sarah leads Food Hub with passion and vision.',
  },
  {
    name: 'Michael Chen',
    role: 'Head of Operations',
    image: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=300&q=80',
    bio: 'Michael ensures smooth operations and exceptional service quality across all our delivery channels.',
  },
  {
    name: 'Emily Rodriguez',
    role: 'Customer Experience Manager',
    image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80',
    bio: 'Emily is dedicated to creating memorable experiences for our customers through excellent service.',
  },
]

const Team = () => {
  return (
    <TeamSection
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
      variants={fadeInUp}
      transition={{ duration: 0.6 }}
    >
      <TeamTitle>Meet Our Team</TeamTitle>
      <Grid>
        {members.map((member, index) => (
          <TeamMember
            key={index}
            variants={fadeInUp}
            transition={{ duration: 0.4, delay: 0.2 * index }}
          >
            <MemberImage>
              <img src={member.image} alt={member.name} />
            </MemberImage>
            <MemberName>{member.name}</MemberName>
            <MemberRole>{member.role}</MemberRole>
            <MemberBio>{member.bio}</MemberBio>
            <SocialLinks>
              <SocialLink href="#"><FaLinkedin size={16} /></SocialLink>
              <SocialLink href="#"><FaTwitter size={16} /></SocialLink>
              <SocialLink href="#"><FaInstagram size={16} /></SocialLink>
            </SocialLinks>
          </TeamMember>
        ))}
      </Grid>
    </TeamSection>
  )
}

export default Team