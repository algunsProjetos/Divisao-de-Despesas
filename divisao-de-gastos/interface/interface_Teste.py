import customtkinter as ctk

ctk.set_appearance_mode("dark")  # "light" ou "dark"
ctk.set_default_color_theme("blue")

def mostrar_resultado():
    resultado.configure(text="Resultado aqui")

app = ctk.CTk()
app.title("Divisão de Renda")
app.geometry("400x300")

# título
titulo = ctk.CTkLabel(app, text="Divisão do Casal", font=("Arial", 20))
titulo.pack(pady=20)

# campos
entrada1 = ctk.CTkEntry(app, placeholder_text="Salário Pessoa 1")
entrada1.pack(pady=10)

entrada2 = ctk.CTkEntry(app, placeholder_text="Salário Pessoa 2")
entrada2.pack(pady=10)



# botão
botao = ctk.CTkButton(app, text="Calcular", command=mostrar_resultado)
botao.pack(pady=20)



# resultado
resultado = ctk.CTkLabel(app, text="")
resultado.pack()

app.mainloop()