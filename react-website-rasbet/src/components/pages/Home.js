import React from 'react';
import '../../App.css';
import HeroSection from '../HeroSection';
import Navbar from '../Navbar';
import Boletim from '../Boletim';
import ListaJogos from '../ListaJogos';
import './Home.css';

function Home() {
  return (
    <>
      <Navbar />
      <div className="edit-pagina-inicial">
        <div className="edit-jogos">
          <ListaJogos />
        </div>
      </div>
    </>
  );
}

export default Home;