import React from 'react';
import '../../App.css';
import '../Init.css';
import Form_R from '../Form_R';
import Dropdown from '../../Lang_Toogle';
function Registo() {
  return (
    <>
      <Dropdown
        trigger={<button>{localStorage.getItem("lang")}</button>}
      />
      <div className='init-container'>
        <div className='init-content'>
            <Form_R/>
            <div className='init-image'/>
        </div>
    </div>
    </>
  );
}

export default Registo;