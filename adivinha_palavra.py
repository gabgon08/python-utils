import os

palavra_secreta = input('Digite a palavra secreta:').upper()
os.system('cls')

letras_certas = ''
palavra_final = ''
cont = 0

while True:
    palpite = input("Digite uma letra:").upper()
    
    if len(palpite) !=1:
        print('Por favor, digite apenas uma letra\n')
        continue
    
    elif not palpite.isalpha():
        print('Por favor, digite apenas letras\n')
        continue

    for letra in palavra_secreta:
        if palpite == letra:
            letras_certas += letra
            continue
        else:
            continue

    for i in palavra_secreta:
        if i in letras_certas:
            palavra_final += i
        else:
            palavra_final += '*'
    
    if palavra_final == palavra_secreta:
        print(f"Você achou a palavra secreta! '{palavra_final}'")
        break
    else:
        print(palavra_final)
        palavra_final = ''
        continue