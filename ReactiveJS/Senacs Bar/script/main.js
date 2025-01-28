const btn = document.querySelector("#menu-header>nav>button");
const listItens = document.querySelector("#menu-header>nav>ul");

btn.addEventListener('click', function(){
    listItens.classList.toggle('ativo')
})

JSON.stringify()