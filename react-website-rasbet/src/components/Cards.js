import React from 'react'
import {CardItem} from './CardItem'

function Cards() {
    return (
        <div className='cards'>
            <h1>Eventos Desposrtivos</h1>
            <div className="cards__container">
                <div className="cards__wrapper">
                    <ul className="cards__items">
                        <CardItem text="Benfica - Porto"
                        data='2022/11/29'
                        hora='19:30'
                        equipas={[['Benfica','1.50'],['Empate','3.50'],['Porto','2.50']]}
                        />
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default Cards