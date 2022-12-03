import React from 'react';
import Navbar from '../Navbar';
import Popup from '../Popup';

function Promocoes() {
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
  
  export default Promocoes;