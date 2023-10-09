import logo from './logo.svg';
import './App.css';
import Home from './components/Home';
import CoinChart from './components/CoinChart';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home/>} />
        <Route
          exact
          path="/:symbol/:id"
          element={<CoinChart />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
