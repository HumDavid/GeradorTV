# Gerador de Tabela Verdade

Este programa lê a descrição de um circuito digital a partir de um arquivo `Circ.txt` e gera sua tabela verdade no arquivo `Saida.txt`.

## Formato do `Circ.txt`

O arquivo deve conter **uma variável com nome e valor separados por "="**, onde o valor é um dicionário com a descrição do circuito.

Você pode usar **quebras de linha, indentação e espaços à vontade**.

### Exemplo válido:

```
circ_teste =
    {'entradas': ['a0', 'b0', 'a1', 'b1'],
    'saidas': ['s0', 's1', 'c'],
    'gates': ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7'],
    'g1': ['xor', 's0', 'a0', 'b0'],
    'g2': ['xor', 's1', 't0', 't1'],
    'g3': ['xor', 't0', 'a1', 'b1'],
    'g4': ['or', 'c', 't2', 't3'],
    'g5': ['and', 't2', 't0', 't1'],
    'g6': ['and', 't1', 'a0', 'b0'],
    'g7': ['and', 't3', 'a1', 'b1']}
```

## Observações:
->  O nome antes do `=` será usado como nome do circuito no arquivo de saída.
->  Pode usar quantas quebras de linha e indentação quiser.
->  Use aspas simples `'` nos nomes de variáveis e portas.
