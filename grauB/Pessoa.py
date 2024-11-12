from datetime import date


class Pessoa:

    def __init__(self, cpf:str, rg:str, nome:str, data:date, cidade:str):
        self.setCPF(cpf)
        self.setRG(rg)
        self._nome = nome
        self._data = data
        self._cidade = cidade

    def setCPF(self, cpf:str):
        if cpf.isnumeric():
            self.CPF = cpf
            return
        raise TypeError("Valor Inválido para CPF")
    
    def setRG(self, rg:str):
        if rg.isnumeric():
            self.RG = rg
            return
        raise TypeError("Valor Inválido para RG")
    
    @property
    def getCPF(self):
        return self.CPF
    
    @property
    def getNome(self):
        return self._nome
    
    def __str__(self) -> str:
        return f"Pessoa {self.getNome} {self.getCPF}"
    

if __name__ == '__main__':
    p = Pessoa("054263A6039", "3119606964", "Pedro Engel", date(day=13 , month=1, year=2005), "São Leopoldo" )
    print(p.getNome)
