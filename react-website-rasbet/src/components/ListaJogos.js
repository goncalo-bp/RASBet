import { useEffect, useState } from 'react';
import Popup from './Popup';
import './ListaJogos.css';
import { Button } from './Button';
import Boletim from './Boletim';


export default function ListaJogos() {

    const [jogos,setJogos] = useState([]);
    const [equipa, setEquipa] = useState(0);
    const [odd, setOdd] = useState(0);
    const [data, setData] = useState(1);
    const [hour, setHour] = useState(1);
    const [id, setId] = useState(1);
    const [apostas, setApostas] = useState([]);
    
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
            setJogos(data);
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };


    useEffect(() => {
        getHistorico();
    }, []);

    function addAposta(id){
        var new_aposta = apostas.concat(id);
        setApostas(new_aposta);
        return new_aposta;
    }

    function remAposta(id){
        var new_aposta = apostas.filter(item => item !== id);
        setApostas(new_aposta);
        return new_aposta;
    }

    const handleClickCard = (e) => {
        var id = e.target.id
        if(e.target.className === "btn--onclick--white--large"){
            document.getElementById(id).classList.add('btn--onclick');
            document.getElementById(id).classList.remove('btn--onclick--white--large');
            
            var new_apostas = addAposta(id);

        
        }
        else {
            document.getElementById(id).classList.add('btn--onclick--white--large');
            document.getElementById(id).classList.remove('btn--onclick');

            var new_apostas = remAposta(id);

        }
        
        
    };

    const concat = (e1,e2) =>{
       return e1 + "" + e2;
    }

    //const getApostasSelect = () => {
    //    var apostas = [];
    //    if(jogos !== []){
//
    //        jogos.map((jogo,index1) => {
    //            jogos.equipas.map((equipa,index2) => {
    //                var id = concat(index1,index2);
    //                if(document.getElementById(id).className === "btn--onclick"){
    //                    apostas.push(id);
    //                }
    //            })
    //        })
    //        
    //    }
    //    return apostas;
    //}

return (
<div className="edit-fundo">
    <form className='edit-content-boletim'>
        <div className='edit-lista-jogos'>
            <div className='edit-lista-jogo'>
                {jogos.map((jogo,index1) => {
                    return (
                    <div className='edit-tipo-jogo'>
                        <span><div id={index1}>{jogo.nome}</div> {/* ! temos de ir buscar a API} */}
                        <div className='edit-tipo-data'><span>{jogo.date} {jogo.hour}</span>
                        </div> 
                        </span>
                        {jogo.equipas.map((equipa,index2) => {return (
                        <span><Button id={concat(index1,index2)} onClick={handleClickCard} className='btn--onclick--white--large'>{equipa.name} {equipa.odd}</Button></span>)})}
                    </div>)
                })}
            </div>
        </div>
    </form> 
    <Boletim apostas={apostas} func={handleClickCard}/>
</div>
);
}