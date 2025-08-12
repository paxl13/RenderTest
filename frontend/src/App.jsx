import React, { useState } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import { Typography, Box, Divider } from '@mui/material';
import ContactForm from './ContactForm.jsx';
import TableView from './TableView.jsx';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
  },
});

function App() {
  const [refreshTable, setRefreshTable] = useState(0);

  const handleContactAdded = () => {
    // Trigger table refresh by changing the refresh prop
    setRefreshTable(prev => prev + 1);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Box sx={{ mb: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom align="center">
            Contact Management System
          </Typography>
          <Divider sx={{ mb: 3 }} />
        </Box>
        
        <ContactForm onSuccess={handleContactAdded} />
        <TableView onRefresh={refreshTable} />
      </Container>
    </ThemeProvider>
  );
}

export default App;