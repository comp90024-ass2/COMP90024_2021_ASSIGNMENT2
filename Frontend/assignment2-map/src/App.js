import React from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import "./App.css";
import Happy from "./components/map/Happy";
import Income from "./components/map/Income";
import Unemployment from "./components/map/Unemployment";
import Spent from "./components/map/Spent";

import BarHappy from "./components/barchart/BarHappy";
import BarIncome from "./components/barchart/BarIncome";
import BarUnemployment from "./components/barchart/BarUnemployment";
import BarSpent from "./components/barchart/BarSpent";

function App() {
  return (
    <Router>
        <div>
            <nav id="chart">
                <ul>
                    <li>
                        <label>Bar Chart: </label>
                    </li>
                    <li>
                        <Link to="/happiness">Happiness</Link>
                    </li>
                    <li>
                        <Link to="/income">Income</Link>
                    </li>
                    <li>
                        <Link to="/unemployment">Unemployment</Link>
                    </li>
                    <li>
                        <Link to="/incomeCo">gini_coefficient_no</Link>
                    </li>
                    <li>
                        <label>Map: </label>
                    </li>
                    <li>
                        <Link to="/h-map">Happiness</Link>
                    </li>
                    <li>
                        <Link to="/i-map">Income</Link>
                    </li>
                    {/* <li>
                        <Link to="/u-map">Unemployment</Link>
                    </li>
                    <li>
                        <Link to="/s-map">Spent</Link>
                    </li> */}
                </ul>
            </nav>

            {/* A <Switch> looks through its children <Route>s and
        renders the first one that matches the current URL. */}
            <Switch>
                <Route path="/happiness">
                    <div>
                        <p className="attempt-1"><em>Happiness percentage</em></p>
                        <br></br>
                        <BarHappy />
                    </div>
                </Route>
                <Route path="/income">
                    <div>
                        <p className="attempt-1"><em>Income level</em></p>
                        <br></br>
                        <BarIncome />
                    </div>
                </Route>
                <Route path="/unemployment">
                    <div>
                        <p className="attempt-1"><em>Unemployment percentage</em></p>
                        <br></br>
                        <BarUnemployment />
                    </div>
                </Route>
                <Route path="/incomeCo">
                    <div>
                        <p className="attempt-1"><em>gini coefficient no</em></p>
                        <br></br>
                        <BarSpent />
                    </div>
                </Route>
                <Route path="/h-map">
                    <Happy />
                </Route>
                <Route path="/i-map">
                    <Income />
                </Route>
                <Route path="/u-map">
                    <Unemployment />
                </Route>
                <Route path="/s-map">
                    <Spent />
                </Route>
            </Switch>
        </div>
    </Router>
  );
}

export default App;
