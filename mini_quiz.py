lista_de_perguntas = [
    {
        'Pergunta': '1 - Qual o primeiro single do álbum reputation?',
        'Opções': [
            'a) Delicate',
            'b) Look What You Made Me Do',
            'c) End Game',
            'd) King of My Heart',
            'e) ...Ready For It?'
            ],
        'Resposta': 'B'
    },
    
    {
        'Pergunta': '2 - Qual o primeiro álbum regravado lançado por Taylor Swift?',
        'Opções': [
            'a) 1989',
            'b) RED',
            'c) Speak Now',
            'd) folklore',
            'e) Fearless'
            ],
        'Resposta': 'E'
    },
    
    {
        'Pergunta': '3 - Qual o nome da turnê de comemoração de carreira da Taylor Swift?',
        'Opções': [
            'a) The Red Tour',
            'b) The Celebration Tour',
            'c) The Eras Tour',
            'd) The Best of Me Tour',
            'e) Tayparty Tour'
            ],
        'Resposta': 'C'
    },
    
    {
        'Pergunta': '4 - Quem é a artista feminina que faz feat. em Snow On The Beach?',
        'Opções': [
            'a) Lana Del Rey',
            'b) Ice Spice',
            'c) Sabrina Carpenter',
            'd) Florence Welch',
            'e) Beyoncé'
            ],
        'Resposta': 'A'
    }
]

contador_de_acertos = 0

def quiz(numero_da_pergunta, contador):
    pergunta = lista_de_perguntas[numero_da_pergunta]
    
    print(f"{pergunta['Pergunta']}\n")
    
    for opcao in pergunta['Opções']:
        print(opcao)
    
    resposta = input('\nResposta: ').upper()

    def conferir_resposta(resposta, contador):
        if resposta == pergunta['Resposta']:
            contador += 1
            return contador, '\nParabéns! Você acertou :)\n'
        return contador, '\nResposta incorreta :(\n'
    
    contador, mensagem = conferir_resposta(resposta, contador)
    print(mensagem)
    return contador

for i in range(len(lista_de_perguntas)):
    contador_de_acertos = quiz(i, contador_de_acertos)

print(f'Você acertou {contador_de_acertos} de {len(lista_de_perguntas)} questões!')