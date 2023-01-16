import { useState } from 'react';
import './Form_R.css';
import Popup from './Popup';
import './AlterarInfo.css';
import { Button } from './Button';

export default function Form_L() {

	// States for registration
	const [nome, setNome] = useState('');
	const [newPassword, setNewPassword] = useState('');

	// States for checking the errors
	const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
	const [btnPopup, setBtnPopup] = useState(false);

	const [lev_Popup, setlev_Popup] = useState(false);
	const [dep_Popup, setdep_Popup] = useState(false);

	const [deposito, setDeposito] = useState(""); // 0 - MBWay | 1 - Transferencia Bancaria 

	// Handling the email change
	const handleNome = (e) => {
		setNome(e.target.value);
	};

	// Handling the password change
	const handleNewPassword = (e) => {
		setNewPassword(e.target.value);
	};

	function toJson(nome,newPassword) {
		console.log(nome);
		console.log(newPassword);
		if (nome === ""){
			return {
				"id" : localStorage.getItem("id"),
				"password": newPassword
			}
		}else if (newPassword === ""){
			return {
				"id" : localStorage.getItem("id"),
				"name": nome
			}
		}
		else
			return {
				"id" : localStorage.getItem("id"),
				"name": nome,
				"password": newPassword,
			}
	}

	function toJsonT(value,type){
		return {
			"id" : localStorage.getItem("id"),
			"value": value,
			"type": type
		}
	}

	const handleSubmit = (e) => {
		e.preventDefault();
		if (newPassword === '' && nome === '') {
			setError(0);
			setBtnPopup(true);
		}
		else {
			fetch('http://localhost:5002/mudarcampo', {  // Enter your IP address here

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
				if (nome !== "")
					localStorage.setItem("name", nome);
			
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
			{error === 0 ? <h1>{translate[lang]['error-0']}</h1> :
			<h1>{translate[lang]['error-1']}</h1>}
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
		<div className='popup-center'>
			<input id="ibanL" type="text" placeholder="IBAN"/>
			<br/>
			<input id="aLevantar" type="number" placeholder={translate[lang]['valor']} />
			<Button className='btn--outline--full--orange--large' onClick={alertValid} >{translate[lang]['levantar']}</Button>
		</div>
		);
	}

	function alertValid() {
		var iban = document.getElementById("ibanL").value;
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
				alert(translate[lang]['inserir']);
			}		
			else if(Number(val) > Number(carteira))
				alert(translate[lang]['no-saldo']);	

			else {
				// LEVANTAR
				fetch('http://localhost:5002/transacao', {  // Enter your IP address here

				method: 'POST', 
				mode: 'cors', 
				body: JSON.stringify(toJsonT(Number(val)*(-1), "L")), // body data type must match "Content-Type" header
				headers: {"Content-Type": "application/json"}
				})
				.then( (response) => {
					if(!response.ok) {
						throw Error(response.status);
					}
					else return response.json();
				}).then( (data) => {
					localStorage.setItem("wallet", Number(carteira) - Number(val));
					window.location.reload();
				})
				.catch( (error,status) => {
					console.log("error: ",status);
					setError(1);
					setBtnPopup(true);
				});

				setlev_Popup(false);
			}
		}
	}
	function isValidIBANNumber(input) {
	    var CODE_LENGTHS = {
	        AD: 24, AE: 23, AT: 20, AZ: 28, BA: 20, BE: 16, BG: 22, BH: 22, BR: 29,
	        CH: 21, CY: 28, CZ: 24, DE: 22, DK: 18, DO: 28, EE: 20, ES: 24,
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
	    if (!code || iban.length - 2 !== CODE_LENGTHS[code[1]]) {
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


	function tipoDeposito(e){
		var id = e.target.id;
		var id2 = (id === "mbway" ? "transf" : "mbway");
		if(e.target.className === "btn--primary--gray--medium"){
			document.getElementById(id).classList.add('btn--primary--gray--medium_click');
			document.getElementById(id).classList.remove('btn--primary--gray--medium');

			document.getElementById(id2).classList.add('btn--primary--gray--medium');
			document.getElementById(id2).classList.remove('btn--primary--gray--medium_click');

			if(id === "mbway"){
				document.getElementById("telf").style.display = "inline";
				document.getElementById("ibanD").style.display = "none";
				document.getElementById("ibanD").value = "";
				setDeposito(0);
			}
			else{
				document.getElementById("telf").style.display = "none";
				document.getElementById("ibanD").style.display = "inline";
				document.getElementById("telf").value = "";
				setDeposito(1);
			}
		}
	}

	//TODO alerts + deposit + withdraw
	function alertValid_Dep() {
		console.log(deposito);
		var valor = document.getElementById("aDepositar").value;
		var ok = false;
		if (valor === ""){
			alert(translate[lang]['inserir']);
		}else{
			if(deposito === 0){
				var telf = document.getElementById("telf").value;
				telf === "" ? alert(translate[lang]['inserir-numero']) : ok = true;

			}else if(deposito === 1){
				var iban = document.getElementById("ibanD").value;
				var res = isValidIBANNumber(iban);
				res === -1 ? alert(translate[lang]['invalido']) : ok = true;
			}
		}

		if(ok){
			// DEPOSITAR
			fetch('http://localhost:5002/transacao', {  // Enter your IP address here

				method: 'POST', 
				mode: 'cors', 
				body: JSON.stringify(toJsonT(Number(valor), "D")), // body data type must match "Content-Type" header
				headers: {"Content-Type": "application/json"}
				})
				.then( (response) => {
					if(!response.ok) {
						throw Error(response.status);
					}
					else return response.json();
				}).then( (data) => {
					localStorage.setItem("wallet", Number(localStorage.getItem("wallet")) + Number(valor));
					window.location.reload();
				})
				.catch( (error,status) => {
					console.log("error: ",status);
					setError(1);
					setBtnPopup(true);
				});

			//localStorage.setItem("wallet", Number(localStorage.getItem("wallet")) + Number(valor));
			setdep_Popup(false);
		}
	}


	const depositar = () => {
		return (
		<div className='popup-center'>
			<div>
				<Button id="mbway" className='btn--primary--gray--medium' onClick={tipoDeposito} >MBWay</Button>
				<Button id="transf" className='btn--primary--gray--medium' onClick={tipoDeposito} >{translate[lang]['transf']}</Button>
			</div>
			<input id="ibanD" type="text" placeholder="IBAN" style={{display: 'none'}}/>
			<input id="telf" type="number" placeholder={translate[lang]['telemovel']} style={{display: 'none'}}/>
			<br/>
			<input id="aDepositar" type="number" placeholder={translate[lang]['valor']} />
			<Button className='btn--outline--full--orange--large' onClick={alertValid_Dep} >{translate[lang]['depositar']}</Button>
		</div>
		);
	}

	var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
			'saldo': 'Saldo',
			'levantar': 'Levantar',
			'depositar': 'Depositar',
			'hist-trans': 'Histórico de Transações',
			'hist-bets': 'Histórico de Apostas',
			'new-name': 'Novo Nome',
			'new-pass': 'Nova Password',
			'edit' : 'Mudar Dados',
			'error-0' : 'Complete pelo menos um campo',
			'error-1' : 'Email / Password incorretos',
			'valor' : 'Valor (€)',
			'telemovel' : 'Telemóvel',
			'transf' : 'Transferência Bancária',
			'inserir' : 'Insira um valor',
			'invalido' : 'IBAN inválido',
			'inserir-numero' : 'Insira um número de telemóvel',
			'no-saldo' : 'Não tem saldo suficiente',
		},
		'en': {
			'saldo': 'Balance',
			'levantar': 'Withdraw',
			'depositar': 'Deposit',
			'hist-trans': 'Transaction History',
			'hist-bets': 'Bet History',
			'new-name': 'New Name',
			'new-pass': 'New Password',
			'edit' : 'Edit Data',
			'error-0' : 'Complete at least one field',
			'error-1' : 'Email / Password incorrect',
			'valor' : 'Value (€)',
			'telemovel' : 'Mobile',
			'transf' : 'Bank Transfer',
			'inserir' : 'Insert a value',
			'invalido' : 'Invalid IBAN',
			'inserir-numero' : 'Insert a mobile number',
			'no-saldo' : 'You do not have enough balance',
		},
		'es': {
			'saldo': 'Saldo',
			'levantar': 'Retirar',
			'depositar': 'Depositar',
			'hist-trans': 'Historial de Transacciones',
			'hist-bets': 'Historial de Apuestas',
			'new-name': 'Nuevo Nombre',
			'new-pass': 'Nueva Contraseña',
			'edit' : 'Cambiar Datos',
			'error-0' : 'Complete al menos un campo',
			'error-1' : 'Email / Password incorrectos',
			'valor' : 'Valor (€)',
			'telemovel' : 'Teléfono',
			'transf' : 'Transferencia Bancaria',
			'inserir' : 'Inserte un valor',
			'invalido' : 'IBAN inválido',
			'inserir-numero' : 'Inserte un número de teléfono',
			'no-saldo' : 'No tiene saldo suficiente',
		}
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
					<h2 id="saldo">{translate[lang]['saldo']} : {localStorage.getItem("wallet")}€</h2>
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
					<Button onClick={handleLev} className="btn--primary--orange--large">{translate[lang]['levantar']}</Button>
					<Button onClick={handleDep} className="btn--primary--orange--large">{translate[lang]['depositar']}</Button>
				</div>
				<br/>
				<div className='edit-form'>
					<Button dest="/home/historico" className="btn--primary--green--large">{translate[lang]['hist-trans']} <i className='far fa-play-circle'/></Button>
					<Button dest="/home/apostas" className="btn--primary--green--large">{translate[lang]['hist-bets']} <i className='far fa-play-circle'/></Button>
				</div>
					
				<input onChange={handleNome} className="input--conta"
				value={nome} type="email" placeholder={translate[lang]['new-name']}/>
				<input onChange={handleNewPassword} className="input--conta"
				value={newPassword} type="newPassword" placeholder={translate[lang]['new-pass']} />
				<Button onClick={handleSubmit} className="btn--primary--orange--large" type="submit">
				{translate[lang]['edit']}
				</Button>
			</form>
		</div>
	);
}