import * as d3 from 'd3'
async function draw () {
  const width = 800
  const height = 500
  const marginTop = 30
  const marginRight = 30
  const marginBottom = 30
  const marginLeft = 50
  const numOfCountries = 10
  const title = "COVID-19 Death Count"
  const svg = d3.select('#chart-container')
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('background-color', '#D3D3D3')

  svg.append('text')
    .attr('x', (marginLeft + width + marginRight) / 2)
    .attr('y', marginTop / 2)
    .attr('dy', '0.33em')
    .text(title)
    .attr('text-anchor', 'end')
  const dawData = await d3.csv('http://127.0.0.1:8080/covid-data.csv')
  const data = dawData.filter(d => d.date === "2020-04-11" && d.location !== "World").sort((a, b) => b.new_deaths - a.new_deaths).filter((d, i) => i < numOfCountries).map(d => ({date: d.date, location: d.location, new_deaths: +d.new_deaths}))
  console.log(data)
  const xScale = d3.scaleBand()
    .domain(data.map(d => d.location))
    .range([marginLeft, width - marginRight])
    .padding(0.3)
  const xAxis = d3.axisBottom()
    .scale(xScale)

  svg.append('g')
    .attr('transform', 'translate(0,' + (height - marginBottom) + ')')
    .call(xAxis)

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.new_deaths)])
    .range([height - marginBottom, marginTop])

  const yAxis = d3.axisLeft()
    .scale(yScale)

  svg.append('g')
    .attr('transform', 'translate(' + marginLeft + ', 0)')
    .call(yAxis)

  svg
    .selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr('x', d => xScale(d.location))
    .attr('y', d => yScale(d.new_deaths))
    .attr('width', xScale.bandwidth())
    .attr('height', d => height - marginBottom - yScale(d.new_deaths))
    .attr('fill', 'yellow')
}
export default draw