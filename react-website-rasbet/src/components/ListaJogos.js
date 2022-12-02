import { useEffect, useState } from 'react';
import './ListaJogos.css';
import { Button } from './Button';
import Boletim from './Boletim';
import Progresso from './Progresso';



export default function ListaJogos() {

    const [jogos,setJogos] = useState([]);
    const [apostas, setApostas] = useState([]);
    const [countMissingOdd, setCountMissingOdd] = useState(0);
    
    const [admin, setAdmin] = useState(false);

    const handleMissingOdd = (e) => {
        if(e === null){
            setCountMissingOdd(countMissingOdd+1);
        }
    }

    function changeColor(missing){
        if (missing === 0)
            document.getElementById('missingOdds').style.backgroundColor = "green";
        if (missing === 1)
            document.getElementById('missingOdds').style.backgroundColor = "yellow";
        if (missing === 2)
            document.getElementById('missingOdds').style.backgroundColor = "yellow";
        if (missing === 3)
            document.getElementById('missingOdds').style.backgroundColor = "red";
    }

    const [inputText, setInputText] = useState("");

    let inputHandler = (e) => {
        console.log(e.target);
        //convert input text to lower case
        var valor = e.target.value;
        var lowerCase = String(valor).toLowerCase();
        setInputText(lowerCase);

        for(var i = 0; i < jogos.length; i++){
            var game_name = document.getElementById(i).textContent.toLowerCase()
            if(!game_name.includes(lowerCase)){
                document.getElementById("M_"+i).style.display="none";
            }
            else {
                document.getElementById("M_"+i).style.display="flex";
            }
        }
    };


    const getJogos = (e) => {
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
            localStorage.setItem('jogos', JSON.stringify(data));
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };


    useEffect(() => {

        if(localStorage.getItem('isAdmin') === 'true') {
            document.getElementById("boletim").style.display="none";
            document.getElementById("progresso").style.display="none";
        }

        else if (localStorage.getItem("isEspecialista") === 'true') {
            document.getElementById("boletim").style.display="none";
            document.getElementById("progresso").style.display="flex";
        }
        else {
            document.getElementById("boletim").style.display="flex";
            document.getElementById("progresso").style.display="none";
        }

        



        var data = localStorage.getItem('jogos');
        var timestamp =  localStorage.getItem('timestamp');
    
        timestamp = new Date(timestamp);
        var now = new Date();

        if(data === "" || Math.abs(now - timestamp) > 600000) { // atualiza quando esta a 0 ou quando passam 10 min
            localStorage.setItem('timestamp', new Date());
            getJogos();
        }else{
            setJogos(JSON.parse(localStorage.getItem('jogos')));
        }
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
        console.log(e);
        var id = e.target.id;
        console.log(id);
        if (id === undefined){
            id = e.id;
        }
        if(e.target.className === "btn--onclick--white--large"){
            document.getElementById(id).classList.add('btn--onclick');
            document.getElementById(id).classList.remove('btn--onclick--white--large');
            
            addAposta(id);
        
        }
        else {
            console.log("ola");
            document.getElementById(id).classList.add('btn--onclick--white--large');
            document.getElementById(id).classList.remove('btn--onclick');

            remAposta(id);

        }
        
        
    };

    const concat = (e1,e2) =>{
       return e1 + "" + e2;
    }


return (
<div className="edit-fundo">
    <form className='edit-content-boletim'>
        <div className='edit-lista-jogos'>
        <input
        id="search"
        type="text"
        value={inputText}
        onChange={inputHandler}
        placeholder="Pesquisar"
        />
            <ul id="edit-lista-jogo">
                {jogos.map((jogo,index1) => {
                    return (
                        <li id={"M_"+index1} className='edit-tipo-jogo'>
                            <div className='jogo-container'>
                                <div id='nome-jogo'>
                                    <div id={index1}>{jogo.nome}</div> 
                                    <div className='edit-tipo-data'>
                                        {jogo.date}
                                        {jogo.hour}
                                    </div> 
                                </div>
                                <div className='resultados-container'>
                                {jogo.equipas.map((equipa,index2) => {
                                    {handleMissingOdd(equipa.odd)}
                                    return (
                                        <span>
                                            <Button id={concat(index1,index2)} onClick={handleClickCard} className='btn--onclick--white--large'>
                                                {equipa.name} <br/>{equipa.odd}
                                            </Button>
                                        </span>
                                    )})}
                                </div>
                            </div>
                            <Button className='btn--x--gray--medium'>x</Button>
                            <div id='missingOdds' className='edit-tipo-missing-odds'>
                                
                            </div>
                        {admin && <Button className='btn--x--gray--medium'>x</Button>}
                        </li>
                    )
                })}
            </ul>
        </div>
    </form> 
    <Boletim id="boletim" apostas={apostas} func={handleClickCard}/>
    <Progresso id="progresso" apostas={apostas} func={handleClickCard}/>
</div>
);
}