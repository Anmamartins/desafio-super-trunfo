import random

# Lista de cartas com 3 atributos cada
cartas = [
    {"nome": "Dragão", "força": 9, "velocidade": 7, "inteligência": 6},
    {"nome": "Fada", "força": 4, "velocidade": 8, "inteligência": 9},
    {"nome": "Gigante", "força": 10, "velocidade": 3, "inteligência": 4},
    {"nome": "Elfo", "força": 6, "velocidade": 9, "inteligência": 8}
]

# Escolhe carta aleatória para o jogador e para o computador
carta_jogador = random.choice(cartas)
carta_computador = random.choice(cartas)

# Garante que as cartas não sejam iguais
while carta_jogador == carta_computador:
    carta_computador = random.choice(cartas)

# Mostra a carta do jogador
print("\nSua carta:")
for chave, valor in carta_jogador.items():
    print(f"{chave.capitalize()}: {valor}")

# Jogador escolhe um atributo
atributo = input("\nEscolha um atributo para disputar (força, velocidade ou inteligência): ").lower()

# Mostra a carta do computador
print("\nCarta do computador:")
for chave, valor in carta_computador.items():
    print(f"{chave.capitalize()}: {valor}")

# Compara os valores do atributo escolhido
if carta_jogador[atributo] > carta_computador[atributo]:
    print("\n🎉 Você venceu!")
elif carta_jogador[atributo] < carta_computador[atributo]:
    print("\n😞 Você perdeu!")
else:
    print("\n⚔️ Empate!")
