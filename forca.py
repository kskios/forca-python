# Importa biblioteca de sorteio
import random

# Lista de palavras
palavras = ["PYTHON", "PROGRAMACAO", "ESTRUTURA", "ALGORITMO"]


# Função responsável por iniciar os dados do jogo
def iniciar_jogo():

    # Sorteia palavra aleatória
    palavra_secreta = random.choice(palavras)

    # Cria lista da palavra oculta
    palavra_oculta = ["_"] * len(palavra_secreta)

    # Cria conjunto de letras tentadas
    letras_tentadas = set()

    # Retorna os dados
    return palavra_secreta, palavra_oculta, letras_tentadas


# Função que processa a letra digitada
def processar_tentativa(letra, palavra_secreta, palavra_oculta):

    # Percorre as letras da palavra
    for indice, caractere in enumerate(palavra_secreta):

        # Verifica se a letra existe
        if caractere == letra:

            # Atualiza a palavra oculta
            palavra_oculta[indice] = letra


# Inicia o jogo
palavra_secreta, palavra_oculta, letras_tentadas = iniciar_jogo()

# Número máximo de tentativas
tentativas_restantes = 6

# Loop principal do jogo
while tentativas_restantes > 0 and "_" in palavra_oculta:
    print("\nPalavra:", " ".join(palavra_oculta))
    print("Letras tentadas:", letras_tentadas)
    print("Tentativas restantes:", tentativas_restantes)
    letra = input("Digite uma letra: ").upper()
    letras_tentadas.add(letra)
    
    if letra in palavra_secreta:
        
        processar_tentativa(letra, palavra_secreta, palavra_oculta)

        print("Você acertou!")

    else: 

        tentativas_restantes -= 1

        print("Você errou!")

# Verifica resultado final
if "_" not in palavra_oculta:

    print("\nParabéns! Você venceu!")
    print("Palavra:", "".join(palavra_oculta))

else:

    print("\nFim de jogo!")
    print("A palavra era:", palavra_secreta)