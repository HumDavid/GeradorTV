def corrigir_dicionario(info):
  corrigido = ""
  i = 0

  while i < len(info):
    char = info[i]

    if char.isalnum() or char == "_":
      palavra = ""
      while i < len(info) and (info[i].isalnum() or info[i] == "_"):
        palavra += info[i]
        i += 1

      if palavra.isdigit() or palavra in ["True", "False", "null"] or corrigido.endswith("'") or corrigido.endswith('"'):
        corrigido += palavra
      else:
        corrigido += f'"{palavra}"'
      continue

    corrigido += char
    i += 1

  return corrigido

#LEITURA DO DICIONÁRIO
with open("Circ.txt", "r") as c:
  dados = c.read()

nome, info = dados.split("=", 1)
nome = nome.strip()
info = info.strip()

info_corrigido = corrigir_dicionario(info)
dicionario = eval(info_corrigido)

#OPERAÇÕES
def and_porta(val_vars):
  for it in val_vars:
    if it == 0:
      return 0
  return 1

def or_porta(val_vars):
  for it in val_vars:
    if it == 1:
      return 1
  return 0

def xor_porta(val_vars):
  final = 0
  for it in val_vars:
    if it == 1:
      final = 1 - final
  return final

#TABELA VERDADE
with open("Saida.txt", "w") as saida:
  entradas = dicionario["entradas"]
  saidas = dicionario["saidas"]
  gates = dicionario["gates"]
  n_variaveis = len(entradas)
  colunas = entradas + saidas

  saida.write(f"Nome do circuito: {nome}\n")
  saida.write(" | ".join(colunas) + "\n")
  saida.write("-" * (4 * len(colunas)) + "\n")

  valores = {}
  n_linhas = 2 ** n_variaveis

  for i in range(n_linhas):
    linha = []
    pendentes = gates[:]
    disponiveis = set(entradas)

    for j in range(n_variaveis):
      freq = 2 ** (n_variaveis - j - 1)
      valor = (i // freq) % 2
      valores[entradas[j]] = valor
      linha.append(valor)

    while pendentes:
      for gate in pendentes[:]:
        gate_info = dicionario[gate]
        operador = gate_info[0]
        saida_var = gate_info[1]
        entradas_gate = gate_info[2:]

        if all(var in disponiveis for var in entradas_gate):
          if operador == "and":
            resultado = and_porta([valores[var] for var in entradas_gate])
          elif operador == "nand":
            resultado = 1 - and_porta([valores[var] for var in entradas_gate])
          elif operador == "or":
            resultado = or_porta([valores[var] for var in entradas_gate])
          elif operador == "nor":
            resultado = 1 - or_porta([valores[var] for var in entradas_gate])
          elif operador == "xor":
            resultado = xor_porta([valores[var] for var in entradas_gate])
          elif operador == "nxor":
            resultado = 1 - xor_porta([valores[var] for var in entradas_gate])
          elif operador == "not":
            resultado = 1 - valores[entradas_gate[0]]

          valores[saida_var] = resultado
          disponiveis.add(saida_var)
          pendentes.remove(gate)

    linha += [valores[var] for var in saidas]
    saida.write(" | ".join(map(str, linha)) + "\n")
