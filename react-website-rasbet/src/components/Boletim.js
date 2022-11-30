import { useState } from 'react';
import Popup from './Popup';
import './Boletim.css';
import { Button } from './Button';

export default function Boletim() {

const [value, setValue] = useState('');
const [oddTotal, setOddTotal] = useState(0);
const [totalGanhos, setTotalGanhos] = useState(0);


const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
const [btnPopup, setBtnPopup] = useState(false);

function addOdd(e){
	oddTotal += e.target.value;
}

function removeOdd(e){
	oddTotal -= e.target.value;
}




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
			<Button className="btn--primary--gray--medium">Simples</Button>
			<Button className="btn--primary--gray--medium">Múltipla</Button>
		</div>
		<br/>
		<div className='edit-lista-jogos'>
			<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>Sporting - Varzim</span>
					<span><Button className='btn--x--gray--medium'>X</Button></span>
				</div>
				<div className='edit-tipo-odds'>
					<span>Resultado: Empate</span>
					<span className='edit-tipo-odd'>3.5</span>
				</div>
			</div>
			<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>Sporting - Varzim</span>
					<span><Button className='btn--x--gray--medium'>X</Button></span>
				</div>
				<div className='edit-tipo-odds'>
					<span>Resultado: Empate</span>
					<span className='edit-tipo-odd'>3.5</span>
				</div>
			</div>
			<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>Sporting - Varzim</span>
					<span><Button className='btn--x--gray--medium'>X</Button></span>
				</div>
				<div className='edit-tipo-odds'>
					<span>Resultado: Empate</span>
					<span className='edit-tipo-odd'>3.5</span>
				</div>
			</div>
			<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>Sporting - Varzim</span>
					<span><Button className='btn--x--gray--medium'>X</Button></span>
				</div>
				<div className='edit-tipo-odds'>
					<span>Resultado: Empate</span>
					<span className='edit-tipo-odd'>3.5</span>
				</div>
			</div>
		</div>
		<div className='edit-total-odd'>
			<span className='edit-odd-total'> <span>Odd:</span>{oddTotal}</span>
			<input onChange={handleValue} className="edit-valor-total"
		value={value} type="value" placeholder='Valor:'/>		
		</div>
		<div className='edit-total-ganho'>
			<span className='edit-ganhos'> <span>Total de ganhos:</span>{totalGanhos}</span>
			<span className='btn--primary--orange--large'> <span>APOSTAR</span></span>
		</div>
	</form>
</div>
);
}