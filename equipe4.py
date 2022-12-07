'''
    Escreva um codigo que leia um numero de até 4 digitos e consiga determinar quantas unidades, dezenas, centanas e 
    unidades de milhar o numero tem, e repita enquanto o usuario nao digitar um numero inteiro
'''


def contar_unidades(n):
    numero = n
    dic = {}
    if numero >= 1000:
        dic['unidade de milhar'] = numero//1000
        numero -= 1000 * dic['unidade de milhar']
    if numero >= 100:
        dic['centenas'] = numero//100
        numero -= 100 * dic['centenas']
    if numero >= 10:
        dic['dezenas'] = numero//10
        numero -= 10 * dic['dezenas']
    dic['unidades'] = numero
    print(dic)


if __name__ == "__main__":
    while True:
        try:
            numero = int(input('Digite um numero inteiro: '))
            break
        except:
            print("Digite apenas numeros inteiros")

    contar_unidades(numero)
