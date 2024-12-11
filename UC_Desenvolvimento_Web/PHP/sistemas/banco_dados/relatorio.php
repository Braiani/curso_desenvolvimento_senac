<?php
session_start();
include('./con.php');
include("./verifica_sessao.php");

verifica_sessao();

$query = "select * from produtos";

$result = mysqli_query($con, $query);

$rows = mysqli_fetch_all($result, MYSQLI_ASSOC);

?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Produtos</title>
    <!-- Link para o Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Estilos adicionais */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 250px;
            height: 100vh;
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
        <h2>Relatório de Produtos</h2>

        <div class="row mt-4">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Produtos Cadastrados</h5>
                        <div class="row">
                            <div class="col-3">
                                <button class="btn btn-success"
                                    data-bs-toggle="modal"
                                    data-bs-target="#createModal" >
                                    + Cadastrar Produto
                                </button>
                            </div>
                        </div>
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Nome</th>
                                    <th>Descrição</th>
                                    <th>Preço</th>
                                    <th>Ações</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach($rows as $row): ?>
                                <tr>
                                    <td><?= $row['id'] ?></td>
                                    <td><?= $row['nome'] ?></td>
                                    <td><?= $row['descricao'] ?></td>
                                    <td><?= $row['preco'] ?></td>
                                    <td>
                                        <button class="btn btn-warning btn-sm" 
                                            data-bs-toggle="modal" 
                                            data-bs-target="#editarModal" 
                                            onclick="preencherModal(<?= $row['id'] ?>, '<?= $row['nome'] ?>', '<?= $row['descricao'] ?>', <?= $row['preco'] ?>)"
                                        >
                                            Editar
                                        </button>
                                        <a href="#" class="btn btn-danger btn-sm">Excluir</a>
                                    </td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal de Edição -->
    <div class="modal fade" id="editarModal" tabindex="-1" aria-labelledby="editarModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="editarModalLabel">Editar Produto</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>
                </div>
                <div class="modal-body">
                    <form id="formEditarProduto">
                        <div class="mb-3">
                            <label for="nomeProduto" class="form-label">Nome do Produto</label>
                            <input type="text" class="form-control" id="nomeProduto" required>
                        </div>
                        <div class="mb-3">
                            <label for="descricaoProduto" class="form-label">Categoria</label>
                            <input type="text" class="form-control" id="descricaoProduto" required>
                        </div>
                        <div class="mb-3">
                            <label for="precoProduto" class="form-label">Preço</label>
                            <input type="number" class="form-control" id="precoProduto" required>
                        </div>
                        <button type="submit" class="btn btn-success">Salvar</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal de Criação -->
    <div class="modal fade" id="createModal" tabindex="-1" aria-labelledby="createModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="createModalLabel">Cadastrar Produto</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>
                </div>
                <div class="modal-body">
                    <form id="formEditarProduto">
                        <div class="mb-3">
                            <label for="nomeProduto" class="form-label">Nome do Produto</label>
                            <input type="text" class="form-control" id="nomeProduto" required>
                        </div>
                        <div class="mb-3">
                            <label for="descricaoProduto" class="form-label">Categoria</label>
                            <input type="text" class="form-control" id="descricaoProduto" required>
                        </div>
                        <div class="mb-3">
                            <label for="precoProduto" class="form-label">Preço</label>
                            <input type="number" class="form-control" id="precoProduto" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Salvar</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Link para o Bootstrap 5 JS e dependências -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
    <script>
        // Função para preencher o modal com os dados do produto a ser editado
        function preencherModal(id, nome, descricao, preco) {
            document.getElementById('nomeProduto').value = nome;
            document.getElementById('descricaoProduto').value = descricao;
            document.getElementById('precoProduto').value = preco;
        }

        // Função para tratar o envio do formulário de edição
        document.getElementById('formEditarProduto').addEventListener('submit', function (event) {
            event.preventDefault();
            // Aqui você pode adicionar a lógica para salvar as alterações, por exemplo, enviar os dados para o servidor.
            alert('Produto editado com sucesso!');
            // Fechar o modal após o envio
            var modal = bootstrap.Modal.getInstance(document.getElementById('editarModal'));
            modal.hide();
        });
    </script>
</body>

</html>
