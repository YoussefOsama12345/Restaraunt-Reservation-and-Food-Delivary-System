import styled from 'styled-components';
import { Plus } from 'lucide-react';
import { useState } from 'react';
import Header from '../components/common/Header';
import StaffTable from '../components/staff/StaffTable';
import AddStaffModal from '../components/staff/AddStaffModal';
import Snackbar from '../components/common/Snackbar';

const PageContainer = styled.div`
	flex: 1;
	overflow: auto;
	position: relative;
	z-index: 10;
	background-color: #111827; /* Dark background to match topbar */
`;

// Main content area with responsive padding
const ContentWrapper = styled.main`
	max-width: 1280px;
	margin: 0 auto;
	padding: 1.5rem 1rem;

	@media (min-width: 1024px) {
		padding: 1.5rem 2rem;
	}
`;

const AddButton = styled.button`
	display: flex;  /* button display */
	align-items: center;
	justify-content: center;
	width: 40px;
	height: 40px;
	background-color: #818cf8;
	color: white;
	border: none;
	border-radius: 10px;
	cursor: pointer;
	font-size: 0.875rem;
	font-weight: 500;
	margin-top: 1rem;
	margin-left: auto;
	transition: all 0.2s ease;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

	&:hover {
		background-color: #6366f1;
		transform: translateY(-1px);
	}

	&:active {
		transform: translateY(0);
	}
`;

const StaffPage = () => {
	const [isModalOpen, setIsModalOpen] = useState(false);
	const [staffTableRef, setStaffTableRef] = useState(null);
	const [snackbar, setSnackbar] = useState({
		isVisible: false,
		message: '',
		type: 'success'
	});

	const handleAddClick = () => {
		setIsModalOpen(true);
	};

	const handleCloseModal = () => {
		setIsModalOpen(false);
	};

	const handleAddStaff = (newStaff) => {
		if (staffTableRef) {
			staffTableRef.handleAddStaff(newStaff);
			setSnackbar({
				isVisible: true,
				message: `${newStaff.name} has been added successfully`,
				type: 'success'
			});
		}
		setIsModalOpen(false);
	};

	const handleCloseSnackbar = () => {
		setSnackbar(prev => ({ ...prev, isVisible: false }));
	};

	return (
		<PageContainer>
			<Header title="Staff" />
			<ContentWrapper>
				<StaffTable ref={setStaffTableRef} />
				<AddButton onClick={handleAddClick}>
					<Plus size={20} />
				</AddButton>
				<AddStaffModal
					isOpen={isModalOpen}
					onClose={handleCloseModal}
					onAdd={handleAddStaff}
				/>
				<Snackbar
					isVisible={snackbar.isVisible}
					message={snackbar.message}
					type={snackbar.type}
					onClose={handleCloseSnackbar}
				/>
			</ContentWrapper>
		</PageContainer>
	);
};

export default StaffPage;