import React, { useState, useEffect, useRef } from "react";
import * as d3 from "d3";
import './BarChart.css';
import request from '../../utils/request'

const margin = {
    top: 20,
    right: 50,
    bottom: 30,
    left: 100
};

const WIDTH = 800;
const HEIGHT = 300;

const data = [
    {
        x: "Greater Melbourne",
        y: 12
    },
    {
        x: "Greater Sydney",
        y: 15
    },
    {
        x: "Greater Brisbane",
        y: 20
    },
    {
        x: "Greater Perth",
        y: 13
    },
    {
        x: "Greater Adelaide",
        y: 13
    }
];

const data2 = () => request.post('/unemployment/_find', {
	"selector": {
       
    },
    "fields": ["gccsa_name_2016", "unemp_rt_15"],
    "limit": 10,
    "skip": 0,
    "execution_stats": true
})

function BarUnemployment() {
    const chartWidth = WIDTH - margin.left - margin.right;
    const chartHeight = HEIGHT - margin.top - margin.bottom;

    const [value, setValue] = useState(() => data.map(d => ({ ...d, y: 0 })));
    const svgRef = useRef(null);

    useEffect(() => {
        
        data2().then(response => {
            const t = d3.transition().duration(1000);
            let data3 = []
            response.data.docs.forEach(element => {

                data3.push({
                    x: element.gccsa_name_2016,
                    y: element.unemp_rt_15
                })
            });

            t.tween("height", () => {
                let interpolates = data3.map((d, i) => {
                    let start = (value[i] && value[i].y) || 0;
                    return d3.interpolateNumber(start, d.y);
                });
                return t => {
                    let newData = data3.map((d, i) => {
                        return { ...d, y: interpolates[i](t) };
                    });

                    setValue(newData);
                };
            });

            
        }).catch((err) =>{
            console.log(err)
          })

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
        .domain([0, 12])
        .range([chartHeight, 0])
        .nice();

    return (
        <svg width={WIDTH} height={HEIGHT} ref={svgRef}>
            <linearGradient id="linear-gradient" x1={0} x2={0} y1={1} y2={0}>
                <stop offset="0%" stopColor="#16a3ff" />
                <stop offset="100%" stopColor="#6ddead" />
            </linearGradient>
            {/* x-axis */}
            <g
                className="x-axis"
                transform={`translate(${margin.left},${HEIGHT - margin.bottom})`}
            >
                {/* axis line */}
                <line x1={0} y1={0} x2={chartWidth} y2={0} stroke={"#000"} />

                {/* axis title */}
                <g className="tick">
                    {data.map((d, i) => {
                        let x = xScale(d.x) + bandwidth / 2;
                        return (
                            <g key={i}>
                                {/* axis value */}
                                <line x1={x} x2={x} y1={0} y2={6} stroke={"#000"} />
                                {/* axis title name */}
                                <text x={x} y={20} fontSize={12} textAnchor={"middle"}>
                                    {d.x}
                                </text>
                            </g>
                        );
                    })}
                </g>
            </g>

            {/* y axis */}
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

            {/* bars */}
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
                                {d.y}
                            </text>
                        </g>
                    );
                })}
            </g>
        </svg>
    );
}

export default BarUnemployment;

