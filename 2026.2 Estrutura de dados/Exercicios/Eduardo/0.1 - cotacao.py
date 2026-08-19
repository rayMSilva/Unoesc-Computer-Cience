#Funções de cálculo
def funcaoDolar(valorInic, cotacao):
    a = valorInic * cotacao
    return a
def funcaoReal(valorInic, cotacao):
    a = valorInic / cotacao
    return a

#Definir cotação
cotacao = float(input("Informe a cotação atual do Dolar\n"))

#Imput de seleção para qual método de converssão deseja usar
ident = int(input(f"Informe o formato de conversão que deseja realizar!\nCotação Dolar base R${cotacao} → $1,00\n1.Dolar → Real\n2.Real → Dolar\n"))

#Qual valor o usuário utilizará para o cálculo
valorInic = float(input("Informe o valor que deseja converter!\n"))


#Identificação do cálculo
if ident == 1:
    print(f"A conversão de ${valorInic} é R${funcaoDolar(valorInic, cotacao)}")
elif ident == 2:
    print(f"A conversão de R${valorInic} é ${funcaoReal(valorInic, cotacao)}")
else:
    print("Valor identificado não é válido")