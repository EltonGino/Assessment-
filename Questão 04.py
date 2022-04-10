valor_Inicial = float(input("Valor inicial: R$ "))
taxa = float(input("Rendimento por período (%): "))
investimento = float(input("Aporte a cada período: ")) 
periodo = int(input("Total de períodos: ")) 

mês = 1
valor_Entrada = valor_Inicial
while mês <= periodo:
    valor_Entrada = valor_Entrada + (valor_Entrada * (taxa / 100)) + investimento
    print ("Após o %d° períodos(s), o montante será de R$ %5.2f." % (mês, valor_Entrada))
    mês = mês + 1
print ("Ao final dos periodos, o montante obtido será de R$%8.2f." % (valor_Entrada-valor_Inicial))