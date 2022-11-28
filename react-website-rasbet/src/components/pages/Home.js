import React from 'react';
import '../../App.css';
import Cards from '../Cards';
import HeroSection from '../HeroSection';
import Navbar from '../Navbar';

function Home() {
  return (
    <>
      <Navbar />
      {/*<HeroSection />  EXEMPLO DE BOTOES*/}
      <Cards />
    </>
  );
}

export default Home;