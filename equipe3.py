"""
    Enunciado = Crie uma aplicação que recebe um número em romano (Ex: "XIX"),
    se não for dígitos romanos, reporta um erro, e depois transforme esse número em cardinal
"""

# Função que recebe o numero romano
def decodificador(numero):
    # Dicionario com o simbolo em romano e seu valor
    dic = {'I': 1, 'IV': 4, 'V': 5,'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
           'CD':400, 'D': 500, 'CM': 900, 'M': 1000}

    # Caracteres que aparecem junto com outros caracteres
    caracter_especiais = ["I", "X", "C"]

    # Por questao de boa pratica nao se trabalha com o parametro que recebeu
    # Então fiz uma variavel receber o parametro
    # E para não ter um erro de formatação, fiz eles ficarem maiúsculo
    numero_romano = numero.upper()

    # variavel que vai receber a soma dos numeros romanos
    valor = 0

    # Uma flag para me informar que aquele numero ja foi contado
    # No caso de ser "IV", para ele não contar o 'V' novamente
    flag = False

    # vai percorrer de 0 ate o tamanho da minha lista
    for i in range(len(numero_romano)): 
        # Se esse valor ainda nao foi contando
        if not flag:
            # verifico se ele ta no Dicionario
            if numero_romano[i] in dic:
                # Se o caracter é um dos especiais
                if numero_romano[i] in caracter_especiais and i < len(numero_romano)-1:
                    # Se o que vem depois desse é um especial tambem
                    # E ainda exista um caractere apos ele
                    # Vai concatenar eles
                    auxiliar = numero_romano[i] + numero_romano[i+1]
                    # Se eles existem no meu dicionario vou pegar os valores dele
                    if auxiliar in dic:
                        # Pego o valor dele e efetuo a soma
                        valor += dic[auxiliar]
                        # Aviso que o proximo numero ja foi contado
                        flag = True
                    else:
                        # Se nao existe ele concatenado no dicionario
                        # Vou somar ele normalmente
                        valor += dic[numero_romano[i]]
                else:
                    # Caso ele nao seja um caracter especial
                    # Vou apenas somar ele
                    valor += dic[numero_romano[i]]
            else:
                # Caso nao exista o caractere no dicionario
                # retorna um erro
                raise TypeError('Apenas numeros romanos sao permitidos')
        else:
            # Se meu numero ja foi contando
            # Vou trocar a flag para False
            # Para avisar que o proximo ainda nao foi contado
            flag = False

    print(valor)

if __name__ == "__main__":
    numero = input('Digite um numero numero romano entre 0 e 3999(Ex: XIX): ')
    decodificador(numero)
