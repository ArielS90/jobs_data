// SVG area dimensions
var svgWidth = 1000;
var svgHeight = 500;

// Define chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 50,
  left: 30
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);


// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);


// load data from csv
d3.csv("state_grouped.csv").then(function(state) {

  console.log(state);

  // Cast the hours number for each state
  state.forEach(function(d) {
    d.Q14_hrs_all_jobs = +d.Q14_hrs_all_jobs;
  });

  // Configure a band scale for the horizontal axis with a padding of 0.1 (10%)
  var xBandScale = d3.scaleBand()
    .domain(state.map(d => d.statename))
    .range([0, chartWidth])
    .padding(0.1);

  // Linear scale for the vertical axis
  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(state, d => d.Q14_hrs_all_jobs)])
    .range([chartHeight, 0]);

  // Create two new functions passing our scales in as arguments
  // These will be used to create the chart's axes
  var bottomAxis = d3.axisBottom(xBandScale);
  var leftAxis = d3.axisLeft(yLinearScale).ticks(10);


  // Append two SVG group elements to the chartGroup area,
  // and create the bottom and left axes inside of them
  chartGroup.append("g")
    .call(leftAxis);

  Bottom = chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    // .attr("transform", "rotate(-45)")
    // .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .call(bottomAxis);

  // Create one SVG rectangle per state
  // Use the linear and band scales to position each rectangle within the chart
  chartGroup.selectAll(".bar")
    .data(state)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", d => xBandScale(d.statename))
    .attr("y", d => yLinearScale(d.Q14_hrs_all_jobs))
    .attr("width", xBandScale.bandwidth())
    .attr("height", d => chartHeight - yLinearScale(d.Q14_hrs_all_jobs));
    
    
    // var margin = {top: 30, right: 40, bottom: 50, left: 50},

    // Axes labels
    // chartGroup.append("text")
    // .attr("transform", "rotate(-90)")
    // .attr("y", 0 - margin.left + 20)
    // .attr("x", 0 - (height / 2))
    // .attr("dy", "1em")
    // .attr("class", "axisText")
    // .text("Number of Hours Per Week");

    // chartGroup.append("text")
    // .attr("transform", "rotate(-90)")
    // .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    // .attr("class", "axisText")
    // .text("State");

}).catch(function(error) {
  console.log(error);
});
