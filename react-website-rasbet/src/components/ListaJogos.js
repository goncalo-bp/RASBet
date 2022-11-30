import { useEffect, useState } from 'react';
import Popup from './Popup';
import './ListaJogos.css';
import { Button } from './Button';


export default function ListaJogos() {

    const [jogos,setJogos] = useState([]);
    const [equipa, setEquipa] = useState(0);
    const [odd, setOdd] = useState(0);
    const [data, setData] = useState(1);
    const [hour, setHour] = useState(1);
    const [id, setId] = useState(1);
    
    function toJson(id) {
		return { "id": id}
	}

    const handleData = (e) => {
        setData(e.target.value);
    };

    
    const handleListaJogos= (e) => {
        handleData(e.date);
        for (var i = 0; e[`equipa${i}`] != undefined; i++){
            setEquipa(e[`equipa${i}`].name);
            setOdd(e[`odd${i}`].odd);
        }
    };

    const getHistorico = (e) => {
        //e.preventDefault(); // TODO - mudar para qualquer nome do desporto
        fetch('http://localhost:5002/sports/Futebol', {  // Enter your IP address here
            method: 'GET',
        })
        .then((response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then((data) => {
            console.log(data);
            setJogos(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };


    useEffect(() => {
        getHistorico();
    }, []);

return (
<div className="edit-fundo">
    <form className='edit-content-boletim'>
        <div className='edit-lista-jogos'>
            <div className='edit-lista-jogo'>
                {jogos.map((jogo,index) => {
                    return (
                    <div className='edit-tipo-jogo'>
                        <span>{jogo.nome} {/* ! temos de ir buscar a API} */}
                        <div className='edit-tipo-data'><span>{jogo.date} {jogo.hour}</span>
                        </div> 
                        </span>
                        {jogo.equipas.map((equipa,index) => {return (
                        <span><Button className='btn--primary--white--large'>{equipa.name} {equipa.odd}</Button></span>)})}
                    </div>)
                })}
            </div>
        </div>
    </form> 
</div>
);
}