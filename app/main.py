import time
from functools import wraps

from tree import BinaryTree
from utils import draw_tree, dict_from_file, SOURCES_PATH


def main():
    bt = BinaryTree()
    subtree = BinaryTree()

    bt.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'tree.txt'))
    subtree.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'subtree.txt'))
    # bt.random_insertion(10, 12, 20)

    # bt.print_full_tree()

    # -----------TIME MEASURING-------------
    with open(SOURCES_PATH + '20nodes_output.txt', 'w') as output_file:
        start_time = time.perf_counter()
        nodes = bt.find_subtrees(subtree.root)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        output_file.write(f'Function find_subtrees Took {total_time*1000:.3f} ms\n')

        for node in nodes:
            output_file.write(str(node.id) + '\n')
    # -------------------------------------

    # bt.export_tree_with_ids_to_file(SOURCES_PATH + 'tree20nodes.txt')
    # subtree.export_tree_with_ids_to_file(SOURCES_PATH + 'subtree3nodes.txt')


if __name__ == '__main__':
    main()
