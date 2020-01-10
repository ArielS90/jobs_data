function init() {
  var data = [{
    values: [1, 2, 3, 39],
    labels: ["White Caucasian", "Black/African American", "Asian", "American Indian or Alaska Native", "Native Hawaiian or Pacific Islander", "Hispanic"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  var PIE = document.getElementById("pie");
  Plotly.restyle(PIE, "values", [newdata]);
}

function getData(dataset) {
  var data = [];
  switch (dataset) {
  case "Alabama":
    data = [68, 16, 2, 1, 0, 1];
    break;
  case "Alaska":
    data = [15, 0, 0, 1, 0, 0];
    break;
  case "Arizona":
    data = [126, 6, 3, 8, 1, 22];
    break;
  case "Arkansas":
    data = [43, 6, 2, 3, 1, 1];
    break;
  case "California":
    data = [485, 44, 71, 23, 9, 115];
    break;
  case "Colorado":
    data = [152, 5, 6, 7, 0, 14];
    break;
  case "Connecticut":
    data = [66, 5, 0, 0, 0, 6];
    break;
  case "Delaware":
    data = [16, 2, 1, 0, 1, 1];
    break;
  case "District of Columbia":
    data = [17, 5, 1, 1, 0, 1];
    break;
  case "Florida":
    data = [281, 35, 14, 2, 2, 64];
    break;
  case "Georgia":
    data = [128, 53, 5, 2, 0, 8];
    break;
  case "Hawaii":
    data = [15, 1, 7, 1, 4, 3];
    break;
  case "Delaware":
    data = [16, 0, 0, 0, 0, 0];
    break;
  case "Idaho":
    data = [60, 0, 1, 0, 0, 2];
    break;
  case "Illinois":
    data = [209, 21, 12, 1, 1, 16];
    break;
  case "Indiana":
    data = [126, 4, 0, 0, 0, 1];
    break;
  case "Iowa":
    data = [96, 0, 3, 0, 1, 0];
    break;
  case "Kansas":
    data = [75, 3, 3, 1, 0, 7];
    break;
  case "Kentucky":
    data = [74, 8, 0, 1, 0, 1];
    break;
  case "Louisiana":
    data = [49, 17, 2, 0, 0, 6];
    break;
  case "Maine":
    data = [39, 0, 0, 2, 0, 0];
    break;
  case "Maryland":
    data = [80, 41, 8, 2, 1, 9];
    break;
  case "Massachussetts":
    data = [156, 10, 8, 2, 2, 8];
    break;
  case "Michigan":
    data = [210, 14, 4, 7, 1, 3];
    break;
  case "Minnesota":
    data = [158, 5, 6, 0, 0, 3];
    break;
  case "Mississippi":
    data = [37, 7, 1, 0, 0, 1];
    break;
  case "Missouri":
    data = [128, 9, 2, 0, 2, 4];
    break;
  case "Montana":
    data = [25, 0, 0, 0, 0, 1];
    break;
  case "Nebraska":
    data = [47, 1, 0, 0, 0, 3];
    break;
  case "Nevada":
    data = [52, 5, 6, 5, 1, 5];
    break;
  case "New Hampshire":
    data = [25, 0, 0, 2, 0, 0];
    break;
  case "New Jersey":
    data = [133, 20, 13, 1, 1, 15];
    break;
  case "New Mexico":
    data = [31, 1, 2, 4, 1, 10];
    break;
  case "New York":
    data = [287, 46, 31, 10, 1, 33];
    break;
  case "North Carolina":
    data = [185, 30, 7, 5, 1, 12];
    break;
  case "North Dakota":
    data = [18, 0, 0, 0, 0, 0];
    break;
  case "Ohio":
    data = [256, 8, 4, 6, 1, 8];
    break;
  case "Oklahoma":
    data = [64, 4, 2, 7, 0, 7];
    break;
  case "Oregon":
    data = [91, 2, 4, 1, 1, 4];
    break;
  case "Pennsylvania":
    data = [310, 23, 4, 4, 3, 14];
    break;
  case "Rhode Island":
    data = [27, 1, 1, 0, 0, 0];
    break;
  case "South Carolina":
    data = [65, 10, 3, 1, 1, 5];
    break;
  case "South Dakota":
    data = [22, 0, 0, 0, 0, 0];
    break;
  case "Tennessee":
    data = [100, 16, 2, 1, 0, 6];
    break;
  case "Texas":
    data = [368, 38, 23, 12, 5, 76];
    break;
  case "Utah":
    data = [68, 3, 4, 1, 1, 5];
    break;
  case "Vermont":
    data = [20, 0, 0, 0, 0, 0];
    break;
  case "Virginia":
    data = [164, 33, 6, 3, 0, 14];
    break;
  case "Washington":
    data = [173, 4, 15, 6, 0, 17];
    break;
  case "West Virginia":
    data = [31, 0, 0, 0, 0, 1];
    break;
  case "Wisconsin":
    data = [137, 2, 2, 3, 0, 2];
    break;
  case "Wyoming":
    data = [18, 0, 0, 0, 0, 0];
    break;
  default:
    data = [0, 0, 0, 0];
  }
  updatePlotly(data);
}

init();
