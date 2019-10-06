# Salva o numero de sessões pomodoro que fiz por dia.
# Permite uma analise posterior do meu rendimento diario.

import csv
import sys
import time
import pandas as pd

if sys.argv[-1] == 'save_db.py':
    project_name = 'none'
else:
    project_name = sys.argv[-1]

# Ler a data e salvar em uma variavel
data_atual = time.strftime("%d/%m/%Y")


def append_linha_nova(data_atual):
    f = open('db.csv', 'a', newline='\n')
    writer=csv.writer(f)
    writer.writerow([str(data_atual), project_name])
    f.close()

append_linha_nova(data_atual)

## Update available projects
