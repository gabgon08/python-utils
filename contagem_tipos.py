'''
Crie uma função que recebe uma lista com qualquer tipo de valor e retorne:

Quantos itens são str
Quantos são int
Quantos são listas
Quantos são dicionários
Use isinstance() para fazer a contagem.
'''

valores_mistos = ["MARINA", 2025, 8.9, True, ['Faustão', 'Cristina Rocha'], ["pop", "indie"], {"nome": "Addison Rae"}, ("álbum", 2024), {"eletrônico", "synthpop"},"Sabrina", 17, 4, False, [7, 14, 21], {"idade": 26}, ("gênero", "pop"), {"metal", "rock"}, "Red Velvet", 12, 2.5, True, ["K-pop", "R&B"], {"grupo": "feminino"}, ("país", "Coreia do Sul"), {"balada", "dance"}, "Taylor", 1989, 9.5, False, ["Midnights", "Folklore"]]

# MODO 1
def contagem_de_tipos(valores):

    contagem = {
        'str': 0,
        'int': 0,
        'list': 0,
        'dict': 0
    }


    for item in valores:
        if isinstance(item, str):
            contagem['str'] += 1
        elif isinstance(item, int):
            contagem['int'] += 1
        elif isinstance(item, list):
            contagem['list'] += 1
        elif isinstance(item, dict):
            contagem['dict'] += 1
            
    return contagem

resultado = contagem_de_tipos(valores_mistos)

print('A lista tem\n')
print(f"{resultado['str']} strings")
print(f"{resultado['int']} inteiros")
print(f"{resultado['list']} listas")
print(f"{resultado['dict']} dicionários")

#------------------------------------------------------------------------------------------------------

# MODO 2
def contagem_de_tipos(valores):

    contagem = [0, 0, 0, 0] # string, inteiro, lista, dicionario
    
    for valor in valores:
        if isinstance(valor, str):
            contagem[0]+=1
        elif isinstance(valor, int):
            contagem[1]+=1
        elif isinstance(valor, list):
            contagem[2]+=1
        elif isinstance(valor, dict):
            contagem[3]+=1
            
    return contagem

string, inteiro, lista, dicionario = contagem_de_tipos(valores_mistos)

print(f'\nA lista tem:\n\n{string} strings\n{inteiro} inteiros\n{lista} listas\n{dicionario} dicionários\n')