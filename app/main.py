from tests import *

from utils import randomly_generate_tree_and_subtree_files


def main():
    bt = BinaryTree()
    bt.random_insertion(0, 100, 20)

    subtree = BinaryTree()
    subtree.random_insertion(0, 100, 3)

    bt.find_subtrees(subtree.root)


if __name__ == '__main__':
    main()
