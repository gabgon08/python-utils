'''
Exercício:
Crie um programa que permita ao usuário adicionar tarefas a uma lista. Cada tarefa deve ser um dicionário com as chaves: "tarefa", "prioridade" (1 a 5), e "concluída" (True/False).

Permita adicionar várias tarefas.
Crie uma função para listar todas as tarefas, ordenadas por prioridade (do maior para o menor).
Crie uma função para mostrar apenas as tarefas que ainda não foram concluídas.
Crie uma função para marcar uma tarefa como concluída, pelo nome da tarefa.
'''

import os
lista_de_tarefas = [{'tarefa': 'Jogar lixo fora', 'prioridade': 3, 'concluida': True}, {'tarefa': 'Ir pra academia', 'prioridade': 4, 'concluida': False}]


# [1] LISTAR TODAS AS TAREFAS
def listar_tarefas(lista):
    
    lista_ordenada = sorted(lista, reverse=True, key=lambda chave: chave['prioridade'])

    print('LISTA DE TAREFAS\n')
    
    for dicionario in lista_ordenada:
        print(f'TAREFA: {dicionario['tarefa']}')
        print(f'PRIORIDADE: {dicionario['prioridade']}')
        print(f'CONCLUÍDA: {'Não' if not dicionario['concluida'] else 'Sim'}\n')
        
    print('-'*50)


# [2] ADICIONAR TAREFA
def adicionar_tarefa(lista):
        
    print('ADICIONAR TAREFA\n')
    
    tarefa = input('TAREFA: ')
    prioridade = input('PRIORIDADE: ')
    lista.append({'tarefa': tarefa, 'prioridade': int(prioridade), 'concluida': False})
    os.system('cls')
    
    print(f'Tarefa adicionada com sucesso!\n')


# [3] LISTAR TAREFAS NÃO CONCLUÍDAS
def listar_tarefas_nao_concluidas(lista):
    
    lista_ordenada = sorted(lista, reverse=True, key=lambda chave: chave['prioridade'])
    
    print('TAREFAS NÃO CONCLUÍDAS\n')
    
    for dicionario in lista_ordenada:    
        if not dicionario['concluida']:
            print(f'TAREFA: {dicionario['tarefa']}')
            print(f'PRIORIDADE: {dicionario['prioridade']}\n')
    
    print('-'*50)        


# MARCAR TAREFA COMO CONCLUÍDA PELO NOME
def marcar_tarefa_como_concluida(lista):
        
    listar_tarefas_nao_concluidas(lista)
    
    tarefa = input('Marcar como concluída: ')
    tarefa_encontrada = False
    
    for dicionario in lista:
        if dicionario['tarefa'] == tarefa:
            dicionario['concluida'] = True
            os.system('cls')
            print('Operação feita com sucesso!\n')
    
    if not tarefa_encontrada:
        os.system('cls')
        print('Tarefa não encontrada\n')
            
    
# MENU
def menu_principal():

    while True:
        opcao = input('MENU PRINCIPAL\n[1] Listar tarefas\n[2] Adicionar tarefa\n[3] Listar tarefas não concluídas\n[4] Marcar tarefa como concluída\n[0] SAIR\n\nDigite uma opção: ')
        
        if opcao in '1234':
            os.system('cls')
            funcoes = [
                listar_tarefas,
                adicionar_tarefa,
                listar_tarefas_nao_concluidas,
                marcar_tarefa_como_concluida
            ]
            funcoes[int(opcao)-1](lista_de_tarefas)
        elif opcao == '0':
            break
        else:
            os.system('cls')
            print('Digite uma opção válida e tente novamente\n')
            continue
        
menu_principal()