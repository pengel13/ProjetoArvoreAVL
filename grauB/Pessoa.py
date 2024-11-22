from datetime import date


class Pessoa:

    def __init__(self, cpf: str, rg: str, nome: str, data: str, cidade: str):
        self.setCPF(cpf)
        self.setRG(rg)
        self._nome = nome
        self._data = data
        self._cidade = cidade

    def setCPF(self, cpf: str):
        if cpf.isnumeric():
            self.CPF = cpf
            return
        raise TypeError("Valor Inválido para CPF")

    def setRG(self, rg: str):
        if rg.isnumeric():
            self.RG = rg
            return
        raise TypeError("Valor Inválido para RG")

    @property
    def getCPF(self):
        return int(self.CPF)

    @property
    def getNome(self):
        return self._nome

    @property
    def getRG(self):
        return self.RG

    @property
    def getData(self):
        return self._data

    @property
    def getCidade(self):
        return self._cidade

    def __str__(self) -> str:
        return f"Nome: {self.getNome}\nCPF: {self.getCPF}\nRG: {self.getRG}\nData de Nascimento: {self.getData}\nCidade Natal: {self.getCidade}"


if __name__ == "__main__":
    p = Pessoa(
        "0542636039",
        "3119606964",
        "Pedro Engel",
        date(day=13, month=1, year=2005),
        "São Leopoldo",
    )
    print(p)
