# Report de Análise de  Banco de Dados - Grupo Enzo e Ricardo

## Primeira Análise - Estrutura de tabelas

1. Falta de normalização dos nomes das tabelas - cliente com c minusculo e demais com inicio maiúsculo;
2. Falta de padrão no uso de singular/plural do nome das tabelas;

## Análise quanto as colunas das tabelas
### Tabela cliente;

1. Falta de informação de senha para realização do login;
2. Tamanho das colunas de e-mail muito pequeno;
3. Tamanho do campo de RG muito pequeno;
4. Campo de Sexo poderia ser uma tabela separada (economia de espaço);
5. Campo de data de nascimento deveria ser do tipo Date - Está Varchar;
6. Campo Situação ICMS poderia ser uma tabela separada;
7. Campo Alíquota deveria ser Float/Decimal;
8. Campo Situação Cadastro poderia ser uma tabela separada;
9. Campo Transportadoras poderia ser uma tabela separada;
10. Campo email_informacao não é muito explicativo, pode ser confundido com outro e-mail de contato;
11. Campos de Estado e Cidade poderiam ser separados;
12. Colunas de ensino_medio e ensino_superior poderiam ser apenas uma coluna com uma tabela extra - coluna escolaridade, por exemplo;
13. Colunas de CPF e CNPJ são Not Null, ou seja, devem ser preenchido, mas não deveriam - Cliente q é pessoal física apenas, por exemplo;

### Tabela EstruturaDeProdutos;

1. Tabela de Produtos, mas com identificador único chamado idpedido;
2. Coluna de código deveria ser maior (varchar 5 é muito pequeno para um código de barras)
3. Coluna Ordem poderia ser um inteiro;
4. Coluna status_pedido poderia ser uma tabela separada;
5. Coluna UM (Unidade de Medida), deveria ser um varchar, não int;

### Tabela NF;

1. Tabela não possui uma coluna com primary Key;
2. Existe uma coluna num_pedido, mas não tem uma tabela de pedidos;


### Tabela OrdemDeServico;