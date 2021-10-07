import React from 'react';
import ReactDOM from 'react-dom';
import {Route, BrowserRouter as Router, Switch} from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import './index.css';

const routing = (
    <Router>
        <React.StrictMode>
            {/* adding the header component */}
            <Header/>
            {/* accessing app component on ' / ' route path */}
            <Switch>
                <Route exact path="/"  component={App}/>
            </Switch>
            {/* adding the footer component */}
            <Footer/>
        </React.StrictMode>
    </Router>
);

// adding routing variable / component into the React DOM
ReactDOM.render(routing, document.getElementById('root'));
