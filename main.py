from time import sleep
from menu import showMenu
from definicaoTree import Tree

choice = 0
tree = Tree()
tree.insert(10)
tree.insert(11)
tree.insert(12)
while choice != 9:
    sleep(0.5)
    showMenu()
    choice = input('Digite o número da escolha o que você deseja fazer: ')
        
    if not choice.isnumeric():
        print('Digite um número')
        sleep(0.5)
        continue

    choice = int(choice)
    match choice:
        case 1:
            number = input('Digite o número a ser inserido na tabela: ')
            if not number.isnumeric():
                print('O valor não vai ser inserido pois a árvore só aceita valores inteiros')
                continue
            print(tree.insert(int(number)))
            print(tree.values)
        case 3:
            number = input('Digite o número que desejas procurar: ')
            if not number.isnumeric():
                print('O valor não vai ser inserido pois a árvore só aceita valores inteiros.')
                continue
            print(tree.select(int(number)))
        case 9:
            print('TCHAUUUU')
