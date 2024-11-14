# Idade pela data do seu nascimento
# Imoprtar e capturar a data completa
import datetime
data_atual = datetime.date.today() # Armazena a data completa
nascimento = int(input('Informe a data o ano do seu nascimento'))
ano_atual = data_atual.year # Armazena o ano atual
idade = ano_atual - nascimento
print(f' A sua é {idade} anos.')