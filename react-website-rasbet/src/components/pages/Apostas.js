import React from 'react';
import HistoricoApostas from '../HistBets';
import Navbar from '../Navbar';

function Apostas() {
  return (
    <>
    {localStorage.getItem('isLogged') === 'true'?
      <>
        <Navbar />
        <HistoricoApostas />
      </>
      :
      window.location.replace('http://localhost:3000/')
    }
    </>
  );
}

export default Apostas;