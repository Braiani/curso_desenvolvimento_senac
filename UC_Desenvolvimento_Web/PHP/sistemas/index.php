<?php

function listarDiretorios($diretorio) {
    
    if (!is_dir($diretorio)) {
        echo "Diretório não encontrado.";
        return;
    }

    $itens = scandir($diretorio);
    $diretorios = array();

    foreach ($itens as $item) {
        
        if ($item == "." || $item == "..") continue;

        $caminho = $diretorio . DIRECTORY_SEPARATOR . $item;

        
        if (is_dir($caminho)) {
            $diretorios[] = $caminho;
        }
    }

    return $diretorios;
}

$diretorioAtual = '.';

$listaDiretorios = listarDiretorios($diretorioAtual);

?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Diretórios e Arquivos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container mt-5">
    <h1 class="mb-4">Lista de Diretórios e Arquivos</h1>
    <!-- <p><strong>Diretório Atual:</strong> <span id="diretorio-atual">/caminho/do/diretorio</span></p> -->

    <div class="list-group">
        <?php foreach($listaDiretorios as $diretorio){ ?>
        <a href="<?= $diretorio; ?>" class="list-group-item list-group-item-action list-group-item-primary">
            <?= $diretorio; ?>
        </a>
        <?php } ?>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
