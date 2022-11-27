import React from 'react'
import '../App.css'
import { Button } from './Button'
import './HeroSection.css'

function HeroSection() {
  return (
    <div className='hero-container'>
      <h1>EXEMPLOS DE BOTÕES</h1>
      <Button dest="/" className="btn--primary--large">Começar</Button>
      <br/>
      <Button dest="/" className="btn--outline--medium">Começar</Button>
      <br/>
      <Button dest="/" className="btn--primary--orange--medium">Começar</Button>
      <br/>
      <Button dest="/" className="btn--outline--orange--large">Começar</Button>
      <br/>
      <Button dest="/" className="btn--primary--green--large">Começar</Button>
      <br/>
      <Button dest="/" className="btn--outline--green--medium">Começar</Button>
      <br/>
      <Button dest="/" className="btn--primary--medium">Merdas <i className='far fa-play-circle'/></Button>
    </div>
  )
}

export default HeroSection