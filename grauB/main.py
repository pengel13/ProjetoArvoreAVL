# from grauA.menu import showMenu
import sys
import os
import pandas as pd
from menu import showMenuMain
from importaCsv import lerCsv, criaPessoas
from Pessoa import Pessoa

sys.path.append(os.getcwd().replace("grauB", ""))

from grauA.Tree import Tree, Node


choice = 99
while choice != 0:
    filePath = str(input("Digite o caminho do arquivo csv a ser lido:"))
    dadosPessoas = lerCsv(filePath)

    # se voltar um dataframe indica que o caminho do csv está certo
    if isinstance(dadosPessoas, pd.DataFrame):
        pessoasList = criaPessoas(dadosPessoas.values)
        choice = 0
    else:
        print(dadosPessoas)


def criarArvore(pessoasList: list[Pessoa], campo: str) -> tuple[Tree, Node]:
    # criar árvores diferentes com a mesma função para ser menos código

    avl = Tree()
    root = None
    for pessoa in pessoasList:
        if campo == "CPF":
            root = avl.insert(root, pessoa.getCPF)
        elif campo == "Data":
            root = avl.insert(root, pessoa.getData)
        elif campo == "Nome":
            root = avl.insert(root, pessoa.getNome)
    
    return avl, root

# cria as 3 instâncias de árvore avl
avlCPF, rootCPF = criarArvore(pessoasList, "CPF")
avlData, rootData = criarArvore(pessoasList, "Data")
avlNome, rootNome = criarArvore(pessoasList, "Nome")

root = None
while choice != 99:
    ## utilizando as funções criadas da árvore e de pessoa, faz a busca por cpf, data e nome

    showMenuMain()
    choice = input("Digite o número da escolha o que você deseja fazer: ")
    if not choice.isnumeric():
        print("Digite um número")
        continue

    choice = int(choice)
    match choice:
        case 1:
            cpf = input("Digite o CPF que desejas buscar:")
            if not cpf.isnumeric():
                print("CPF deve ser escrito apenas com números")
                continue
            cpf = int(cpf)
            if avlCPF.search(rootCPF, cpf):
                for pessoa in pessoasList:
                    if pessoa.getCPF == cpf:
                        print(pessoa)
                        continue
            else:
                print("Não há a pessoa com este CPF na árvore")
        case 2:
            data = input("Digite a data de nascimento que desejas buscar:")
    
            if avlData.search(rootData, data):
                for pessoa in pessoasList:
                    if pessoa.getData == data:
                        print(pessoa)
                        continue
            else:
                print("Não há a pessoa com esta data de nascimento na árvore")

        case 3:
            nome = input("Digite o nome que desejas buscar:")
    
            if avlNome.search(rootNome, nome):
                for pessoa in pessoasList:
                    if pessoa.getNome == nome:
                        print(pessoa)
                        continue
            else:
                print("Não há a pessoa com este nome  na árvore")
        case 99:
            print("Abraço!")
            choice = 99
        case others:
            print("Número inválido")
        