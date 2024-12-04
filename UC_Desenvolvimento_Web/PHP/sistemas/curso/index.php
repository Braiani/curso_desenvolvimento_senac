<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aulas de PHP</title>
</head>
<body>
    <?php
    define('MIN_VALUE', '20');
    // const MIN_VALUE = '20';
    $color = "preto";
    echo "Meu carro é ". $color ."<br>";
    echo "Minha casa é ". $COLOR ."<br>";
    echo "Minha bicicleta é ". $coLoR ."<br>";
    echo "Constante: ". MIN_VALUE ."<br>";

    $nota = [];
    $nota[1] = 10;
    $nota[2] = 8;
    $nota[3] = 6;
    $nota[4] = 10;

    $i = 0;
    $soma = 0;
    $media = 0;
    while ($i < count($nota)){
        $soma += $nota[$i];
        $i++;
    }
    
    $media = $soma/count($nota);

    echo "Média: $media!"
    ?>
</body>
</html>