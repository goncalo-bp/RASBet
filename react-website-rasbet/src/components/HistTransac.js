import React, { useEffect, useState } from 'react'
import { Button } from './Button'
import '../App.css'
import './HistTransac.css'
import Table from "./Table";

function HistoricoTransacao() {
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

    const getHistorico = (e) => {
        //e.preventDefault();
        fetch('http://localhost:5002/transactions', {  // Enter your IP address here
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(toJson(localStorage.getItem('id'))),
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
    }, []);

    var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
            'hist-trans' : 'Histórico de Transações',
            'saldo' : 'Saldo',
		},
		'en': {
            'hist-trans' : 'Transaction History',
            'saldo' : 'Balance',
		},
		'es': {
            'hist-trans' : 'Historial de transacciones',
            'saldo' : 'Saldo',
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
                    <h1 className='title-text'>{translate[lang]['hist-trans']}</h1>
                </div>
                <br/>
                <h2>{translate[lang]['saldo']} : {localStorage.getItem('wallet')}€</h2>
                <br/>
                <div className='table-container'>
                    <Table tableData={tableData}/>
                </div>
            </div>
        </div>
    )
}

export default HistoricoTransacao
