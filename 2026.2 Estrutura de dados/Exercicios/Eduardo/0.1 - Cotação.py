#Funções de cálculo
def FuncaoDolar(ValorInic, Cotacao):
    a = ValorInic * Cotacao
    return a
def FuncaoReal(ValorInic, Cotacao):
    a = ValorInic / Cotacao
    return a

#Definir cotação
Cotacao = float(input("Informe a cotação atual do Dolar\n"))

#Imput de seleção para qual método de converssão deseja usar
Ident = int(input(f"Informe o formato de conversão que deseja realizar!\nCotação Dolar base R${Cotacao} → $1,00\n1.Dolar → Real\n2.Real → Dolar\n"))

#Qual valor o usuário utilizará para o cálculo
ValorInic = float(input("Informe o valor que deseja converter!\n"))


#Identificação do cálculo
if Ident == 1:
    print(f"A conversão de ${ValorInic} é R${FuncaoDolar(ValorInic, Cotacao)}")
elif Ident == 2:
    print(f"A conversão de R${ValorInic} é ${FuncaoReal(ValorInic, Cotacao)}")
else:
    print("Valor identificado não é válido")