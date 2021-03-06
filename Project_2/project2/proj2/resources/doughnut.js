
new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        labels : {{labels | safe}},
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: "5",
        datasets:
            [{ data: 
              [
            {% for value in values  %}
            {{ value | safe}},
            {% endfor %}
              ],
            backgroundColor: {{colors | safe}},
            fill: true
        }],
        
    },
    options: {
        cutoutPercentage: 85,
        title: {
            display: true,
            text: 'Self-assesed quality of life based on whether one has a good job',
            fontSize: 20,
            fontStyle: "Bold"
        },
        tooltips: {
            callbacks: {
                label: function(tooltipItem, data) {
                    var label = data.datasets[tooltipItem.datasetIndex].label || '';
                    //console.log(data.datasets[0].data[tooltipItem['index']])
                    
                    if (label) {
                        label += ': ';
                    }
                    label += Math.round(data.datasets[0].data[tooltipItem['index']]* 100);
                    label = label + '%';
                    return label;
        }
            }
        }
    }

});