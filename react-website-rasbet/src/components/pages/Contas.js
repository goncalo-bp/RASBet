import React from 'react';
import GerirContas from '../GerirContas';
import Navbar from '../Navbar';

function Contas() {
    return (
      <>
      {localStorage.getItem('isLogged') === 'true'?
        <>
          <Navbar />
          <GerirContas />
        </>
        :
        window.location.replace('http://localhost:3000/')
      }
      </>
    );
  }
  
  export default Contas;