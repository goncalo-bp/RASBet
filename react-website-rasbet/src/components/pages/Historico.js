import React from 'react';
import HistoricoTransacao from '../HistTransac';
import Navbar from '../Navbar';

function Historico() {
  return (
    <>
    {localStorage.getItem('isLogged') === 'true'?
      <>
        <Navbar />
        <HistoricoTransacao />
      </>
      :
      window.location.replace('http://localhost:3000/')
    }
    </>
  );
}

export default Historico;