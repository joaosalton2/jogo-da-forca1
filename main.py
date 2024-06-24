import tkinter as tk
import random

#palavras da categoria
categorias = {
    'Animais': ['cachorro', 'gato', 'elefante'],
    'Frutas': ['abacate', 'abacaxi', 'acerola'],
    'Cores': ['vermelho', 'azul', 'verde']
}

#escolher uma palavra com base na categoria
def escolher_palavra(categoria):
    return random.choice(categorias[categoria])

#letras adivinhadas
def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao.strip()

#desenha o boneco da forca
def desenhar_boneco():
    if tentativas_erradas == 1:
        canvas.create_line(10, 190, 190, 190)  # Base
    elif tentativas_erradas == 2:
        canvas.create_line(50, 190, 50, 20)  # Poste
        canvas.create_line(50, 20, 100, 20)  # Haste superior
        canvas.create_line(100, 20, 100, 30)  # Haste inferior
    elif tentativas_erradas == 3:
        canvas.create_oval(70, 40, 130, 120)  # Cabeça
    elif tentativas_erradas == 4:
        canvas.create_oval(85, 55, 95, 65)  # Olho esquerdo
        canvas.create_oval(105, 55, 115, 65)  # Olho direito
    elif tentativas_erradas == 5:
        canvas.create_line(90, 80, 110, 80)  # Boca
    elif tentativas_erradas == 6:
        canvas.create_line(100, 100, 100, 160)  # Corpo
    elif tentativas_erradas == 7:
        canvas.create_line(100, 110, 70, 140)  # Braço esquerdo
    elif tentativas_erradas == 8:
        canvas.create_line(100, 110, 130, 140)  # Braço direito
    elif tentativas_erradas == 9:
        canvas.create_line(100, 160, 70, 190)  # Perna esquerda
    elif tentativas_erradas == 10:
        canvas.create_line(100, 160, 130, 190)  # Perna direita

#inicia o jogo da forca
def iniciar_jogo():
    global palavra, letras_adivinhadas, tentativas_erradas, tentativas_maximas
    categoria_escolhida = categoria_var.get()
    palavra = escolher_palavra(categoria_escolhida)
    letras_adivinhadas = []
    tentativas_erradas = 0
    tentativas_maximas = 10

    categoria_label.config(text=f"Categoria: {categoria_escolhida}")
    palavra_label.config(text=exibir_palavra(palavra, letras_adivinhadas))
    tentativas_label.config(text=f"Tentativas erradas: {tentativas_erradas}/{tentativas_maximas}")
    adivinhar_entry.delete(0, tk.END)
    resultado_label.config(text='')
    canvas.delete("all")

#verifica a letra adivinhada
def verificar_letra():
    global tentativas_erradas
    tentativa = adivinhar_entry.get().lower()
    adivinhar_entry.delete(0, tk.END)

    if tentativa in letras_adivinhadas:
        resultado_label.config(text="Você já adivinhou essa letra.")
        return

    letras_adivinhadas.append(tentativa)

    if tentativa in palavra:
        resultado_label.config(text="Boa! Você adivinhou uma letra.")
    else:
        resultado_label.config(text="Errado! Essa letra não está na palavra.")
        tentativas_erradas += 1
        desenhar_boneco()

    palavra_label.config(text=exibir_palavra(palavra, letras_adivinhadas))
    tentativas_label.config(text=f"Tentativas erradas: {tentativas_erradas}/{tentativas_maximas}")

    if all(letra in letras_adivinhadas for letra in palavra):
        resultado_label.config(text=f"Parabéns! Você adivinhou a palavra: {palavra}")
    elif tentativas_erradas >= tentativas_maximas:
        resultado_label.config(text=f"Você perdeu! A palavra era: {palavra}")

#interface gráfica
root = tk.Tk()
root.title("Jogo da Forca")

categoria_var = tk.StringVar(value='Animais')

categoria_label = tk.Label(root, text="Escolha uma categoria:")
categoria_label.pack()

categoria_menu = tk.OptionMenu(root, categoria_var, 'Animais', 'Frutas', 'Cores')
categoria_menu.pack()

iniciar_button = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo)
iniciar_button.pack()

palavra_label = tk.Label(root, text="")
palavra_label.pack()

tentativas_label = tk.Label(root, text="")
tentativas_label.pack()

adivinhar_entry = tk.Entry(root)
adivinhar_entry.pack()

adivinhar_button = tk.Button(root, text="Adivinhar", command=verificar_letra)
adivinhar_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

root.mainloop()