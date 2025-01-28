window.onload = getPokemons()

async function fetchPokemonApi(url, callback) {
    await fetch(url).then(response => response.json()).then(callback);
}

function getPokemons (){
    const url = 'https://pokeapi.co/api/v2/'
    const lista = document.getElementById('lista');
    
    fetchPokemonApi(url + 'pokemon?limit=40&offset=0', (data) => {
        
        let pokemons = data.results;

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


                html = `<div class="col-3 my-2">
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
    });
}