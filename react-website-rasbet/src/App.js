import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Registo from './components/pages/Registo';
import Login from './components/pages/Login';
import Home from './components/pages/Home';
import Edit from './components/pages/Edit';

function App() {
  return (
    <>
      <Router>
      <Routes>
        <Route exact path="/"  element={<Login/>} />
        <Route exact path="/sign-up"  element={<Registo/>} />
        <Route exact path="/home"  element={<Home/>} />
        <Route exact path="/home/edit"  element={<Edit/>} />
      </Routes> 
      </Router>
    </>
  );
}

export default App;
