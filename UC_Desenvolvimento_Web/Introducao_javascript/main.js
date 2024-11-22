function quotes(data){
    data['quotes'].forEach(element => {
        document.write('<p>' + element.quote + '</p>')
    });
}


console.log(10>20 ? 'Sim': 'Não')
document.write("<p>Hello World!!!</p>")
document.write(Date())

fetch('https://dummyjson.com/quotes?limit=3&skip=10', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(res => res.json())
.then(quotes)