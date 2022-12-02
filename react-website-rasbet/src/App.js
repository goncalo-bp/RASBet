import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Registo from './components/pages/Registo';
import Login from './components/pages/Login';
import Home from './components/pages/Home';
import Edit from './components/pages/Edit';
import Levantar from './components/pages/Levantar';
import Depositar from './components/pages/Depositar';
import Historico from './components/pages/Historico';
import Apostas from './components/pages/Apostas';


function App() {
  return (
    <>
      <Router>
      <Routes>
        <Route exact path="/"  element={<Login/>} />
        <Route exact path="/sign-up"  element={<Registo/>} />
        <Route exact path="/home"  element={<Home/>} />
        <Route exact path="/home/edit"  element={<Edit/>} />
        <Route exact path="/home/levantar"  element={<Levantar/>} />
        <Route exact path="/home/depositar"  element={<Depositar/>} />
        <Route exact path="/home/historico"  element={<Historico/>} />
        <Route exact path="/home/apostas"  element={<Apostas/>} />
      </Routes> 
      </Router>
    </>
  );
}

export default App;
