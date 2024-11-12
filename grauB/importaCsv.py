import pandas as pd
from datetime import date
from Pessoa import Pessoa


def lerCsv(filePath: str) -> pd.DataFrame | str:
    try:
        dados = pd.read_csv(filePath, sep=";", header=None)
    except pd.errors.EmptyDataError:
        return "Arquivo vazio"
    except FileNotFoundError:
        return f"Não foi achado o arquivo {filePath}"
    return dados


def criaPessoas(data: list[list]) -> list[Pessoa]:
    pessoas = []
    for dado in data:
        dia, mes, ano = str(dado[3]).split("/")
        pessoa = Pessoa(
            cpf=str(dado[0]),
            rg=str(dado[1]),
            nome=dado[2],
            data=date(int(ano), int(mes), int(dia)),
            cidade=dado[4],
        )
        pessoas.append(pessoa)
    return pessoas


if __name__ == "__main__":
    pessoas = lerCsv("exemplo.csv")
    if isinstance(pessoas, pd.DataFrame):
        criaPessoas(pessoas.values)
        for pessoa in pessoas.values:
            print(pessoa)
    else:
        print(pessoas)
