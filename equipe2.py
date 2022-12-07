'''
    Escreva um programa para ler uma senha e verificar se a mesma contém as exigências de segurança.Pelo menos 
    um caractere maiúsculo e um minúsculo,além de conter números e letras, bem como contenha no minimo 4
    e no maximo 8
'''


def verifsenha(senha):
    numeros = False
    maiusculo = False
    minusculo = False
    if len(senha) >= 4 and len(senha) <= 8:
        if senha.lower() != senha:
            minusculo = True
        else:
            print('senha não contém letras minusculas')
        if senha.upper() != senha:
            maiusculo = True
        else:
            print('senha não contém letras maiúsculas')
        for letra in senha:
            if letra.isnumeric():
                numeros = True
        if not numeros:
            print('senha não contém numeros')
        if maiusculo and minusculo and numeros:
            print('senha segura')
        else:
            print('senha nao é segura')
    else:
        print('Senha com tamanho invalido')


while True:
    senha = input('digite uma senha: ')
    if senha == 'sair':
        break
    verifsenha(senha)
