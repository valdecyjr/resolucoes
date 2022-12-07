"""
    Enunciado = Fazer um programa onde seja inserido nomes de alunos e a quantidade de equipes.
Esses alunos tem que ser organizados na equipe com quantidades iguais.
Obs: O divisão das equipes fica a seu critério
"""


def orgequipe(alunos):
    equipe1, equipe2 = [], []
    if len(alunos) % 2 == 0:
        limiteinferior = int(len(alunos)/2)
        limitesuperior = int(len(alunos))

        for numero in range(limiteinferior):
            equipe1.append(alunos[numero])
        for numero in range(limiteinferior, limitesuperior):
            equipe2.append(alunos[numero])

        print(f'Equipe1: {equipe1}')
        print(f'Equipe2: {equipe2}')
    else:
        print('Não é possivel dividir de forma igual')
alunos = []
qnt_alunos = int(input('Digite a quantidade de alunos: '))
while len(alunos) < qnt_alunos:
    alunos.append(input('Digite o nome do aluno: '))
orgequipe(alunos)
