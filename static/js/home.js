google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);

function drawChart() {
  var gold_data = $.getJSON('/data');
  gold_data.success(function(json_data){
    var data = new google.visualization.DataTable();
    data.addColumn('datetime','Time');
    data.addColumn('number','Percentage');
    for (var i = 0; i < json_data.length; i++) {
      var date = new Date(json_data[i][0]);
      var value = json_data[i][1];
      data.addRow([date, value]);
    }
    var options = {
      title: 'Gold Donations',
      legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('line-chart'));
    chart.draw(data, options);
  });
}
