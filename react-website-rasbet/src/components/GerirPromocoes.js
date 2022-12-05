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
    const [popupRem, setPopupRem] = useState(false);


    const [idProm, setIdProm] = useState('');
    const [idJogo, setIdJogo] = useState('');
    const [percentagem, setPercentagem] = useState(0);


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
        
        fetch('http://localhost:5002/promocoes', {get: 'POST',})
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setPromocoes(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
        
    };


    const handlePopupRem = () => {
        setPopupRem(true);
    };

    const handleIdPromocao = (e) => {
        e.preventDefault();
        setIdProm(e.target.value);
    };


    

    const removePromocao = (e) => {
        // TODO remover conta com query do flask
        setPopupRem(false);
    };

    const removePopupRem = (e) => {
        setPopupRem(false);
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
                        <div className='entry-container'>
                            <div className='account-info'>
                                <a>{promocao.nome} ({promocao.aumento}) </a>
                            </div>
                            <div className='delete-button'>
                                <Button onClick={removePromocao} className={'btn--circle--green--small'}><i className="fa-solid fa-trash" ></i></Button>
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