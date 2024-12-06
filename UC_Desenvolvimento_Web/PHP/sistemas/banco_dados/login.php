<?php

session_start();
include_once('con.php');

$email = $_POST['email'];
$senha = $_POST['senha'];
// $email = mysqli_real_escape_string($con, $_POST['email']);
// $senha = mysqli_real_escape_string($con, $_POST['senha']);

if (empty($email) or empty($senha)){
    $_SESSION["error"] = 'Por favor, preencha todos os campos!';
    header('location: index.php');
    exit();
}

$query = "SELECT * FROM users WHERE email = '{$email}' AND senha = '{$senha}'";

$result= mysqli_query($con, $query);


$row = mysqli_num_rows($result);
$user = mysqli_fetch_assoc($result);

if ($row === 0){
    $_SESSION["error"] = 'Por favor, verifique os dados e tente novamente!';
    header('location: index.php');
    exit();
}

$_SESSION["logado"] = true;
$_SESSION["usuario"] = $user;

if ($user['is_admin']){
    header('location: admin.php');
    exit;
}
header('location: user.php');