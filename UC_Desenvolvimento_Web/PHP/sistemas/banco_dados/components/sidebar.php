<?php
$dashboard = $_SESSION['usuario']['is_admin'] ? 'admin.php' : 'user.php';
?>

<div class="sidebar">
    <h4 class="text-center text-white">Menu</h4>
    <ul class="nav flex-column">
        <li class="nav-item">
            <a class="nav-link text-white" href="./<?= $dashboard ?>">Dashboard</a>
        </li>
        <li class="nav-item">
            <a class="nav-link text-white" href="./relatorio.php">Relatórios</a>
        </li>
        <li class="nav-item">
            <a class="nav-link text-white" href="./clients.php">Cadastrar Cliente</a>
        </li>
        <?php if($usuarioLogado['is_admin']){ ?>
        <li class="nav-item">
            <a class="nav-link text-white" href="./admin.php">Ambiente Administrativo</a>
        </li>
        <?php } ?>
        <li class="nav-item">
            <a class="nav-link text-white" href="./logout.php">Sair</a>
        </li>
    </ul>
</div>