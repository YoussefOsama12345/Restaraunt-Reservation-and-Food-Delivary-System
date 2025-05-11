import { CheckCircle, Clock, DollarSign, ShoppingBag } from "lucide-react";
import { motion } from "framer-motion";
import styled from "styled-components";
import { useState } from "react";

import Header from "../components/common/Header";
import StatsCard from "../components/common/StatsCard";
import DailyOrders from "../components/orders/DailyOrders";
import OrderDistribution from "../components/orders/OrderDistribution";
import OrdersTable from "../components/orders/OrdersTable";

// 📊 Sample order statistics data
const orderStats = {
	totalOrders: "1,234",
	pendingOrders: "56",
	completedOrders: "1,178",
	totalRevenue: "$98,765"
};

/* ------------------------- Styled Components ------------------------- */

// Main wrapper for scrollable content
const PageWrapper = styled.div`
	flex: 1;
	position: relative;
	z-index: 10;
	overflow: auto;
	background-color: #111827;
`;

// Main content container
const MainContent = styled.main`
	max-width: 80rem; // 1280px
	margin: 0 auto;
	padding: 1.5rem 1rem;

	@media (min-width: 1024px) {
		padding: 1.5rem 2rem;
	}
`;

// Grid for the stats cards
const StatsGrid = styled(motion.div)`
	display: grid;
	grid-template-columns: 1fr;
	gap: 1.25rem;
	margin-bottom: 2rem;

	@media (min-width: 640px) {
		grid-template-columns: repeat(2, 1fr);
	}
	@media (min-width: 1024px) {
		grid-template-columns: repeat(4, 1fr);
	}
`;

// Grid for the two main order charts
const ChartsGrid = styled.div`
	display: grid;
	grid-template-columns: 1fr;
	gap: 2rem;
	margin-bottom: 2rem;

	@media (min-width: 1024px) {
		grid-template-columns: repeat(2, 1fr);
	}
`;

// Styled Components
const ModalOverlay = styled(motion.div)`
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1000;
`;

const ModalContent = styled(motion.div)`
	background-color: #1f2937;
	padding: 2rem;
	border-radius: 1rem;
	width: 90%;
	max-width: 500px;
	border: 1px solid #374151;
`;

const ModalHeader = styled.div`
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 1.5rem;
`;

const ModalTitle = styled.h2`
	color: #f9fafb;
	font-size: 1.25rem;
	font-weight: 600;
`;

const CloseButton = styled.button`
	background: transparent;
	border: none;
	color: #9ca3af;
	cursor: pointer;
	font-size: 1.5rem;
	padding: 0.5rem;
	&:hover {
		color: #f9fafb;
	}
`;

const Form = styled.form`
	display: flex;
	flex-direction: column;
	gap: 1rem;
`;

const FormGroup = styled.div`
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
`;

const Label = styled.label`
	color: #f9fafb;
	font-size: 0.875rem;
`;

const Input = styled.input`
	padding: 0.5rem;
	border-radius: 0.375rem;
	border: 1px solid #374151;
	background-color: #374151;
	color: #f9fafb;
	&:focus {
		outline: none;
		border-color: #818cf8;
	}
`;

const Select = styled.select`
	padding: 0.5rem;
	border-radius: 0.375rem;
	border: 1px solid #374151;
	background-color: #374151;
	color: #f9fafb;
	&:focus {
		outline: none;
		border-color: #818cf8;
	}
`;

const ErrorMessage = styled.span`
	color: #ef4444;
	font-size: 0.75rem;
`;

const SubmitButton = styled.button`
	background-color: #818cf8;
	color: white;
	padding: 0.75rem;
	border-radius: 0.375rem;
	border: none;
	cursor: pointer;
	font-weight: 500;
	margin-top: 1rem;
	&:hover {
		background-color: #6366f1;
	}
`;

const Snackbar = styled(motion.div)`
	position: fixed;
	bottom: 2rem;
	right: 2rem;
	background-color: #10b981;
	color: white;
	padding: 1rem 2rem;
	border-radius: 0.5rem;
	box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
`;

const DeleteModalOverlay = styled(motion.div)`
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1000;
`;

const DeleteModalContent = styled(motion.div)`
	background-color: #1f2937;
	padding: 2rem;
	border-radius: 1rem;
	width: 90%;
	max-width: 400px;
	border: 1px solid #374151;
`;

const DeleteModalTitle = styled.h2`
	color: #f9fafb;
	font-size: 1.25rem;
	font-weight: 600;
	margin-bottom: 1rem;
`;

const DeleteModalText = styled.p`
	color: #d1d5db;
	margin-bottom: 1.5rem;
`;

const DeleteModalButtons = styled.div`
	display: flex;
	justify-content: flex-end;
	gap: 1rem;
`;

const DeleteButton = styled.button`
	background-color: #ef4444;
	color: white;
	padding: 0.5rem 1rem;
	border-radius: 0.375rem;
	border: none;
	cursor: pointer;
	font-weight: 500;
	&:hover {
		background-color: #dc2626;
	}
`;

const CancelButton = styled.button`
	background-color: #374151;
	color: #f9fafb;
	padding: 0.5rem 1rem;
	border-radius: 0.375rem;
	border: none;
	cursor: pointer;
	font-weight: 500;
	&:hover {
		background-color: #4b5563;
	}
`;

/* ------------------------- Component ------------------------- */

const OrdersPage = () => {
	const [isEditModalOpen, setIsEditModalOpen] = useState(false);
	const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
	const [isSnackbarOpen, setIsSnackbarOpen] = useState(false);
	const [snackbarMessage, setSnackbarMessage] = useState('');
	const [orderToDelete, setOrderToDelete] = useState(null);
	const [formData, setFormData] = useState({
		customer: '',
		status: '',
		date: ''
	});
	const [errors, setErrors] = useState({});

	const validateForm = () => {
		const newErrors = {};
		if (!formData.customer) newErrors.customer = 'Customer is required';
		if (!formData.status) newErrors.status = 'Status is required';
		if (!formData.date) newErrors.date = 'Date is required';
		
		setErrors(newErrors);
		return Object.keys(newErrors).length === 0;
	};

	const showSnackbar = (message) => {
		setSnackbarMessage(message);
		setIsSnackbarOpen(true);
		setTimeout(() => {
			setIsSnackbarOpen(false);
		}, 3000);
	};

	const handleEditClick = (item) => {
		setFormData({
			customer: item.customer,
			status: item.status,
			date: item.date
		});
		setIsEditModalOpen(true);
	};

	const handleEditSubmit = (e) => {
		e.preventDefault();
		if (validateForm()) {
			console.log('Updating order:', formData);
			setIsEditModalOpen(false);
			showSnackbar('Order has been modified successfully');
			setFormData({
				customer: '',
				status: '',
				date: ''
			});
			setErrors({});
		}
	};

	const handleDeleteClick = (order) => {
		setOrderToDelete(order);
		setIsDeleteModalOpen(true);
	};

	const handleDeleteConfirm = () => {
		if (orderToDelete) {
			// Here you would typically make an API call to delete the order
			console.log('Deleting order:', orderToDelete);
			setIsDeleteModalOpen(false);
			showSnackbar(`Order "${orderToDelete.id}" has been deleted successfully`);
			setOrderToDelete(null);
		}
	};

	const handleCloseDeleteModal = () => {
		setIsDeleteModalOpen(false);
		setOrderToDelete(null);
	};

	return (
		<PageWrapper>
			<Header title="Orders" />
			<MainContent>
				<StatsGrid
					initial={{ opacity: 0, y: 20 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 1 }}
				>
					<StatsCard name="Total Orders" icon={ShoppingBag} value={orderStats.totalOrders} color="#6366F1" />
					<StatsCard name="Pending Orders" icon={Clock} value={orderStats.pendingOrders} color="#F59E0B" />
					<StatsCard name="Completed Orders" icon={CheckCircle} value={orderStats.completedOrders} color="#10B981" />
					<StatsCard name="Total Revenue" icon={DollarSign} value={orderStats.totalRevenue} color="#EF4444" />
				</StatsGrid>

				<ChartsGrid>
					<DailyOrders />
					<OrderDistribution />
				</ChartsGrid>

				<OrdersTable 
					onEditClick={handleEditClick}
					onDeleteClick={handleDeleteClick}
				/>

				{isEditModalOpen && (
					<ModalOverlay
						initial={{ opacity: 0 }}
						animate={{ opacity: 1 }}
						exit={{ opacity: 0 }}
					>
						<ModalContent
							initial={{ scale: 0.9, opacity: 0 }}
							animate={{ scale: 1, opacity: 1 }}
							exit={{ scale: 0.9, opacity: 0 }}
						>
							<ModalHeader>
								<ModalTitle>Edit Order</ModalTitle>
								<CloseButton onClick={() => setIsEditModalOpen(false)}>×</CloseButton>
							</ModalHeader>
							<Form onSubmit={handleEditSubmit}>
								<FormGroup>
									<Label>Customer Name</Label>
									<Input
										type="text"
										value={formData.customer}
										onChange={(e) => setFormData({ ...formData, customer: e.target.value })}
										placeholder="Enter customer name"
									/>
									{errors.customer && <ErrorMessage>{errors.customer}</ErrorMessage>}
								</FormGroup>
								<FormGroup>
									<Label>Status</Label>
									<Select
										value={formData.status}
										onChange={(e) => setFormData({ ...formData, status: e.target.value })}
									>
										<option value="">Select status</option>
										<option value="Pending">Pending</option>
										<option value="Processing">Processing</option>
										<option value="Shipped">Shipped</option>
										<option value="Delivered">Delivered</option>
									</Select>
									{errors.status && <ErrorMessage>{errors.status}</ErrorMessage>}
								</FormGroup>
								<FormGroup>
									<Label>Date</Label>
									<Input
										type="date"
										value={formData.date}
										onChange={(e) => setFormData({ ...formData, date: e.target.value })}
									/>
									{errors.date && <ErrorMessage>{errors.date}</ErrorMessage>}
								</FormGroup>
								<SubmitButton type="submit">Save Changes</SubmitButton>
							</Form>
						</ModalContent>
					</ModalOverlay>
				)}

				{isDeleteModalOpen && (
					<DeleteModalOverlay
						initial={{ opacity: 0 }}
						animate={{ opacity: 1 }}
						exit={{ opacity: 0 }}
					>
						<DeleteModalContent
							initial={{ scale: 0.9, opacity: 0 }}
							animate={{ scale: 1, opacity: 1 }}
							exit={{ scale: 0.9, opacity: 0 }}
						>
							<DeleteModalTitle>Delete Order</DeleteModalTitle>
							<DeleteModalText>
								Are you sure you want to delete order "{orderToDelete?.id}"? This action cannot be undone.
							</DeleteModalText>
							<DeleteModalButtons>
								<CancelButton onClick={handleCloseDeleteModal}>
									Cancel
								</CancelButton>
								<DeleteButton onClick={handleDeleteConfirm}>
									Delete
								</DeleteButton>
							</DeleteModalButtons>
						</DeleteModalContent>
					</DeleteModalOverlay>
				)}

				{isSnackbarOpen && (
					<Snackbar
						initial={{ opacity: 0, y: 50 }}
						animate={{ opacity: 1, y: 0 }}
						exit={{ opacity: 0, y: 50 }}
					>
						{snackbarMessage}
					</Snackbar>
				)}
			</MainContent>
		</PageWrapper>
	);
};

export default OrdersPage;
