window.onload = main();

function main(){
    const nextPage = document.getElementById("nextPageLink");
    const previousPage = document.getElementById("previousPageLink");
    const formSearch = document.getElementById("form-search");

    nextPage.addEventListener('click', (e) => {
        e.preventDefault();
        let params = new URL(nextPage.href).searchParams;
        getPokemons(params.get('limit'), params.get('offset'))
    });

    previousPage.addEventListener('click', (e) => {
        e.preventDefault();
        let params = new URL(previousPage.href).searchParams;
        getPokemons(params.get('limit'), params.get('offset'))
    });

    formSearch.addEventListener('submit', (e) => {
        e.preventDefault();
        const url = 'https://pokeapi.co/api/v2/'
        let pokemonSearch = document.querySelector("#form-search>input").value;

        if(pokemonSearch === '') {
            getPokemons();
            return;
        }

        const lista = document.getElementById('lista');
        setPlaceholders(false);
        lista.innerHTML = '';

        fetchPokemonApi(url + `pokemon/${pokemonSearch}`, (pokemon) => {
            generatePagination({next: null, previous: null});
            
            if (pokemon.error){
                setPlaceholders();
                lista.innerHTML = `
                <div class="my-5">
                    <div class="p-5 text-center bg-body-tertiary">
                        <div class="container py-5">
                            <h1 class="text-body-emphasis">Oops</h1>
                            <p class="col-lg-8 mx-auto lead">
                                Não localizamos nenhum Pokemon com esse nome ou ID!
                            </p>
                        </div>
                    </div>
                </div>`;
                return;
            }

            let listaAbilidades = `
            <ul class="list-group list-group-flush text-capitalize">
            `;
            
            pokemon.stats.map(abilidade => {
                listaAbilidades += `<li class="list-group-item m-0">${abilidade.stat.name}: ${abilidade.base_stat}</li>`;
            });

            listaAbilidades += `</ul>`;


            html = `<div class="col-md-4 col-sm-6 col-lg-3 my-2">
                        <div class="card">
                            <img src="${pokemon.sprites.other.home.front_default}" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title text-capitalize">${pokemon.name}</h5>
                                <p class="card-text">
                                    <strong>Estatísticas:</strong>
                                    ${listaAbilidades}
                                </p>
                                <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                            </div>
                        </div>
                    </div>`;
            lista.innerHTML += html;

            setPlaceholders();
        });
    });

    getPokemons();
}

async function fetchPokemonApi(url, callback) {
    await fetch(url).then(response => response.ok ? response.json() : {error: true}).then(callback); 
}

function setPlaceholders(hidden = true) {
    let placeholderAttr = document.getElementById("placeholder");
    if (hidden && !placeholderAttr.classList.contains('hidden')){
        placeholderAttr.classList.add('hidden')
    }

    if ( !hidden && placeholderAttr.classList.contains('hidden')){
        placeholderAttr.classList.remove('hidden')
    }
}

function generatePagination(pages) {
    let next = document.querySelector('.next');
    let previous = document.querySelector('.previous');

    
    if (pages.next !== null){
        next.setAttribute('href', pages.next)
        if(next.classList.contains('disabled')){
            next.classList.remove('disabled')
        }
    }else{
        if(!next.classList.contains('disabled')){
            next.classList.add('disabled')
        }
    }

    if (pages.previous !== null){
        previous.setAttribute('href', pages.previous)
        if(previous.classList.contains('disabled')){
            previous.classList.remove('disabled')
        }
    }else{
        if(!previous.classList.contains('disabled')){
            previous.classList.add('disabled')
        }
    }
}

function getPokemons (limit = 8, offset = 0){
    const url = 'https://pokeapi.co/api/v2/'
    const lista = document.getElementById('lista');
    setPlaceholders(false);
    lista.innerHTML = '';
    
    fetchPokemonApi(url + `pokemon?limit=${limit}&offset=${offset}`, (data) => {
        
        let pokemons = data.results;

        generatePagination({
            'previous': data.previous,
            'next': data.next
        });

        pokemons.forEach(pokemon => {

            fetchPokemonApi(pokemon.url, (options) => {
                //console.log(options.stats);

                let listaAbilidades = `
                <ul class="list-group list-group-flush text-capitalize">
                `;
                
                options.stats.map(abilidade => {
                    listaAbilidades += `<li class="list-group-item m-0">${abilidade.stat.name}: ${abilidade.base_stat}</li>`;
                });

                listaAbilidades += `</ul>`;


                html = `<div class="col-md-4 col-sm-6 col-lg-3 my-2">
                            <div class="card">
                                <img src="${options.sprites.other.home.front_default}" class="card-img-top" alt="...">
                                <div class="card-body">
                                    <h5 class="card-title text-capitalize">${pokemon.name}</h5>
                                    <p class="card-text">
                                        <strong>Estatísticas:</strong>
                                        ${listaAbilidades}
                                    </p>
                                    <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                                </div>
                            </div>
                        </div>`;
                lista.innerHTML += html;
            });
        });
        setPlaceholders();
    });
}