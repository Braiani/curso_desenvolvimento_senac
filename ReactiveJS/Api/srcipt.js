
fetch("./dados.json ")
    .then(res => res.status == 200 ? res.json() : alert('errroouuu'))
    .then(pessoa => {
        const divPessoa = document.createElement("div");
        const paragrafo = document.createElement("p");

        const frase = `Meu nome é ${pessoa.nome}, tenho ${pessoa.idade} anos e sou ${pessoa.profissao}`;

        paragrafo.innerText = frase;

        divPessoa.appendChild(paragrafo);

        document.getElementById("app").appendChild(divPessoa);
    })