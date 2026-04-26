"""
Para fazer uma conexão limpa com a interface, vou precisar usar funções(def). 
contionua sendo a mesma logica, tirando os inputs e prints.
"""

#sim, esses nomes são enormes, eu realmente n pensei em nada melhor.
def cal_proporcionalmente(salario1,salario2,gasto):
    valor_Bruto = salario1 + salario2 #retorna valor bruto da casa (soma dos salarios)
    
    ##add alguma verificação aq caso digite zero

    representacao_parceiro1 = salario1 / valor_Bruto #quanto deste salario influencia no valor bruto da casa
    representacao_parceiro2 = salario2 / valor_Bruto

    parte_paga_parceiro1=gasto*representacao_parceiro1 
    parte_paga_parceiro2=gasto*representacao_parceiro2

    return (
        valor_Bruto,
        representacao_parceiro1,
        representacao_parceiro2,
        parte_paga_parceiro1,
        parte_paga_parceiro2
    )


