aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] >= 7 :
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')