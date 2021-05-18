import React, { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import * as d3 from "d3";
import './index.css';
//import App from './App';
import reportWebVitals from './reportWebVitals';

const data = [
  {
    x: "Melbourne",
    y: 320
  },
  {
    x: "Sydney",
    y: 200
  },
  {
    x: "Brisbane",
    y: 25
  },
  {
    x: "Perth",
    y: 190
  },
  {
    x: "Adelaide",
    y: 90
  }
];

const margin = {
  top: 20,
  right: 0,
  bottom: 30,
  left: 40
};

const WIDTH = 450;
const HEIGHT = 400;

function Bar() {
  const chartWidth = WIDTH - margin.left - margin.right;
  const chartHeight = HEIGHT - margin.top - margin.bottom;

  const [value, setValue] = useState(() => data.map(d => ({ ...d, y: 0 })));
  const svgRef = useRef(null);

  useEffect(() => {
    const t = d3.transition().duration(1000);

    t.tween("height", () => {
      let interpolates = data.map((d, i) => {
        let start = (value[i] && value[i].y) || 0;
        return d3.interpolateNumber(start, d.y);
      });
      return t => {
        let newData = data.map((d, i) => {
          return { ...d, y: interpolates[i](t) };
        });

        setValue(newData);
      };
    });
  }, []);

  const xScale = d3
    .scaleBand()
    .domain(data.map(d => d.x))
    .range([0, chartWidth])
    .paddingInner(0.3)
    .paddingOuter(0.4)
    .round(true);

  const bandwidth = xScale.bandwidth();

  const yScale = d3
    .scaleLinear()
    .domain([0, d3.max(data.map(d => d.y))])
    .range([chartHeight, 0])
    .nice();

  return (
    <svg width={WIDTH} height={HEIGHT} ref={svgRef}>
      <linearGradient id="linear-gradient" x1={0} x2={0} y1={1} y2={0}>
        <stop offset="0%" stopColor="#16a3ff" />
        <stop offset="100%" stopColor="#6ddead" />
      </linearGradient>
      {/* x轴 */}
      <g
        className="x-axis"
        transform={`translate(${margin.left},${HEIGHT - margin.bottom})`}
      >
        {/* 轴线 */}
        <line x1={0} y1={0} x2={chartWidth} y2={0} stroke={"#000"} />

        {/* 轴标签*/}
        <g className="tick">
          {data.map((d, i) => {
            let x = xScale(d.x) + bandwidth / 2;
            return (
              <g key={i}>
                {/* 轴刻度 */}
                <line x1={x} x2={x} y1={0} y2={6} stroke={"#000"} />
                {/* 轴标签文本 */}
                <text x={x} y={20} fontSize={12} textAnchor={"middle"}>
                  {d.x}
                </text>
              </g>
            );
          })}
        </g>
      </g>

      {/* y轴 */}
      <g
        className="y-axis"
        transform={`translate(${margin.left},${margin.top})`}
      >
        <line x1={0} y1={0} x2={0} y2={chartHeight} stroke={"#000"} />
        <g className="tick">
          {yScale.ticks(10).map((d, i) => {
            let y = yScale(d);

            return (
              <g key={i} transform={`translate(0, ${y})`}>
                <line x1={0} x2={-6} y1={0} y2={0} stroke={"#000"} />
                <text
                  x={-12}
                  y={0}
                  dy={"0.32em"}
                  fontSize={12}
                  textAnchor={"end"}
                >
                  {d}
                </text>
              </g>
            );
          })}
        </g>
      </g>

      {/* 柱子 */}
      <g
        transform={`translate(${margin.left}, ${margin.top})`}
        fill={"url(#linear-gradient)"}
      >
        {value.map((d, i) => {
          let x = xScale(d.x);
          let y = yScale(d.y);
          let height = chartHeight - y;

          return (
            <g key={i}>
              <rect x={x} y={y} width={bandwidth} height={height} />
              <text
                x={x + bandwidth / 2}
                y={y - 4}
                fontSize={12}
                textAnchor={"middle"}
              >
                {d.y.toFixed(0)}
              </text>
            </g>
          );
        })}
      </g>
    </svg>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Bar />, rootElement);

  /*
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
