import random
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
alunos = [a1, a2, a3, a4]

print('\nOs alunos da turma são:\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
print('Aluno escolhido para apagar o quadro foi {}!'.format(random.choice(alunos)))
