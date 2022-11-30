import { useState } from 'react';
import './Form_R.css';
import Popup from './Popup';
import './AlterarInfo.css';
import { Button } from './Button';

export default function Form_L() {

// States for registration
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [newPassword, setNewPassword] = useState('');

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

// Handling the password change
const handleNewPassword = (e) => {
	setNewPassword(e.target.value);
};

function toJson(email,password,newPassword) {
	return {
		"email": email,
		"password": password,
		"newPassword": newPassword
	}
}

const handleSubmit = (e) => {
	e.preventDefault();
	if (newPassword === '' || email === '' || password === '') {
	setError(0);
	setBtnPopup(true);
	}
	else {

	setError(false);
	fetch('http://localhost:5002/login', {  // Enter your IP address here

	method: 'POST', 
	mode: 'cors', 
	body: JSON.stringify(toJson(email,password, newPassword)), // body data type must match "Content-Type" header
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
			<br/>
      		<hr style={{
    		color: '#E0E0E0',
    		height: '3px',
			width: '80%'
  			}}
			/>
		</div>
		<br/>
		<br/>
		<div className='edit-form'>
			<Button dest="/home/levantar" className="btn--primary--orange--large">Levantar</Button>
			<Button dest="/home/depositar" className="btn--primary--orange--large">Depositar</Button>
		</div>
		<br/>
		<div className='edit-form'>
			<Button dest="/home/historico" className="btn--primary--green--large">Histórico de Transações <i className='far fa-play-circle'/></Button>
			<Button dest="/home/apostas" className="btn--primary--green--large">Histórico de Apostas <i className='far fa-play-circle'/></Button>
		</div>
		
		<input onChange={handleEmail} className="input--conta"
		value={email} type="email" placeholder='E-mail'/>
		<input onChange={handlePassword} className="input--conta"
		value={password} type="password" placeholder='Palavra-passe' />
		<input onChange={handleNewPassword} className="input--conta"
		value={newPassword} type="newPassword" placeholder='Nova Palavra-passe' />
		<button onClick={handleSubmit} className="btn--primary--orange--large" type="submit">
		Mudar Palavra-passe
		</button>
	</form>
</div>
);
}