import React from 'react'
import './Button.css'
import { Link } from 'react-router-dom';

const STYLES = ['btn--primary', 'btn--outline', 'btn--white','btn--orange']

const SIZES = ['btn--medium', 'btn--large']

export const Button = ({ children, type, onClick, buttonStyle, buttonSize, dest }) => {
    const checkButtonStyle = STYLES.includes(buttonStyle) ? buttonStyle : STYLES[0]
    const checkButtonSize = SIZES.includes(buttonSize) ? buttonSize : SIZES[0]
    const checkDest = dest ? dest : '/sign-up'
    return (
        <Link to={checkDest}>
            <button
            className={`btn ${checkButtonStyle} ${checkButtonSize}`}
            onClick={onClick}>
                {children}
            </button>
        </Link>
    )
};

