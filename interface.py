import tkinter as tk
import random
from PIL import Image, ImageTk

# ----------------------------
# DADOS DO JOGO
# ----------------------------

palavras = [
    "PYTHON",
    "PROGRAMACAO",
    "ESTRUTURA",
    "ALGORITMO"
]

palavra_secreta = random.choice(palavras)

palavra_oculta = ["_"] * len(palavra_secreta)

letras_tentadas = set()

tentativas_restantes = 6


# ----------------------------
# TROCAR SPRITE
# ----------------------------

def trocar_sprite(caminho_imagem):

    global sprite_personagem

    imagem = Image.open(caminho_imagem)

    imagem = imagem.resize((170, 170))

    sprite_personagem = ImageTk.PhotoImage(imagem)

    personagem_label.config(image=sprite_personagem)

    personagem_label.image = sprite_personagem


# ----------------------------
# ATUALIZA SPRITE
# ----------------------------

def atualizar_sprite():

    # Vitória
    if "_" not in palavra_oculta:
        trocar_sprite("assets/dwarf_victory.png")
        return

    # Derrota
    if tentativas_restantes <= 0:
        trocar_sprite("assets/dwarf_gameover.png")
        return

    # Estados normais
    if tentativas_restantes == 6:
        trocar_sprite("assets/dwarf_idle.png")

    elif tentativas_restantes == 5:
        trocar_sprite("assets/dwarf_hang_1.png")

    elif tentativas_restantes == 4:
        trocar_sprite("assets/dwarf_hang_2.png")

    elif tentativas_restantes == 3:
        trocar_sprite("assets/dwarf_hang_3.png")

    elif tentativas_restantes == 2:
        trocar_sprite("assets/dwarf_hang_4.png")

    elif tentativas_restantes == 1:
        trocar_sprite("assets/dwarf_hang_5.png")


# ----------------------------
# ATUALIZA INTERFACE
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

    atualizar_sprite()

    # Vitória
    if "_" not in palavra_oculta:

        mensagem.config(
            text="⚔️ Você salvou o guerreiro! ⚔️",
            fg="#00ff88"
        )

        entrada_letra.config(state="disabled")

        botao.config(state="disabled")

    # Derrota
    elif tentativas_restantes <= 0:

        mensagem.config(
            text=f"💀 O guerreiro foi derrotado! Palavra: {palavra_secreta}",
            fg="#ff5555"
        )

        entrada_letra.config(state="disabled")

        botao.config(state="disabled")


# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------

def tentar_letras():

    global tentativas_restantes

    # Impede jogadas após derrota
    if tentativas_restantes <= 0:
        return

    letra = entrada_letra.get().upper()

    # Limpa input
    entrada_letra.delete(0, tk.END)

    # Validação
    if len(letra) != 1 or not letra.isalpha():

        mensagem.config(
            text="⚠ Digite apenas UMA letra! ⚠",
            fg="#ffaa00"
        )

        return

    # Verifica repetição
    if letra in letras_tentadas:

        mensagem.config(
            text="⚠ Essa letra já foi usada! ⚠",
            fg="#ffaa00"
        )

        return

    # Adiciona letra
    letras_tentadas.add(letra)

    # Acertou
    if letra in palavra_secreta:

        for indice, caractere in enumerate(palavra_secreta):

            if caractere == letra:

                palavra_oculta[indice] = letra

        mensagem.config(
            text="⚔️ Você acertou!",
            fg="#00ffe1"
        )

    # Errou
    else:

        tentativas_restantes -= 1

        mensagem.config(
            text="❌ Você errou!",
            fg="#ff5555"
        )

    atualizar_interface()


# ----------------------------
# REINICIAR JOGO
# ----------------------------

def reiniciar_jogo():

    global palavra_secreta
    global palavra_oculta
    global letras_tentadas
    global tentativas_restantes

    palavra_secreta = random.choice(palavras)

    palavra_oculta = ["_"] * len(palavra_secreta)

    letras_tentadas = set()

    tentativas_restantes = 6

    entrada_letra.config(state="normal")

    botao.config(state="normal")

    entrada_letra.delete(0, tk.END)

    mensagem.config(text="")

    atualizar_interface()


# ----------------------------
# JANELA
# ----------------------------

janela = tk.Tk()

janela.title("Jogo da Forca")

janela.geometry("900x700")

janela.config(bg="#0f172a")


# ----------------------------
# PERSONAGEM
# ----------------------------

imagem_personagem = Image.open("assets/dwarf_idle.png")

imagem_personagem = imagem_personagem.resize((170, 170))

sprite_personagem = ImageTk.PhotoImage(imagem_personagem)

personagem_label = tk.Label(
    janela,
    image=sprite_personagem,
    bg="#0f172a"
)

personagem_label.pack(pady=5)


# ----------------------------
# TÍTULO
# ----------------------------

titulo = tk.Label(
    janela,
    text="⚔️ Jogo da Forca ⚔️",
    font=("Orbitron", 28, "bold"),
    bg="#0f172a",
    fg="#00ffe1"
)

titulo.pack(pady=10)


# ----------------------------
# PALAVRA
# ----------------------------

palavra_label = tk.Label(
    janela,
    text=" ".join(palavra_oculta),
    font=("Orbitron", 36, "bold"),
    bg="#0f172a",
    fg="#00ffe1"
)

palavra_label.pack(pady=15)


# ----------------------------
# TENTATIVAS
# ----------------------------

tentativas_label = tk.Label(
    janela,
    text=f"Tentativas restantes: {tentativas_restantes}",
    font=("Orbitron", 16, "bold"),
    bg="#0f172a",
    fg="white"
)

tentativas_label.pack()


# ----------------------------
# LETRAS USADAS
# ----------------------------

letras_label = tk.Label(
    janela,
    text="Letras usadas:",
    font=("Orbitron", 16, "bold"),
    bg="#0f172a",
    fg="white"
)

letras_label.pack(pady=10)


# ----------------------------
# INPUT
# ----------------------------

entrada_letra = tk.Entry(
    janela,
    font=("Orbitron", 22, "bold"),
    width=5,
    justify="center",
    relief="flat",
    bd=0
)

entrada_letra.pack(pady=10)


# ----------------------------
# BOTÃO ENVIAR
# ----------------------------

botao = tk.Button(
    janela,
    text="⚔️ Enviar ⚔️",
    font=("Orbitron", 14, "bold"),
    bg="#00ffe1",
    fg="#0f172a",
    activebackground="#00c8b4",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=tentar_letras
)

botao.pack(pady=10)


# ----------------------------
# BOTÃO REINICIAR
# ----------------------------

botao_reiniciar = tk.Button(
    janela,
    text="🔄 Reiniciar 🔄",
    font=("Orbitron", 16, "bold"),
    bg="#a855f7",
    fg="white",
    activebackground="#9333ea",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8,
    bd=0,
    cursor="hand2",
    command=reiniciar_jogo
)

botao_reiniciar.pack(pady=10)


# ----------------------------
# MENSAGEM
# ----------------------------

mensagem = tk.Label(
    janela,
    text="",
    font=("Orbitron", 18, "bold"),
    bg="#0f172a",
    fg="#00ffe1"
)

mensagem.pack(pady=20)


# ----------------------------
# INICIALIZA
# ----------------------------

atualizar_interface()

janela.mainloop()