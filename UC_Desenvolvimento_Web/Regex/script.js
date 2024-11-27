/*
document.write(/[az]/i.test("AZ"))
document.write("<br>")
document.write(/love/i.test("LovE"))
document.write("<br>")
document.write(/[\bx]/.test("123x"))
document.write("<br>")
document.write(/\s/i.test(" w"))
document.write("<br>")
document.write(/^\d{2}\/\d{2}\/\d{4}$/i.test("33/33/3333"))
document.write("<br>")
document.write(/^\d{2}\/\d{2}\/\d{4}$/i.test("33/33/3333"))
document.write("<br>")
document.write(/^(0[1-9]|1[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(\d{4})$/i.test("31/12/3333"))
document.write("<br>")
document.write(/^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$/i.test("123.456.789-00"))
document.write("<br>")
document.write(/^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$/i.test("teste@teste.com"))
document.write("<br>")
 */

const inputEmail = document.getElementById('email')
const spanEmail = document.getElementById('email-span')

function emailValidate(){
    if(inputEmail.value == ''){
        removeError()
        return
    }

    const regex = /^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$/i
    if (!regex.test(inputEmail.value)){
        setError()
        return
    }

    removeError()
}

function removeError(){
    spanEmail.style.display = 'none'
}

function setError(){
    spanEmail.style.display = 'block'
}