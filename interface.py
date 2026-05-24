import tkinter as tk
import random

# Lista de palavras
palavras = ["PYTHON", "PROGRAMACAO", "ESTRUTURA", "ALGORITMO"]

# Sorteia a palavra
palavra_secreta = random.choice(palavras)

# Cria a palavra oculta
palavra_oculta = ["_"] * len(palavra_secreta)

# Letras já usadas
letras_tentadas = set()

# Número de tentativas
tentativas_restantes = 6


# ----------------------------
# FUNÇÃO PRINCIPAL DO JOGO
# ----------------------------

def tentar_letras():
    global tentativas_restantes

    # Pega a letra digitada
    letra = entrada_letra.get().upper()

    # Limpa campo
    entrada_letra.delete(0, tk.END)

    # Evita letra vazia
    if letra == "":
        return
    
    # Adiciona no conjunto
    letras_tentadas.add(letra)

    # Verifica se acertou
    if letra in palavra_secreta:
        for indice, caractere in enumerate(palavra_secreta):
            if caractere == letra:
                palavra_oculta[indice] = letra

        mensagem.config(text="Você acertou!")

    else:
        tentativas_restantes -= 1
        mensagem.config(text="Você errou!")
    
    # Atualiza elementos da tela
    atualizar_interface()


# ----------------------------
# ATUALIZA TELA
# ----------------------------

def atualizar_interface():
    palavra_label.config(
        text=" ".join(palavra_oculta)
    )

    letras_label.config(
        text=f"Letras usadas: {', '.join(letras_tentadas)}"
    )

    tentativas_label.config(
        text=f"Tentativas restantes: {tentativas_restantes}"
    )

    # Vitória
    if "_" not in palavra_oculta:

        mensagem.config(
            text="⚔️ Você venceu! ⚔️"
        )

        botao.config(state="disabled")

    # Derrota
    elif tentativas_restantes == 0:

        mensagem.config(
            text=f"💀 Você perdeu! A palavra era: {palavra_secreta} 💀"
        )

        botao.config(state="disabled")


# ----------------------------
# JANELA
# ----------------------------

janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("900x600")
janela.config(bg="#0f172a")

# ----------------------------
# TÍTULO
# ----------------------------

titulo = tk.Label(
    janela,
    text="⚔️ Jogo da Forca ⚔️",
    font=("Arial", 28),
    bg="#0f172a",
    fg="#00ffe1"
)

titulo.pack(pady=20)

# ----------------------------
# PALAVRA
# ----------------------------

palavra_label = tk.Label(
    janela,
    text=" ".join(palavra_oculta),
    font=("Arial", 32),
    bg="#0f172a",
    fg="#00ffe1"
)

palavra_label.pack(pady=20)

# ----------------------------
# TENTATIVAS
# ----------------------------

tentativas_label = tk.Label(
    janela,
    text=f"Tentativas restantes: {tentativas_restantes}",
    font=("Arial", 16),
    bg="#0f172a",
    fg="white"
)

tentativas_label.pack()

# ----------------------------
# LETRAS USADAS
# ----------------------------

letras_label = tk.Label(
    janela,
    text="Letras usadas: ",
    font=("Arial", 16),
    bg="#0f172a",
    fg="white"
)

letras_label.pack(pady=10)

# ----------------------------
# INPUT
# ----------------------------

entrada_letra = tk.Entry(
    janela,
    font=("Arial", 22),
    width=5,
    justify="center"
)

entrada_letra.pack(pady=20)

# ----------------------------
# BOTÃO
# ----------------------------

botao = tk.Button(
    janela,
    text="Enviar Letra",
    font=("Arial", 16),
    command=tentar_letras
)

botao.pack()

# ----------------------------
# MENSAGEM
# ----------------------------

mensagem = tk.Label(
    janela,
    text="",
    font=("Arial", 18),
    bg="#0f172a",
    fg="#00ffe1"
)

mensagem.pack(pady=20)

# Atualiza interface inicial
atualizar_interface()

# Mantém janela aberta
janela.mainloop()

