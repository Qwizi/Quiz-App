import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="wrapper">
        <header className="page-header">
            <h1>Quiz App</h1>
        </header>
      <main className="main">
          <div className="welcome">
              <form className="nick-form">
                  <label htmlFor="nick" className="label">Wpisz swoj nick</label>
                  <input type="text" id="nick" name="nick" placeholder="Nick" className="nick"/>
                  <button className="btn btn--ok">OK</button>
              </form>
          </div>
      </main>
        <fotter className="page-footer">
            Created by Qwizi & Poftorek
        </fotter>
    </div>
  );
}

export default App;
