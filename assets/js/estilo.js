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

//Função do Menu Responsivo
var menuTogle = document.querySelector('.menu-toggle');
var bar = document.querySelector('.menu-toggle i');
var menuUl = document.querySelector('.menu ul');

menuTogle.addEventListener("click", (e) => {

    if (menuUl.classList == "") {
        menuUl.classList.toggle("on");
        bar.classList.remove("fa-bars");
        bar.classList.add("fa-times");
    } else {
        menuUl.classList.toggle("on");
        bar.classList.remove("fa-times");
        bar.classList.add("fa-bars");
    }
});

//Função de Menu Rodapé
var titulo = document.querySelectorAll('.rodape__links__divisao__titulo');
var lista = document.querySelectorAll('.rodape__links__divisao__lista');

for (let i = 0; i < titulo.length; i++) {
    titulo[i].addEventListener("click", (e) => {
        if (lista[i].style.display != "block") {
            lista[i].style.display = "block";
        } else {
            lista[i].style.display = "none";
        }

    })

}

//Função do Slider

var portifolio = document.querySelector('.conteudo__portifolio');
if (portifolio != null) {
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("conteudo__portifolio__slideshow__slide");
        var dots = document.getElementsByClassName("dot");
        if (n > slides.length) {
            slideIndex = 1
        }
        if (n < 1) {
            slideIndex = slides.length
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "grid";
        dots[slideIndex - 1].className += " active";
    }
}


var body = document.querySelector('body');
var header = document.querySelector('header');
var main = document.querySelector('main');
var footer = document.querySelector('footer');
var altoContraste = document.querySelector('#alto-contraste');

function trocaContraste() {

    if (body.classList.contains("contraste")) {

        body.classList.remove("contraste");
        header.classList.remove("contraste");
        main.classList.remove("contraste");
        footer.classList.remove("contraste");

    } else {

        var retorno = confirm("Ei, espera um momento.\nA função que você acaba de habilitar ativa o Alto Contraste da página que pode ser desconfortável para pessoas autistas.\nNossa preocupação é oferecer a melhor experiência ao usuário.\nPortanto se você for autista ou estiver acompanhando uma pessoa autista, pode cancelar essa ação.\nMas se for uma pessoa de baixa visão, essa função foi pensada em você! Nessa caso, basta clicar em Ok.");

        if (retorno == true) {

            body.classList.add("contraste");
            header.classList.add("contraste");
            main.classList.add("contraste");
            footer.classList.add("contraste");
        }
    }
}

altoContraste.addEventListener('click', trocaContraste);

//Função da galeria de imagens
let modal = document.querySelector('.conteudo__equipamento__modal');
let btnFechar = document.querySelector('.conteudo__equipamento__modal i');
let imagem = document.querySelectorAll('.conteudo__equipamento__galeria__foto img');
let imagemModal = document.querySelector('.conteudo__equipamento__modal__imagem');
let textoModal = document.querySelector('.conteudo__equipamento__modal__descricao');

imagem.forEach(imagem => {
    imagem.addEventListener('click', () => {
        modal.classList.add('abrir');
        let srcModal = imagem.getAttribute("data-original");
        imagemModal.src = srcModal;
        let altTexto = imagem.alt;
        textoModal.textContent = altTexto;
    });
});

if (modal != null) {
    modal.addEventListener('click', fecharModal);
    btnFechar.addEventListener('click', removeAbrirModal);
}

document.addEventListener('keydown', (e) => {
    if (e.keyCode == 27) {
        if (modal != null) {
            removeAbrirModal();
        }
    }
});

function fecharModal(e) {
    if (e.target.classList.contains('conteudo__equipamento__modal')) {
        removeAbrirModal();
    }
}

function removeAbrirModal() {
    modal.classList.remove('abrir');
}