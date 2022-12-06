import { useState } from 'react';
import Popup from './Popup';
import './Boletim.css';
import { Button } from './Button';

export default function Boletim(aposta) {
	var apostas = aposta.apostas;
	const [value, setValue] = useState('');
	const [oddTotal, setOddTotal] = useState(0);
	const [totalGanhos, setTotalGanhos] = useState(0);

	const [tipoAposta, setTipoAposta] = useState(''); // s = simples, m = multipla

	const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
	const [btnPopup, setBtnPopup] = useState(false);

    
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
		act_TotalGanhos();
		return tipoAposta;
	}

	const handleType = (e) => {
		var id = e.target.id;
		var tipo = e.target.className;

		changeType(id,tipo)
	};


	// Handling the password change
	const handleValue = (e) => {
		setValue(e.target.value);
		setTotalGanhos((e.target.value * getOddTotal()).toFixed(2));
	};

	function act_TotalGanhos(){
		var mont = document.getElementById("montante");
		if (mont === null)
			return 0;
		var val = mont.value * getOddTotal();

		document.getElementById("total").textContent = val.toFixed(2);
	};

	function apostasSelecionadas(){
		return (apostas.map(aposta => {
			var info = document.getElementById(aposta).textContent.split(" ");
			var nome = document.getElementById(aposta[0]).textContent

			return entradaAposta(nome, info.slice(0,-1), info.at(-1), aposta);
		}));
	}

	const getOddTotal = () => {
		var odd = 0;
		apostas.map(aposta => {
			var info = document.getElementById(aposta).textContent.split(" ");
			if(tipoAposta === "s")
				odd += parseFloat(info.at(-1));

			else if(tipoAposta === "m")
				odd !== 0 ? odd *= parseFloat(info.at(-1)) : odd = parseFloat(info.at(-1));

		})
		odd = odd.toFixed(2);

		return odd;
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
					<span>{translate[lang]['resultado']}: {aposta}</span>
					<span className='edit-tipo-odd'>{odd}</span>
				</div>
			</div>
		)
	}

	const handleRemove = (e) => {
		var id = e.target.id;
		console.log(id);
		var selecao = document.getElementById(id.split("_")[0]);
		console.log(selecao.id);
		aposta.func(selecao);
		act_TotalGanhos();
	}

	const handleAposta = (e) => {
		var aApostar = document.getElementById("montante").value;

		if (aApostar=== ""){
			setError(3);
		}

		var saldo = Number(localStorage.getItem('wallet'));
		console.log(saldo);
		console.log(aApostar);
		if(aApostar > saldo){
			setError(1);
		}else if(tipoAposta === ''){
			setError(2);
		}else if(apostas.length === 0){
			setError(4);
		}
		else{


			//fetch('http://localhost:5002/registoaposta', {
			//	method: 'POST',
			//	headers: {
			//		'Content-Type': 'application/json',
			//		},
			//		body: JSON.stringify({
			//			"id": localStorage.getItem('id'),
			//			"apostas": apostas,
			//			"tipoAposta": tipoAposta,
			//			"montante": aApostar,
			//		})
			//})




			setError(0);
		}

		setBtnPopup(true);
	}

	const mensagem = () => {
		switch(error){
			case 0:
				return translate[lang]['error-msg-0'];
			case 1:
				return translate[lang]['error-msg-1'];
			case 2:
				return translate[lang]['error-msg-2'];
			case 3:
				return translate[lang]['error-msg-3'];
			case 4:
				return translate[lang]['error-msg-4'];
		}
	}

	var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
			'error-msg-0' : 'Aposta registada com sucesso!',
			'error-msg-1' : 'Saldo insuficiente',
			'error-msg-2' : 'Escolha o tipo de aposta',
			'error-msg-3' : 'Insira o montante a apostar',
			'error-msg-4' : 'Insira pelo menos uma aposta',
			'progresso' : 'Progresso',
			'ganhos' : 'Total de Ganhos',
			'bet-btn' : 'APOSTAR',
			'resultado' : 'Resultado',
		},
		'en': {
			'error-msg-0' : 'Bet registered successfully!',
			'error-msg-1' : 'Insufficient balance',
			'error-msg-2' : 'Choose the type of bet',
			'error-msg-3' : 'Enter the amount to bet',
			'error-msg-4' : 'Enter at least one bet',
			'progresso' : 'Progress',
			'ganhos' : 'Total Earnings',
			'bet-btn' : 'BET',
			'resultado' : 'Result',
		},
		'es': {
			'error-msg-0' : 'Apuesta registrada con éxito!',
			'error-msg-1' : 'Saldo insuficiente',
			'error-msg-2' : 'Elija el tipo de apuesta',
			'error-msg-3' : 'Ingrese la cantidad a apostar',
			'error-msg-4' : 'Ingrese al menos una apuesta',
			'progresso' : 'Progreso',
			'ganhos' : 'Ganancias totales',
			'bet-btn' : 'APOSTAR',
			'resultado' : 'Resultado',
		}
	}

	return (
		<form id={aposta.id} className='content-boletim'>
			<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
				{mensagem()}
			</Popup>
			<div className='edit-header'>
				<h1 style = {{fontSize:'70px'}}> {translate[lang]['progresso']}</h1>
				<br/>
			</div>
			<br/>
			<div className='edit-lista-jogos'>
				{apostasSelecionadas()} {act_TotalGanhos()}
			</div>
			<div className='edit-total-odd'>
				<span className='edit-odd-total'> <span>Odd:</span>{getOddTotal()}</span>
				<input id="montante" onChange={handleValue} className="edit-valor-total"
			value={value} type="value" placeholder='Valor (€):'/>		
			</div>
			<div className='edit-total-ganho'>
				<span className='edit-ganhos'>{translate[lang]['ganhos']}: <div id="total">{totalGanhos}</div></span>
				<Button className='btn--primary--orange--large' onClick={handleAposta}> {translate[lang]['bet-btn']}</Button>
			</div>
		</form>
	);
}