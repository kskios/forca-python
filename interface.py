import tkinter as tk
import random
from PIL import Image, ImageTk

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

    # Verifica se foi digitado apenas uma letra
    if len(letra) != 1 or not letra.isalpha():

        mensagem.config(
            text="⚠ Digite apenas uma letra! ⚠"
        )
        return

    # Verifica se a letra já foi usada
    if letra in letras_tentadas:
        mensagem.config(
            text="⚠ Você já tentou essa letra! ⚠"
            
        )

        return


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
# REINICIAR PARTIDA
# ----------------------------

def reiniciar_jogo():

    global palavra_secreta
    global palavra_oculta
    global letras_tentadas
    global tentativas_restantes

    # Sorteia nova palavra
    palavra_secreta = random.choice(palavras)

    # Reinicia palavra oculta
    palavra_oculta = ["_"] * len(palavra_secreta)

    # Limpa letras usadas
    letras_tentadas = set()

    # Reinicia tentativas
    tentativas_restantes = 6

    # Limpa mensagem
    mensagem.config(text="")

    # Reativa o botão
    botao.config(state="normal")

    # Atualiza a tela
    atualizar_interface()

# ----------------------------
# JANELA
# ----------------------------

janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("900x600")
janela.config(bg="#0f172a")

# ----------------------------
# PERSONAGEM
# ----------------------------

# Carrega sprite do personagem
imagem_personagem = Image.open("anão.png")

# Redimensiona 
image_personagem = imagem_personagem.resize((220, 220))

# Converte para formato do Tkinter
sprite_personagem = ImageTk.PhotoImage(image_personagem)

personagem_label = tk.Label(
    janela,
    image=sprite_personagem,
    bg="#0f172a"
)

personagem_label.pack(pady=10)

# ----------------------------
# TÍTULO
# ----------------------------

titulo = tk.Label(
    janela,
    text="⚔️ Jogo da Forca ⚔️",
    font=("Obitron", 28, "bold"),
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
    font=("Obitron", 32, "bold"),
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
    font=("Obitron", 16, "bold"),
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
    font=("Obitron", 16, "bold"),
    bg="#0f172a",
    fg="white"
)

letras_label.pack(pady=10)

# ----------------------------
# INPUT
# ----------------------------

entrada_letra = tk.Entry(
    janela,
    font=("Obitron", 22, "bold"),
    width=5,
    justify="center"
)

entrada_letra.pack(pady=20)

# ----------------------------
# BOTÃO
# ----------------------------

botao = tk.Button(
    janela,
    text="⚔️ Enviar ⚔️",
    font=("Arial", 16, "bold"),
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

botao_reiniciar = tk.Button(
    janela,
    text="🔄 Reiniciar 🔄",
    font=("Obitron", 16, "bold"),
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
    font=("Obitron", 18, "bold"),
    bg="#0f172a",
    fg="#00ffe1"
)

mensagem.pack(pady=20)

# Atualiza interface inicial
atualizar_interface()

# Mantém janela aberta
janela.mainloop()