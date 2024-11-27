const input = document.getElementById('numProc')
const span = document.getElementById('numProc-span')

function numProcValidate(){
    const regex = /\d{7}\-\d{2}\.\d{4}\.8\.12\.\d{4}/i

    if (!regex.test(input.value)){
        setError()
        return
    }

    removeError()
}

function setError(){
    span.style.display = 'block'
}

function removeError(){
    span.style.display = 'none'
}