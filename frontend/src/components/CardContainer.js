import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import { makeStyles } from '@material-ui/core/styles';
import CoinCard from './CoinCard';
import axios from 'axios';

const useStyles = makeStyles({
  gridContainer: {
    paddingTop: '20px',
  },
});

const CardContainer = () => {
  const classes = useStyles();
  const [coinsData, setCoinsData] = useState([]);

  useEffect(() => {
    const getCoins = async () => {
      const { data :{data} } = await axios.get('https://api.coinranking.com/v2/coins');
      console.log("data is ",data)
      console.log(data.coins)
      setCoinsData(data.coins);
    };

    getCoins();
  }, []);

  return (
    <Grid container>
      <Grid item sm={2} />

      <Grid
        container
        item
        xs={12}
        sm={8}
        spacing={4}
        className={classes.gridContainer}
        justify="center"
        align="center"
      >
        {coinsData.map((coinData) => {
          return (
            <Grid key={coinData.uuid} item xs={12} lg={4}>
              <CoinCard coinData={coinData} />;
            </Grid>
          );
        })}
      </Grid>

      <Grid item sm={2} />
    </Grid>
  );
};

export default CardContainer;