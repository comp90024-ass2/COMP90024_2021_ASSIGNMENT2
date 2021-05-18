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

const WIDTH = 450;
const HEIGHT = 400;
const margin = {
  top: 20,
  right: 0,
  bottom: 30,
  left: 40
};
const COLORS = ["#16a3ff", "#6ddead", "#5edfff", "#3e64ff", "#505bda"];

const normalStyle = {
  cursor: "pointer",
  opacity: 1,
  transform: "scale(1)",
  transition: "all linear 200ms"
};

const hoverStyle = {
  transform: "scale(1.1)"
};

const noHoverStyle = {
  opacity: 0.5
};

function Pie() {
  const chartWidth = WIDTH - margin.left - margin.right;
  const chartHeight = HEIGHT - margin.top - margin.bottom;

  const [value, setValue] = useState(0);
  const [active, setActive] = useState(null);

  useEffect(() => {
    const transition = d3.transition().duration(1000);

    transition.tween("height", () => {
      return t => {
        setValue(t);
      };
    });
  }, []);

  const pieRadius = d3.min([chartWidth, chartHeight]) / 2;

  let pie = d3
    .pie()
    .sort(null)
    .value(d => d.y);
  let pieData = pie(data);

  let arc = d3
    .arc()
    .innerRadius(0) // 如果想要实现环图，修改这里的半径参数即可
    .outerRadius(pieRadius);

  return (
    <svg width={WIDTH} height={HEIGHT}>
      <g
        transform={`translate(${margin.left + pieRadius},${margin.top +
          pieRadius})`}
      >
        {pieData.map((d, i) => {
          let arcGen = arc
            .startAngle(d.startAngle * value)
            .endAngle(d.endAngle * value);

          let style =
            active != null
              ? active === i
                ? { ...normalStyle, ...hoverStyle }
                : { ...normalStyle, ...noHoverStyle }
              : normalStyle;
          return (
            <g
              key={i}
              style={style}
              onMouseEnter={() => setActive(i)}
              onMouseLeave={() => setActive(null)}
            >
              <path
                d={arcGen()}
                fill={COLORS[i % COLORS.length]}
                stroke="#fff"
              />
            </g>
          );
        })}

        {pieData.map((d, i) => {
          let arcGen = arc
            .startAngle(d.startAngle * value)
            .endAngle(d.endAngle * value);

          let center = arcGen.centroid();
          let style =
            active != null
              ? active === i
                ? { ...normalStyle, ...hoverStyle }
                : { ...normalStyle, ...noHoverStyle }
              : normalStyle;
          return (
            <g
              key={i}
              style={style}
              onMouseEnter={() => setActive(i)}
              onMouseLeave={() => setActive(null)}
            >
              <text
                fontSize={16}
                fill="#fff"
                textAnchor="middle"
                x={center[0]}
                y={center[1]}
              >
                {d.data.x}:{d.value}
              </text>
            </g>
          );
        })}
      </g>
    </svg>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Pie />, rootElement);


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
