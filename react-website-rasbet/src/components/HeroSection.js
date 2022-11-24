import React from 'react'
import '../App.css'
import { Button } from './Button'
import './HeroSection.css'

function HeroSection() {
  return (
    <div className='hero-container'>
        <video src="/public/perfil.png" autoPlay loop muted />
        <h1>Olá, eu sou o chinoca fodido</h1>
        <p>Suiiiiiiiii</p>
        <Button className='btns' buttonStyle='btn--outline'
        buttonSize='btn--large'>
            Começar</Button>

            <Button className='btns' 
            buttonStyle='btn--primary'
            buttonSize='btn--large'>
            merdas <i className='far fa-play-circle'/>
            </Button>
    </div>
  )
}

export default HeroSection