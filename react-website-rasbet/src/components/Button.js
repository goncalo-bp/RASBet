import React from 'react'
import './Button.css'
import { Link } from 'react-router-dom';

const STYLES = ['btn--primary', 'btn--outline', 'btn--white','btn--orange']

const SIZES = ['btn--medium', 'btn--large']

const NAMES = ['btn--primary--medium', 'btn--primary--large',
               'btn--outline--medium', 'btn--outline--large',
               'btn--primary--orange--medium', 'btn--primary--orange--large',
               'btn--outline--orange--medium', 'btn--outline--orange--large',
               'btn--primary--green--medium', 'btn--primary--green--large',
               'btn--outline--green--medium', 'btn--outline--green--large',
               'btn--primary--gray--medium', 'btn--primary--gray--large',
               'btn--circle--green--small',
            ]

export const Button = ({ children, type, onClick, className, dest }) => {
    const checkClassName = NAMES.includes(className) ? className : NAMES[0]
    const checkDest = dest ? dest : null
    return (
        <a href={checkDest} className={checkClassName} onClick={onClick}>{children}</a>
    )
};

