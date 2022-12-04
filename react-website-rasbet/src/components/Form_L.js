import { useState, useEffect } from 'react';
import './Form_R.css';
import Popup from './Popup';

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
				console.log(data);
				localStorage.setItem('id', data.id);
				localStorage.setItem('name', data.name);
				localStorage.setItem('wallet', data.wallet);
				localStorage.setItem('isLogged', true);
				localStorage.setItem('timestamp', new Date());
				localStorage.setItem('desporto',"Futebol");
				localStorage.setItem('isAdmin', data.isAdmin);
				localStorage.setItem('isEspecialista', data.isEspecialista);
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

	useEffect(() => {
		localStorage.setItem('isLogged', false);
		localStorage.setItem('lang', 'pt');
	}, []);

	const translate = {
        "pt": {
            "bv" : "BEM VINDO",
            "aceder" : "Aceder",
			"reg" : ["Não tem conta?","Registe-se já!"]
        },
        "en": {
            "bv" : "WELCOME",
            "aceder" : "Log In",
			"reg" : ["Don't have an account?","Register now!"]
        },
        "es": {
            "bv" : "BIENVENIDO",
			"aceder" : "Acceder",
			"reg" : ["¿No tienes cuenta?","¡Regístrate ahora!"]
		}

    }
	var lang = localStorage.getItem('lang');
	return (		
		<div className="form">
			<form className='list-item'>
				<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
					{errorMessage()}
				</Popup>
				<div className='title'>
					<h1>{translate[lang]["bv"]}</h1>
				</div>
				<br/>
				{/* Labels and inputs for form data */}
				<input onChange={handleEmail} className="input"
				value={email} type="email" placeholder='E-mail'/>
				<br/>
				<input onChange={handlePassword} className="input"
				value={password} type="password" placeholder='Password' />
				<br/>
				<button onClick={handleSubmit} className="btn" type="submit">
				{translate[lang]["aceder"]}
				</button>
		        {translate[lang]["reg"][0]} <a href="/sign-up">{translate[lang]["reg"][1]}</a>
			</form>
		</div>
	);
}

