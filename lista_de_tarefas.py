from os import system
import json

tarefas_todas = []
tarefas_desfeitas = []


def adicionar(tarefas_todas):
    while True:
        tarefa = input('[0] Voltar\nDigite a tarefa: ')
        system('cls')
        
        if tarefa == '0': break
        tarefas_todas.append(tarefa)
        print('Tarefa adicionada com sucesso!\n')


def listar(tarefas_todas):
    if tarefas_todas:
        for i, tarefa in enumerate(tarefas_todas): print(i+1, tarefa, sep=' - ')
        print()
    else:
        print('Lista vazia\n')
        
        
def desfazer(tarefas_todas, tarefas_desfeitas):
    try:
        tarefas_desfeitas.append(tarefas_todas[-1])
        tarefas_todas.pop()
        
    except IndexError:
        print('Não há tarefas para desfazer\n')
        
    finally:
        listar(tarefas_todas)
    
    
def refazer(tarefas_todas, tarefas_desfeitas):
    try:
        tarefas_todas.append(tarefas_desfeitas[-1])
        tarefas_desfeitas.pop(-1)
        
    except IndexError:
        print('Não há tarefas para refazer\n')
        
    finally:
        listar(tarefas_todas)
    
def salvar(tarefas_todas):
    with open('lista_save.json', 'w', encoding='utf8') as f:
        json.dump(tarefas_todas, f, ensure_ascii=False, indent=2)
        system('cls')
        print('Arquivo salvo com sucesso!\n')
        
    
        
def carregar(tarefas_todas):
    try:
        with open('lista_save.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
            tarefas_todas.extend(dados)
            print('Arquivo carregado com sucesso!\n')
    except FileNotFoundError:
        print('Arquivo não encontrado\n')
        
    
while True:
    opcao = input('[1] Adicionar\n[2] Listar\n[3] Desfazer\n[4] Refazer\n[5] Salvar\n[6] Carregar\n[0] Sair\nDIGITE UMA OPÇÃO: ')
    system('cls')
    try:
        if opcao == '0': break

        opcoes = {
            '1': lambda: adicionar(tarefas_todas),
            '2': lambda: listar(tarefas_todas),
            '3': lambda: desfazer(tarefas_todas, tarefas_desfeitas),
            '4': lambda: refazer(tarefas_todas, tarefas_desfeitas),
            '5': lambda: salvar(tarefas_todas),
            '6': lambda: carregar(tarefas_todas),
        }
        
        acao = opcoes.get(opcao)
        acao()
        

    except TypeError:
        print('Digite uma opção válida e tente novamente')