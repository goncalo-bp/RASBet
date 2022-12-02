import React from 'react';
import AlterarInfo from '../AlterarInfo';
import Navbar from '../Navbar';

function Edit() {
  return (
    <>
    {localStorage.getItem('isLogged') === 'true'?
      <>
        <Navbar />
        <AlterarInfo />
      </>
      :
      window.location.replace('http://localhost:3000/')
    }
    </>
  );
}

export default Edit;