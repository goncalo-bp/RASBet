import React from 'react';
import '../../App.css';
import Navbar from '../Navbar';
import Boletim from '../Boletim';
import ListaJogos from '../ListaJogos';
import './Home.css';

function Home() {
  return (
    <>
    {localStorage.getItem('isLogged') === 'true' ?
      <>
      <Navbar />
        <div className="edit-pagina-inicial">
          <div className="edit-jogos">
            <ListaJogos />
          </div>
        </div>
      </>
      :
      window.location.replace('http://localhost:3000/')
    }
    </>
  );
}

export default Home;