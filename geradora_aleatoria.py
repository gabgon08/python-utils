'''
Implemente um gerador que simule uma sequência pseudo-aleatória com base em um valor inicial (seed), usando a fórmula:
novo_valor = (anterior * 7 + 3) % 100
'''

def geradora_aleatoria(seed, n):
    anterior = seed
    novo_valor = 0
    
    for _ in range(n):
        novo_valor = (anterior * 7 + 3) % 100
        anterior = novo_valor
        yield novo_valor
        
for i in geradora_aleatoria(1, 8):
    print(i)