import csv
import random

# Armazenando em uma lista as opções da roda
with open('roda.txt', 'r') as arquivo:
    roda = arquivo.read().split()

# Armazenando em uma lista as palavras
palavras = []
with open('roda.csv', 'r') as file:
    arq_csv = csv.reader(file)
    for item in arq_csv:
        palavras.append(item)

# Armazenando cada palavra em uma lista independente
palavra = palavras[0][0]
palavra1 = []
for i in range(len(palavra)):
    palavra1.append(palavra[i])

palavra = palavras[0][1]
palavra2 = []
for i in range(len(palavra)):
    palavra2.append(palavra[i])

palavra = palavras[0][2]
palavra3 = []
for i in range(len(palavra)):
    palavra3.append(palavra[i])

# Armazenando os nomes dos jogadores
nomes = [input("Digite o nome do primeiro jogador: "),
         input("Digite o nome do segundo jogador: "),
         input("Digite o nome do terceiro jogador: ")]

# Exibe a dica e o painel das palavras
print("\nDica: AVIÃO")
painel1 = []
for i in range(len(palavra1)):
    painel1.append("_")
painel2 = []
for i in range(len(palavra2)):
    painel2.append("_")
painel3 = []
for i in range(len(palavra3)):
    painel3.append("_")
print(*painel1)
print(*painel2)
print(*painel3)

# Lista da pontuação e variável do jogador atual
pontos = [0, 0, 0]
jogador_atual = 0

# Armazenando total de letras do jogo
total_letras = len(palavra1) + len(palavra2) + len(palavra3)
acertos = 0
ponto_roda = 0
palpites = {''}
palpites.pop()

# Jogando enquanto o total de acertos for menor que o total de letras
while acertos < total_letras:
    input(f"\nJogador: {nomes[jogador_atual].upper()}. Pressione ENTER para rodar a roda...")
    sorteio_roda = random.choice(roda)
    print(f"\nA roda parou em: {sorteio_roda}")

    # Convertendo valor da roda (se for um número)
    if sorteio_roda != 'PASSA_A_VEZ' and sorteio_roda != 'PERDE_TUDO':
        ponto_roda = int(sorteio_roda)

    # Verificando opções da roda
    if sorteio_roda == 'PASSA_A_VEZ':
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PASSOU A VEZ")
        jogador_atual += 1
    elif sorteio_roda == 'PERDE_TUDO':
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PERDEU TUDO")
        jogador_atual += 1
    else:
        # Verificando se faltam 3 letras ou menos
        if acertos < total_letras - 3:
            # Pedindo para digitar uma letra
            letra = input("Digite uma letra: ").upper()

            # Verifica se a letra já foi um palpite utilizado
            if letra in palpites:
                print("\nEssa letra já foi utilizada")
                jogador_atual += 1
            else:
                palpites.add(letra)
                # Verificando se a letra está contida nas palavras
                if letra in palavra1 or letra in palavra2 or letra in palavra3:
                    # Substituindo a letra correta e atualizando acertos
                    for i in range(len(palavra1)):
                        if letra == palavra1[i]:
                            painel1[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda

                    for i in range(len(palavra2)):
                        if letra == palavra2[i]:
                            painel2[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda

                    for i in range(len(palavra3)):
                        if letra == palavra3[i]:
                            painel3[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda
                else:
                    print("\nNão temos essa letra")
                    jogador_atual += 1
        else:
            # Quando faltar 3 letras (ou menos), pedir digitação
            print(f"Jogador: {nomes[jogador_atual].upper()}. Você já sabe quais são as palavras?")
            print("Gostaria de digitá-las? (SIM OU NÃO)?")
            escolha = input("Escolha : ").upper()
            if escolha == "SIM":
                print(f"Jogador: {nomes[jogador_atual].upper()}. Digite quais são as palavras")
                resposta1 = input("Palavra 1: ").upper()
                resposta2 = input("Palavra 2: ").upper()
                resposta3 = input("Palavra 3: ").upper()
                if resposta1 == palavras[0][0] and resposta2 == palavras[0][1] and resposta3 == palavras[0][2]:
                    painel1 = palavra1
                    painel2 = palavra2
                    painel3 = palavra3
                    pontos[jogador_atual] += ponto_roda * (total_letras - acertos)
                    acertos = total_letras
                else:
                    print("\nQue pena, Você errou e PERDEU TUDO!")
                    pontos[jogador_atual] = 0
                    jogador_atual += 1
            else:
                print("\nNeste caso, passamos a vez para o próximo jogador")
                jogador_atual += 1

    print("\nDica: AVIÃO")
    print("-" * 30)
    print("Palpites:", *palpites)
    print("-" * 30)
    print("Pontuação geral:")
    print(f"Nome: {nomes[0].upper():{pontos[0]}}")
    print(f"Nome: {nomes[1].upper():{pontos[1]}}")
    print(f"Nome: {nomes[2].upper():{pontos[2]}}")

    # Ajustando jogador atual
    if jogador_atual >= 3:
        jogador_atual = 0
