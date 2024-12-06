<?php

function verifica_sessao($admin = false){
    if (empty($_SESSION) or !$_SESSION['logado']){
        $_SESSION["error"] = 'Efetue o login primeiro!';
        header('location: index.php');
        exit();
    }

    if($admin and !$_SESSION['usuario']['is_admin']){
        $_SESSION["error"] = 'Você não tem permissão para acessar aquela página!';
        header('location: user.php');
        exit();
    }
}