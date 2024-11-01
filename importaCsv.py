import pandas as pd

def lerCsv(filePath:str) -> list[tuple]:
    try:
        dados = pd.read_csv(filePath, sep = ';', header=None)
    except pd.errors.EmptyDataError:
        return "Arquivo vazio"
    except FileNotFoundError:
        return f"Não foi achado o arquivo {filePath}"
    return dados

