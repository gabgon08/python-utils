'''Exercício:
- Aumente os preços dos produtos a seguir em 10%
- Gere 'novos_produtos' por deep copy

- Ordene os produtos por nome decrescente (do maior para menor)
- Gere 'produtos_ordenados_por_nome' por deep copy (cópia profunda)

- Ordene os produtos por preco crescente (do menor para maior)
- Gere 'produtos_ordenados_por_preco' por deep copy (cópia profunda)'''

#-----------------------------------------------------------------------------------------------------------------------------------
import copy

produtos = [
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# CÓPIA PROFUNDA
def copia_profunda(lista):
    return copy.deepcopy(lista)


# EXIBIR PRODUTOS
def exibir_produtos(funcao):
    for produto in funcao:
        print(f'NOME: {produto['nome']}\nPREÇO: {produto['preco']:.2f}\n')


# AUMENTAR 10%
def aumentar_preco_em_dez_por_cento(lista):
    print('AUMENTO DE 10%\n')
    
    copia_lista = copia_profunda(lista)
    
    for produto in copia_lista:
        produto.update(preco=produto['preco']*1.1)
        
    return copia_lista


# ORDENAR POR NOME (DECRESCENTE)
def ordenar_por_nome(lista):
    print('POR NOME (DECRESCENTE)\n')
        
    produtos_ordenados_por_nome = sorted(copia_profunda(lista), key=lambda chave: chave['nome'], reverse=True)
    
    return produtos_ordenados_por_nome

        
# ORDENAR POR PREÇO (CRESCENTE)
def ordenar_por_preco(lista):
    print('POR PREÇO (CRESCENTE)\n')
        
    produtos_ordenados_por_preco = sorted(copia_profunda(lista), key=lambda chave: chave['preco'])
    
    return produtos_ordenados_por_preco        
        
# exibir_produtos(aumentar_preco_em_dez_por_cento(ordenar_por_preco(produtos)))

if __name__ == "__main__":
    # 1. Aumente os preços dos produtos a seguir em 10%
    novos_produtos = aumentar_preco_em_dez_por_cento(produtos)
    exibir_produtos(novos_produtos)

    # 2. Ordene os produtos por nome decrescente
    produtos_ordenados_por_nome = ordenar_por_nome(produtos)
    exibir_produtos(produtos_ordenados_por_nome)

    # 3. Ordene os produtos por preço crescente
    produtos_ordenados_por_preco = ordenar_por_preco(produtos)
    exibir_produtos(produtos_ordenados_por_preco)