import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import theme from './styles/theme'
import { ThemeProvider } from '@material-ui/core/styles';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ThemeProvider theme={theme}>
    <App />
  </ThemeProvider>
);