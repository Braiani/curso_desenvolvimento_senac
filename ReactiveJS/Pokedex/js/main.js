window.onload = getPokemons()

async function getPokemonApi() {
    const url = 'https://pokeapi.co/api/v2/pokemon'

    try {
        return await fetch(url).then(response => response.json());
    } catch (e) {
        return 'caught';
    }
    let 
        /* .then(response => response.json())
        .then(data => pokemons = data.body); */

    return pokemons
}

function getPokemons (){
    let listaPokemons = getPokemonApi()
    
    console.log(listaPokemons)
}