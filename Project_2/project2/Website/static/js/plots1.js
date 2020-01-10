// Trace1 for the Greek Data
var trace1 = {
  x: data.map(row => row.usState),
  y: data.map(row => row.trumpVoters),

  name: "Trump",
  type: "bar"
};

// Trace 2 for the Roman Data
var trace2 = {
  x: data.map(row => row.usState),
  y: data.map(row => row.clintonVoters),
  
  name: "Clinton",
  type: "bar"
};

// Combining both traces
var data = [trace1, trace2];

// Apply the group barmode to the layout
var layout = {
  title: "Trump vs Clinton % voters",
  barmode: "group"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
