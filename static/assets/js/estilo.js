//Função de troca da imagem do background do cabeçalho
var backgroundImage = document.querySelector('.cabecalho');

var images = [
    '../static/assets/img/header/MEV_Espiculas_Bio.jpg',
    '../static/assets/img/header/MET_NanoTubo_Fis.jpg',
    '../static/assets/img/header/MEV_Inseto_Bio.jpg',
    '../static/assets/img/header/MEV_Inseto_Pan_Bio.jpg',
    '../static/assets/img/header/MEV_Planta_Bio.jpg',
    '../static/assets/img/header/MEV_Planta_Pan_Bio.jpg',
    '../static/assets/img/header/MEV_Planta_Transv_Bio.jpg'
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

//Funções de Menu Rodapé
var titulo = document.querySelectorAll('.rodape__links__divisao__titulo');
var lista = document.querySelectorAll('.rodape__links__divisao__lista');

for (let i = 0; i < titulo.length; i++) {
    titulo[i].addEventListener("click", () => {
        if (lista[i].style.display != "block") {
            lista[i].style.display = "block";
        } else {
            lista[i].style.display = "none";
        }

    })

}

//Funções do Slider

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

//Funções da galeria de imagens
let modal;
let btnFechar;
let imagem;
let imagemModal;
let textoModal = document.querySelector('.conteudo__equipamento__modal__descricao');

let equipamentos = document.querySelector('.conteudo__equipamento');
let galeria = document.querySelector('.conteudo__galeria');

let imagemModalGaleria = document.querySelector('.conteudo__galeria__modal__contexto__imagem__foto');
let textoAmostraModal = document.querySelector('.conteudo__galeria__modal__contexto__imagem__titulo');
let textoEquipamentoModal = document.querySelector('#modal-galeria-equipamento');
let textoDescricaoModal = document.querySelector('#modal-galeria-descricao');
let pesquisadorDescricaoModal = document.querySelector('#modal-galeria-solicitante');
let pesquisadorImagemModal = document.querySelector('#modal-galeria-solicitante-imagem');
let departamentoDescricaoModal = document.querySelector('#modal-galeria-departamento');
let tecnicoDescricaoModal = document.querySelector('#modal-galeria-tecnico');
let tecnicoImagemModal = document.querySelector('#modal-galeria-tecnico-imagem');
let cargoTecnicoDescricaoModal = document.querySelector('#modal-galeria-cargo');

if (equipamentos != null) {
    modal = document.querySelector('.conteudo__equipamento__modal');
    imagem = document.querySelectorAll('.conteudo__equipamento__galeria__foto img');
    btnFechar = document.querySelector('.conteudo__equipamento__modal i');
    imagemModal = document.querySelector('.conteudo__equipamento__modal__imagem');

    imagem.forEach(imagem => {
        imagem.addEventListener('click', () => {
            modal.classList.add('abrir');
            let srcModal = imagem.getAttribute("data-original");
            imagemModal.src = srcModal;
            let altTexto = imagem.alt;
            textoModal.textContent = altTexto;
        });
    });

} else if (galeria) {
    modal = document.querySelector('.conteudo__galeria__modal');
    imagem = document.querySelectorAll('.conteudo__galeria__foto img');
    btnFechar = document.querySelector('.conteudo__galeria__modal i');

    imagem.forEach(imagem => {
        imagem.addEventListener('click', () => {
            modal.classList.add('abrir');
            let srcModal = imagem.getAttribute("data-original");
            let amostraModal = imagem.getAttribute("data-amostra");
            let equipamentoModal = imagem.getAttribute("data-equipamento");
            let descricaoModal = imagem.getAttribute("data-descricao");
            let pesquisadorModal = imagem.getAttribute("data-pesquisador");
            let pesquisadorSrcModal = imagem.getAttribute("data-pesquisadorImagem");
            let departamentoModal = imagem.getAttribute("data-departamento");
            let tecnicoModal = imagem.getAttribute("data-tecnico");
            let tecnicoSrcModal = imagem.getAttribute("data-tecnicoImagem");
            let cargoModal = imagem.getAttribute("data-cargo");
            imagemModalGaleria.src = srcModal;
            textoAmostraModal.textContent = amostraModal;
            textoEquipamentoModal.textContent = equipamentoModal;
            textoDescricaoModal.textContent = descricaoModal;
            pesquisadorDescricaoModal.textContent = pesquisadorModal;
            pesquisadorImagemModal.src = pesquisadorSrcModal;
            departamentoDescricaoModal.textContent = departamentoModal;
            tecnicoDescricaoModal.textContent = tecnicoModal;
            tecnicoImagemModal.src = tecnicoSrcModal;
            cargoTecnicoDescricaoModal.textContent = cargoModal;
        });
    });
}


if (modal != null) {
    modal.addEventListener('click', fecharModal);
    btnFechar.addEventListener('click', removeAbrirModal);

    document.addEventListener('keydown', (e) => {
        if (e.keyCode == 27) {
            if (modal != null) {
                removeAbrirModal();
            }
        }
    });
}

function fecharModal(e) {
    if (e.target.classList.contains('conteudo__equipamento__modal') || e.target.classList.contains('conteudo__galeria__modal')) {
        removeAbrirModal();
    }
}

function removeAbrirModal() {
    modal.classList.remove('abrir');
}

// Funnções de estatíticas

function selecionaValor() {
    let seletor = document.querySelector('.conteudo__estatisticas__formulario__selecao');
    let opcao = seletor.value;
    let sections = ['porEquipamentos', 'porDepartamentos', 'tabelaDeValores'];

    sections.forEach(section => {
        if (section != opcao) {
            let sectionOcultada = document.querySelector('#' + section);
            sectionOcultada.style.display = "none";
        } else {
            let sectionMostrada = document.querySelector('#' + section);
            sectionMostrada.style.display = "grid";
        }
    });
}


function addDepartamento() {
    let controle = document.getElementById('controle');
    let departamento = prompt("Digite o departamento");


    if (departamento != null) {
        let div = document.createElement("div");
        div.classList.add('formulario__departamentos__departamento');
        let input = document.createElement("input");
        input.classList.add('formulario__departamentos__departamento__input');
        input.setAttribute("type", "checkbox");
        input.setAttribute("name", departamento);
        input.setAttribute("id", departamento);
        input.checked = true;
        input.setAttribute("value", departamento);
        let label = document.createElement("label");
        label.classList.add('formulario__departamentos__departamento__label');
        label.setAttribute("for", departamento);
        label.innerText = departamento.toUpperCase();
        div.appendChild(input);
        div.appendChild(label);
        controle.insertAdjacentElement('beforebegin', div);
        atualizaDepartamentos();
    }
}

function atualizaDepartamentos() {
    let departamentos = document.querySelectorAll('.formulario__departamentos__departamento__input');
    let departamentoDiscentes = document.querySelectorAll('.formulario__discentes__discente__departamento__select');

    for (let i = 0; i < departamentoDiscentes.length; i++) {
        const select = departamentoDiscentes[i];
        select.textContent = "";

        for (let i = 0; i < departamentos.length; i++) {
            const departamento = departamentos[i];
            let valoreDepartamento = departamento.value;
            let optionDiscientes = document.createElement("option");
            optionDiscientes.text = valoreDepartamento.toUpperCase();
            optionDiscientes.setAttribute("value", valoreDepartamento);
            select.options.add(optionDiscientes);
        }
    }
}

function constroiInput(classe, atribuicao, id, nomeLabel, tipo, requerido = true, placeholderTexto = "", opcoes = []) {

    let div = document.createElement("div");
    div.classList.add(classe);
    let label = document.createElement("label");
    let atributo = atribuicao + "_" + id
    label.classList.add(classe + "__label");
    label.setAttribute("for", atributo);
    label.innerHTML = "<b>" + nomeLabel + "</b>";
    div.appendChild(label);

    if (tipo != "select") {
        let input = document.createElement("input");
        input.classList.add(classe + "__input");
        input.setAttribute("type", tipo);
        input.setAttribute("name", atributo);
        input.setAttribute("id", atributo);
        input.setAttribute("placeholder", placeholderTexto);
        input.required = requerido;
        div.appendChild(input);
    } else {
        let select = document.createElement("select");
        select.classList.add(classe + "__select");
        select.setAttribute("name", atributo);
        select.setAttribute("id", atributo);

        for (let i = 0; i < opcoes.length; i++) {
            const opcaoValor = opcoes[i];
            opcao = document.createElement("option");
            opcao.text = opcaoValor;
            opcao.setAttribute("value", opcaoValor);
            select.options.add(opcao);
        }
        div.appendChild(select);
    }
    return div;
}

function addDiscente() {
    let controle = document.getElementById('controle_discentes');
    let div = document.createElement("div");
    div.classList.add('formulario__discentes__discente');
    let id = constroiIdDiscentes();
    div.setAttribute("id", id);
    let i = document.createElement("i");
    i.classList.add('fa');
    i.classList.add('fa-times');
    i.classList.add('formulario__discentes__discente__remove');
    i.setAttribute("aria-hidden", "true");
    i.setAttribute("onclick", "remover('#" + id + "')");

    let divNome = constroiInput("formulario__discentes__discente__nome", "nome", id, "Nome", "text", true, "Digite o nome do discente");

    let divEmail = constroiInput("formulario__discentes__discente__email", "email", id, "E-mail", "email", true, "Digite o email do discente");

    opcoesVinculo = ["Iniciação Científica", "Mestrado", "Doutorado", "Pós-Doutorado", "Outros"];

    let divVinculo = constroiInput("formulario__discentes__discente__vinculo", "vinculo", id, "Vínculo", "select", false, "", opcoesVinculo);

    let divInicio = constroiInput("formulario__discentes__discente__inicio", "inicio", id, "Início do Vínculo", "date", true, "");

    let opcoesSetor = ["Setor de Artes, Comunicação e Design", "Setor de Ciências Agrárias", "Setor de Ciências Biológicas", "Setor de Ciêcnias da Saúde", "Setor de Ciências da Terra", "Setor de Ciêcnias Exatas", "Setor de Ciências Humanas", "Setor de Ciências Jurídicas", "Setor de Ciências Sociais Aplicadas", "Setor de Educação", "Setor de Educação Profissional e Tecnológica", "Setor de Tecnologia", "Setor Litoral", "Setor Palotina", "Campus de Jandaia do Sul"];

    let divSetor = constroiInput("formulario__discentes__discente__setor", "setor", id, "Setor", "select", false, "", opcoesSetor);

    let opcoesDepartamento = [];

    let divDepartamento = constroiInput("formulario__discentes__discente__departamento", "departamento", id, "Departamento", "select", false, "", opcoesDepartamento);

    div.appendChild(i);
    div.appendChild(divNome);
    div.appendChild(divEmail);
    div.appendChild(divVinculo);
    div.appendChild(divInicio);
    div.appendChild(divSetor);
    div.appendChild(divDepartamento);
    controle.insertAdjacentElement('beforebegin', div);
    atualizaDepartamentos();
}

function constroiIdDiscentes() {
    let discentes = document.querySelectorAll('.formulario__discentes__discente');
    let discente = discentes[discentes.length - 1];
    let id = discente.getAttribute("id");
    idNumInicio = id.indexOf("_");
    idNumFinal = id.length;
    idNum = parseInt(id.slice((idNumInicio + 1), idNumFinal));
    idNovo = "discente_" + (idNum + 1);
    return idNovo;
}

function remover(registro) {
    let divs = document.querySelectorAll(registro);
    let ultimo = divs[divs.length - 1]
    ultimo.remove();
}

function revelarCodigo(id, icone) {
    let senha = document.getElementById(id);
    let icon = document.getElementById(icone)

    if (senha.type === 'password') {
        senha.type = "text";
        icon.classList.toggle('fa-eye-slash')
    } else {
        senha.type = "password";
        icon.classList.toggle('fa-eye-slash')
    }
}

let foto = document.querySelector('.formulario__foto__upload__input');
let preview = document.querySelector('.formulario__foto__preview');

if (foto != null) {
    foto.addEventListener('change', updateImageDisplay);

    function updateImageDisplay() {
        while (preview.firstChild) {
            preview.removeChild(preview.firstChild);
        }

        const curFiles = foto.files;
        if (curFiles.length === 0) {
            const para = document.createElement('p');
            para.textContent = 'Nenhum arquivo selecionado para upload';
            preview.appendChild(para);
        } else {
            const list = document.createElement('ol');
            preview.appendChild(list);

            for (const file of curFiles) {
                const listItem = document.createElement('li');
                const para = document.createElement('p');
                if (validFileType(file)) {
                    const image = document.createElement('img');
                    image.src = URL.createObjectURL(file);
                    image.classList.add('imagem__perfil')

                    listItem.appendChild(image);
                    listItem.appendChild(para);
                } else {
                    para.textContent = `Nome do arquivo ${file.name}: Tipo de arquivo não é válido.`;
                    listItem.appendChild(para);
                }

                list.appendChild(listItem);
            }
        }
    }

    const fileTypes = [
        "image/jpeg",
        "image/png",
    ];

    function validFileType(file) {
        return fileTypes.includes(file.type);
    }

    function returnFileSize(number) {
        if (number < 1024) {
            return number + 'bytes';
        } else if (number >= 1024 && number < 1048576) {
            return (number / 1024).toFixed(1) + 'KB';
        } else if (number >= 1048576) {
            return (number / 1048576).toFixed(1) + 'MB';
        }
    }
}

let senhaCME = document.getElementById('senha');
let senhaConfirmacaoCME = document.getElementById('confirma-senha');
let botao_enviar = document.getElementById('botao-enviar');

function validaSenha() {
    var regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if (senhaCME.value != senhaConfirmacaoCME.value ||
        senhaCME.value.length < 8 ||
        senhaCME.value.match(regex)
    ) {
        senhaCME.style.borderColor = "red";
        senhaConfirmacaoCME.style.borderColor = "red";
        botao_enviar.disabled = true;
        botao_enviar.textContent = "Existem erros nos dados"
    } else {
        senhaCME.style.borderColor = "green";
        senhaConfirmacaoCME.style.borderColor = "green";
        botao_enviar.disabled = false;
        botao_enviar.textContent = "Cadastrar"
    }

}

if (senhaCME != null && senhaConfirmacaoCME != null) {
    botao_enviar.disabled = true;
    senhaCME.onchange = validaSenha;
    senhaConfirmacaoCME.onkeyup = validaSenha;
}

function limpa_formulário_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('rua').value = ("");
    document.getElementById('bairro').value = ("");
    document.getElementById('cidade').value = ("");
    document.getElementById('uf').value = ("");
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('rua').value = (conteudo.logradouro);
        document.getElementById('bairro').value = (conteudo.bairro);
        document.getElementById('cidade').value = (conteudo.localidade);
        document.getElementById('uf').value = (conteudo.uf);
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep();
        alert("CEP não encontrado.");
    }
}

function pesquisacep(valor) {

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep != "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('rua').value = "...";
            document.getElementById('bairro').value = "...";
            document.getElementById('cidade').value = "...";
            document.getElementById('uf').value = "...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            limpa_formulário_cep();
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep();
    }
};