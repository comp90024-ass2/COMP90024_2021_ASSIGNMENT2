import React, { Component } from 'react';
import './App.css';

import ChoroplethMap from './components/ChoroplethMap';

class App extends Component {
  state = {
    data: [
      ["AU", 75], ["JB", 43], ["NT", 50], ["WA", 88], ["CT", 21], ["NS", 43],
      ["SA", 21], ["VI", 19], ["QL", 60], ["CT", 60], ["TS", 60]],
  }
  render() {
    return (
      <div style={{
        height:"100vh",
        width: "100vw"
      }}>
        <ChoroplethMap data={this.state.data}/>
      </div>
    );
  }
}

export default App;
