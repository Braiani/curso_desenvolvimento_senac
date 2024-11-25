const inputs = document.querySelectorAll('.required')
const spans = document.querySelectorAll('.span-required')

document.addEventListener('submit', function(e){
    e.preventDefault()
    if(!nomeValidate() || !senhaValidate() || !confirmarValidate()){
        alert("Verifique os campos e tente novamente")
    }
})

function nomeValidate(){
    let nome = inputs[0].value
    if(nome.length == 0){
        return false
    }

    if(nome.length < 3){
        setError(0)
        return false
    }

    hideError(0)
    return true
}

function senhaValidate(){
    let senha = inputs[1].value
    if(senha.length == 0){
        return false
    }
    if(senha.length < 8){
        setError(1, 'O campo de senha deve ter no mínimo 8 caracteres.')
        return false
    }
    if (!validarTemNumero(senha)){
        setError(1, 'A senha deve conter pelo menos um número.')
        return false
    }
    if(senha == 'password123'){
        setError(1, 'Essa senha está sendo utilizada pelo usuário John_Doe.')
        return false
    }
    hideError(1)
    return true
}

function confirmarValidate(){
    if(inputs[2].value != inputs[1].value){
        setError(2, 'Os campos de senha e confirmação de senha devem ser iguais.')
        return false
    }
    
    hideError(2)
    return true
}

function validarTemNumero(text){
    for (i = 0, len = text.length; i < len; i++){
        if(Number(text[i]) == text[i]){
            return true
        }
    }
    return false
}

function hideError(index){
    spans[index].style.display = 'none'
}

function setError(index, text = ''){
    spans[index].style.display = 'block'
    if (text != ''){
        spans[index].innerText = text
    }
}