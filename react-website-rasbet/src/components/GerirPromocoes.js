import React, { useEffect, useState } from 'react';
import './GerirContas.css';
import { Button } from './Button';
import Popup from './Popup';



export default function GerirContas() {
    const [promocoes, setPromocoes] = useState([]);
    const [button, setButton] = useState(true);
    const [popupAdd, setPopupAdd] = useState(false);
    const [popupRem, setPopupRem] = useState(false);


    const [idProm, setIdProm] = useState('');
    const [idJogo, setIdJogo] = useState('');
    const [percentagem, setPercentagem] = useState('');


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
        /*
        fetch('http://localhost:5002/contas', {get: 'POST',})
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setContas(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
        */
        setPromocoes([
            {
                'idProm' : 'Conta 1',
                'idJogo' : 'Administrador',
                'percentagem' : '20',
            },
            {
                'idProm' : 'Conta 2',
                'idJogo' : 'Administrador',
                'percentagem' : '20',
            },
            {
                'idProm' : 'Conta 3',
                'idJogo' : 'Administrador',
                'percentagem' : '20',
            },
            {
                'idProm' : 'Conta 4',
                'idJogo' : 'Administrador',
                'percentagem' : '20',
            },
        ]);
    };

    const handlePopupAdd = () => {
        setPosition('admin');
        setPopupAdd(true);
    };

    const handlePopupRem = () => {
        setPosition('admin');
        setPopupRem(true);
    };

    const handleIdPromocao = (e) => {
        e.preventDefault();
        setNome(e.target.value);
    };

    const handleIdJogo = (e) => {
        e.preventDefault();
        setEmail(e.target.value);
    };

    const handlePercentagem = (e) => {
        e.preventDefault();
        setPosition(e.target.value);
    };


    const addProm = (e) => {
        // TODO confirmar padrao email se for preciso
        if(idProm === '' || idJogo === '' || percentagem === '') {
            alert("Preencha todos os campos!");
            return;
        }
        setPopupAdd(false);
        // TODO adicionar conta com query do flask
    };

    const removePromocao = (e) => {
        // TODO remover conta com query do flask
        setPopupRem(false);
    };

    const removePopupRem = (e) => {
        setPopupRem(false);
    };

    useEffect(() => {
        getContas();
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
                {contas.map((conta, index) => {
                    return (
                        <div className='entry-container'>
                            <div className='account-info'>
                                <a>{conta.nome} ({conta.position})</a>
                            </div>
                            <div className='delete-button'>
                                <Button onClick={removeConta} className={'btn--circle--green--small'}><i className="fa-solid fa-trash" ></i></Button>
                            </div>
                        </div>
                    );
                })}
                </div>
                <br/>
                <div className='add-button'>
                    <Popup trigger={popup} setTrigger={setPopup}>
                        <div className='popup-container'>
                            <div className='popup-title'>
                                <h1>Adicionar Conta</h1>
                            </div>
                            <div className='popup-form'>
                                <form>
                                    <div className='form-group'>
                                        <label>Nome: </label>
                                        <input onChange={handleNome} type='text' className='form-control' placeholder='Nome' />
                                    </div>
                                    <div className='form-group'>
                                        <label>E-mail: </label>
                                        <input onChange={handleEmail} type='email' className='form-control' placeholder='E-mail' />
                                    </div>
                                    <div className='form-group'>
                                        <label>Posição: </label>
                                        <select onChange={handlePosition} className='form-control'>
                                            <option value='admin'>Administrador</option>
                                            <option value='especialista'>Especialista</option>
                                        </select>
                                    </div>
                                    <div className='form-group'>
                                        <label>Palavra-passe: </label>
                                        <input onChange={handlePassword} type='password' className='form-control' placeholder='Palavra-passe' />
                                    </div>
                                    <div className='form-group'>
                                        <label>Confirmar Palavra-passe: </label>
                                        <input onChange={handleConfirmPassword} type='password' className='form-control' placeholder='Confirmar Palavra-passe' />
                                    </div>
                                    <div className='add-group'>
                                        <Button className={'btn--circle--green--small'} onClick={addConta}><i className="fa-solid fa-plus" ></i></Button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </Popup>
                    <Button className={'btn--circle--green--medium'} onClick={showForm} >Adicionar Conta</Button>
                </div>
            </div>
        </div>
    );
}