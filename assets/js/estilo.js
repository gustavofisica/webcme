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
var titulo= document.querySelectorAll('.rodape__links__divisao__titulo');
var lista = document.querySelectorAll('.rodape__links__divisao__lista');

for (let i = 0; i < titulo.length; i++) {
    titulo[i].addEventListener("click", (e)=>{
        if (lista[i].style.display != "block") {
            lista[i].style.display = "block";
        } else{
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
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
    }
}