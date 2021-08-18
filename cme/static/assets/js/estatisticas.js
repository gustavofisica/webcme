// Funções de construção de gráficos dinâmica


function desenharGrafico(tipo, dados, id, titulo) {
    if (tipo == 'pizza') {
        google.charts.load('current', {
            packages: ['corechart']
        });

        var opcoesPizza = {
            title: titulo,
            is3D: true,
            sliceVisibilityThreshold: 0.08,
            chartArea: {
                width: '100%',
                height: '80%'
            },
        };

        google.charts.setOnLoadCallback(desenharPizza);

        function desenharPizza() {
            var data = google.visualization.arrayToDataTable(dados);

            var chart = new google.visualization.PieChart(document.getElementById(id));

            chart.draw(data, opcoesPizza);
        };
    } else if (tipo == 'barra') {
        google.charts.load('current', {
            'packages': ['bar']
        });

        var opcoesBarra = {
            title: titulo,
            chartArea: {
                left: 200,
                width: '100%',
                height: '80%'
            },
            legend: 'none'
        };

        google.charts.setOnLoadCallback(desenharBarra);

        function desenharBarra() {
            var view = new google.visualization.arrayToDataTable(dados);

            var chart = new google.visualization.BarChart(document.getElementById(id));

            chart.draw(view, opcoesBarra);
        };
    } else if (tipo == 'coluna') {
        google.charts.load('current', {
            'packages': ['bar']
        });

        var opcoesBarra = {
            title: titulo,
            chartArea: {
                width: '85%',
                height: '80%'
            },
            legend: 'none'
        };

        google.charts.setOnLoadCallback(desenharColuna);

        function desenharColuna() {
            var view = new google.visualization.arrayToDataTable(dados);

            var chart = new google.visualization.ColumnChart(document.getElementById(id));

            chart.draw(view, opcoesBarra);
        };
    }
}