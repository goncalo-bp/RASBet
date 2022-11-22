import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import { Button } from './Button';
import './Navbar.css';


function Navbar() {
  const [click, setClick] = useState(false);
  const [button,setButton] = useState(true);

  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  const showButton = () => {
    if(window.innerWidth <= 960) {
      setButton(false);
    } else {
      setButton(true);
    }
  };

  window.addEventListener('resize', showButton);

  return (
    <>
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-logo">
                    RASBET
                </Link>
                <div className='menu-icon' onClick={handleClick}>
                    <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li className='nav-item'>
                        <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                            Home
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/jogos' className='nav-links' onClick={closeMobileMenu}>
                            Jogos
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/desportos' className='nav-links' onClick={closeMobileMenu}>
                            Desportos
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/sign-up' className='nav-links-mobile' onClick={closeMobileMenu}>
                            Registar
                        </Link>
                    </li>
                </ul>
                {button && <Button buttonStyle='btn--outline'>Sign UP</Button>}
            </div>
        </nav>
    </>
  )
}

export default Navbar
