import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Search, Edit, Trash2 } from "lucide-react";
import styled from "styled-components";

// Dummy order data
const orderData = [
  { id: "ORD001", customer: "John Doe", total: 235.4, status: "Delivered", date: "2023-07-01" },
  { id: "ORD002", customer: "Jane Smith", total: 412.0, status: "Processing", date: "2023-07-02" },
  { id: "ORD003", customer: "Bob Johnson", total: 162.5, status: "Shipped", date: "2023-07-03" },
  { id: "ORD004", customer: "Alice Brown", total: 750.2, status: "Pending", date: "2023-07-04" },
  { id: "ORD005", customer: "Charlie Wilson", total: 95.8, status: "Delivered", date: "2023-07-05" },
  { id: "ORD006", customer: "Eva Martinez", total: 310.75, status: "Processing", date: "2023-07-06" },
  { id: "ORD007", customer: "David Lee", total: 528.9, status: "Shipped", date: "2023-07-07" },
  { id: "ORD008", customer: "Grace Taylor", total: 189.6, status: "Delivered", date: "2023-07-08" },
];

// Styled components
const Container = styled(motion.div)`
  background: rgba(31, 41, 55, 0.5);
  backdrop-filter: blur(6px);
  border: 1px solid #374151;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
`;

const TitleRow = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
`;

const Heading = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #f9fafb;
`;

const SearchInputWrapper = styled.div`
  position: relative;
`;

const SearchInput = styled.input`
  background: #374151;
  color: #fff;
  border-radius: 8px;
  padding: 8px 12px 8px 36px;
  border: none;
  outline: none;
  width: 200px;
  font-size: 14px;
`;

const SearchIcon = styled(Search)`
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
  color: #9ca3af;
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const TableHead = styled.thead`
  background-color: #1f2937;
`;

const TableHeader = styled.th`
  text-align: left;
  padding: 12px 16px;
  font-size: 12px;
  font-weight: 500;
  color: #9ca3af;
  text-transform: uppercase;
`;

const TableBody = styled.tbody``;

const TableRow = styled(motion.tr)`
  border-bottom: 1px solid #374151;
`;

const TableCell = styled.td`
  padding: 12px 16px;
  font-size: 14px;
  color: #d1d5db;
`;

const ActionButton = styled.button`
  background: transparent;
  border: none;
  cursor: pointer;
  margin-right: 0.25rem;
  color: ${({ color }) => color || '#60a5fa'};
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.375rem;
  transition: all 0.2s;
  padding: 0.25rem;

  &:hover {
    opacity: 0.8;
  }

  &:last-child {
    margin-right: 0;
  }
`;

// Badge for status with dynamic color
const StatusBadge = styled.span`
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  background-color: ${(props) =>
    props.status === "Delivered"
      ? "#dcfce7"
      : props.status === "Processing"
      ? "#fef3c7"
      : props.status === "Shipped"
      ? "#dbeafe"
      : "#fee2e2"};
  color: ${(props) =>
    props.status === "Delivered"
      ? "#166534"
      : props.status === "Processing"
      ? "#92400e"
      : props.status === "Shipped"
      ? "#1e40af"
      : "#991b1b"};
`;

const OrdersTable = ({ onEditClick, onDeleteClick }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredOrders, setFilteredOrders] = useState(orderData);

  // Update filtered orders when orderData changes
  useEffect(() => {
    handleSearch({ target: { value: searchTerm } });
  }, [orderData]);

  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = orderData.filter(
      (order) =>
        order.id.toLowerCase().includes(term) ||
        order.customer.toLowerCase().includes(term) ||
        order.status.toLowerCase().includes(term) || 
        order.date.toLowerCase().includes(term)
    );
    setFilteredOrders(filtered);
  };

  const handleDelete = (order) => {
    // Remove the order from orderData
    const index = orderData.findIndex(o => o.id === order.id);
    if (index !== -1) {
      orderData.splice(index, 1);
      // Update filtered orders
      handleSearch({ target: { value: searchTerm } });
    }
    onDeleteClick(order);
  };

  return (
    <Container
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.4 }}
    >
      <TitleRow>
        <Heading>Order List</Heading>
        <SearchInputWrapper>
          <SearchInput
            aria-label='Search Orders'
            placeholder='Search orders...'
            value={searchTerm}
            onChange={handleSearch}
          />
          <SearchIcon size={18} />
        </SearchInputWrapper>
      </TitleRow>

      <div style={{ overflowX: "auto" }}>
        <Table>
          <TableHead>
            <tr>
              <TableHeader>Order ID</TableHeader>
              <TableHeader>Customer</TableHeader>
              <TableHeader>Total</TableHeader>
              <TableHeader>Status</TableHeader>
              <TableHeader>Date</TableHeader>
              <TableHeader>Actions</TableHeader>
            </tr>
          </TableHead>

          <TableBody>
            {filteredOrders.map((order) => (
              <TableRow
                key={order.id}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.3 }}
              >
                <TableCell>{order.id}</TableCell>
                <TableCell>{order.customer}</TableCell>
                <TableCell>${order.total.toFixed(2)}</TableCell>
                <TableCell>
                  <StatusBadge status={order.status}>{order.status}</StatusBadge>
                </TableCell>
                <TableCell>{order.date}</TableCell>
                <TableCell>
                  <ActionButton 
                    color="#818cf8" 
                    onClick={() => onEditClick(order)}
                    title="Edit Order"
                  >
                    <Edit size={16} />
                  </ActionButton>
                  <ActionButton 
                    color="#f87171" 
                    onClick={() => handleDelete(order)}
                    title="Delete Order"
                  >
                    <Trash2 size={16} />
                  </ActionButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </Container>
  );
};

export default OrdersTable;
