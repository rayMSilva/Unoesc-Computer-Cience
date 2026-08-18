
ValorCons = float
TaxaGorje = int
def ValorGorjeta(ValorCons,TaxaGorje):
    vGorjeta = ValorCons * (TaxaGorje/100)
    TotalGasto = ValorCons + vGorjeta
    print(f"Com base no valor de consumo de R${ValorCons} do cliente, mais a taxa de {TaxaGorje}%, resulta no valor de R${vGorjeta} de gorjeta para o garçom.\nO que totaliza um valor de R${TotalGasto}.")
    return TotalGasto

def SemGorjeta(ValorCons):
    print(f"O valor total gasto fica R${ValorCons}, sem acréscimo de gorjeta.")


ValorCons = int(input("Informe o valor total de consumo do cliente\n"))
TaxaGorje = int(input("Informe a porcentagem da gorjeta que desejar\n"))

if ValorCons == 0:
    print("O valor da compra consta 0 verifique se o valor está correto")

elif TaxaGorje == 0:
    SemGorjeta(ValorCons)
  
else:
    ValorGorjeta(ValorCons,TaxaGorje)