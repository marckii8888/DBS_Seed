import React, { useState } from 'react';
import {BrowserRouter as Router, Route, Switch, Redirect} from 'react-router-dom';

import Login from './Login';
import Home from './Home';
import ShoppingCart from './ShoppingCart';

const App = () => {

    const [isLoggedIn, setIsLoggedIn] = useState(false);

    return (
        <div className="ui container">
            <Router>
                <div>
                    <Switch>
                        <Route path="/" exact render={
                            () => isLoggedIn? <Redirect to="/home"/> : <Login path="/login" setIsLoggedIn/>}
                        />
                        <Route path="/home" exact component={Home} />
                        <Route path="/cart" exact component={ShoppingCart} />
                    </Switch>
                </div>
            </Router>
        </div>
    );
};

export default App;