'''
Crie uma função criar_caixa(valor_inicial) que retorna uma função interna que aceita:

"saldo": retorna o saldo atual
"sacar", valor: saca o valor, se houver saldo
"depositar", valor: adiciona ao saldo
'''

def sacar(x, y):
    return x - y

def depositar(x, y):
    return x + y

def criar_caixa(valor_inicial):
    saldo_em_caixa = valor_inicial
    
    def funcao_interna(*solicitacao):
        nonlocal saldo_em_caixa
        
        if solicitacao[0] == 'sacar':
            if solicitacao[1] <= saldo_em_caixa:
                saldo_em_caixa = sacar(saldo_em_caixa, solicitacao[1])
                return f'Saque de {solicitacao[1]} realizado'
            return 'Saldo insuficiente'
        
        elif solicitacao[0] == 'depositar':
            saldo_em_caixa = depositar(saldo_em_caixa, solicitacao[1])
            return f'Depósito de {solicitacao[1]} realizado'
        
        elif solicitacao[0] == 'saldo':
            return f'Saldo: {saldo_em_caixa}'
        
    return funcao_interna

#-----------------------------------------------------------------------------
# Execução do script

caixa = criar_caixa(100)

print(caixa("saldo"))
print(caixa("sacar", 40))
print(caixa('depositar', 10))
print(caixa('sacar', 20))
print(caixa("saldo"))
print(caixa('sacar', 60))