import { useState } from 'react';
import './Form_R.css';

export default function Form_R() {

// States for registration
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [nif, setNIF] = useState('');
const [date, setDate] = useState('');


// States for checking the errors
const [submitted, setSubmitted] = useState(false);
const [error, setError] = useState(false);


// Handling the email change
const handleEmail = (e) => {
	setEmail(e.target.value);
	setSubmitted(false);
};

// Handling the password change
const handlePassword = (e) => {
	setPassword(e.target.value);
	setSubmitted(false);
};

// Handling the date change
const handleDate = (e) => {
	e.target.type="date";
	setDate(e.target.value);
	setSubmitted(false);
};

// Handling the nif change
const handleNIF = (e) => {
	if (e.target.value.length <= 9) {
		setNIF(e.target.value);
		setSubmitted(false);
	}
};


// Handling the form submission
const handleSubmit = (e) => {
	e.preventDefault();
	if (nif === '' || email === '' || password === '' || date === '') {
	setError(true);
	} else {
	setSubmitted(true);
	setError(false);
	}
};

const setToDate = (e) => {
	e.target.type="date";
}

// Showing success message
const successMessage = () => {
	return (
	<div
		className="success"
		style={{
		display: submitted ? '' : 'none',
		}}>
		<h1>User {email} successfully registered!!</h1>
	</div>
	);
};

// Showing error message if error is true
const errorMessage = () => {
	return (
	<div
		className="error"
		style={{
		display: error ? '' : 'none',
		}}>
		<h1>Please enter all the fields</h1>
	</div>
	);
};

document.addEventListener("click", (evt) => {
	const date = document.getElementById("date");
	let targetEl = evt.target; // clicked element      
	do {
	  if(targetEl == date) {
		// This is a click inside, does nothing, just return.
		document.getElementById("date").type = "date";
		return;
	  }
	  // Go up the DOM
	  targetEl = targetEl.parentNode;
	} while (targetEl);
	// This is a click outside.      
	if(date.value=='') 
		document.getElementById("date").type = "text";
  });

return (
<div className="form">
	

	{/* Calling to the methods */}
	<div className="messages">
		{errorMessage()}
		{successMessage()}
	</div>

	<form className='list-item'>
		<div className='title'>
			<h1>REGISTO</h1>
		</div>
		<br/>
		{/* Labels and inputs for form data */}
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
