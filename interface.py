"""
grafico na mesma janela do tk: https://www.youtube.com/watch?v=oob3P5pOWgg&t=4s
"""
from calculo import cal_proporcionalmente
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def mostrar_grafico(salario1, salario2, nome1, nome2):

    figura, grafico = plt.subplots()

    valores = [salario1, salario2]
    nomes = [nome1, nome2]

    grafico.pie(valores, labels=nomes, autopct='%1.1f%%')
    grafico.set_title("Divisão de Gastos")

    canvas = FigureCanvasTkAgg(figura, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)


def clicar_botao():

    nome1 = entrada_nome1.get()
    nome2 = entrada_nome2.get()

    salario1 = float(entrada_salario1.get())
    salario2 = float(entrada_salario2.get())
    gasto = float(entrada_gasto.get())

    resultado = cal_proporcionalmente(salario1, salario2, gasto)

    paga1 = resultado[3]
    paga2 = resultado[4]

    resultado_label.config(
        text=f"{nome1} paga: R$ {paga1:.2f} | {nome2} paga: R$ {paga2:.2f}"
    )

    mostrar_grafico(paga1, paga2, nome1, nome2)


# -------------------------
# JANELA
# -------------------------
janela = tk.Tk()
janela.title("Divisão de Gastos")
janela.geometry("450x450")


titulo = tk.Label(janela, text="Dividir proporcionalmente", font=("Arial", 14))
titulo.pack(pady=10)


frame = tk.Frame(janela)
frame.pack()

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)


# -------------------------
# PESSOA 1
# -------------------------
entrada_nome1 = tk.Entry(frame)
entrada_nome1.grid(row=0, column=0, padx=10, pady=5)
entrada_nome1.insert(0, "Seu nome")

entrada_salario1 = tk.Entry(frame)
entrada_salario1.grid(row=1, column=0, padx=10, pady=5)
entrada_salario1.insert(0, "Sua renda")


# -------------------------
# PESSOA 2
# -------------------------
entrada_nome2 = tk.Entry(frame)
entrada_nome2.grid(row=0, column=1, padx=10, pady=5)
entrada_nome2.insert(0, "Parceiro(a)")

entrada_salario2 = tk.Entry(frame)
entrada_salario2.grid(row=1, column=1, padx=10, pady=5)
entrada_salario2.insert(0, "Renda dele(a)")


# -------------------------
# GASTO
# -------------------------
entrada_gasto = tk.Entry(frame)
entrada_gasto.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
entrada_gasto.insert(0, "Valor do gasto")


botao = tk.Button(frame, text="Calcular", command=clicar_botao)
botao.grid(row=3, column=0, columnspan=2, pady=10)


resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)


janela.mainloop()