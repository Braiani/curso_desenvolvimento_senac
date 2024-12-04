<?php

session_start();
include_once('con.php');

$email = $_POST['email'];
$senha = $_POST['senha'];

if (empty($email) or empty($senha)){
    $_SESSION["error"]= 'Por favor, preencha todos os campos!';
    header('location: index.php');
    exit();
}