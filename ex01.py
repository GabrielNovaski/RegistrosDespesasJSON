from pathlib import Path
import json
from datetime import datetime
import locale

def get_current_date():
    data = datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M:%S')
    return data

def create_new_file(caminho):
    if caminho.exists():
        return
    
    with open(caminho, 'w') as file:
        json.dump({}, file, ensure_ascii=False, indent=2)
    
def adicionar_gasto(valor, caminho):
    with open(caminho, 'r') as file:
        conteudo = json.load(file)
    mes = getmonth()
    if mes not in conteudo:
        conteudo[mes] = []

    data = get_current_date()
    conteudo[mes].append(f'R${valor:.2f} - {data}')
    with open(caminho, 'w') as file:
        json.dump(conteudo, file, indent=2, ensure_ascii=False)

def getmonth():
    locale.setlocale(locale.LC_ALL, '')
    mes = datetime.now().strftime('%B')
    return mes

caminho = Path(__file__).parent
caminho = caminho / 'gastos.json'


valor = float(input('Informe o valor gasto: '))

create_new_file(caminho)   
adicionar_gasto(valor, caminho)

