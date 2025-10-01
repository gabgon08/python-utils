'''
Exercício:
Dado um dicionário de contatos com nome: telefone, agrupe todos os nomes por inicial (nome maiúscula) e mostre os grupos.
'''

lista_de_contatos = {
    'Bruno Silva': '(31) 91234-5678',
    'Carlos Andrade': '(51) 93456-7890',
    'Daniel Torres': '(71) 98712-3456',
    'Alice Martins': '(11) 98765-4321',
    'Clara Neves': '(61) 94567-8901',
    'Eduarda Lima': '(81) 95678-9012',
    'Aline Moraes': '(21) 99887-7766',
    'Giovana Rocha': '(85) 96789-1234',
    'Beatriz Souza': '(41) 97654-3210',
    'Felipe Mendes': '(91) 94321-6789',
}

# DEFINIR INICIAIS
def definir_iniciais(contatos):
    return sorted({nome[0] for nome in contatos})    
    
# AGRUPAR NOMES
def agrupar_nomes(contatos):
    
    nomes_agrupados = {}

    for nome in contatos:
        inicial = nome[0]
        nomes_agrupados.setdefault(inicial, []).append(nome)
        
    for inicial in sorted(nomes_agrupados):
        nomes = nomes_agrupados[inicial]
        print(f'{inicial}:\n{', '.join(nomes)}\n')