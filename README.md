# python-utils
<h3>Um repositório com pequenos scripts e utilitários em Python, criados para aprendizado, prática e automação de tarefas do dia a dia.</h3><br>

**💡OBJETIVO:**
Centralizar códigos pequenos, mas úteis, que podem servir tanto como referência para estudos quanto como ferramentas rápidas no dia a dia.

**📌CONTEÚDO:**
- Scripts simples para resolver problemas práticos.
- Exercícios e experimentos de estudos em Python.
- Exemplos de manipulação de arquivos, listas e dicionários.
---

## 📂 Scripts incluídos

**adivinha_palavra.py** → Jogo de adivinhação de palavras no terminal:
  - jogador digita a palavra secreta
  - usuário tenta adivinhar letra por letra
  - exibe progresso com '*' para letras não acertadas
  - termina quando a palavra completa é descoberta
##
**agrupar_contatos.py** → Script que agrupa nomes de contatos por inicial:
  - dado um dicionário nome: telefone
  - organiza os nomes por letra inicial maiúscula
  - exibe cada grupo de nomes agrupados pela inicial
##
**caixa_eletronico.py** → Simulação de caixa eletrônico com closures:
  - inicia com um valor definido (`criar_caixa(valor_inicial)`)
  - permite consultar saldo
  - permite sacar valores (se houver saldo suficiente)
  - permite depositar valores
  - mantém o saldo atualizado entre as operações
##
**contagem_tipos.py** → Script que conta tipos de elementos em uma lista:
  - recebe uma lista com qualquer tipo de valor
  - conta quantos elementos são `str`, `int`, `list` e `dict`
  - utiliza `isinstance()` para fazer a contagem
  - exibe o total de cada tipo no terminal
##
**filtro_condicional.py** → Sistema de filtros condicionais com closures:
  - permite adicionar funções de filtragem
  - permite verificar valores aplicando todos os filtros
  - retorna True apenas se todas as funções aprovarem o valor
##
**gerenciador_tarefas.py** → Programa de gerenciamento de tarefas no terminal:
  - adiciona tarefas com nome, prioridade (1–5) e status (concluída ou não)
  - lista todas as tarefas ordenadas por prioridade
  - mostra apenas as tarefas não concluídas
  - permite marcar tarefas como concluídas pelo nome
  - possui menu interativo para navegação
##
**lista_de_tarefas.py** → Gerenciador de tarefas no terminal, com opções de:
  - adicionar e listar tarefas
  - desfazer e refazer ações
  - salvar em arquivo JSON
  - carregar tarefas salvas
##
**manipulacao_produtos.py** → Script que realiza operações em uma lista de produtos:
  - aumenta os preços em 10% (gera novos_produtos)
  - ordena produtos por nome decrescente (gera produtos_ordenados_por_nome)
  - ordena produtos por preço crescente (gera produtos_ordenados_por_preco)
##
**mini_quiz.py** → Quiz no terminal:
  - perguntas de múltipla escolha com cinco opções cada
  - jogador digita a letra da resposta
  - informa se a resposta está correta ou incorreta
  - exibe o total de acertos ao final
##
**validar_cpf.py** → Script para validar CPF no terminal:
  - usuário digita um CPF de 11 dígitos
  - calcula os dígitos verificadores
  - informa se o CPF é válido ou inválido

