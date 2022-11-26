import { useState } from 'react';
import './Form_R.css';
import Popup from './Popup';
import './AlterarInfo.css';
import { Button } from './Button';

export default function Form_L() {

// States for registration
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');

// States for checking the errors
const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
const [btnPopup, setBtnPopup] = useState(false);


// Handling the email change
const handleEmail = (e) => {
	setEmail(e.target.value);
};

// Handling the password change
const handlePassword = (e) => {
	setPassword(e.target.value);
};


function toJson(email,password) {
	return {
		"email": email,
		"password": password
	}
}

const handleSubmit = (e) => {
	e.preventDefault();
	if (email === '' || password === '') {
	setError(0);
	setBtnPopup(true);
	}
	else {

	setError(false);
	fetch('http://localhost:5002/login', {  // Enter your IP address here

	method: 'POST', 
	mode: 'cors', 
	body: JSON.stringify(toJson(email,password)), // body data type must match "Content-Type" header
	headers: {"Content-Type": "application/json"}
	})
	.then( (response) => {
		if(!response.ok) {
			throw Error(response.status);
		}
		else return response.json();
	}).then( (data) => {
		window.location.replace('http://localhost:3000/home');
	})
	.catch( (error,status) => {
		console.log("error: ",status);
		setError(1);
		setBtnPopup(true);
	});
	}
};




const errorMessage = () => {
	return (
	<div>
		{error === 0 ? <h1>Complete todos os campos</h1> :
		<h1>Email / Password incorretos</h1>}
	</div>
	);
};

return (
<div className="edit-fundo">
	<form className='edit-content'>
		<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
			{errorMessage()}
		</Popup>
		<div className='edit-header'>
			<h1>Carlos Pereira</h1>
			<br/>
      		<h2>Saldo : 1000€</h2>
      		<hr style={{
    		color: '#E0E0E0',
    		height: '3px',
			width: '80%'
  			}}
			/>
		</div>
		<br/>
		<div className='edit-trans' >
			<Button buttonStyle='btn--white'
            buttonSize='btn--large' dest="/home">Levantar
			</Button>
			<Button buttonStyle='btn--orange'
            buttonSize='btn--large' dest="/home">Depositar</Button>
		</div>

		Consultar Histórico de Apostas
		{/* Labels and inputs for form data */}
		<input onChange={handleEmail} className="input"
		value={email} type="email" placeholder='E-mail'/>
		<br/>
		<input onChange={handlePassword} className="input"
		value={password} type="password" placeholder='Palavra-passe' />
		<br/>
		<button onClick={handleSubmit} className="btn" type="submit">
		Aceder
		</button>
        Não tem conta? <a href="/sign-up">Registe-se já!</a>
	</form>

	</div>
);
}
