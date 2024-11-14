# Programa Prestação em atraso
# cls limpar
prestacao = float(input('Informe o valor da prestação'))
taxa = float(input('Informe o valor da taxa'))
tempo = float(input('Informe a quantidade de meses em atraso'))
valorfinal = prestacao+(prestacao*(taxa/100)*tempo)
print(f' O valor fina da prestação é R$ {valorfinal}')