import { useEffect, useState } from 'react';
import './ListaJogos.css';
import { Button } from './Button';
import Boletim from './Boletim';
import Progresso from './Progresso';
import Popup from './Popup';



export default function ListaJogos() {

    const [jogos,setJogos] = useState([]);
    const [apostas, setApostas] = useState([]);
    const [countMissingOdd, setCountMissingOdd] = useState(0);
    
    const [admin, setAdmin] = useState(false);
    const [especialista, setEspecialista] = useState(false);

    const [date, setDate] = useState('');
    const [containsDate, setContainsDate] = useState(false);

    const [search, setSearch] = useState('');
    const [fech_Popup, setfech_Popup] = useState(false);

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

    function checkDate(d1, d2) {
        var bool;
        //if (d1 === '') {
        //    setContainsDate(true);
        //}
        //if (d1.length === 4) {
        //    d1 === d2.substring(0, 4) ? 
        //    setContainsDate(true) : 
        //    setContainsDate(false);
        //}
        //if (d1.length === 7) {
        //    d1.substring(0, 4) === d2.substring(0, 4) && 
        //    d1.substring(5, 7) === d2.substring(5, 7) ? 
        //    setContainsDate(true) : 
        //    setContainsDate(false);
        //}
        if (d1.length === 10) {
            d1.substring(0, 4) === d2.substring(0, 4) && 
            d1.substring(5, 7) === d2.substring(5, 7) &&
            d1.substring(8, 10) === d2.substring(8, 10) ? 
            bool = true : 
            bool = false;
        }

        return bool;
    }

    let handleDate = (e) => {
        var data_act = e.target.value;
        setDate(data_act);

        for(var i = 0; i < jogos.length; i++){
            var jogo = document.getElementById("Date_"+i).textContent;
            var containsDate = checkDate(data_act, jogo.substring(0,10));
            if (containsDate === true) {
                document.getElementById("M_"+i).style.display="flex";
            }
            else {
                document.getElementById("M_"+i).style.display="none";
            }
        }
    };

    let inputHandler = (e) => {
        //convert input text to lower case
        var valor = e.target.value;
        var lowerCase = String(valor).toLowerCase();
        setInputText(lowerCase);

        for(var i = 0; i < jogos.length; i++){
            var game_name = document.getElementById("Date_"+i).textContent.toLowerCase()
            if(!game_name.includes(lowerCase)){
                document.getElementById("M_"+i).style.display="none";
            }
            else {
                document.getElementById("M_"+i).style.display="flex";
            }
        }
    };

    const handleMissingOdd = (e) => {
        if(e === null){
            setCountMissingOdd(countMissingOdd+1);
        }
    }

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
            setAdmin(true);
            document.getElementById("boletim").style.display="none";
            document.getElementById("progresso").style.display="none";
        }

        else if (localStorage.getItem("isEspecialista") === 'true') {
            setEspecialista(true);
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
        } else {
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

    const setToDate = (e) => {
        e.target.type="date";
    }

    const handlefech = (e) => {
		setfech_Popup(true);
	}

    document.addEventListener("click", (evt) => {
        const date = document.getElementById("searchDate");
        let targetEl = evt.target; // clicked element      
        do {
          if(targetEl === date) {
            // This is a click inside, does nothing, just return.
            document.getElementById("searchDate").type = "date";
            return;
          }
          // Go up the DOM
          targetEl = targetEl.parentNode;
        } while (targetEl);
        // This is a click outside.      
        if(date.value==='') 
            document.getElementById("searchDate").type = "text";
      });

      const fechar = () => {
		return (
		<div className='popup-center'>
            Deseja fechar o jogo?
            <div>
			<Button className='btn--outline--full--orange--large'  >Sim</Button>
            <Button className='btn--outline--full--orange--large'  >Não</Button>
            </div>
		</div>
		);
	}

    return (
        <div className="edit-fundo">
            <form className='edit-content-boletim'>
                <div className='edit-lista-jogos'>
                <Popup trigger={fech_Popup} setTrigger={setfech_Popup}>
					{fechar()}
                    </Popup>
                <span className='filters'>
                    <span>
                        <a>Nome: </a>
                        <input
                        id="search"
                        type="text"
                        value={inputText}
                        onChange={inputHandler}
                        placeholder="Pesquisar"
                        />
                    </span>
                    <span>
                        Data:
                        <input
                        onChange={handleDate}
                        id="searchDate"
                        type="text"
                        value={date}
                        placeholder="Escolha uma data"
                        onClick={setToDate}
                        />
                    </span>
                </span>
                    <ul id="edit-lista-jogo">
                        {jogos.map((jogo,index1) => {
                            return (
                                <li id={"M_"+index1} className='edit-tipo-jogo'>
                                    <div className='jogo-container'>
                                        <div id='nome-jogo'>
                                            <div id={index1}>{jogo.nome}</div> 
                                            <div id={'Date_'+index1} className='edit-tipo-data'>
                                                {jogo.date} {jogo.hour}
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
                                    {especialista && <div id='missingOdds' className='edit-tipo-missing-odds'></div>}
                                    {admin && <Button onClick={handlefech} className='btn--x--gray--small'>x</Button>}
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