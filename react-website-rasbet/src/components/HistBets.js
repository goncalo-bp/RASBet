import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistBets.css'
import Table from "./Table";

function HistoricoApostas() {
    const [id, setId] = useState(1); //TODO - ir buscar o id do utilizador
    const [tableData, setTableData] = useState([]);
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
            //setTableData(data);
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
            //setTableData(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    useEffect(() => {
        getSimples();
        getMultiplas();
    }, []);

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
                        <Button className='btn--outline--full--orange--large'>
                            Simples
                        </Button>
                        <Button className='btn--outline--full--orange--large'>
                            Múltiplas
                        </Button>
                    </div>
                </span>
                <div className='table-container'>
                    
                </div>
            </div>
        </div>
    )
}

export default HistoricoApostas
