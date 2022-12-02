import React from 'react';
import Navbar from '../Navbar';

function Depositar() {
  return (
    <>
    {localStorage.getItem('isLogged') === 'true'?
      <>
        <Navbar />
      </>
      :
      window.location.replace('http://localhost:3000/')
    }
    </>
  );
}

export default Depositar;