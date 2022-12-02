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
				window.location.replace('http://localhost:3000/home');
				if(data.isAdmin) {
					window.location.replace('http://localhost:3000/home-admin');  
				}
				if(data.isEspecialista) {
					window.location.replace('http://localhost:3000/home/apostas');
				}
				if(!data.isAdmin && !data.isEspecialista) {
					window.location.replace('http://localhost:3000/home');
				}
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
	}, []);

	return (
		<div className="form">
			<form className='list-item'>
				<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
					{errorMessage()}
				</Popup>
				<div className='title'>
					<h1>BEM VINDO</h1>
				</div>
				<br/>
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
