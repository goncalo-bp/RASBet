import React from 'react';
import './Lang_Toogle.css';

const Dropdown = ({ trigger}) => {
    const [open, setOpen] = React.useState(false);
  
    const handleOpen = () => {
      setOpen(!open);
    };

    const handleClick = (e) => {
        var lang = e.target.firstChild.data;
        console.log(localStorage);
        localStorage.setItem('lang',lang);
        window.location.reload();
    }

    const menu = () => {
        return (
        <>
        <li key={"pt"} className="menu-item">
        <button onClick={handleClick}>pt</button>
        </li>
        <li key={"eng"} className="menu-item">
        <button onClick={handleClick}>en</button>
        </li>
        <li key={"es"} className="menu-item">
        <button onClick={handleClick}>es</button>
        </li>
        </>
        );
    }
    return (
      <div className="dropdown">
        {React.cloneElement(trigger, {
          onClick: handleOpen,
        })}
        {open ? (
          <ul className="menu">
            {menu()}
          </ul>
        ) : null}
      </div>
    );
  };

export default Dropdown;