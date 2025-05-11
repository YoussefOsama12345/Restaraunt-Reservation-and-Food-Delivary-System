import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import styled from 'styled-components';

// Styled components
const Container = styled(motion.div)`
  background: rgba(31, 41, 55, 0.5);
  backdrop-filter: blur(12px);
  border: 1px solid #374151;
  border-radius: 1rem;
  padding: 1.5rem;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
`;

const Title = styled.h2`
  font-size: 1.125rem;
  font-weight: 600;
  color: #f3f4f6;
`;

const SearchInput = styled.input`
  background: #374151;
  color: #fff;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  border: none;
  outline: none;
  width: 240px;
  &::placeholder {
    color: #9ca3af;
  }
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const TableHead = styled.thead`
  background-color: #374151;
  color: #f3f4f6;
  text-transform: uppercase;
  font-size: 0.75rem;
`;

const Th = styled.th`
  text-align: left;
  padding: 0.75rem 1.5rem;
`;

const Td = styled.td`
  padding: 0.75rem 1.5rem;
  color: #d1d5db;
  vertical-align: middle;
`;

const Badge = styled.span`
  display: inline-block;
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 9999px;
  background-color: ${({ bg }) => bg};
  color: ${({ color }) => color};
`;

const Avatar = styled.div`
  height: 2.5rem;
  width: 2.5rem;
  border-radius: 9999px;
  background: linear-gradient(to right, #a78bfa, #3b82f6);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 600;
`;

const ActionButton = styled.button`
  background: transparent;
  border: none;
  cursor: pointer;
  margin-right: 0.5rem;
  color: ${({ color }) => color};

  &:hover {
    opacity: 0.8;
  }
`;

const UsersTable = ({ users, onEditClick, onDeleteClick }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredUsers, setFilteredUsers] = useState(users);

  // Update filtered users when users prop changes
  useEffect(() => {
    setFilteredUsers(users);
  }, [users]);

  // Handles user input to filter users
  const handleSearch = (e) => {
    const term = e.target.value;
    setSearchTerm(term);
    const filtered = users.filter((user) =>
      user.name.toLowerCase().includes(term.toLowerCase()) ||
      user.email.toLowerCase().includes(term.toLowerCase())
    );
    setFilteredUsers(filtered);
  };

  const handleDelete = (user) => {
    onDeleteClick(user);
  };

  const handleEdit = (user) => {
    onEditClick(user);
  };

  return (
    <Container
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.2 }}
    >
      <Header>
        <Title>Users</Title>
        <SearchInput
          type="text"
          placeholder="Search users..."
          value={searchTerm}
          onChange={handleSearch}
        />
      </Header>

      <div style={{ overflowX: "auto" }}>
        <Table>
          <TableHead>
            <tr>
              <Th>Name</Th>
              <Th>User ID</Th>
              <Th>Email</Th>
              <Th>Role</Th>
              <Th>Status</Th>
              <Th>Actions</Th>
            </tr>
          </TableHead>
          <tbody>
            {filteredUsers.map((user) => (
              <motion.tr
                key={user.id}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.3 }}
              >
                <Td>
                  <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
                    <Avatar>{user.name.charAt(0)}</Avatar>
                    <span>{user.name}</span>
                  </div>
                </Td>
                <Td>{user.userId}</Td>
                <Td>{user.email}</Td>
                <Td>
                  <Badge bg="#1e40af" color="#dbeafe">{user.role}</Badge>
                </Td>
                <Td>
                  <Badge
                    bg={user.status === "Active" ? "#dcfce7" : "#fee2e2"}
                    color={user.status === "Active" ? "#166534" : "#991b1b"}
                  >
                    {user.status}
                  </Badge>
                </Td>
                <Td>
                  <ActionButton color="#818cf8" onClick={() => handleEdit(user)}>Edit</ActionButton>
                  <ActionButton color="#f87171" onClick={() => handleDelete(user)}>Delete</ActionButton>
                </Td>
              </motion.tr>
            ))}
          </tbody>
        </Table>
      </div>
    </Container>
  );
};

export default UsersTable;