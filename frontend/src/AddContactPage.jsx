import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Typography, IconButton, Paper } from '@mui/material';
import { ArrowBack as ArrowBackIcon } from '@mui/icons-material';
import ContactForm from './ContactForm.jsx';

export default function AddContactPage() {
  const navigate = useNavigate();

  const handleSuccess = () => {
    // Navigate back to the main page after successful addition
    navigate('/');
  };

  const handleBackClick = () => {
    navigate('/');
  };

  return (
    <Box sx={{ minHeight: '100vh', pb: 4 }}>
      <Paper elevation={0} sx={{ mb: 3, p: 2, display: 'flex', alignItems: 'center' }}>
        <IconButton onClick={handleBackClick} sx={{ mr: 2 }}>
          <ArrowBackIcon />
        </IconButton>
        <Typography variant="h4" component="h1">
          Add New Contact
        </Typography>
      </Paper>
      
      <ContactForm onSuccess={handleSuccess} />
    </Box>
  );
}