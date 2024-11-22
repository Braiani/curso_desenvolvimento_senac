function quotes(data){
    data['quotes'].forEach(element => {
        document.write('<p>' + element.quote + '</p>')
    });
}


// console.log(10>20 ? 'Sim': 'Não')
// document.write("<p>Hello World!!!</p>")
// document.write(Date())

// fetch('https://dummyjson.com/quotes?limit=3&skip=10', {
//     method: 'GET',
//     headers: {
//         'Content-Type': 'application/json'
//     }
// })
// .then(res => res.json())
// .then(quotes)

window.onload = function(){
    let p = document.getElementsByTagName('p')[1]
    p.style.background = 'blue'
    p.style.fontSize = '32px'

    p.innerHTML = 'É isso aí mesmo!'
}

function respPedro(){
    let li = document.getElementById('pedro')
    li.innerText = 'Certa Resposta!'
    li.style.color = 'white'
    li.style.backgroundColor = 'green'
}

function respJoao(){
    let li = document.getElementById('joao')
    li.innerText = 'Certa Errada!'
    li.style.color = 'white'
    li.style.backgroundColor = 'red'
}

function respMaria(){
    let li = document.getElementById('maria')
    li.innerText = 'Certa Errada!'
    li.style.color = 'white'
    li.style.backgroundColor = 'red'
}