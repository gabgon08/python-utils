'''
Crie uma função filtro_condicional() que retorna uma função filtrar(dado).

Cada vez que filtrar() é chamada com uma tupla do tipo ('adicionar', func) ou ('verificar', valor), o closure deve armazenar as funções de filtragem e aplicar todas sobre o valor passado, retornando True somente se todas as funções aprovarem o valor.

Exemplo:
filtro = filtro_condicional()
filtro(('adicionar', lambda x: x > 10))
filtro(('adicionar', lambda x: x % 2 == 0))

print(filtro(('verificar', 12)))  # True
print(filtro(('verificar', 9)))   # False
'''

def filtro_condicional():
    
    filtros = []
    
    def filtrar(dado):
        opcao = dado[0]
        valor = dado[1]
        
        # opcao, valor = dado (desempacotamento)
        
        if opcao == 'adicionar':
            filtros.append(valor)
            
        elif opcao == 'verificar':
            verificacao = [i(valor) for i in filtros]
            return False if False in verificacao else True
        
        # alternativa usando 'all()': return all(i(valor) for i in filtros)
                    
    return filtrar


filtro = filtro_condicional()

filtro(('adicionar', lambda x: x > 5))
filtro(('adicionar', lambda x: x%2 == 0))
print(filtro(('verificar', 10)))
print(filtro(('verificar', 4)))
print(filtro(('verificar', 8)))