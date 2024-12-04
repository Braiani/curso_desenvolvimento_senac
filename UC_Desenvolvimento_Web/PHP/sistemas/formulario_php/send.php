<?php

if (!isset($_POST) or empty($_POST)) {
    echo "<script>window.location = 'index.html'</script>";
}

//var_dump($_POST['sexo']);

function translatePergunta($pergunta): String {
    $listaPerguntas = [
        "nome" => "Nome Completo",
        "rg" => "RG",
        "cpf" => "CPF",
        "epoca_ano" => "Época do Ano",
        "endereco" => "Endereço",
        "idade" => "Idade",
        "sexo" => "Sexo",
        "data" => "Data",
        "instagram" => "Instagram",
        "twitter" => "Twitter (X)",
        "usuario" => "Usuário",
        "profissao" => "Profissão",
        "comentario" => "Comentários",
        "cor" => "Cor",
    ];

    if (! array_key_exists($pergunta, $listaPerguntas)){
        return 'Pergunta não reconhecida';
    }

    return $listaPerguntas[$pergunta];
}


?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Cliente</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <div class="container-sm">
        <div class="card mt-4">
            <div class="card-title">
                <div class="m-3 text-center">
                    <h1>Resultado dos dados preenchidos</h1>
                </div>
            </div>
            <div class="card-body">
                <table class="table table-hover">
                    <thead>
                        <tr>
                        <th scope="col">Pergunta</th>
                        <th scope="col">Resposta</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($_POST as $pergunta => $resposta): ?>
                        <tr>
                            <th scope="row">
                                <?= translatePergunta($pergunta) ?>
                            </th>
                            <td>
                                <?= $resposta ?>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
        integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
        crossorigin="anonymous"></script>
</body>
</html>