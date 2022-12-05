import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom';
import { Button } from './Button';
import './Navbar.css';
import Popup from './Popup';
import Dropdown from '../Lang_Toogle';

function Navbar() {
    const [click, setClick] = useState(false);
    const [button,setButton] = useState(true);
  
    const [admin, setAdmin] = useState(false);
    const [add_Popup, setAdd_Popup] = useState(false);

    const handleClick = () => setClick(!click);
    const closeMobileMenu = (e) => {
        console.log(e.target);
        var desp = e.target.firstChild.data;
        switch(desp){
            case translate[lang]["desp"][0]:
                localStorage.setItem('desporto',"Futebol");
                e.forceUpdate();
                break;
            case translate[lang]["desp"][1]:
                localStorage.setItem('desporto',"Basquetebol");
                e.forceUpdate();
                break;
            case translate[lang]["desp"][2]:
                localStorage.setItem('desporto',"Tenis");
                e.forceUpdate();
                break;
            case translate[lang]["desp"][3]:
                localStorage.setItem('desporto',"MotoGP");
                e.forceUpdate();
                break;
        }
        setClick(false);
    }
    
    const handleadd = (e) => {
		setAdd_Popup(true);
	}

    const add = () => {
		return (
		<div className='popup-center'>
            Adicionar novo jogo:
            <input type="text" placeholder="Desporto" style={{display: 'none'}}/>
            <input type="text" placeholder="Equipa 1" style={{display: 'none'}}/>
            <input type="text" placeholder="Equipa 2" style={{display: 'none'}}/>
            <Button className='btn--outline--full--orange--large'  >Adicionar Jogo</Button>
		</div>
		);
	}
    
    const showButton = () => {
        if(window.innerWidth <= 1350) {
            setButton(false);
        } else {
            setButton(true);
        }
    };
  
    const logOut = (e) => {
        closeMobileMenu(e);
        localStorage.clear();
        localStorage.setItem('isLogged', false);
    }

    useEffect(() => {
        setAdmin(JSON.parse(localStorage.getItem("isAdmin")))


        showButton();
    }, []);
  
    window.addEventListener('resize', showButton);

    const translate = {
        "pt": {
            "desp" : ["Futebol", "Basquetebol", "Ténis", "MotoGP"],
            "sair" : "Sair",
            "bv" : "Bem vindo",
            "conta" : "Contas",
            "prom" : "Promoções"
        },
        "en": {
            "desp" : ["Football", "Basketball", "Tennis", "MotoGP"],
            "sair" : "Log Out",
            "bv" : "Welcome",
            "conta" : "Accounts",
            "prom" : "Promotions"
        },
        "es": {
            "desp" : ["Fútbol", "Baloncesto", "Tenis", "MotoGP"],
            "sair" : "Cerrar sesión",
            "bv" : "Bienvenido",
            "conta" : "Cuentas",
            "prom" : "Promociones"
        }
    }

    var lang = localStorage.getItem('lang');
  
    return (
        <>
        <Dropdown
        trigger={<button>{localStorage.getItem("lang")}</button>}
        />
        <nav className="navbar">
            
            <div className="navbar-container">
            <Popup trigger={add_Popup} setTrigger={setAdd_Popup}>
                {add()}
                </Popup>
                <div className="navbar-logo">
                    RASBET
                </div>
                <div className='menu-icon' onClick={handleClick}>
                    <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li id="futebol" className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu} >
                            {translate[lang]["desp"][0]}
                        </Link>
                    </li>
                    <li id="tenis" className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                        {translate[lang]["desp"][1]}
                        </Link>
                    </li>
                    <li id="basquetebol" className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                        {translate[lang]["desp"][2]}
                        </Link>
                    </li>
                    <li id="motogp" className='nav-item'>
                        <Link to='/home' className='nav-links' onClick={closeMobileMenu}>
                        {translate[lang]["desp"][3]}
                        </Link>
                    </li>
                    {!admin && <li className='nav-item'>
                        <Link to='/home/edit' className='nav-links' onClick={closeMobileMenu}>
                            {translate[lang]["bv"]} {localStorage.getItem("name")}
                        </Link>
                    </li>}
                    {admin && <li className='nav-item'>
                        <Link to='/home/promocoes' className='nav-links' onClick={closeMobileMenu}>
                            {translate[lang]["prom"]}
                        </Link>
                    </li>}
                    {admin && <li className='nav-item'>
                        <Link to='/home/contas' className='nav-links' onClick={closeMobileMenu}>
                            {translate[lang]["conta"]}
                        </Link>
                    </li>}
                    {!button &&
                    <li className='nav-item'>
                        <Link to='/' className='nav-links-mobile' onClick={logOut}> 
                        {translate[lang]["sair"]}
                        </Link>
                    </li>
                    }
                </ul>
                {button && <Button className='btn--outline--green--large' dest='/' onClick={logOut}>{translate[lang]["sair"]}</Button>}
            </div>
        </nav>
        </>
    )
}

export default Navbar
