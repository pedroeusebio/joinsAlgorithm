# ED04 - Construção de Banco de Dados - UFRJ

* ## Alunos:
    * Eduardo Castanho
    * Henrique Maio
    * Pedro Eusébio

## Introdução

O trabalho contém dois arquivos em python. O arquivo file-generator.py é o script utilizado para os dados das tabelas utilizados nesse trabalho. O segundo arquivo é o arquivos que contem todos os algoritmos de *merge*.

## Tabelas

Foram gerados duas tabelas de dados. Uma tabela que contém apenas um indice e o resto preenchido com letras aleatoriamente. A segunda tabela contem o indice da tabela e uma chave estrangeira representada pelo indice da primeira tabela.

Exemplo:

Tabela1:

| Indice |      junk       |
| ------ | --------------- |
| 0      | AsDfGhJkLlZxXcV |
| 1      | AsDfGhJkLOIoihV |
| 2      | AKACiABkLlZxXcV |

Tabela 2:

| Indice | FK tabela 2 | junk           |
| ------ | ----------- | -------------- |
|  0     | 1           | ASgdAShawecshd |
|  1     | 2           | ASgdAShgdAjshd |
|  2     | 0           | ASgdAShgdKJHBM |


O script dentro do file-generator.py gera 2 tabelas e 4 arquivos csv. Dois csv ordenados pelo indice da tabela 2 e outros dois desordenados.

## Analise dos tempos




| Tamanho da Tabela | Nested Loop | Merge Join | Hash Join | BTree  |
| ----------------- | ----------- | ---------- | --------- | ------ | 
| 1000              | 5.17s       | 0.026s     | 0.049s    | 0.051s | 
| 10000             | 597.65s     | 0.249s     | 0.528s    | 0.652s |
| 100000            | N/A         | 3.142s     | 7.273s    | 8.316s |
