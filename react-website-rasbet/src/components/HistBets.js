import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistBets.css'
import Table from "./Table";

function HistoricoApostas() {
    const [id, setId] = useState(1); //TODO - ir buscar o id do utilizador

    const [simples, setSimples] = useState([]);
    const [multipla, setMultipla] = useState([]);

    const [btnSimples, setBtnSimples] = useState(false);
    const [btnMultipla, setBtnMultipla] = useState(false);

    const [empty, setEmpty] = useState({control : false});

    const [nome, setNome] = useState("Carlos Pereira");

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
		return { "id": id}
	}

    const getSimples = (e) => {
        //e.preventDefault();
        fetch('http://localhost:5002/apostas/simples', {  // Enter your IP address here
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(toJson(id)),
            headers: {"Content-Type": "application/json"}
        })
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setSimples(data);
            {data.length === 0 ? setEmpty({control : true, msg : 'Ainda não fez apostas simples.'}) : setEmpty({control : false})}
            {data.length > 0 ? setBtnSimples(true) : setBtnSimples(false)}
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    const getMultiplas = (e) => {
        //e.preventDefault();
        fetch('http://localhost:5002/apostas/multipla', {  // Enter your IP address here
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(toJson(id)),
            headers: {"Content-Type": "application/json"}
        })
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setMultipla(data);
            {data.length === 0 ? setEmpty({control : true, msg : 'Ainda não fez apostas múltiplas.'}) : setEmpty({control : false})}
            {data.length ? setBtnMultipla(true) : setBtnMultipla(false)}
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    const handleSimples = (e) => {
        getSimples();
        setBtnMultipla(false);
    };

    const handleMultipla = (e) => {
        getMultiplas();
        setBtnSimples(false);
    };

    return (
        <div className='container'>
            <div className='box-container'>
                <div className='title-container'>
                    <div className='back'>
                        {button && <Button dest='/home/edit' className={'btn--circle--green--small'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                        {!button && <Button dest='/home/edit' className={'btn--circle--green--tiny'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                    </div>
                    <h1 className='title-text'>{nome}</h1>
                </div>
                <br/>
                <h2>Histórico de Apostas</h2>
                <br/>
                <span>
                    <div className='bet-type'>
                        {button &&
                        <>
                        <Button className='btn--outline--full--orange--large' onClick={handleSimples}>
                            Simples
                        </Button>
                        <Button className='btn--outline--full--orange--large' onClick={handleMultipla}>
                            Múltiplas
                        </Button>
                        </>
                        }
                        {!button &&
                        <>
                        <Button className='btn--outline--full--orange--medium' onClick={handleSimples}>
                            Simples
                        </Button>
                        <Button className='btn--outline--full--orange--medium' onClick={handleMultipla}>
                            Múltiplas
                        </Button>
                        </>
                        }
                    </div>
                </span>
                <br/>{button && <br/>}
                <div className='bets-container'>
                    {btnSimples && 
                        <div className='entry'>
                            <div>
                                {simples.jogo.map((value, index) => {
                                    return(
                                        <div className='jogo'>
                                            <a className='nome-jogo'>
                                                <h3>{value[0]}</h3>
                                            </a>
                                            <a className='resultado'>
                                                {value[1] == 'Draw' ? `Resultado: Empate` : `Vencedor: ${value[1]}`}
                                            </a>
                                        </div>
                                    )})
                                }
                            </div>
                            <div className='valores'>
                                <div className='valores-text'>
                                    Montante Apostado: <a className='montante'>{simples.montante}€</a>
                                </div>
                                <br/>
                                <div className='valores-text'>
                                    Total de banhos: <a className='ganho'>{simples.ganho}€</a>
                                </div>
                            </div>
                        </div>
                    }
                    {btnMultipla && 
                        <div>
                            {multipla.map((entry, index) => {
                                return(
                                    <div className='entry'>
                                        <div>
                                            {entry.jogo.map((value, index) => {
                                                return(
                                                    <div className='jogo'>
                                                        <a className='nome-jogo'>
                                                            <h3>{value[0]}</h3>
                                                        </a>
                                                        <a className='resultado'>
                                                            {value[1] == 'Draw' ? `Resultado: Empate` : `Vencedor: ${value[1]}`}
                                                        </a>
                                                    </div>
                                                )})
                                            }
                                        </div>
                                        <div className='valores'>
                                            <div className='valores-text'>
                                                Montante apostado: <a className='montante'>{entry.montante}€</a>
                                            </div>
                                            <br/>
                                            <div className='valores-text'>
                                                Total de ganhos: <a className='ganho'>{entry.ganho}€</a>
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
