import React, { useEffect, useState } from 'react';
import './GerirContas.css';
import { Button } from './Button';
import Popup from './Popup';
//
//
//
export default function GerirContas() {
    const [promocoes, setPromocoes] = useState([]);
    const [button, setButton] = useState(true);

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

    const getPromocoes = (e) => {
        //e.preventDefault();
        
        fetch('http://localhost:5002/promocoes', {
            get: 'POST',
            headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            setPromocoes(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
        
    };

    const removePromocao = (e) => {
        var idPromo = e.target.id;
        console.log(idPromo);
        fetch('http://localhost:5002/promocoes/remove', {  // Enter your IP address here
            method: 'POST', 
            mode: 'cors', 
            body: JSON.stringify({"idPromo" : idPromo}), // body data type must match "Content-Type" header
            headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        }).then( (response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then( (data) => {
            var desporto = localStorage.getItem('desporto');
            localStorage.setItem(desporto, "");
            window.location.reload();
        })
        .catch( (error,status) => {
            console.log("error: ",status);
            alert(status);
        });
    };

    useEffect(() => {
        getPromocoes();
    }, []);

    return (
        <div className='container'>
            <div className='box-container'>
                <div className='title-container'>
                    <div className='back'>
                        {button && <Button dest='/home' className={'btn--circle--green--small'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                        {!button && <Button dest='/home' className={'btn--circle--green--tiny'}><i className="fa-solid fa-arrow-left" ></i></Button>}
                    </div>
                    <h1 className='title-text'>Gerir Promoções</h1>
                </div>
                <div className='accounts-container'>
                {promocoes.map((promocao, index) => {
                    return (
                        <div key={index} className='entry-container'>
                            <div className='account-info'>
                                <a>{promocao.nome} ({promocao.aumento}) </a>
                            </div>
                            <div className='delete-button'>
                                <Button id={promocao.idPromo} onClick={removePromocao} className={'btn--circle--green--small'}><i id={promocao.idPromo} className="fa-solid fa-trash" ></i></Button>
                            </div>
                        </div>
                    );
                })}
                </div>
                <br/>
            </div>
        </div>
    );
}