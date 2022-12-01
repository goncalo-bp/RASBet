import { useState } from 'react';
import './Form_R.css';
import Popup from './Popup';
import './AlterarInfo.css';
import { Button } from './Button';

export default function Form_L() {

// States for registration
const [nome, setNome] = useState('');
const [newPassword, setNewPassword] = useState('');

const [saldo, setSaldo] = useState(0);

// States for checking the errors
const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
const [btnPopup, setBtnPopup] = useState(false);

const [lev_Popup, setlev_Popup] = useState(false);
const [dep_Popup, setdep_Popup] = useState(false);

// Handling the email change
const handleNome = (e) => {
	setNome(e.target.value);
};

// Handling the password change
const handleNewPassword = (e) => {
	setNewPassword(e.target.value);
};

function toJson(nome,newPassword) {
	return {
		"name": nome,
		"password": newPassword,
	}
}

function toJson2(id) {
	return {
		"id": Number(id),
	}
}

const handleSubmit = (e) => {
	e.preventDefault();
	if (newPassword === '' && nome === '') {
		setError(0);
		setBtnPopup(true);
	}
	else {

		setError(false);
		fetch('http://localhost:5002/login', {  // Enter your IP address here

		method: 'POST', 
		mode: 'cors', 
		body: JSON.stringify(toJson(nome, newPassword)), // body data type must match "Content-Type" header
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
		{error === 0 ? <h1>Complete pelo menos um campo</h1> :
		<h1>Email / Password incorretos</h1>}
	</div>
	);
};

const handleLev = (e) => {
	setlev_Popup(true);
}

const handleDep = (e) => {
	setdep_Popup(true);
}

const levantar = () => {
	return (
	<div>
		<h1>Levantar</h1>
		<input type="text" onKeyPress={onlyNumberKey} placeholder="IBAN" />
		<br/>
		<input type="number" placeholder="Valor" />
		<Button buttonStyle='btn--outline' >Levantar</Button>
	</div>
	);
}

const onlyNumberKey = (evt) => {
	// Only ASCII character in that range allowed
	var ASCIICode = (evt.which) ? evt.which : evt.keyCode
	if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
		return false;
	return true;
}

const depositar = () => {

}

const getSaldo = () => {
	var valor = 0;
	fetch('http://localhost:5002/saldoCarteira', {  // Enter your IP address here

	method: 'POST',
	mode: 'cors', 
	body: JSON.stringify(toJson2(localStorage.getItem('id'))), // body data type must match "Content-Type" header 
	headers: {"Content-Type": "application/json"}	
	})
	.then( (response) => {
		if(!response.ok) {
			throw Error(response.status);
		}
		else return response.json();
	}).then( (data) => {
		valor = data.saldo;
		setSaldo(valor);
	})
	.catch( (error,status) => {
		console.log("error: ",status);
	});
}

return (
<div className="edit-fundo">
	{console.log(JSON.stringify(toJson2(localStorage.getItem('id'))))}
	<form className='edit-content'>
		<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
			{errorMessage()}
		</Popup>
		<Popup trigger={lev_Popup} setTrigger={setlev_Popup}>
			{levantar()}
		</Popup>
		<Popup trigger={dep_Popup} setTrigger={setdep_Popup}>
			{depositar()}
		</Popup>

		<div className='edit-header'>
			<h1>{localStorage.getItem("name")}</h1>
			<br/>
      		<h2 id="saldo">{getSaldo()}Saldo : {saldo}€</h2>
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
			<Button onClick={handleLev} className="btn--primary--orange--large">Levantar</Button>
			<Button onClick={handleDep} className="btn--primary--orange--large">Depositar</Button>
		</div>
		<br/>
		<div className='edit-form'>
			<Button dest="/home/historico" className="btn--primary--green--large">Histórico de Transações <i className='far fa-play-circle'/></Button>
			<Button dest="/home/apostas" className="btn--primary--green--large">Histórico de Apostas <i className='far fa-play-circle'/></Button>
		</div>
		
		<input onChange={handleNome} className="input--conta"
		value={nome} type="email" placeholder='Novo Nome'/>
		<input onChange={handleNewPassword} className="input--conta"
		value={newPassword} type="newPassword" placeholder='Nova Palavra-passe' />
		<button onClick={handleSubmit} className="btn--primary--orange--large" type="submit">
		Mudar Dados
		</button>
	</form>
</div>
);
}