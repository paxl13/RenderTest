import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Fab, Typography } from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import TableView from './TableView.jsx';

export default function ContactsPage() {
  const navigate = useNavigate();
  const [refreshTable, setRefreshTable] = useState(0);

  const handleAddClick = () => {
    navigate('/add');
  };

  return (
    <Box sx={{ position: 'relative', minHeight: '100vh', pb: 8 }}>
      <Box sx={{ mb: 3 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Contact Management System
        </Typography>
      </Box>
      
      <TableView onRefresh={refreshTable} />
      
      {/* Floating Action Button - Bottom Right */}
      <Fab
        color="primary"
        aria-label="add"
        onClick={handleAddClick}
        sx={{
          position: 'fixed',
          bottom: 24,
          right: 24,
        }}
      >
        <AddIcon />
      </Fab>
    </Box>
  );
}