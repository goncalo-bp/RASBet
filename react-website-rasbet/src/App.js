import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Registo from './components/pages/Registo';

function App() {
  return (
    <>
      <Router>
      <Routes>
        <Route exact path="/"  element={<Registo/>} />
      </Routes> 
      </Router>
    </>
  );
}

export default App;
