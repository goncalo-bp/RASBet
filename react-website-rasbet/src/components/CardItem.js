import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from './Button'
import './CardItem.css'

export const CardItem = ({ children,text, label,data, num_buttons, onClick }) => {
    return (
        <>  
            <li className="cards__item">
                    <div className='cards__item__info'>
                        <h1>{label}</h1>
                        <h5 className='cards__item__text'>{text}</h5>
                    </div>
                    <div className='card_buttons'>
                        <Button className='btn--primary--green--medium' onClick={onClick} dest={data}>ola</Button>
                        <Button className='btn--primary--green--medium' onClick={onClick} dest={data}>como</Button>
                        <Button className='btn--primary--green--medium' onClick={onClick} dest={data}>estas</Button>
                    </div>
            </li>
        </>
    )
}