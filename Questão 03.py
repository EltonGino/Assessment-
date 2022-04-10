rendaMensal = float(input("Renda mensal total: R$ "))
gastoMoradia = float(input("Gastos totais com moradia: R$ "))
gastoEducacao = float(input("Gastos totais com educação: R$ "))
gastoTransporte = float(input("Gastos totais com transporte: R$"))

percentualMaximoMoradia = 30
percentualMaximoEducacao = 20
percentualMaximoTransporte = 15

def imprimirGastos(tipo, percentualMaximo, gasto, renda):
    percentual = calcularPercentual(gasto,renda)
    msg = obterMsg(gasto, renda, percentualMaximo, percentual)
    print(f"Seus gastos totais com {tipo} comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximo}%. {msg}")

def calcularPercentual(gasto, renda):
    return gasto * 100 / renda

def calcularValorMaximo(renda, percentualMaximo):
    return renda * percentualMaximo/ 100

def obterMsg(gasto, renda, percentualMaximo, percentual):
    msg = "Seus gastos estão dento da margem recomendada"
    if percentual > percentualMaximo:
        msg = f"Portanto, idealmente, o maximo de sua renda comprometida com moradia deveria ser de R$ {calcularValorMaximo(renda, percentualMaximo)}."
        
    return msg

print("Diagnóstico")
imprimirGastos("moradia", percentualMaximoMoradia, gastoMoradia,rendaMensal)
imprimirGastos("educação", percentualMaximoEducacao, gastoEducacao, rendaMensal)
imprimirGastos("transporte", percentualMaximoTransporte, gastoTransporte, rendaMensal)