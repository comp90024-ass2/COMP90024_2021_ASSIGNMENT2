import React from "react";
import "./App.css";
import Happy from "./components/Happy";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import BarHappy from "./components/BarHappy";
import BarIncome from "./components/BarIncome";
import BarUnemployment from "./components/BarUnemployment";
import BarSpent from "./components/BarSpent";

function App() {
  return (
    <Router>
        <div>
            <nav>
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
                        <Link to="/spent">Spent</Link>
                    </li>
                    <li>
                        <label>Map: </label>
                    </li>
                    <li>
                        <Link to="/map">Map</Link>
                    </li>
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
                <Route path="/spent">
                    <div>
                        <p className="attempt-1"><em>Average spent</em></p>
                        <br></br>
                        <BarSpent />
                    </div>
                </Route>
                <Route path="/map">
                    <Happy />
                </Route>
            </Switch>
        </div>
    </Router>
  );
}

export default App;
