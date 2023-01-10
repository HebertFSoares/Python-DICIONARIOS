#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Leadro'
#pessoas['peso'] = 98.5

'''
for k,v in pessoas.items():
    print(f"O {k} = {v}")
'''

'''
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
'''

#print(estado1)
#print(estado2)
#print(brasil[0]['uf'])

#estado = dict()
#brasil = list()

'''
for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f"O Campo {k} tem valor {v}.")
'''