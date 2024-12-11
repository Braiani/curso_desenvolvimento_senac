<?php
session_start();
include("./verifica_sessao.php");
include_once('./con.php');

verifica_sessao(false);
$usuarioLogado = $_SESSION['usuario'];

$query = "select count(*) as count from users;";

try {
    $result = mysqli_query($con, $query);

    $users = mysqli_fetch_assoc($result);
} catch (mysqli_sql_exception $e) {
    echo "Falha na conexão: $e";
    exit;
}

?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Simples Usuário</title>
    <!-- Link para o Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Estilos adicionais */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .dashboard-card {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 250px;
            height: 100vh;
            /* Altura total da janela */
            background-color: #c75136;
            color: white;
            padding-top: 20px;
        }

        .content {
            margin-left: 250px;
            padding: 20px;
        }

        .sidebar .nav-link {
            color: white;
        }

        .sidebar .nav-link:hover {
            background-color: #495057;
        }
    </style>
</head>

<body>
    <?php include('components/sidebar.php'); ?>

    <div class="content">
        <h2>Dashboard Usuário Comum</h2>
        <?php if (isset($_SESSION['error']) and !empty($_SESSION['error'])): ?>
            <div class="row mt-4">
                <div class="alert alert-danger" role="alert">
                    <?= $_SESSION['error'] ?>
                </div>
            </div>
        <?php
            unset($_SESSION['error']);
        endif;
        ?>
        <div class="row mt-4">
            <!-- Card 1 -->
            <div class="col-md-4 mb-4">
                <div class="card dashboard-card">
                    <div class="card-body">
                        <h5 class="card-title">Usuários</h5>
                        <p class="card-text">Número total de usuários.</p>
                        <h3 class="text-center">
                            <?= $users['count'] ?>
                        </h3>
                    </div>
                </div>
            </div>
            <!-- Card 2 -->
            <div class="col-md-4 mb-4">
                <div class="card dashboard-card">
                    <div class="card-body">
                        <h5 class="card-title">Livros</h5>
                        <p class="card-text">Total de livros cadastrados.</p>
                        <h3 class="text-center">50</h3>
                    </div>
                </div>
            </div>
            <!-- Card 3 -->
            <div class="col-md-4 mb-4">
                <div class="card dashboard-card">
                    <div class="card-body">
                        <h5 class="card-title">Clientes</h5>
                        <p class="card-text">Total de clientes cadastrados.</p>
                        <h3 class="text-center">12</h3>
                    </div>
                </div>
            </div>
        </div>

        <div class="mt-5">
            <h4>Seja Bem-vindo, <?= $usuarioLogado['nome'] . ' - ' . $usuarioLogado['email']; ?></h4>
        </div>

        <!-- Gráfico ou Estatísticas -->
        <div class="mt-5">
            <h4>Gráfico de Desempenho</h4>
            <div class="alert alert-info" role="alert">
                Este seria um gráfico de desempenho, mas por enquanto é apenas um espaço para você adicionar.
            </div>
        </div>
    </div>

    <!-- Link para o Bootstrap 5 JS e dependências -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</body>

</html>