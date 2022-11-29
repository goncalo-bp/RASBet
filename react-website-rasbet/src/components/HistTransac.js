import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistTransac.css'
import Table from "./Table";

function HistoricoTransacao() {
    const [saldo, setSaldo] = useState(0);
    const [id, setId] = useState(1); //TODO - ir buscar o id do utilizador
    const [tableData, setTableData] = useState([]);
    
    function toJson(id) {
		return { "id": id}
	}

    const handleSaldo = (e) => {
        setSaldo(100.00);
        //setSaldo(e.target.value);
    };

    const handleTableData = (e) => {
        setTableData(current => [...current, e]);
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
            for (var i = 0; data[`transaction${i}`] != undefined; i++) {
                handleTableData(data[`transaction${i}`]);
            }
            console.log(tableData);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };

    useEffect(() => {
        setTableData([]);
        getHistorico();
        handleSaldo();
    }, []);

    return (
        <div className='container'>
            <div className='box-container'>
                <div className='title-container'>
                    <div className='back'>
                        <Button dest='/home/edit' className={'btn--circle--green--small'}><i className="fa-solid fa-arrow-left" ></i></Button>
                    </div>
                    <h1 className='title-text'>Histórico de Transações</h1>
                </div>
                <br/>
                <h2>Saldo : {saldo}€</h2>
                <br/>
                <Table tableData={tableData}/>
            </div>
        </div>
    )
}

export default HistoricoTransacao
