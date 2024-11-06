import pandas as pd
from Pessoa import Pessoa
from datetime import date

def lerCsv(filePath:str) -> pd.DataFrame:
    try:
        dados = pd.read_csv(filePath, sep = ';', header=None)
    except pd.errors.EmptyDataError:
        return "Arquivo vazio"
    except FileNotFoundError:
        return f"Não foi achado o arquivo {filePath}"
    return dados

def criaPessoas(data:list[list]) -> list[Pessoa]:
    pessoas = []
    for dado in data:
        
        dia, mes, ano = str(dado[3]).split('/')
        pessoa = Pessoa(cpf=str(dado[0]), rg= dado[1], nome=dado[2], data=date(int(ano), int(mes), int(dia)), cidade = dado[4])  
        pessoas.append(pessoa)
    return pessoas

pessoas = criaPessoas(lerCsv("exemplo.csv").values)
for pessoa in pessoas:
    print(pessoa)
# print(lerCsv("exemplo.csv"))