import tkinter as tk
import random
import sys
import os
from PIL import Image, ImageTk
import vlc


# ==================================================
# RESOURCE PATH (necessário para o .exe funcionar)
# ==================================================

def resource_path(relative_path):
    """Resolve o caminho dos assets dentro ou fora do .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# ==================================================
# MÚSICA
# ==================================================

player = vlc.MediaPlayer(resource_path("assets/sounds/theme.mp3"))
player.audio_set_volume(45)


def tocar_musica():
    global player
    player = vlc.MediaPlayer(resource_path("assets/sounds/theme.mp3"))
    player.audio_set_volume(45)
    player.play()


# ==================================================
# DADOS DO JOGO
# ==================================================

palavras = [
    "PYTHON",
    "ALGORITMO",
    "BACKEND",
    "FRONTEND",
    "DATABASE",
    "LINUX",
    "CYBERSEC",
    "PROGRAMACAO",
    "ESTRUTURA",
    "JAVASCRIPT"
]

palavra_secreta = random.choice(palavras)
palavra_oculta = ["_"] * len(palavra_secreta)
letras_tentadas = set()
tentativas_restantes = 6


# ==================================================
# FUNÇÕES MENU
# ==================================================

def mostrar_menu():
    frame_jogo.pack_forget()
    frame_menu.pack(fill="both", expand=True)


def iniciar_partida():
    frame_menu.pack_forget()
    frame_jogo.pack(fill="both", expand=True)


def voltar_menu():
    frame_jogo.pack_forget()
    frame_menu.pack(fill="both", expand=True)


# ==================================================
# SPRITES
# ==================================================

def trocar_sprite(caminho):
    global sprite_personagem
    imagem = Image.open(resource_path(caminho))
    imagem = imagem.resize((170, 170))
    sprite_personagem = ImageTk.PhotoImage(imagem)
    personagem_label.config(image=sprite_personagem)
    personagem_label.image = sprite_personagem


def atualizar_sprite():

    # Vitória
    if "_" not in palavra_oculta:
        trocar_sprite("assets/sprites/dwarf_victory.png")
        return

    # Derrota
    if tentativas_restantes <= 0:
        trocar_sprite("assets/sprites/dwarf_gameover.png")
        return

    # Estados
    if tentativas_restantes == 6:
        trocar_sprite("assets/sprites/dwarf_idle.png")
    elif tentativas_restantes == 5:
        trocar_sprite("assets/sprites/dwarf_hang_0.png")
    elif tentativas_restantes == 4:
        trocar_sprite("assets/sprites/dwarf_hang_1.png")
    elif tentativas_restantes == 3:
        trocar_sprite("assets/sprites/dwarf_hang_2.png")
    elif tentativas_restantes == 2:
        trocar_sprite("assets/sprites/dwarf_hang_3.png")
    elif tentativas_restantes == 1:
        trocar_sprite("assets/sprites/dwarf_hang_4.png")


# ==================================================
# INTERFACE
# ==================================================

def atualizar_interface():

    palavra_label.config(text=" ".join(palavra_oculta))
    letras_label.config(text=f"Letras usadas: {', '.join(sorted(letras_tentadas))}")
    vidas_label.config(text="❤️ " * tentativas_restantes)
    atualizar_sprite()

    # Vitória
    if "_" not in palavra_oculta:
        mensagem.config(text="⚔ Você salvou o guerreiro! ⚔", fg="#00ff88")
        entrada_letra.config(state="disabled")
        botao.config(state="disabled")

    # Derrota
    elif tentativas_restantes <= 0:
        mensagem.config(text=f"💀 Palavra: {palavra_secreta}", fg="#ff5555")
        entrada_letra.config(state="disabled")
        botao.config(state="disabled")


# ==================================================
# GAMEPLAY
# ==================================================

def tentar_letra():

    global tentativas_restantes

    letra = entrada_letra.get().upper()
    entrada_letra.delete(0, tk.END)

    # Validação
    if len(letra) != 1 or not letra.isalpha():
        mensagem.config(text="⚠ Digite apenas UMA letra ⚠", fg="#ffaa00")
        return

    # Letra repetida
    if letra in letras_tentadas:
        mensagem.config(text="⚠ Letra já utilizada ⚠", fg="#ffaa00")
        return

    letras_tentadas.add(letra)

    # Acerto
    if letra in palavra_secreta:
        for indice, caractere in enumerate(palavra_secreta):
            if caractere == letra:
                palavra_oculta[indice] = letra
        mensagem.config(text="⚔ Acertou ⚔", fg="#00ffee")

    # Erro
    else:
        tentativas_restantes -= 1
        mensagem.config(text="❌ Você errou ❌", fg="#ff5555")

    atualizar_interface()


# ==================================================
# REINICIAR
# ==================================================

def reiniciar_jogo():

    global palavra_secreta, palavra_oculta, letras_tentadas, tentativas_restantes

    palavra_secreta = random.choice(palavras)
    palavra_oculta = ["_"] * len(palavra_secreta)
    letras_tentadas = set()
    tentativas_restantes = 6

    entrada_letra.config(state="normal")
    botao.config(state="normal")
    entrada_letra.delete(0, tk.END)
    mensagem.config(text="")

    atualizar_interface()


# ==================================================
# JANELA
# ==================================================

janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("1100x900")
janela.resizable(False, False)
janela.config(bg="black")

# ==================================================
# FRAMES
# ==================================================

frame_menu = tk.Frame(janela, bg="black")
frame_jogo = tk.Frame(janela, bg="black")

# ==================================================
# BACKGROUND MENU
# ==================================================

imagem_menu = Image.open(resource_path("assets/backgrounds/background_menu.png"))
imagem_menu = imagem_menu.resize((1100, 900))
bg_menu = ImageTk.PhotoImage(imagem_menu)

label_bg_menu = tk.Label(frame_menu, image=bg_menu)
label_bg_menu.image = bg_menu
label_bg_menu.place(x=0, y=0, relwidth=1, relheight=1)
label_bg_menu.lower()

# ==================================================
# BACKGROUND GAMEPLAY
# ==================================================

imagem_jogo = Image.open(resource_path("assets/backgrounds/background_game.png"))
imagem_jogo = imagem_jogo.resize((1100, 900))
bg_jogo = ImageTk.PhotoImage(imagem_jogo)

label_bg_jogo = tk.Label(frame_jogo, image=bg_jogo)
label_bg_jogo.image = bg_jogo
label_bg_jogo.place(x=0, y=0, relwidth=1, relheight=1)
label_bg_jogo.lower()

# ==================================================
# MENU UI
# ==================================================

titulo_menu = tk.Label(
    frame_menu,
    text="⚔ JOGO DA FORCA ⚔",
    font=("Orbitron", 38, "bold"),
    fg="#00ffee",
    bg="black"
)
titulo_menu.pack(pady=150)

botao_jogar = tk.Button(
    frame_menu,
    text="⚔ JOGAR ⚔",
    font=("Orbitron", 22, "bold"),
    bg="#00ffee",
    fg="black",
    relief="flat",
    padx=40,
    pady=15,
    cursor="hand2",
    command=iniciar_partida
)
botao_jogar.pack(pady=20)

botao_sair = tk.Button(
    frame_menu,
    text="✖ SAIR ✖",
    font=("Orbitron", 18, "bold"),
    bg="#a855f7",
    fg="white",
    relief="flat",
    padx=30,
    pady=12,
    cursor="hand2",
    command=janela.destroy
)
botao_sair.pack(pady=10)

# ==================================================
# PERSONAGEM
# ==================================================

imagem_personagem = Image.open(resource_path("assets/sprites/dwarf_idle.png"))
imagem_personagem = imagem_personagem.resize((170, 170))
sprite_personagem = ImageTk.PhotoImage(imagem_personagem)

personagem_label = tk.Label(frame_jogo, image=sprite_personagem, bg="black")
personagem_label.pack(pady=20)

# ==================================================
# TÍTULO
# ==================================================

titulo = tk.Label(
    frame_jogo,
    text="⚔ Jogo da Forca ⚔",
    font=("Orbitron", 30, "bold"),
    fg="#00ffee",
    bg="black"
)
titulo.pack(pady=10)

# ==================================================
# PALAVRA
# ==================================================

palavra_label = tk.Label(
    frame_jogo,
    text=" ".join(palavra_oculta),
    font=("Orbitron", 40, "bold"),
    fg="#00ffee",
    bg="black"
)
palavra_label.pack(pady=20)

# ==================================================
# VIDAS
# ==================================================

vidas_label = tk.Label(
    frame_jogo,
    text="❤️❤️❤️❤️❤️❤️",
    font=("Orbitron", 24, "bold"),
    fg="#ff5555",
    bg="black"
)
vidas_label.pack()

# ==================================================
# LETRAS USADAS
# ==================================================

letras_label = tk.Label(
    frame_jogo,
    text="Letras usadas:",
    font=("Orbitron", 18, "bold"),
    fg="white",
    bg="black"
)
letras_label.pack(pady=15)

# ==================================================
# INPUT
# ==================================================

entrada_letra = tk.Entry(
    frame_jogo,
    font=("Orbitron", 24, "bold"),
    width=5,
    justify="center",
    relief="flat",
    bd=0
)
entrada_letra.pack(pady=10)

# ==================================================
# BOTÃO ENVIAR
# ==================================================

botao = tk.Button(
    frame_jogo,
    text="⚔ ENVIAR ⚔",
    font=("Orbitron", 16, "bold"),
    bg="#00ffee",
    fg="black",
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2",
    command=tentar_letra
)
botao.pack(pady=10)

# ==================================================
# BOTÃO REINICIAR
# ==================================================

botao_reiniciar = tk.Button(
    frame_jogo,
    text="🔄 REINICIAR 🔄",
    font=("Orbitron", 16, "bold"),
    bg="#a855f7",
    fg="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=reiniciar_jogo
)
botao_reiniciar.pack(pady=10)

# ==================================================
# BOTÃO MENU
# ==================================================

botao_menu = tk.Button(
    frame_jogo,
    text="◄ MENU",
    font=("Orbitron", 14, "bold"),
    bg="#111827",
    fg="#00ffee",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2",
    command=voltar_menu
)
botao_menu.pack(pady=10)

# ==================================================
# MENSAGEM
# ==================================================

mensagem = tk.Label(
    frame_jogo,
    text="",
    font=("Orbitron", 18, "bold"),
    fg="#00ffee",
    bg="black"
)
mensagem.pack(pady=20)

# ==================================================
# ENTER
# ==================================================

janela.bind("<Return>", lambda event: tentar_letra())

# ==================================================
# INICIALIZA
# ==================================================

atualizar_interface()
tocar_musica()
mostrar_menu()

janela.mainloop()