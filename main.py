from menu import showMenu
from Tree import Tree, Node

avl = Tree()
root = None
choice = 99
while choice != 0:

    showMenu()
    choice = input("Digite o número da escolha o que você deseja fazer: ")

    if not choice.isnumeric():
        print("Digite um número")
        continue

    choice = int(choice)
    match choice:
        case 1:
            number = input("Digite o número a ser inserido na tabela: ")
            if not number.isnumeric():
                print(
                    "O valor não vai ser inserido pois a árvore só aceita valores inteiros"
                )
                continue
            if not avl.search(root, number):
                root = avl.insert(root, number)
                print(f"{number} inserido")
            else:
                print("Árvore AVL não aceita valores duplicados")
        case 2:
            number = input("Digite o número a ser deletado da tabela: ")
            if not number.isnumeric():
                print(
                    "O valor não vai ser inserido pois a árvore só aceita valores inteiros"
                )
                continue
            if avl.search(root, number):
                avl.delete(root, number)
                print(f"{number} deletado")
            else:
                print(f"{number} não existe na tabela")

        case 3:
            number = input("Digite o número que desejas procurar: ")
            if not number.isnumeric():
                print(
                    "O valor não vai ser inserido pois a árvore só aceita valores inteiros."
                )
                continue
            if avl.search(root, number):
                print(f"Número {number} existe na tabela")
            else:
                print(f"Número não existe na tabela")
        case 4:
            print(avl.pre_ordem(root))
        case 5:
            print(avl.em_ordem(root))
        case 6:
            print(avl.pos_ordem(root))
        case 7:
            avl.print_tree(root)
        case 8:
            print(avl.get_numero_balanceamento(root))
        case 9:
            print(avl.get_altura(root))
        case 0:
            print("Abraçoes")
        case others:
            print("Número inválido")
