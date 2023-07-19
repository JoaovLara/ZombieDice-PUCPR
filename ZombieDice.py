"""
ZOMBIE DICE Prototipo FINAL
João Vitor de Lara
Raciocínio Computacional
"""

from random import randint

def CorDado(numSorteado):
    if numSorteado <= 5:
        return "verde"
    elif numSorteado <= 9:
        return "amarelo"
    else:
        return "vermelho"

def VerificarGanhador(listaJogadores, ListaCerebros, numJogadores):
    for i in range(numJogadores):
        if ListaCerebros[i] >= 13:
            print('O jogador', listaJogadores[i], 'Venceu')
            return True
    if numJogadores > 1:
        return False
    else:
        print('O jogador', listaJogadores[0], 'Venceu')
        print("\n")
        return True

print("ZOMBIE DICE PROJETO FINAL")
print("SEJA BEM VINDO AO JOGO ZOMBIE DICE")
print("\n")

numJogadores = 0
while numJogadores < 2:
    numJogadores = int(input("Informe o número de jogadores: "))
    if numJogadores < 2:
        print('ATENÇÃO! VOCÊ PRECISA DE NO MÍNIMO 2 JOGADORES!')

listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    listaJogadores.append(nome)

# Definindo os dados
dadoVerde = ["C", "P", "C", "T", "P", "C"]
dadoAmarelo = ["T", "P", "C", "T", "P", "C"]
dadoVermelho = ["T", "P", "T", "C", "P", "T"]

# Quantidade dos dados por cores
listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

# Pontuação dos Jogadores
lista_tiro = []
ListaCerebros = []

for _ in range(numJogadores):
    ListaCerebros.append(0)
    lista_tiro.append(0)

jogadorAtual = 0
alguemGanhou = False

print("\n")
print('INICIANDO O JOGO...')
print("\n")

# Sorteando os dados por jogador em cada turno
while not alguemGanhou:
    passos = 0

    print("Turno do jogador: {}".format(listaJogadores[jogadorAtual]))
    for i in range(3):
        numSorteado = randint(0, 12)
        corDado = CorDado(numSorteado)
        print("Dado sorteado {}: {}".format((i + 1), corDado))
        dadoSorteado = listaDados[numSorteado]
        faceDado = randint(0, 5)
        if dadoSorteado[faceDado] == 'C':
            print("VOCE COMEU UM CEREBRO!!\n")
            ListaCerebros[jogadorAtual] += 1

        elif dadoSorteado[faceDado] == "T":
            print("VOCE LEVOU UM TIRO!!\n")
            lista_tiro[jogadorAtual] += 1
            if lista_tiro[jogadorAtual] >= 3:
                print("FALECEU")
                print("\n")
                del listaJogadores[jogadorAtual]
                del ListaCerebros[jogadorAtual]
                numJogadores -= 1
                passos = 0
                break

        else:
            print("A vitima escapou!\n")
            passos += 1

    print("\n")

    if passos > 0:
        playGame = input("Jogar dados de novo? (sim / nao): ")

        if playGame == "nao":
            print("Continuar jogo!\n")
            lista_tiro[jogadorAtual] = 0
            jogadorAtual = (jogadorAtual + 1) % numJogadores
    else:
        lista_tiro[jogadorAtual] = 0
        jogadorAtual = (jogadorAtual + 1) % numJogadores

    alguemGanhou = VerificarGanhador(listaJogadores, ListaCerebros, numJogadores)

print('Fim do jogo...')
