import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { X } from 'lucide-react';

const ModalOverlay = styled.div`
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

const ModalContent = styled.div`
  background-color: #1f2937;
  padding: 2rem;
  border-radius: 1rem;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
`;

const CloseButton = styled.button`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  transition: all 0.2s;

  &:hover {
    background-color: #374151;
    color: #f9fafb;
  }
`;

const Form = styled.form`
  display: grid;
  gap: 1rem;
  margin-top: 1rem;
`;

const FormGroup = styled.div`
  display: grid;
  gap: 0.5rem;
`;

const Label = styled.label`
  color: #f9fafb;
  font-size: 0.875rem;
  font-weight: 500;
`;

const Input = styled.input`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;

  &:focus {
    outline: none;
    border-color: #818cf8;
  }
`;

const Select = styled.select`
  padding: 0.75rem;
  background-color: #374151;
  border: 1px solid #4b5563;
  border-radius: 0.5rem;
  color: #f9fafb;
  font-size: 0.875rem;

  &:focus {
    outline: none;
    border-color: #818cf8;
  }
`;

const SubmitButton = styled.button`
  background-color: #818cf8;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: #6366f1;
  }

  &:disabled {
    background-color: #4b5563;
    cursor: not-allowed;
  }
`;

const ModifyStaffModal = ({ isOpen, onClose, onModify, staffData }) => {
  const [formData, setFormData] = useState({
    name: '',
    staffId: '',
    role: '',
    age: '',
    phone: '',
    address: '',
    salary: '',
    shiftType: 'Morning',
    shiftFrom: '08:00am',
    shiftTo: '4:00pm',
  });

  useEffect(() => {
    if (staffData) {
      setFormData({
        name: staffData.name || '',
        staffId: staffData.staffId || '',
        role: staffData.role || '',
        age: staffData.age || '',
        phone: staffData.phone || '',
        address: staffData.address || '',
        salary: staffData.salary || '',
        shiftType: staffData.shift?.type || 'Morning',
        shiftFrom: staffData.shift?.from || '08:00am',
        shiftTo: staffData.shift?.to || '4:00pm',
      });
    }
  }, [staffData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const modifiedStaff = {
      ...formData,
      age: parseInt(formData.age),
      salary: parseInt(formData.salary),
      shift: {
        type: formData.shiftType,
        from: formData.shiftFrom,
        to: formData.shiftTo
      }
    };
    onModify(modifiedStaff);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <ModalOverlay onClick={onClose}>
      <ModalContent onClick={e => e.stopPropagation()}>
        <CloseButton onClick={onClose}>
          <X size={20} />
        </CloseButton>
        <h2 style={{ color: '#f9fafb', marginBottom: '1.5rem' }}>Modify Staff Member</h2>
        <Form onSubmit={handleSubmit}>
          <FormGroup>
            <Label>Name</Label>
            <Input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label>Staff ID</Label>
            <Input
              type="text"
              name="staffId"
              value={formData.staffId}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label>Role</Label>
            <Select
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
            >
              <option value="">Select Role</option>
              <option value="Chef">Chef</option>
              <option value="Manager">Manager</option>
              <option value="Waiter">Waiter</option>
              <option value="Chef assistant">Chef Assistant</option>
              <option value="Delivery">Delivery</option>
              <option value="Steward">Steward</option>
              <option value="Host">Host</option>
            </Select>
          </FormGroup>
          <FormGroup>
            <Label>Age</Label>
            <Input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
              min="18"
            />
          </FormGroup>
          <FormGroup>
            <Label>Phone</Label>
            <Input
              type="tel"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label>Address</Label>
            <Input
              type="text"
              name="address"
              value={formData.address}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label>Salary</Label>
            <Input
              type="number"
              name="salary"
              value={formData.salary}
              onChange={handleChange}
              required
              min="0"
            />
          </FormGroup>
          <FormGroup>
            <Label>Shift Type</Label>
            <Select
              name="shiftType"
              value={formData.shiftType}
              onChange={handleChange}
              required
            >
              <option value="Morning">Morning</option>
              <option value="Evening">Evening</option>
              <option value="Night">Night</option>
            </Select>
          </FormGroup>
          <FormGroup>
            <Label>Shift From</Label>
            <Input
              type="text"
              name="shiftFrom"
              value={formData.shiftFrom}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label>Shift To</Label>
            <Input
              type="text"
              name="shiftTo"
              value={formData.shiftTo}
              onChange={handleChange}
              required
            />
          </FormGroup>
          <SubmitButton type="submit">Update Staff Member</SubmitButton>
        </Form>
      </ModalContent>
    </ModalOverlay>
  );
};

export default ModifyStaffModal; 