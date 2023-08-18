# ZombieDice-PUCPR
Projeto da Disciplina de Raciocínio Computacional com Python

## Regras do Jogo Zombie Dice

O Zombie Dice é um jogo de dados para 2 ou mais jogadores, onde você assume o papel de um zumbi faminto em busca de cérebros. 
O objetivo é acumular 13 cérebros antes de seus adversários.

### Componentes

1. Dados: Existem três tipos de dados com diferentes cores e probabilidades de cérebros, passos e tiros:
   - Dado Verde: 3 Cérebros, 2 Tiros, 1 Passo (C, T, P)
   - Dado Amarelo: 2 Cérebros, 2 Tiros, 2 Passos (C, T, P)
   - Dado Vermelho: 1 Cérebro, 3 Tiros, 2 Passos (C, T, P)
  

As probabilidades de cores dos dados no Zombie Dice são as seguintes:

Dado Verde:
Cérebro (C): 3/6 (50%)
Tiro (T): 2/6 (33.33%)
Passo (P): 1/6 (16.67%)

Dado Amarelo:
Cérebro (C): 2/6 (33.33%)
Tiro (T): 2/6 (33.33%)
Passo (P): 2/6 (33.33%)

Dado Vermelho:
Cérebro (C): 1/6 (16.67%)
Tiro (T): 3/6 (50%)
Passo (P): 2/6 (33.33%)

### Objetivo

O jogador que acumular 13 cérebros primeiro é o vencedor. No entanto, um jogador é eliminado do jogo se for atingido por três tiros em um único turno.

### Preparação

1. Cada jogador escolhe seu nome para registrar  sua pontuação.
2. Os dados são agrupados por cor e colocados no centro da mesa.

### Jogabilidade

1. Os jogadores se revezam em turnos.
2. Em cada turno, um jogador lança três dados.
3. O jogador escolhe e rola os três dados escolhidos.
4. Cada dado tem três possíveis resultados:
   - "C" (cérebro): O jogador acumula um cérebro.
   - "T" (tiro): O jogador recebe um tiro. Três tiros no mesmo turno eliminam o jogador.
   - "P" (passo): A vítima escapou. Nada acontece.

### Eliminação

Se um jogador acumular três tiros em um único turno, ele é eliminado do jogo. Se todos os jogadores, exceto um, forem eliminados, o jogador restante vence.

### Vencedor

O jogador que acumular 13 cérebros PRIMEIRO é declarado vencedor.

### Observações Finais

O Zombie Dice é um jogo de sorte, estratégia e risco. Os jogadores devem decidir quando parar de rolar os dados em um turno para evitar tiros e manter seus cérebros conquistados. Use táticas inteligentes para acumular cérebros enquanto evita tiros!

Divirta-se jogando o Zombie Dice!
