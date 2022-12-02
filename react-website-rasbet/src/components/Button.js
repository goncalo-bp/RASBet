import React from 'react'
import './Button.css'

const NAMES = ['btn--primary--medium', 'btn--primary--large',
               'btn--outline--medium', 'btn--outline--large',
               'btn--primary--orange--medium', 'btn--primary--orange--large',
               'btn--outline--orange--medium', 'btn--outline--orange--large',
               'btn--outline--full--orange--medium', 'btn--outline--full--orange--large',
               'btn--active--orange--medium', 'btn--active--orange--large',
               'btn--primary--green--medium', 'btn--primary--green--large',
               'btn--outline--green--medium', 'btn--outline--green--large',
               'btn--primary--gray--medium', 'btn--primary--gray--large',
               'btn--circle--green--small', 'btn--circle--green--tiny',
               'btn--x--gray--medium','btn--primary--white--large',
               'btn--onclick--white--large'
            ]

export const Button = ({ children, onClick, className, dest, id }) => {
    const checkClassName = NAMES.includes(className) ? className : NAMES[0]
    const checkDest = dest ? dest : null
    const checkID = id ? id : null
    return (
        <a id={checkID} href={checkDest} className={checkClassName} onClick={onClick}>{children}</a>
    )
};

