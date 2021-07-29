google.charts.load('current', {
    packages: ['corechart', 'bar']
}); // Roda a biblioteca do Google Charts mais recente

var dadosSecundarios = [
    ['Cursos',
        'TEM JEOL JEM 1200EX-II',
        'SEM JEOL JSM 6360-LV',
        'SEM TESCAN VEGA3 LMU',
        'SEM FEI Quanta 450 FEG',
        'Raman Witec alpha 300R',
        'AFM Shimadzu SPM 9500 J3',
        'SEM FEI Phenom',
        'TEM Novo'
    ],
    ['Química', 12.5, 98.7, 25.3, 0.6, 3.3, 2.8, 1.2, 1.9],
    ['Física', 13.0, 90.7, 17.1, 0.8, 2.8, 3.4, 1.2, 15.6],
    ['Botânica', 9.3, 93.0, 15.8, 0.9, 1.8, 3.8, 1.2, 5.9],
    ['Biologia Celular', 14.9, 97.5, 17.1, 1.3, 4.4, 5.1, 1.2, 6.8],
    ['PIPE', 14.3, 98.7, 13.6, 2.1, 4.9, 5.7, 1.2, 10.0],
    ['Engenharia Mecânica', 18.2, 16.5, 0.0, 2.2, 5.2, 2.3, 1.2, 7.2]
];

google.charts.setOnLoadCallback(desenharGraficoSecundario);

function desenharGraficoSecundario() {

    var data = new google.visualization.arrayToDataTable(dadosSecundarios); //Instancia um objeto para transformar os dados da tabela secundária para formatação
    var view = new google.visualization.DataView(data); // Formata a visualização dos dados para construção do gráfico

    for (let index = 0; index < dadosPrimarios.length; index++) {

        view.setColumns([0, index + 1]);

        var graficoEscondido = document.getElementById('grafico-escondido'); //Identifica a div onde será construida o gráfico secundário
        var graficoSecundario = new google.visualization.PieChart(graficoEscondido); //Constrói um gráfico tipo Pizza

        google.visualization.events.addListener(graficoSecundario, 'ready', function () {

            var imagemGraficoSecundario = '<img src="' + graficoSecundario.getImageURI() + '">'; //Monta a estrutura HTML que será chamada no houver do mouse em cada barra

            dadosPrimarios[index][3] = imagemGraficoSecundario; // devolve ao conjunto de dados primários a imagem gerada do gráfico secundário
        });

        graficoSecundario.draw(view, opcoesSecundaria); //desenha o gráfico secundário

    }; // constrói um gráfico secundário para cada linha dos dados primários

    var opcoesSecundaria = {
        'title': 'Distribuição por Cursos',
        'height': 300,
        'width': 400
    }; // Carrega as opções para a construção do gráfico secundário

    desenharGrafico(); // Chama a função que desenha o gráfico na página
}


var dadosPrimarios = [
    ['TEM JEOL JEM 1200EX-II', 1000, 'color: #FF6347'],
    ['SEM JEOL JSM 6360-LV', 500, 'color: #2E8B57'],
    ['SEM TESCAN VEGA3 LMU', 230, 'color: #F4A460'],
    ['SEM FEI Quanta 450 FEG', 500, 'color: #708090'],
    ['Raman Witec alpha 300R', 900, 'color: #9400D3'],
    ['AFM Shimadzu SPM 9500 J3', 260, 'color: #2F4F4F'],
    ['SEM FEI Phenom', 400, 'color: #20B2AA'],
    ['TEM Novo', 1000, 'color: #4682B4']
]; // Elenca os dados do Gráfico

function desenharGrafico() {
    var tabela = new google.visualization.DataTable(); //Constroí a planilha de dados
    tabela.addColumn('string', 'Equipamento'); //Insere a primeira coluna
    tabela.addColumn('number', 'Horas de Uso'); // Insere a segunda coluna
    tabela.addColumn({
        type: 'string',
        role: 'style'
    }); //Insere a regra de cor do dado no gráfico

    tabela.addColumn({
        type: 'string',
        label: 'Tooltip Chart',
        role: 'tooltip',
        'p': {
            'html': true
        }
    }); //Insere a coluna com as regras para o gráfico secundário

    tabela.addRows(dadosPrimarios); // Insere as linhas que estão na variável dados

    var opcoes = {
        'tooltip': {
            isHtml: true
        },
        'chartArea': {
            left: 200,
            top: 0,
            width: '100%',
            height: '100%'
        },
        'legend': 'none'
    }; // Carrega as opções para a construção do gráfico

    var grafico = new google.visualization.BarChart(document.getElementById('grafico')); //Identifica o tipo de gráfico e onde ele deve ser desenhado no HTML
    grafico.draw(tabela, opcoes); // Desenha o gráfico com os dados da tabela com as opções elencadas
} //Função que carrega os dados
