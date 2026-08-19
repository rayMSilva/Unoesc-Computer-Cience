
valorCons = float
taxaGorje = int
def valorGorjeta(valorCons,taxaGorje):
    vGorjeta = valorCons * (taxaGorje/100)
    totalGasto = valorCons + vGorjeta
    print(f"Com base no valor de consumo de R${valorCons} do cliente, mais a taxa de {taxaGorje}%, resulta no valor de R${vGorjeta} de gorjeta para o garçom.\nO que totaliza um valor de R${totalGasto}.")
    return totalGasto

def SemGorjeta(valorCons):
    print(f"O valor total gasto fica R${valorCons}, sem acréscimo de gorjeta.")


valorCons = int(input("Informe o valor total de consumo do cliente\n"))
taxaGorje = int(input("Informe a porcentagem da gorjeta que desejar\n"))

if valorCons == 0:
    print("O valor da compra consta 0 verifique se o valor está correto")

elif taxaGorje == 0:
    SemGorjeta(valorCons)
  
else:
    valorGorjeta(valorCons,taxaGorje)