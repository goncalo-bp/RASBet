import React from 'react';
import '../../App.css';
import '../Init.css';
import Form_L from '../Form_L';



function Login() {
  localStorage.clear();

  return (
    <>
      <div className='init-container'>
        <div className='init-content'>
            <Form_L/>
            <div className='init-image'/>
        </div>
    </div>
    </>
  );
}

export default Login;