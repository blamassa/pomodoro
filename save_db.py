# Salva o numero de sessões pomodoro que fiz por dia.
# Permite uma analise posterior do meu rendimento diario.

import csv
import time

# Ler a data e salvar em uma variavel
data_atual = time.strftime("%d/%m/%Y")

print(data_atual)

def append_linha_nova(data_atual):
    f = open('/home/blamassa/apps/pomodoro-database/db.csv', 'a', newline='')
    writer=csv.writer(f)
    writer.writerow([str(data_atual)])
    f.close()

append_linha_nova(data_atual)
