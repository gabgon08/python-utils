import os

while True:
    
    cpf_completo = input('Digite seu CPF: ')

    if len(cpf_completo) != 11:
        print('CPF deve conter 11 dígitos.')
        continue
        
    try:                
        cpf_completo_int = []
        multiplicacao_d1 = []
        multiplicacao_d2 = []

        # INT CONVERSÃO
        for digito in cpf_completo:
            digito_int = int(digito)
            cpf_completo_int.append(digito_int)

        # MULTIPLICAÇÃO PRIMEIRO DÍGITO
        multiplicador_d1 = 10

        for i in cpf_completo_int[0:9]:
            multiplicacao_d1.append(i * multiplicador_d1)
            multiplicador_d1 -= 1
            
        # SOMA PRIMEIRO DÍGITO
        soma_d1 = sum(multiplicacao_d1)

        # VERIFICAÇÃO PRIMEIRO DÍGITO
        resto_d1 = soma_d1 % 11
        digito1 = 0 if resto_d1 < 2 else 11 - resto_d1 

        # MULTIPLICAÇÃO SEGUNDO DÍGITO
        multiplicador_d2 = 11

        for i in cpf_completo_int[0:10]:
            multiplicacao_d2.append(i * multiplicador_d2)
            multiplicador_d2 -= 1

        # SOMA SEGUNDO DÍGITO
        soma_d2 = sum(multiplicacao_d2)

        #VERIFICAÇÃO SEGUNDO DÍGITO
        resto_d2 = soma_d2 % 11
        digito2 = 0 if resto_d2 < 2 else 11 - resto_d2

        # RESPOSTA FINAL
        if digito1 == cpf_completo_int[9] and digito2 == cpf_completo_int[10]:
            os.system('cls')
            print('CPF válido!')
            
        else:
            os.system('cls')
            print('CPF inválido')
        
    except:
        os.system('cls')
        print('Digite um número válido e tente novamente')