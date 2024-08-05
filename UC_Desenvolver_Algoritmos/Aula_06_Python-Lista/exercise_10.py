print("""
Enunciado do exercício:
      10. Um almoxarifado controla o estoque de 5 produtos indentificados pelo seu código abaixo:

+======================+
|  Código  |  Produto  |
+==========+===========+
|    10    | -Caderno  |
|    20    | -Caneta   |
|    30    | -Lápis    |
|    40    | -Borracha |
|    50    | -Régua    |
+======================+

Faça um programa que leia o estoque inicial de cada um dos produtos,
e depois processe um certo número de operações, de acordo com o código abaixo:

+=======================================================================================================+
|  Código  |      Operação      |                                Ação                                   |
|----------+--------------------+-----------------------------------------------------------------------|
|     E    | Entrada do Estoque | Ler o código do produto que está entrando no estoque e a quantidade.  |
|          |                    | Atualizar o estoque do produto.                                       |
|----------+--------------------+-----------------------------------------------------------------------|
|     S    | Saída no Estoque   | Ler o código do produto que está saindo do estoque e a quantidade.    |
|          |                    | Atualizar o estoque do produto.                                       |
|----------+--------------------+-----------------------------------------------------------------------|
|     R    |     Relatório      | Imprime um relatório mostrando as quantidades atuais de cada produto. |
|----------+--------------------+-----------------------------------------------------------------------|
|     X    |       Sair         | Encerra a execução do programa.                                       |
+=======================================================================================================+

Antes de ler cada operação, o programa deve imprimir um menu de opções, assim:

Escolha a operação:
E -Entrada no Estoque;
S -Saída no Estoque;
R -Relatório;
X -Sair;

A operação de saída do estoque deve checar se a quantidade em estoque é suficiente para atender
à quantidade que está sendo retirada do estoque. Se não for, deve exibir mensagem e impedir a operação.
""")