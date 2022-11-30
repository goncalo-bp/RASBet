import { useState } from 'react';
import Popup from './Popup';
import './ListaJogos.css';
import { Button } from './Button';

export default function Form_L() {

    const [jogo, setJogo] = useState(0);
    const [, setId] = useState(1); //TODO - ir buscar o id do utilizador
    const [tableData, setTableData] = useState([]);
    
    function toJson(id) {
		return { "id": id}
	}

    const handleTableData = (e) => {
        setTableData(current => [...current, e]);
    };

    const getHistorico = (e) => {
        //e.preventDefault();
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
            for (var i = 0; data[`jogo${i}`] != undefined; i++) {
                //handleTableData(data[`jogo${i}`]);
            }
        })
        .catch(error => {
            console.log("error: ", error);
        });
    };



return (
<div className="edit-fundo">
	<form className='edit-content-boletim'>
		<div className='edit-lista-jogos'>
			<div className='edit-lista-jogo'>
				<div className='edit-tipo-jogo'>
					<span>Sporting - Varzim
                    <div className='edit-tipo-data'><span>20/11/2022 16:00</span>
                    </div> 
                    </span>
					<span><Button className='btn--primary--white--large'>Sporting 1.98</Button></span>
					<span><Button className='btn--primary--white--large'>Empate 3.20</Button></span>
					<span><Button className='btn--primary--white--large'>Varzim 5.60</Button></span>
				</div>
            </div>
		</div>
	</form>
</div>
);
}