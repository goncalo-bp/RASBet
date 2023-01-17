import { useEffect, useState } from 'react';
import './ListaJogos.css';
import { Button } from './Button';
import Boletim from './Boletim';
import Popup from './Popup';
import Progresso from './Progresso';



export default function ListaJogos() {

    const [jogos, setJogos] = useState([]);
    const [numJogos, setNumJogos] = useState(0);
    const [apostas, setApostas] = useState([]);

    const [admin, setAdmin] = useState(false);
    const [especialista, setEspecialista] = useState(false);
    const [apostador, setApostador] = useState(false);

    const [date, setDate] = useState('');
    const [containsDate, setContainsDate] = useState(false);

    const [search, setSearch] = useState('');
    const [fech_Popup, setFech_Popup] = useState(false);

    const [error, setError] = useState(0); // 0 - incompleto | 1 - mail/pass incorretos
    const [btnPopup, setBtnPopup] = useState(false);

    const [alt_Popup, setAlt_Popup] = useState(false);
    const [abrir_Popup, setAbrir_Popup] = useState(false);
    const [notif_Popup, setNotif_Popup] = useState(false);

    const [infoAltera, setInfoAltera] = useState({});
    const [newOdd, setNewOdd] = useState(0);

    const [infoRemove, setInfoRemove] = useState({});

    const [nomeNovaEquipas, setNomeNovaEquipas] = useState('');
    const [novaDataJogo, setNovaDataJogo] = useState('');
    const [novaHoraJogo, setNovaHoraJogo] = useState('');

    const [res, setRes] = useState("");
    const [popupAdd, setPopupAdd] = useState(false);
    const [idJogo, setIdJogo] = useState('');
    const [percentagem, setPercentagem] = useState(0);

    const [notif, setNotificacoes] = useState([]);
    const [listaObservados, setListaObservados] = useState([]);




    const handlePercentagem = (e) => {
        e.preventDefault();
        setPercentagem(e.target.value);
    };

    const handleIdJogo = (e) => {
        var info = e.target.id;
        setIdJogo(info);
        setPopupAdd(true);
    }

    const handleAddFollow = (e) => {
        var info = e.target.id;
        console.log(info);
        sendNewFollow(info);
    }

    const sendNewFollow = (id_jogo) => {
        fetch('http://localhost:5002/observador/adicionar', {  // Enter your IP address here
                method: 'POST',
                mode: 'cors', 
                body: JSON.stringify({"idUser" : localStorage.getItem("id"), "idJogo" : id_jogo}), // body data type must match "Content-Type" header
                headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
        .then((response) => {
            if (!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
            }).then((data) => {
                window.location.reload();
            })
            .catch(error => {
                console.log("error: ", error);
            });
    }

    const handleRemoveFollow = (e) => {
        var info = e.target.id;
        sendUnfollow(info);
    }

    const sendUnfollow = (id_jogo) => {
        fetch('http://localhost:5002/observador/remover', {  // Enter your IP address here
                method: 'POST',
                mode: 'cors', 
                body: JSON.stringify({"idUser" : localStorage.getItem("id"), "idJogo" : id_jogo}), // body data type must match "Content-Type" header
                headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
        .then((response) => {
            if (!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
            }).then((data) => {
                window.location.reload();
            })
            .catch(error => {
                console.log("error: ", error);
            });
    }

    

    const addProm = (e) => {
        if(percentagem === '') {
            alert(translate[lang]['fill-all-fields']);
            return;
        }
        var perc = percentagem/100;
        fetch('http://localhost:5002/promocoes/adiciona', {  // Enter your IP address here
                    method: 'POST', 
                    mode: 'cors', 
                    body: JSON.stringify({"idJogo" : idJogo , "aumento" : perc}), // body data type must match "Content-Type" header
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
        setPopupAdd(false);
    };

    const handleNovaHoraJogo = (e) => {
        setNovaHoraJogo(e.target.value);
    }

    const handleNovaDataJogo = (e) => {
        setNovaDataJogo(e.target.value);
    }


    const handleNomeNovaEquipas = (e) => {
        setNomeNovaEquipas(e.target.value);
    };

    const handleAlt = (e) => {
        var info = e.target.id;

        var infoArray = info.split("_");
        setInfoAltera(info);
        suspenderJogo(1,infoArray[0]);
    }

    const handleNewOdd = (e) => {
        setNewOdd(e.target.value);
    }

    const handleAbrir = () => {
        setAbrir_Popup(true);
    }

    function checkList(list, id) {
        var bool = false;
        if(list.length === 0){return false;}
        else{
            list.forEach(element => {
            if(element === id) {
                bool = true;
            }
        });}
        return bool;
    }


    function changeColor(missing) {
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
        if (data_act.length === 0)
            for (var i = 0; i < numJogos; i++) {
                if(document.getElementById("M_"+i) !== null)
                    document.getElementById("M_" + i).style.display = "flex";
            }

        else
            for (var i = 0; i < numJogos; i++) {
                if(document.getElementById("Date_"+i) !== null){

                    var jogo = document.getElementById("Date_" + i).textContent;
                    var containsDate = checkDate(data_act, jogo.substring(0, 10));
                    if (containsDate === true) {
                        document.getElementById("M_" + i).style.display = "flex";
                    }
                    else {
                        document.getElementById("M_" + i).style.display = "none";
                    }
                }
            }
    };

    let inputHandler = (e) => {
        //convert input text to lower case
        var valor = e.target.value;
        var lowerCase = String(valor).toLowerCase();
        setInputText(lowerCase);

        for (var i = 0; i < numJogos; i++) {
            if(document.getElementById(i) !== null){
                var game_name = document.getElementById(i).textContent.toLowerCase()
                if (!game_name.includes(lowerCase)) {
                    document.getElementById("M_" + i).style.display = "none";
                }
                else {
                    document.getElementById("M_" + i).style.display = "flex";
                }
            }
        }
    };


    function getJogos(){
        var desporto = localStorage.getItem('desporto');

        fetch('http://localhost:5002/sports/' + desporto, {  // Enter your IP address here
            method: 'GET',
            headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
            .then((response) => {
                if (!response.ok) {
                    throw Error(response.status);
                }
                else return response.json();
            }).then((data) => {
                setJogos(data);
                setNumJogos(data.length);
                localStorage.setItem(desporto, JSON.stringify(data));
            })
            .catch(error => {
                console.log("error: ", error);
            });
    };

    function getListaObservados(){
        fetch('http://localhost:5002/observador/' , {  // Enter your IP address here
            method: 'POST', 
            mode: 'cors', 
            body: JSON.stringify({"idUser" : localStorage.getItem("id")}), // body data type must match "Content-Type" header
            headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
            .then((response) => {
                if (!response.ok) {
                    throw Error(response.status);
                }
                else return response.json();
            }).then((data) => {
                setListaObservados(data.listaObservados);
            })
            .catch(error => {
                console.log("error: ", error);
            });
    };


    useEffect(() => {

        if (localStorage.getItem('isAdmin') === 'true') {
            setAdmin(true);
            document.getElementById("boletim").style.display = "none";
            //document.getElementById("progresso").style.display="none";
        }

        else if (localStorage.getItem("isEspecialista") === 'true') {
            setEspecialista(true);
            document.getElementById("boletim").style.display = "none";
            //document.getElementById("progresso").style.display="flex";
        }
        else {
            setApostador(true);
            document.getElementById("boletim").style.display = "flex";
            getListaObservados();
            //document.getElementById("progresso").style.display="none";
        }

        var desportoAtual = localStorage.getItem('desporto');
        var data = localStorage.getItem(desportoAtual);
        var timestamp = localStorage.getItem('timestamp');

        timestamp = new Date(timestamp);
        var now = new Date();

        if (data === null || data === "" || Math.abs(now - timestamp) > 30000) { // atualiza quando esta a 0 ou quando passam 10 min
            localStorage.setItem('timestamp', new Date());
            getJogos();
        } else {
            setJogos(JSON.parse(localStorage.getItem(desportoAtual)));
            setNumJogos(JSON.parse(localStorage.getItem(desportoAtual)).length);
        }

    }, []);

    function addAposta(id) {
        var new_aposta = apostas.concat(id);
        setApostas(new_aposta);
        return new_aposta;
    }

    function remAposta(id) {
        var new_aposta = apostas.filter(item => item !== id);
        setApostas(new_aposta);
        return new_aposta;
    }

    const handleClickCard = (e) => {
        var id = e.target.id;
        if (id === undefined) {
            id = e.id;
        }
        if (e.target.className === "btn--onclick--white--large") {
            document.getElementById(id).classList.add('btn--onclick');
            document.getElementById(id).classList.remove('btn--onclick--white--large');

            addAposta(id);
        }
        else {
            document.getElementById(id).classList.add('btn--onclick--white--large');
            document.getElementById(id).classList.remove('btn--onclick');

            remAposta(id);
        }
    };

    const concat = (e1, e2) => {
        return e1 + "" + e2;
    }

    const concat2 = (e1, e2) => {
        return e1 + "_" + e2;
    }

    const setToDate = (e) => {
        e.target.type = "date";
    }

    function suspenderJogo(valor,idJogo){
        fetch('http://localhost:5002/jogo/suspender/'+valor, { 
            method: 'POST', 
            mode: 'cors', 
            body: JSON.stringify({"idJogo" : idJogo}), // body data type must match "Content-Type" header
            headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        }).then( (response) => {
            if(!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
        }).then( (data) => {
            if(valor === 1){
                setAlt_Popup(true);
            }
            else{
                setAlt_Popup(false);
                window.location.reload();
            }
        })
        .catch( (error,status) => {
            console.log("error: ",status);
            alert(status);
        });
    }

    function desSuspender(){
        var id = infoAltera.split("_")[0];
        var desporto = localStorage.getItem('desporto');
        localStorage.setItem(desporto, "");
        suspenderJogo(0,id)
    }

    function alertValid_Odd() {
        var id = infoAltera.split("_")[0];
        var equipa = infoAltera.split("_")[1];
        var valor = Number(newOdd);
        if (valor === 0 || valor === "") {
            alert(translate[lang]['insert-value']);
        }
        else {
            var ok = 0;
            ok = fetch('http://localhost:5002/jogo/mudaOdd', {
                method: 'POST', 
                mode: 'cors', 
                body: JSON.stringify({"idJogo" : id , "nomeEquipa" : equipa , "newOdd" : valor}), // body data type must match "Content-Type" header
                headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        
            }).then( (response) => {
                if(!response.ok) {
                    throw Error(response.status);
                }
                else return response.json();
            }).then( (data) => {
                alert(translate[lang]['change-odd']);
            })
            .catch( (error,status) => {
                console.log("error: ",status);
                alert(status);
            });        
            
        }
    }

    document.addEventListener("click", (evt) => {
        const date = document.getElementById("searchDate");
        let targetEl = evt.target; // clicked element      
        do {
            if (targetEl === date) {
                // This is a click inside, does nothing, just return.
                document.getElementById("searchDate").type = "date";
                return;
            }
            // Go up the DOM
            targetEl = targetEl.parentNode;
        } while (targetEl);
        // This is a click outside.      
        if (date !== null && date.value === '')
            document.getElementById("searchDate").type = "text";
    });

    const alterarOdd = (e) => {
        return (
            <div className='popup-center'>
                <div>
                    <h1>{translate[lang]['suspend-game']}</h1>
                    <br />
                    {translate[lang]['insert-new-odd']}
                </div>
                <div>
                    <input id="novaOdd" type="number" onChange={handleNewOdd} placeholder="Odd " />
                </div>
                <br />
                <Button className='btn--outline--full--orange--large' onClick={alertValid_Odd} >Confirmar</Button>
                <Button className='btn--outline--full--orange--large' onClick={desSuspender} >Fechar</Button>
            </div>
        );
    }

    function testValidGame(info_equipas) {
        var res = true;
        info_equipas.map((equipa, index2) => {
            if (equipa.odd === "0.00")
                res = false;
        });
        return res;
    }

    function closeFecharJogo() {
        setFech_Popup(false);
    }

    const handleInfoRemove = (e) => {
        var info = e.target.id;
        setInfoRemove(info);
        setFech_Popup(true);
    }

    function test_Vencedor(){
        for (var i = 0; i < numJogos; i++){
            var jogo = jogos[i];
            if(jogo !== null){
                if(jogo.id === infoRemove){
                    for(var j = 0; j < jogo.equipas.length; j++){
                        if(jogos[i].equipas[j].name === res){
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    function removeJogo(){

        if(test_Vencedor() === false){
            alert(translate[lang]['vencedor-invalido'])
        }
        else{
            fetch('http://localhost:5002/jogo/fechar', {  // Enter your IP address here
                    method: 'POST', 
                    mode: 'cors', 
                    body: JSON.stringify({"idJogo" : infoRemove , "vencedor" : res}), // body data type must match "Content-Type" header
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
        }
    }

    function adicionaJogo() {
        var equipas = document.getElementById("nomeEquipas").value;
        var data = document.getElementById("dataJogo").value;
        var hora = document.getElementById("horaJogo").value;

        if(equipas === "" || data === "" || hora === ""){
            alert(translate[lang]['preencha-todos-campos']);
        }
        else if((data - new Date())<0){
            alert(translate[lang]['preencha-todos-campos']);
        }
        else{
            equipas = equipas.split(",");
            var desporto = localStorage.getItem('desporto');
            fetch('http://localhost:5002/sports/' + desporto + '/addJogo', {  // Enter your IP address here
                    method: 'POST', 
                    mode: 'cors', 
                    body: JSON.stringify({"equipas" : equipas, "data" : data,"hora" : hora }), // body data type must match "Content-Type" header
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
            setAbrir_Popup(false);
        }
    }

    const handleRes = (e) =>{
        setRes(e.target.value);
    }

    const fechar = () => {
        return (
            <div className='popup-center'>
                {translate[lang]['close-game-question']}
                <br />
                <br />
                <input
                        onChange={handleRes}
                        id="result"
                        type="text"
                        value={res}
                        placeholder={translate[lang]['result']}
                        />
            <div>
                    <Button onClick={removeJogo} className='btn--outline--full--orange--large'  >{translate[lang]['sim']}</Button>
                    <Button onClick={closeFecharJogo} className='btn--outline--full--orange--large'  >{translate[lang]['nao']}</Button>
                </div>
            </div>
        );
    }

    const abrir = () => {
		return (
		<div className='popup-center'>
            {translate[lang]['add-jogo']}
            <br/>
            <br/>
            <input id="nomeEquipas" type="text" onChange={handleNomeNovaEquipas} placeholder={translate[lang]['equipas']+':'}  />
            <input
                        onChange={handleNovaDataJogo}
                        id="dataJogo"
                        type="text"
                        value={novaDataJogo}
                        placeholder={translate[lang]['chose-date']}
                        onClick={setToDate}
            />
            <input type="time" id="horaJogo" name="appt" onChange={handleNovaHoraJogo} required></input>
            <br/>
            <br/>
			<Button onClick={adicionaJogo} className='btn--outline--full--orange--large'  >{translate[lang]['confirmar']}</Button>
        </div>
        );
    }

    const handleNotif = () => {
        fetch('http://localhost:5002/notificacoes', {  // Enter your IP address here
                method: 'POST',
                mode: 'cors', 
                body: JSON.stringify({"idConta" : localStorage.getItem("id")}), // body data type must match "Content-Type" header
                headers: {"Content-Type": "application/json", 'Authorization': 'Bearer ' + localStorage.getItem('token'),}
        })
        .then((response) => {
            if (!response.ok) {
                throw Error(response.status);
            }
            else return response.json();
            }).then((data) => {
                setNotificacoes(data);
                setNotif_Popup(true);
            })
            .catch(error => {
                console.log("error: ", error);
            });
    }



    const notificacoes = () => {
        return (
            <div className='popup-notif'>
                {translate[lang]['notif']}
                {
                notif.map((notificacao) => {
                    return (
                        <div className='popup-center'>
                            <br/>
                            <h1>{notificacao.titulo}</h1>
                            {notificacao.texto}
                            
                        </div>
                    );
                })
                }
            </div>
        )
    }

    var lang = localStorage.getItem('lang');
	const translate = {
		'pt': {
            'jogos': 'Jogos',
            'add-jogo': 'Adicionar Jogo',
            'data': 'Data',
            'chose-date': 'Escolha uma data',
            'pesquisar': 'Pesquisar',
            'add-promo' : 'Adicionar Promoção',
            'percentagem' : 'Percentagem',
            'insert-odd' : 'Insira a odd',
            'notif' : 'Notificações',
            'equipas' : 'Equipas',
            'confirmar' : 'Confirmar',
            'result' : 'Resultado',
            'sim' : 'Sim',
            'nao' : 'Não',
            'close-game-question' : 'Deseja fechar o jogo?',
            'data-invalida' : 'Data inválida',
            'preencha-todos-campos' : 'Preencha todos os campos',
            'vencedor-invalido' : 'Vencedor inválido',
            'suspended-game' : 'Jogo suspenso',
            'insert-new-odd' : 'Por favor, insira uma nova odd:',
            'insert-value' : 'Insira um valor',
            'fill-all-fields' : 'Preencha todos os campos!',
            'change-odd' : 'Odd alterada com sucesso',
		},
		'en': {
            'jogos': 'Games',
            'add-jogo': 'Add Game',
            'data': 'Date',
            'chose-date': 'Choose a date',
            'pesquisar': 'Search',
            'add-promo' : 'Add Promotion',
            'percentagem' : 'Percentage',
            'insert-odd' : 'Insert the odd',
            'notif' : 'Notifications',
            'equipas' : 'Teams',
            'confirmar' : 'Confirm',
            'result' : 'Result',
            'sim' : 'Yes',
            'nao' : 'No',
            'close-game-question' : 'Do you want to close the game?',
            'data-invalida' : 'Invalid date',
            'preencha-todos-campos' : 'Fill all fields',
            'vencedor-invalido' : 'Invalid winner',
            'suspended-game' : 'Suspended game',
            'insert-new-odd' : 'Please, insert a new odd:',
            'insert-value' : 'Insert a value',
            'fill-all-fields' : 'Fill all fields!',
            'change-odd' : 'Odd changed successfully',
		},
		'es': {
            'jogos': 'Juegos',
            'add-jogo': 'Añadir Juego',
            'data': 'Fecha',
            'chose-date': 'Elija una fecha',
            'pesquisar': 'Buscar',
            'add-promo' : 'Añadir Promoción',
            'percentagem' : 'Porcentaje',
            'insert-odd' : 'Inserte la odd',
            'notif' : 'Notificaciones',
            'equipas' : 'Equipos',
            'confirmar' : 'Confirmar',
            'result' : 'Resultado',
            'sim' : 'Sí',
            'nao' : 'No',
            'close-game-question' : '¿Quieres cerrar el juego?',
            'data-invalida' : 'Fecha inválida',
            'preencha-todos-campos' : 'Rellene todos los campos',
            'vencedor-invalido' : 'Ganador inválido',
            'suspended-game' : 'Juego suspendido',
            'insert-new-odd' : 'Por favor, inserte una nueva odd:',
            'insert-value' : 'Inserte un valor',
            'fill-all-fields' : 'Rellene todos los campos!',
            'change-odd' : 'Odd cambiada con éxito',
		}
	}

    return (
        <div className="edit-fundo">
            <form className='edit-content-boletim'>
                <Button className='btn--notif' onClick={handleNotif}>{translate[lang]['notif']}</Button>
                <Popup trigger={notif_Popup} setTrigger={setNotif_Popup}>
                    {notificacoes()}
                </Popup>
                <Popup trigger={alt_Popup} setTrigger={setAlt_Popup}>
                    {alterarOdd()}
                </Popup>
                <div className='edit-lista-jogos'>
                    <Popup trigger={fech_Popup} setTrigger={setFech_Popup}>
                        {fechar()}
                    </Popup>
                    <Popup trigger={abrir_Popup} setTrigger={setAbrir_Popup}>
                        {abrir()}
                    </Popup>
                    <span className='filters'>
                        <span>
                            <a>{translate[lang]['pesquisar']}: </a>
                            <input
                                id="search"
                                type="text"
                                value={inputText}
                                onChange={inputHandler}
                                placeholder={translate[lang]['pesquisar']}
                            />
                        </span>
                        <span>
                            <a>{translate[lang]['data']}: </a>
                            <input
                                onChange={handleDate}
                                id="searchDate"
                                type="text"
                                value={date}
                                placeholder={translate[lang]['chose-date']}
                                onClick={setToDate}
                            />
                        </span>
                        {admin && <span>
                            <Button onClick={handleAbrir} className='btn--outline--full--orange--large' >{translate[lang]['add-jogo']}</Button>
                        </span>}
                    </span>
                    <br />
                    <ul id="edit-lista-jogo">
                        {jogos.map((jogo, index1) => {
                            if (especialista || admin || testValidGame(jogo.equipas)) {
                                return (
                                    <li id={"M_" + index1} className='edit-tipo-jogo' key={index1}>
                                        <div className='jogo-container'>
                                            <div id='nome-jogo'>
                                            <Popup trigger={popupAdd} setTrigger={setPopupAdd}>
                                                    <div className='popup-container'>
                                                        <div className='popup-title'>
                                                            <h1>{translate[lang]['add-promo']}</h1>
                                                        </div>
                                                        <div className='popup-form'>
                                                            <form>
                                                                <div className='form-group'>
                                                                    <label>{translate[lang]['percentagem']}: </label>
                                                                    <input onChange={handlePercentagem} type='number' className='form-control' placeholder={translate[lang]['perccentagem']} />
                                                                </div>
                                                                <div className='add-group'>
                                                                    <Button className={'btn--circle--green--small'} onClick={addProm}><i className="fa-solid fa-plus" ></i></Button>
                                                                </div>
                                                            </form>
                                                        </div>
                                                    </div>
                                                </Popup>
                                                {admin && <Button id={jogo.id} onClick={handleIdJogo} className='btn--x--gray--remove--jogo'>%</Button>}
                                                <div id={index1}>{jogo.nome}</div>
                                                <div id={index1+"_id"} style={{display: 'none'}}>{jogo.id}</div>
                                                <div id={'Date_'+index1} className='edit-tipo-data'>
                                                    {jogo.date} {jogo.hour}
                                                </div>
                                                {apostador && checkList(listaObservados,jogo.id) &&  <Button id={jogo.id} onClick={handleRemoveFollow} className='btn--primary--green--medium'>Seguido</Button>}
                                                {apostador && !checkList(listaObservados,jogo.id) && <Button id={jogo.id} onClick={handleAddFollow} className='btn--primary--green--medium'>Seguir</Button>}
                                            </div>
                                            <div className='resultados-container'>
                                            {jogo.equipas.map((equipa,index2) => {
                                                return (
                                                    <span key={index2}>
                                                        {especialista ? 
                                                            <div id={concat(index1,index2)} className='btn--onclick--white--large'>
                                                                <div id={index1+index2+"_N"}>{equipa.name}</div> <br/> 
                                                                {equipa.odd === "0.00" ?
                                                                    <Button id={concat2(jogo.id,equipa.name)} onClick={handleAlt} className='btn--inserir--odd' >{translate[lang]['insert-odd']}</Button>
                                                                    :
                                                                    <Button id={concat2(jogo.id,equipa.name)} onClick={handleAlt} className='btn--inserir--odd' >{equipa.odd}</Button>
                                                                }
                                                            </div>
                                                            :  
                                                            <Button id={concat(index1,index2)} onClick={handleClickCard} className='btn--onclick--white--large'>
                                                                {equipa.name} <br/>{equipa.odd}
                                                            </Button>
                                                        }
                                                    </span>
                                                )})}
                                            </div>
                                        </div>
                                        {admin && <Button id={jogo.id} onClick={handleInfoRemove} className='btn--x--gray--remove--jogo'>x</Button>}
                                    </li>
                                )
                            }
                        })}
                    </ul>
                </div>
            </form>
            <Boletim id="boletim" apostas={apostas} func={handleClickCard} />
        </div>
    );
}