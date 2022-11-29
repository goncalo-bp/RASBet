import { useState } from 'react';
import Popup from './Popup';
import './Boletim.css';
import { Button } from './Button';

export default function Form_L() {

const [value, setValue] = useState('');


const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
const [btnPopup, setBtnPopup] = useState(false);


// Handling the password change
const handleValue = (e) => {
	setValue(e.target.value);
};

return (
<div className="edit-fundo">
	<form className='edit-content-boletim'>
		<div className='edit-header'>
			<h1 style = {{fontSize:'70px'}}> Boletim</h1>
			<br/>
		</div>
		<div className='edit-tipo-aposta'>
			<Button className="btn--primary--gray--medium">Levantar</Button>
			<Button className="btn--primary--gray--medium">Depositar</Button>
		</div>
		<br/>
        <div className='edit-tipo-jogo'>
			<span>Sporting - Varzim</span>
			<span><Button className='btn--x--gray--medium'>X</Button></span>
        </div>
		<div className='edit-tipo-odds'>
			<span>Resultado: Empate</span>
			<span className='edit-odd'>3.5</span>
		</div>
		<br/>
        <div className='edit-tipo-jogo'>
			<span>Sporting - Varzim</span>
			<span><Button className='btn--x--gray--medium'>X</Button></span>
        </div>
		<div className='edit-tipo-odds'>
			<span>Resultado: Empate</span>
			<span className='edit-odd'>3.5</span>
		</div>
	</form>
</div>
);
}