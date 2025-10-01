'''
Crie uma função que recebe dois números e uma operação (+, -, *, /). Trate os seguintes erros:

Divisão por zero
Operação inválida
Entrada não numérica

Entrada:
calc(10, 'a', '*')
'''
import operator

def calculadora(x, y, op):
    
    operadores = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    try:
        conta = operadores[op](x, y)
        return f'{x} {op} {y} é: {conta}'
    
    except TypeError:
        return 'ERRO: Digite um valor numérico'
    
    except ZeroDivisionError:
        return 'ERRO: Não é possível dividir por zero'
    
    except KeyError:
        return f"ERRO: '{op}' não é um operador válido, tente novamente"
    
        
print(calculadora(10, 20, '-'))
