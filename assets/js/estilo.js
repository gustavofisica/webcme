//Função de troca da imagem do background do cabeçalho
var backgroundImage = document.querySelector('.cabecalho');

var images = [
    'assets/img/header/MEV_Espiculas_Bio.png',
    'assets/img/header/MET_NanoTubo_Fis.png',
    'assets/img/header/MET_Polimero_Qui.png',
    'assets/img/header/MEV_Inseto_Bio.png',
    'assets/img/header/MEV_Inseto_Pan_Bio.png',
    'assets/img/header/MEV_Planta_Bio.png',
    'assets/img/header/MEV_Planta_Pan_Bio.png',
    'assets/img/header/MEV_Planta_Transv_Bio.png'
];

var bg = images[Math.floor(Math.random() * images.length)];

backgroundImage.style.backgroundImage = "url(" + bg + ")";