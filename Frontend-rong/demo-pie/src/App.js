import React, { useEffect } from 'react';
import './App.css';
import draw from './draw'
function App() {
  useEffect(() => {
    draw()
  })
  return (
    <div className="APP">
      <h1>D3 Simple Bar Chart</h1>
      <div id="chart-container"></div>
    </div>
  );
}
export default App;