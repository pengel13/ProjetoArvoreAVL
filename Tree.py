class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def get_altura(self, node):
        if not node:
            return 0
        return node.height

    def get_numero_balanceamento(self, node):
        if not node:
            return 0
        return self.get_altura(node.left) - self.get_altura(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right))
        x.height = 1 + max(self.get_altura(x.left), self.get_altura(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_altura(x.left), self.get_altura(x.right))
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right))
        return y

    # Processo de inserção
    def insert(self, node, key):

        if not node:
            return Node(key)

        # Checa se nó é duplicado
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        # Atualiza a altura do nó
        node.height = 1 + max(self.get_altura(node.left), self.get_altura(node.right))

        # Obtem o fator de balanceamento para checar se este nó ficou desbalanceado
        balance = self.get_numero_balanceamento(node)

        # Casos de rotação para balancear a árvore

        # Caso Esquerda-Esquerda
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Caso Direita-Direita
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Caso Esquerda-Direita
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Caso Direita-Esquerda
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Funcao para encontrar o sucessor de um nó quando um nó que tem 2 filhos for deletado
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Processo de exclusão
    def delete(self, root, key):
        
        if not root:
            return root
        
        # checa se o nó existe e faz a pesquisa pelo nó.
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # Atualiza a altura do nó
        root.height = 1 + max(self.get_altura(root.left), self.get_altura(root.right))

        # Obtem o fator de balanceamento para checar se este nó ficou desbalanceado
        balance = self.get_numero_balanceamento(root)

        # Casos de rotação para balancear a árvore

        # Caso Esquerda-Esquerda
        if balance > 1 and self.get_numero_balanceamento(root.left) >= 0:
            return self.right_rotate(root)

        # Caso Esquerda-Direita
        if balance > 1 and self.get_numero_balanceamento(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Direita-Direita
        if balance < -1 and self.get_numero_balanceamento(root.right) <= 0:
            return self.left_rotate(root)

        # Caso Direita-Esquerda
        if balance < -1 and self.get_numero_balanceamento(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Processo de pesquisa de nó
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Retorna uma lista com os números em pré ordem
    def pre_ordem(self, root):
        if not root:
            return []
        return [root.key] + self.pre_ordem(root.left) + self.pre_ordem(root.right)

    # Retorna uma lista com os números em ordem
    def em_ordem(self, root):
        if not root:
            return []
        return self.em_ordem(root.left) + [root.key] + self.em_ordem(root.right)

    # Retorna uma lista com os números em pós ordem
    def pos_ordem(self, root):
        if not root:
            return []
        return self.pos_ordem(root.left) + self.pos_ordem(root.right) + [root.key]

    # Função para imprimir a árvore em esquema de árvore
    def print_tree(self, root, level=0, prefix="Root: "):
        # Checa se a árvore é vazia
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            if root.left is not None or root.right is not None:
                if root.left:
                    self.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        else:
            print("Árvore Vazia")


if __name__ == "__main__":
    # Exemplo de uso
    avl = Tree()
    root = None

    # Inserindo nós
    nums = [10, 20, 30, 40, 50, 25]
    for num in nums:
        root = avl.insert(root, num)

    # Imprimindo a árvore
    print("Estrutura da Árvore AVL:")
    avl.print_tree(root)

    # Encaminhamento
    print("\nPré-ordem:", avl.pre_ordem(root))  # Pré-ordem
    print("Em ordem:", avl.em_ordem(root))  # Em ordem
    print("Pós-ordem:", avl.pos_ordem(root))  # Pós-ordem

    # Buscando um elemento
    search_key = 30
    found_node = avl.search(root, search_key)
    if found_node:
        print(f"\nElemento {search_key} encontrado.")
    else:
        print(f"\nElemento {search_key} não encontrado.")

    # Deletando um nó
    delete_key = 20
    root = avl.delete(root, delete_key)
    print(f"\nApós deletar {delete_key}, estrutura da árvore AVL:")
    avl.print_tree(root)
