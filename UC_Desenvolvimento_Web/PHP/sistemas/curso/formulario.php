<?php

$nome = $_POST['nome'];
$sistema = $_POST['sistema'];
$professores = $_POST['prof'];

echo "O nome digitado foi $nome <br>";
echo "O seu sistema operacional é $sistema <br>";

$teachers = '';
foreach($professores as $professor){
    $teachers .= "$professor, ";
}
echo "Seus professores são: $teachers";