import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistTransac.css'
import Table from "./Table";

function HistoricoTransacao() {
    const [saldo, setSaldo] = useState(0);
    const [id, setId] = useState(1); //TODO - ir buscar o id do utilizador
    const [tableData, setTableData] = useState([]);
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

    const handleSaldo = (e) => {
        setSaldo(100.00);
        //setSaldo(e.target.value);
    };

    const getHistorico = (e) => {
        //e.preventDefault();
        fetch('http://localhost:5002/transactions', {  // Enter your IP address here
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
            setTableData(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    useEffect(() => {
        getHistorico();
        handleSaldo();
    }, []);

    return (
        <div className='container'>
            <div className='box-container'>
                <div className='title-container'>
                    <div className='back'>
                        {button && <Button dest='/home/edit' className={'btn--circle--green--small'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                        {!button && <Button dest='/home/edit' className={'btn--circle--green--tiny'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                    </div>
                    <h1 className='title-text'>Histórico de Transações</h1>
                </div>
                <br/>
                <h2>Saldo : {saldo}€</h2>
                <br/>
                <div className='table-container'>
                    <Table tableData={tableData}/>
                </div>
            </div>
        </div>
    )
}

export default HistoricoTransacao
