import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistBets.css'

function HistoricoApostas() {
    const [simples, setSimples] = useState([]);
    const [multipla, setMultipla] = useState([]);

    const [btnSimples, setBtnSimples] = useState(false);
    const [btnMultipla, setBtnMultipla] = useState(false);

    const [empty, setEmpty] = useState({control : false});

    const [button,setButton] = useState(true);

    const showButton = () => {
        if(window.innerWidth <= 740) {
            setButton(false);
        } else {
            setButton(true);
        }
    };
  
    useEffect(() => {
        showButton();
    }, []);
  
    window.addEventListener('resize', showButton);
    
    function toJson(id) {
		return {"id": id}
	}

    const getBets = (e) => {
        //e.preventDefault();
        fetch('http://localhost:5002/apostas', {  // Enter your IP address here
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(toJson(localStorage.getItem('id'))),
            headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setSimples(data.simples[0]);
            setMultipla(data.multipla[0]);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    const handleSimples = (e) => {
        {simples.length === 0 ? setEmpty({control : true, msg : translate[lang]['no-simples']}) : setEmpty({control : false})}
        {simples.length > 0 ? setBtnSimples(true) : setBtnSimples(false)}
        setBtnMultipla(false);
    };

    const handleMultipla = (e) => {
        {multipla.length === 0 ? setEmpty({control : true, msg : translate[lang]['no-multipla']}) : setEmpty({control : false})}
        {multipla.length > 0 ? setBtnMultipla(true) : setBtnMultipla(false)}
        setBtnSimples(false);
    };

    // TODO corrigir isto
    useEffect(() => {
        getBets();
    }, []);

    var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
            'hist-bets' : 'Histórico de Apostas',
            'simples' : 'Simples',
            'multipla' : 'Múltiplas',
            'empate' : 'Resultado: Empate',
            'vencedor' : 'Vencedor:',
            'montante' : 'Montante apostado: ',
            'ganhos' : 'Total de ganhos: ',
            'no-simples' : 'Ainda não fez apostas simples.',
            'no-multipla' : 'Ainda não fez apostas múltiplas.',
		},
		'en': {
            'hist-bets' : 'Bets History',
            'simples' : 'Simples',
            'multipla' : 'Multiple',
            'empate' : 'Result: Draw',
            'vencedor' : 'Winner:',
            'montante' : 'Bet amount: ',
            'ganhos' : 'Total winnings: ',
            'no-simples' : 'You haven\'t made any simple bets yet.',
            'no-multipla' : 'You haven\'t made any multiple bets yet.',
		},
		'es': {
            'hist-bets' : 'Historial de apuestas',
            'simples' : 'Simples',
            'multipla' : 'Múltiples',
            'empate' : 'Resultado: Empate',
            'vencedor' : 'Ganador:',
            'montante' : 'Cantidad apostada: ',
            'ganhos' : 'Total de ganancias: ',
            'no-simples' : 'Aún no ha realizado apuestas simples.',
            'no-multipla' : 'Aún no ha realizado apuestas múltiples.',
		}
	}

    return (
        <div className='container'>
            <div className='box-container'>
                <div className='title-container'>
                    <div className='back'>
                        {button && <Button dest='/home/edit' className={'btn--circle--green--small'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                        {!button && <Button dest='/home/edit' className={'btn--circle--green--tiny'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                    </div>
                    <h1 className='title-text'>{localStorage.getItem('name')}</h1>
                </div>
                <br/>
                <h2>{translate[lang]['hist-bets']}</h2>
                <br/>
                <span>
                    <div className='bet-type'>
                        {button &&
                        <>
                            {btnSimples &&
                            <>
                                <Button className='btn--active--orange--large' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--outline--full--orange--large' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                            {btnMultipla &&
                            <>
                                <Button className='btn--outline--full--orange--large' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--active--orange--large' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                            {!btnSimples && !btnMultipla &&
                            <>
                                <Button className='btn--outline--full--orange--large' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--outline--full--orange--large' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                        </>
                        }
                        {!button &&
                        <>
                            {btnSimples &&
                            <>
                                <Button className='btn--active--orange--medium' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--outline--full--orange--medium' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                            {btnMultipla &&
                            <>
                                <Button className='btn--outline--full--orange--medium' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--active--orange--medium' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                            {!btnSimples && !btnMultipla &&
                            <>
                                <Button className='btn--outline--full--orange--medium' onClick={handleSimples}>
                                    {translate[lang]['simples']}
                                </Button>
                                <Button className='btn--outline--full--orange--medium' onClick={handleMultipla}>
                                    {translate[lang]['multipla']}
                                </Button>
                            </>
                            }
                        </>
                        }
                    </div>
                </span>
                <br/>{button && <br/>}
                <div className='bets-container'>
                    {btnSimples && 
                        <div>
                            {simples.map((entry, index) => {
                                return(
                                    <div key={index} className='entry'>
                                        <div>
                                            {entry.jogo.map((value, index) => {
                                                return(
                                                    <div key={index} className='jogo'>
                                                        <div className='nome-jogo'>
                                                            <h3>{value[0]}</h3>
                                                        </div>
                                                        <div className='resultado'>
                                                            {value[1] === 'Draw' ? translate[lang]['empate'] : `${translate[lang]['vencedor']} ${value[1]}`}
                                                        </div>
                                                    </div>
                                                )})
                                            }
                                        </div>
                                        <div className='valores'>
                                            <div className='valores-text'>
                                                {translate[lang]['montante']}<div className='montante'>{entry.montante}€</div>
                                            </div>
                                            <br/>
                                            <div className='valores-text'>
                                                {translate[lang]['ganhos']}<div className='ganho'>{entry.ganho}€</div>
                                            </div>
                                        </div>
                                    </div>
                                )})
                            }
                        </div>
                    }
                    {btnMultipla && 
                        <div>
                            {multipla.map((entry, index) => {
                                return(
                                    <div key={index} className='entry'>
                                        <div>
                                            {entry.jogo.map((value, index) => {
                                                return(
                                                    <div key={index} className='jogo'>
                                                        <div className='nome-jogo'>
                                                            <h3>{value[0]}</h3>
                                                        </div>
                                                        <div className='resultado'>
                                                            {value[1] === 'Draw' ? translate[lang]['empate'] : `${translate[lang]['vencedor']} ${value[1]}`}
                                                        </div>
                                                    </div>
                                                )})
                                            }
                                        </div>
                                        <div className='valores'>
                                            <div className='valores-text'>
                                                {translate[lang]['montante']}<div className='montante'>{entry.montante}€</div>
                                            </div>
                                            <br/>
                                            <div className='valores-text'>
                                                {translate[lang]['ganhos']}<div className='ganho'>{entry.ganho}€</div>
                                            </div>
                                        </div>
                                    </div>
                                )})
                            }
                        </div>
                    }
                    {empty.control && 
                        <div className='empty-message'>
                            <h3>{empty.msg}</h3>
                        </div>
                    }
                </div>
            </div>
        </div>
    )
}

export default HistoricoApostas
