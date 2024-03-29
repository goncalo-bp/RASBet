import { useState } from 'react';
import Popup from './Popup';
import './Boletim.css';
import { Button } from './Button';

export default function Boletim(aposta) {
	var apostas = aposta.apostas
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
		} ))
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
						<span>Resultado: {aposta}</span>
						<span className='edit-tipo-odd'>{odd}</span>
					</div>
		</div>)
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
		else{
			var saldo = Number(localStorage.getItem('wallet'));
			if(aApostar > saldo){
				setError(1);
			}else if(tipoAposta === ''){
				setError(2);
			}else if(apostas.length === 0){
				setError(4);
			}
			else{
				var type = tipoAposta;
				tipoAposta === 's' ? type = 'simples' :	type = 'multipla';
				var res = new Object();
				
				for(var i = 0; i < apostas.length; i++){
					var game_id =  document.getElementById(apostas[i][0]+"_id").textContent;
					var team_name = document.getElementById(apostas[i]).textContent.split(" ");
					team_name = team_name.slice(0,-1).join(" ");
					console.log(team_name);
					res[game_id] = team_name;
				}

				fetch('http://localhost:5002//apostas/registo/'+type, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'Bearer ' + localStorage.getItem('token'),
						},
						body: JSON.stringify({
							"id": localStorage.getItem('id'),
							"boletim": res,
							"montante": aApostar,
						})
				}).then((response) => {
					if(!response.ok) {
						throw Error(response.status);
					}
					else return response.json();
				}).then((data) => {
					setError(0);
					var atual = Number(localStorage.getItem('wallet'));
					if (tipoAposta === 's')
						aApostar = aApostar * apostas.length;
						
					localStorage.setItem("wallet",atual - aApostar);
				})
				.catch(error => {
					console.log("error: ", error);
					setError(5);
				});				
			}
		}


		setBtnPopup(true);
	}

	const mensagem = () => {
		switch(error){
			case 0:
				return "Aposta registada com sucesso!";
			case 1:
				return "Saldo insuficiente";
			case 2:
				return "Escolha o tipo de aposta";
			case 3:
				return "Insira o montante a apostar";
			case 4:
				return "Insira pelo menos uma aposta";
			case 5:
				return "Erro a registar aposta!";
		}
	}

	var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
			'apostar': 'APOSTAR',
			'boletim': 'Boletim',
			'valor' : 'Valor (€):',
			'total-ganhos': 'Total de ganhos: ',
			'odd': 'Odd:',
			'simples': 'Simples',
			'multipla': 'Múltipla',
		},
		'en': {
			'apostar': 'BET',
			'boletim': 'Report Card',
			'valor' : 'Value (€):',
			'total-ganhos': 'Total winnings: ',
			'odd': 'Odd:',
			'simples': 'Simple',
			'multipla': 'Multiple',
		},
		'es': {
            'apostar' : 'APOSTAR',
			'boletim' : 'Boletín',
			'valor' : 'Valor (€):',
            'total-ganhos' : 'Total de ganancias: ',
			'odd' : 'Odd:',
            'simples' : 'Simple',
            'multipla' : 'Múltiple',
		}
	}

return (
	<form id={aposta.id} className='content-boletim'>
		<Popup trigger={btnPopup} setTrigger={setBtnPopup}>
			{mensagem()}
		</Popup>
		<div className='edit-header'>
			<h1 style = {{fontSize:'70px'}}> {translate[lang]['boletim']}</h1>
			<br/>
		</div>
		<div className='edit-tipo-aposta'>
			<Button id={"tipo1"} className="btn--primary--gray--medium" onClick={handleType}>{translate[lang]['simples']}</Button>
			<Button id={"tipo2"} className="btn--primary--gray--medium" onClick={handleType}>{translate[lang]['multipla']}</Button>
		</div>
		<br/>
		<div className='edit-lista-jogos'>
			{apostasSelecionadas()} {act_TotalGanhos()}
		</div>
		<div className='edit-total-odd'>
			<span className='edit-odd-total'> <span>{translate[lang]['odd']}</span>{getOddTotal()}</span>
			<input id="montante" onChange={handleValue} className="edit-valor-total"
		value={value} type="value" placeholder={translate[lang]['valor']}/>
		</div>
		<div className='edit-total-ganho'>
			<span className='edit-ganhos'>{translate[lang]['total-ganhos']}<div id="total">{totalGanhos}</div></span>
			<Button className='btn--primary--orange--large' onClick={handleAposta}> {translate[lang]['apostar']}</Button>
		</div>
	</form>
);
}