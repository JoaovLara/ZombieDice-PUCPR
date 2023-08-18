from random import randint

def cor_dado(num_sorteado):
    if num_sorteado <= 5:
        return "verde"
    elif num_sorteado <= 9:
        return "amarelo"
    else:
        return "vermelho"

def verificar_ganhador(lista_jogadores, lista_cerebros, num_jogadores):
    for i in range(num_jogadores):
        if lista_cerebros[i] >= 13:
            print('O jogador', lista_jogadores[i], 'Venceu')
            return True
    if num_jogadores > 1:
        return False
    else:
        print('O jogador', lista_jogadores[0], 'Venceu')
        print("\n")
        return True

print("ZOMBIE DICE PROJETO FINAL")
print("SEJA BEM VINDO AO JOGO ZOMBIE DICE")
print("\n")

num_jogadores = 0
while num_jogadores < 2:
    num_jogadores = int(input("Informe o número de jogadores: "))
    if num_jogadores < 2:
        print('ATENÇÃO! VOCÊ PRECISA DE PELO MENOS 2 JOGADORES!')

lista_jogadores = []

for i in range(num_jogadores):
    nome = input(f"Informe o nome do jogador {i + 1}: ")
    lista_jogadores.append(nome)

# Definindo os dados
dado_verde = ["C", "P", "C", "T", "P", "C"]
dado_amarelo = ["T", "P", "C", "T", "P", "C"]
dado_vermelho = ["T", "P", "T", "C", "P", "T"]

# Quantidade dos dados por cores
lista_dados = [
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
    dado_vermelho, dado_vermelho, dado_vermelho
]

# Pontuação dos Jogadores
lista_tiro = []
lista_cerebros = []

for i in range(num_jogadores):
    lista_cerebros.append(0)
    lista_tiro.append(0)

jogador_atual = 0
alguem_ganhou = False

print("\n")
print('INICIANDO O JOGO...')
print("\n")

# Sorteando os dados por jogador em cada turno
while not alguem_ganhou:
    passos = 0

    print("Turno do jogador:", lista_jogadores[jogador_atual])
    for i in range(3):
        num_sorteado = randint(0, 12)
        cor_do_dado = cor_dado(num_sorteado)  # Renomeie a variável aqui
        print(f"Dado sorteado {i + 1}: {cor_do_dado}")
        dado_sorteado = lista_dados[num_sorteado]
        face_dado = randint(0, 5)
        if dado_sorteado[face_dado] == 'C':
            print("VOCE COMEU UM CEREBRO!!\n")
            lista_cerebros[jogador_atual] += 1
        elif dado_sorteado[face_dado] == "T":
            print("VOCE LEVOU UM TIRO!!\n")
            lista_tiro[jogador_atual] += 1
            if lista_tiro[jogador_atual] >= 3:
                print("FALECEU")
                print("\n")
                del lista_jogadores[jogador_atual]
                del lista_cerebros[jogador_atual]
                num_jogadores -= 1
                passos = 0
                break
        else:
            print("A vítima escapou!\n")
            passos += 1

    print("\n")

    if passos > 0:
        play_game = input("Jogar dados de novo? (sim / nao): ")
        if play_game.lower() == "nao":
            print("Continuar jogo!\n")
            lista_tiro[jogador_atual] = 0
            jogador_atual = (jogador_atual + 1) % num_jogadores
    else:
        lista_tiro[jogador_atual] = 0
        jogador_atual = (jogador_atual + 1) % num_jogadores

    alguem_ganhou = verificar_ganhador(lista_jogadores, lista_cerebros, num_jogadores)

print('Fim do jogo...')
