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
		<input id="iban" type="text" placeholder="IBAN"/>
		<br/>
		<input id="aLevantar" type="number" placeholder="Valor (€)" />
		<Button buttonStyle='btn--outline' onClick={alertValidIBAN} >Levantar</Button>
	</div>
	);
}

function alertValidIBAN(iban) {
	iban = document.getElementById("iban").value;
    var res = isValidIBANNumber(iban);
	if (res === -1) {
		alert("IBAN válido");
	}
	else {
		var val = document.getElementById("aLevantar").value;
		var carteira = localStorage.getItem("wallet");
		console.log(val);
		console.log(carteira)
		if(val === ""){
			alert("Insira um valor");
		}		
		else if(Number(val) > Number(carteira))
			alert("Não tem saldo suficiente");	
			
		else {
			//
		}
	}
}
function isValidIBANNumber(input) {
    var CODE_LENGTHS = {
        AD: 24, AE: 23, AT: 20, AZ: 28, BA: 20, BE: 16, BG: 22, BH: 22, BR: 29,
        CH: 21, CR: 21, CY: 28, CZ: 24, DE: 22, DK: 18, DO: 28, EE: 20, ES: 24,
        FI: 18, FO: 18, FR: 27, GB: 22, GI: 23, GL: 18, GR: 27, GT: 28, HR: 21,
        HU: 28, IE: 22, IL: 23, IS: 26, IT: 27, JO: 30, KW: 30, KZ: 20, LB: 28,
        LI: 21, LT: 20, LU: 20, LV: 21, MC: 27, MD: 24, ME: 22, MK: 19, MR: 27,
        MT: 31, MU: 30, NL: 18, NO: 15, PK: 24, PL: 28, PS: 29, PT: 25, QA: 29,
        RO: 24, RS: 22, SA: 24, SE: 24, SI: 19, SK: 24, SM: 27, TN: 24, TR: 26,   
        AL: 28, BY: 28, CR: 22, EG: 29, GE: 22, IQ: 23, LC: 32, SC: 31, ST: 25,
        SV: 28, TL: 23, UA: 29, VA: 22, VG: 24, XK: 20
    };
    var iban = String(input).toUpperCase().replace(/[^A-Z0-9]/g, ''), // keep only alphanumeric characters
            code = iban.match(/^([A-Z]{2})(\d{2})([A-Z\d]+)$/), // match and capture (1) the country code, (2) the check digits, and (3) the rest
            digits;
    // check syntax and length
    if (!code || iban.length !== CODE_LENGTHS[code[1]]) {
		console.log(code)
        return -1;
    }
    // rearrange country code and check digits, and convert chars to ints
    digits = (code[3] + code[1] + code[2]).replace(/[A-Z]/g, function (letter) {
        return letter.charCodeAt(0) - 55;
    });
    // final check
    return mod97(digits);
}

function mod97(string) {
    var checksum = string.slice(0, 2), fragment;
    for (var offset = 2; offset < string.length; offset += 7) {
        fragment = String(checksum) + string.substring(offset, offset + 7);
        checksum = parseInt(fragment, 10) % 97;
    }
    return checksum;
}



const depositar = () => {

}


return (
<div className="edit-fundo">
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
      		<h2 id="saldo">Saldo : {localStorage.getItem("wallet")}€</h2>
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