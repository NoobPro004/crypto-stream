import React from 'react';
import Box from '@mui/material/Box';
import { makeStyles } from '@mui/styles';  // Updated import
import GitHubIcon from '@mui/icons-material/GitHub';
import IconButton from '@mui/material/IconButton';

const useStyles = makeStyles((theme) => ({
  hero: {
    backgroundImage: `linear-gradient(rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.75)), url('https://images.unsplash.com/photo-1518544801976-3e159e50e5bb?ixlib=rb-1.2.1&auto=format&fit=crop&w=1349&q=80')`,
    height: '500px',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
    position: 'relative',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    color: '#fff',
    fontSize: '4rem',
  },
}));

console.log("aa gya bhaiiiiii")
const HeroImage = () => {
  const classes = useStyles();
  return (
   <Box className={classes.hero}>
      <Box style={{ fontFamily: 'Raleway' }}>
        Real-Time <span style={{ color: '#f2a365' }}>Cryptocurrency</span>{' '}
        Updates
      </Box>
      <a
        href="https://github.com/NoobPro004/crypto-stream"
        target="_blank"
        rel="noopener noreferrer"
      >
        <IconButton aria-label="github-repo" color="primary">
          <GitHubIcon />
        </IconButton>
      </a>
    </Box>

  );
};

export default HeroImage;
