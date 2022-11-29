import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from './Button'
import './CardItem.css'

export const CardItem = ({ children,text, equipas,data,hora, onClick }) => {
    var hoje = new Date();
    var data = new Date(data);
    
    const isToday = (someDate) => {
        const today = new Date()
        return someDate.getDate() == today.getDate() &&
          someDate.getMonth() == today.getMonth() &&
          someDate.getFullYear() == today.getFullYear()
    }
      
    const buttons = (equipas) => {
        return equipas.map((item) => {
            var [a,b] = item
            console.log(a,b)
            return <Button buttonStyle='btn--outline' onClick={onClick}>{a}{b}</Button>
        })
    }
    const desc = isToday(data) ? 'Hoje' : data.toLocaleDateString('pt-PT', { year: 'numeric', month: 'numeric', day: 'numeric' })    
    return (
        <>  
            <li className="cards__item">
                    <div className='cards__item__info'>
                        <h1>{text}</h1>
                        <h5 className='cards__item__text'>{desc} {hora}</h5>
                    </div>
                    <div className='card_buttons'>
                        {buttons(equipas)}
                    </div>
            </li>
        </>
    )
}