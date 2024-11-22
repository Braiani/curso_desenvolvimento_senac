function exercicio_1(){
    temp_fahrenheit = window.prompt("Digite a temperatura em Fahrenheit: ")
    if (temp_fahrenheit == null){
        window.alert('Temperatura não digitada!')
        return
    }

    temp_celsius = (5/9) * (temp_fahrenheit - 32)
    window.alert(`A temperatura em Celsius é ${temp_celsius.toFixed(0)}º`)
}

function exercicio_2(){
    produto = window.prompt('Digite o nome do produto: ')
    quantidade = window.prompt('Digite a quantidade comprada: ')
    valor_unitario = window.prompt('Digite o valor unitário: ')
    percent_desconto = window.prompt('Digite o desconto a ser aplicado (%): ')

    total = parseFloat(quantidade) * parseFloat(valor_unitario)
    subtotal = total - ((total * percent_desconto) / 100)
    window.alert(`
    - Produto: ${produto}
    - Valor total da venda: R$ ${subtotal.toFixed(2)}
    `)
}

function exercicio_3(){
    compra = window.prompt("Qual o valor em reais da compra: ")

    fetch('https://economia.awesomeapi.com.br/json/last/BRL-USD')
    .then(res => res.json())
    .then(function (res) {
        valor_compra = parseFloat(this.compra)
        cotacao = res['BRLUSD'].bid
        convertido = valor_compra * parseFloat(cotacao)
        window.alert(`O valor de R$ ${valor_compra.toFixed(2)} em dólares é igual a U$ ${convertido.toFixed(2)}`)
    })
}