import { useState } from 'react';
import Popup from './Popup';
import './Boletim.css';
import { Button } from './Button';

export default function Boletim(aposta) {
var apostas = aposta.apostas
const [value, setValue] = useState('');
//const [oddTotal, setOddTotal] = useState(0);
const [totalGanhos, setTotalGanhos] = useState(0);

const [tipoAposta, setTipoAposta] = useState(''); // s = simples, m = multipla

const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
const [btnPopup, setBtnPopup] = useState(false);

function addOdd(e){
	//oddTotal += e.target.value;
}

function removeOdd(e){
	//oddTotal -= e.target.value;
}

function changeType(id,tipo){
	var id2 = (id === "tipo1" ? "tipo2" : "tipo1");
	if(tipo === "btn--primary--gray--medium"){
		document.getElementById(id).classList.add('btn--primary--gray--medium_click');
		document.getElementById(id).classList.remove('btn--primary--gray--medium');

		document.getElementById(id2).classList.add('btn--primary--gray--medium');
		document.getElementById(id2).classList.remove('btn--primary--gray--medium_click');
		
		if (id === "tipo2"){
			setTipoAposta('m');
			return "m";
		}
		else
			setTipoAposta('s');
			return "s";
		
	}
	return tipoAposta;
}

const handleType = (e) => {
	var id = e.target.id;
	var tipo = e.target.className;
	
	var tipoAtualizado = changeType(id,tipo)

	if(tipoAtualizado !== tipoAposta){
		
	}
	
};


// Handling the password change
const handleValue = (e) => {
	setValue(e.target.value);
	setTotalGanhos(e.target.value * 1);
};

function apostasSelecionadas(){
	console.log(apostas);
	return (apostas.map(aposta => {
		var info = document.getElementById(aposta).textContent.split(" ");
		var nome = document.getElementById(aposta[0]).textContent
		
		return entradaAposta(nome, info.slice(0,-1), info.at(-1), aposta);
	} ))
}

const getOddTotal = () => {
	var oddTotal = 0;
	apostas.map(aposta => {
		var info = document.getElementById(aposta).textContent.split(" ");
		if(tipoAposta === "s")
			oddTotal += parseFloat(info.at(-1));
			
		else if(tipoAposta === "m")
			oddTotal !== 0 ? oddTotal *= parseFloat(info.at(-1)) : oddTotal = 1 + parseFloat(info.at(-1));
		
	})
	oddTotal = oddTotal.toFixed(2);
	return oddTotal;
}

const concat = (e1,e2) =>{
	return e1 + "_" + e2;
 }

function entradaAposta(nome, aposta, odd,id){
	return (
	<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>{nome}</span>
					<span><Button id={concat(id,"rem")} className='btn--x--gray--medium' onClick={handleRemove} >-</Button></span>
				</div>
				<div className='edit-tipo-odds'>
					<span>Resultado: {aposta}</span>
					<span className='edit-tipo-odd'>{odd}</span>
				</div>
	</div>)
}

function handleRemove(){

	document.getElementById(concat(aposta,"rem"));
	aposta.func()
}

return (
	<form className='content-boletim'>
		<div className='edit-header'>
			<h1 style = {{fontSize:'70px'}}> Boletim</h1>
			<br/>
		</div>
		<div className='edit-tipo-aposta'>
			<Button id={"tipo1"} className="btn--primary--gray--medium" onClick={handleType}>Simples</Button>
			<Button id={"tipo2"} className="btn--primary--gray--medium" onClick={handleType}>Múltipla</Button>
		</div>
		<br/>
		<div className='edit-lista-jogos'>
			{apostasSelecionadas()}
		</div>
		<div className='edit-total-odd'>
			<span className='edit-odd-total'> <span>Odd:</span>{getOddTotal()}</span>
			<input onChange={handleValue} className="edit-valor-total"
		value={value} type="value" placeholder='Valor (€):'/>		
		</div>
		<div className='edit-total-ganho'>
			<span className='edit-ganhos'> <span>Total de ganhos:</span>{totalGanhos}</span>
			<span className='btn--primary--orange--large'> <span>APOSTAR</span></span>
		</div>
	</form>
);
}