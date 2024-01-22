import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import CustomComponent1 from './components/CustomComponent1';
import CustomComponent2 from './components/CustomComponent2';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './styles/main.css';

function App() {
  return (
    <Router>
      <div id="app-root">
        <Navbar />
        <Switch>
          <Route exact path="/" component={CustomComponent1} />
          <Route path="/feature" component={CustomComponent2} />
          {/* Add additional Routes for other extracted or custom components as needed */}
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;