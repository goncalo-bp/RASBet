import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom';
import { Button } from './Button';
import './Navbar.css';


function Navbar() {
    const [click, setClick] = useState(false);
    const [button,setButton] = useState(true);
  
    const handleClick = () => setClick(!click);
    const closeMobileMenu = (e) => {
        var desp = e.target.firstChild.data;
        switch(desp){
            case "Home":
                localStorage.setItem('desporto',"");
                break;
            case "Futebol":
                localStorage.setItem('desporto',"Futebol");
                break;
            case "Basquetebol":
                localStorage.setItem('desporto',"Basquetebol");
                break;
            case "Ténis":
                localStorage.setItem('desporto',"Tenis");
                break;
            case "MotoGP":
                localStorage.setItem('desporto',"MotoGP");
                break;
        }
        setClick(false);
    }    
    
    const showButton = () => {
        if(window.innerWidth <= 1000) {
            setButton(false);
        } else {
            setButton(true);
        }
    };
  
    const logOut = () => {
        closeMobileMenu();
        localStorage.clear();
        localStorage.setItem('isLogged', false);
    }

    useEffect(() => {
        showButton();
    }, []);
  
    window.addEventListener('resize', showButton);
  
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/home" className="navbar-logo" onClick={closeMobileMenu}>
                    RASBET
                </Link>
                <div className='menu-icon' onClick={handleClick}>
                    <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                            Home
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                            Futebol
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                            Ténis
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                            Basquetebol
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                            MotoGP
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/home/edit' className='nav-links' onClick={closeMobileMenu}>
                            Conta
                        </Link>
                    </li>
                    {!button &&
                    <li className='nav-item'>
                        <Link to='/' className='nav-links-mobile' onClick={logOut}> 
                            Sair
                        </Link>
                    </li>
                    }
                </ul>
                {button && <Button className='btn--outline--green--large' dest='/' onClick={logOut}>Sair</Button>}
            </div>
        </nav>
    )
}

export default Navbar
