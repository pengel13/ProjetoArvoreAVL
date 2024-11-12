# from grauA.menu import showMenu
import sys
import os

sys.path.append(os.getcwd().replace("grauB", ''))

from grauA.Tree import Tree, Node
from grauA.menu import showMenu

avl = Tree()
root = None
choice = 99
while choice != 0:

