import { useState } from 'react';
import './Form_R.css';
import Popup from './Popup';
import { redirect } from 'react-router-dom';


export default function Form_R() {
	// States for registration
	const [name, setName] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [nif, setNIF] = useState('');
	const [date, setDate] = useState('');

	// States for checking the errors
	const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/nif | 2 - menor
	const [btnPopup, setBtnPopup] = useState(false);

	// Handling the name change
	const handleName = (e) => {
		setName(e.target.value);
	};

	// Handling the email change
	const handleEmail = (e) => {
		setEmail(e.target.value);
	};

	// Handling the password change
	const handlePassword = (e) => {
		setPassword(e.target.value);
	};

	// Handling the date change
	const handleDate = (e) => {
		e.target.type="date";
		setDate(e.target.value);
	};

	function getAge(data) {
		var ano = data.substring(0,4);
		var mes = data.substring(5,7);
		var dia = data.substring(8,10);
	    var today = new Date();
	    var birthDate = new Date(ano,mes-1,dia);
	    var age = today.getFullYear() - birthDate.getFullYear();
	    var m = today.getMonth() - birthDate.getMonth();
	    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
	        age--;
	    }    
	    return age;
	}


	// Handling the nif change
	const handleNIF = (e) => {
		if (e.target.value.length <= 9) {
			setNIF(e.target.value);
		}
	};

	function toJson(name,email,password,nif,date) {
		return {
			"name" : name,
			"email": email,
			"password": password,
			"nif": nif,
			"date": date
		}
	}


	// Handling the form submission
	const handleSubmit = (e) => {
		e.preventDefault();
		if (name === '' || nif === '' || email === '' || password === '' || date === '') {
			setError(0);
			setBtnPopup(true);
		} else if (getAge(date) < 18) {
			setError(2);
			setBtnPopup(true);	
		}
		else {
			setError(false);
			fetch('http://localhost:5002/register', {  // Enter your IP address here
				method: 'POST', 
				mode: 'cors', 
				body: JSON.stringify(toJson(name,email,password,nif,date)), // body data type must match "Content-Type" header
				headers: {"Content-Type": "application/json"}
			})
			.then( (response) => {
				if(!response.ok) {
					throw Error(response.status);
				}
				else return response.json();
			}).then( (data) => {
				console.log(data);
				window.location.href = 'http://localhost:3000/';
			}).catch( (error) => {
				console.log("error: ",error);
				setError(1);
				setBtnPopup(true);
			});
		}
	};

	const setToDate = (e) => {
		e.target.type="date";
	}

	// Showing error message if error is true
	const errorMessage = () => {
		return (
		<div>
			{error === 0 ? <h1>Complete todos os campos</h1>  : ""}
			{error === 1 ? <h1>Email / NIF já registados</h1> : ""}
			{error === 2 ? <h1>Tem de ser maior de idade</h1> : ""}
		</div>
		);
	};

	document.addEventListener("click", (evt) => {
		const date = document.getElementById("date");
		let targetEl = evt.target; // clicked element      
		do {
			if(targetEl === date) {
				// This is a click inside, does nothing, just return.
				document.getElementById("date").type = "date";
				return;
			}
			// Go up the DOM
			targetEl = targetEl.parentNode;
		} while (targetEl);
		// This is a click outside.      
		if(date.value==='') 
			document.getElementById("date").type = "text";
	});

  	const translate = {
		"pt": {
			"nome": "Nome",
			"pass" : "Palavra-passe",
			"data" : "Data de nascimento",
			"concluir" : "Concluir",
			"reg" : "REGISTAR"
		},
		"en": {
			"nome": "Name",
			"pass" : "Password",
			"data" : "Date of birth",
			"concluir" : "Complete",
			"reg" : "REGISTER"
		},
		"es": {
			"nome": "Nombre",
			"pass" : "Contraseña",
			"data" : "Fecha de nacimiento",
			"concluir" : "Completar",
			"reg" : "REGISTRAR"
		}
	}

	var lang = localStorage.getItem('lang');

	return (
		<div className="form">
			<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
				{errorMessage()}
			</Popup>
			<form className='list-item'>
				<div className='rasbet-image'/>
				<div className='title'>
					<h1>{translate[lang]["reg"]}</h1>
				</div>
				<br/>
				{/* Labels and inputs for form data */}
				<input onChange={handleName} className="input"
				value={name} type="name" placeholder='Name'/>
				<br/>
				<input onChange={handleEmail} className="input"
				value={email} type="email" placeholder='E-mail'/>
				<br/>
				<input onChange={handlePassword} className="input"
				value={password} type="password" placeholder='Palavra-passe' />
				<br/>
				<input onChange={handleDate} className="input" id="date"
				value={date} type="text" placeholder='Data de Nascimento' onClick={setToDate}/>
				<br/>
				<input onChange={handleNIF} className="input"
				value={nif} type="number" placeholder='NIF' />
		
		
				<button onClick={handleSubmit} className="btn" type="submit">
				Concluir
				</button>
			</form>
		</div>
	);
}
