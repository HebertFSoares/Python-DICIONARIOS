partida = list()
jogador = dict()
jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input(f"Quantas partidas o {jogador['nome'] } Jogou? "))
for c in range(0, tot):
    partida.append(int(input(f"Quantos gols na partida {c+1}?")))

jogador['gols'] = partida[:]
jogador['total'] = sum(partida) 
print('-' * 35)
print(jogador)
print('-' * 35)
for k,v in jogador.items():
    print(f"o Campo {k} tem o valor {v}")
print('-' * 35)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i,v in enumerate(jogador['gols']):
    print(f" na partida {i+1}, fez {v} gols")
    
print(f"Foi um total de {jogador['total']} gols.")