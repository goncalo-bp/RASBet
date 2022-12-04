import React from 'react';
import '../../App.css';
import '../Init.css';
import Form_L from '../Form_L';
import Dropdown from '../../Lang_Toogle';


function Login() {
  var lang = localStorage.getItem('lang');
  localStorage.clear();
  if (lang === "null"){
    localStorage.setItem("lang", "pt");
    lang = "pt";
  }
  else
    localStorage.setItem("lang", lang); 
<<<<<<< HEAD

  localStorage.setItem('lang',lang);
=======
>>>>>>> 2f1726aa0c63438199ab6d98bcb408bf510b2441
  return (
    <>
      <Dropdown
        trigger={<button>{lang}</button>}
      />
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