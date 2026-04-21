def Entrada_Float(num):
    return float(input(num))

def Entrada_string(caractere):
    return str(input(caractere))

p1 = Entrada_string('Parceiro 1: ')
s1 = Entrada_Float('Salário do parceiro 1: ')

p2 = Entrada_string('Parceiro 2: ')
s2 = Entrada_Float('Salário do parceiro 2: ')

valor_Bruto = s1 + s2

if valor_Bruto == 0:
    print("Erro: renda total não pode ser zero.")
    exit()

representacao_P1 = s1 / valor_Bruto
representacao_P2 = s2 / valor_Bruto

gasto_fixo_exemplo = 1300

pg_P1 = gasto_fixo_exemplo * representacao_P1
pg_P2 = gasto_fixo_exemplo * representacao_P2

print('\n--- Divisão de Despesas ---')
print(f'{p1} paga: R$ {pg_P1:.2f}')
print(f'{p2} paga: R$ {pg_P2:.2f}')
print(f'{p1} representa {representacao_P1*100:.1f}% da renda')
print(f'{p2} representa {representacao_P2*100:.1f}% da renda')