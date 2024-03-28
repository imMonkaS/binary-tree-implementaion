import datetime

from tree import BinaryTree
from utils import SOURCES_PATH, dict_from_file, draw_tree
import time


def ultimate_test(tree_file: str, subtree_file: str, output_file: str, time_file: str):
    with open(output_file, 'w') as f:
        f.write('')

    start_time = time.perf_counter()
    bt = BinaryTree()
    subtree = BinaryTree()

    bt.read_tree_from_dict(dict_from_file(tree_file))
    subtree.read_tree_from_dict(dict_from_file(subtree_file))

    # -----------TIME MEASURING-------------
    with open(time_file, 'a') as f:
        nodes = bt.find_subtrees_and_print_to_file(subtree.root, output_file)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        f.write(f'{datetime.datetime.now()}: Function find_subtrees Took {total_time*1000:.3f} ms or {total_time:.6f} s\n\n')
    # -------------------------------------


def two_million_random_test():
    bt = BinaryTree()
    subtree = BinaryTree()

    start_time = time.perf_counter()
    bt.random_insertion(10, 15, 5 * 10**5)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Function random_insertion for 2 million nodes Took {total_time * 1000:.3f} ms or {total_time:.6f} s\n')

    subtree.random_insertion(10, 12, 5)

    # -----------TIME MEASURING-------------
    start_time = time.perf_counter()
    nodes = bt.find_subtrees(subtree.root)
    end_time = time.perf_counter()
    total_time = end_time - start_time

    print(f'Function find_subtrees Took {total_time * 1000:.3f} ms or {total_time:.6f} s\n')

    for node in nodes:
        print(str(node.id) + '\n')
    # -------------------------------------

def two_million_nodes_test():
    bt = BinaryTree()
    subtree = BinaryTree()

    # bt.random_insertion(10, 15, 2 * 10**6)
    # subtree.random_insertion(10, 12, 5)

    tree_dict = dict_from_file(SOURCES_PATH + '2miltest/tree.txt')
    bt.read_tree_from_dict(tree_dict)
    subtree.read_tree_from_dict(dict_from_file(SOURCES_PATH + '2miltest/subtree.txt'))

    # -----------TIME MEASURING-------------
    output_file_name = '2miltest/output.txt'
    with open(SOURCES_PATH + output_file_name, 'w') as output_file:
        start_time = time.perf_counter()
        nodes = bt.find_subtrees(subtree.root)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        output_file.write(f'Function find_subtrees Took {total_time*1000:.3f} ms or {total_time:.6f} s\n')

        for node in nodes:
            output_file.write(str(node.id) + '\n')
    # -------------------------------------

    # bt.export_tree_with_ids_to_file(SOURCES_PATH + '2miltest/tree.txt')
    # subtree.export_tree_with_ids_to_file(SOURCES_PATH + '2miltest/subtree.txt')
    # draw_tree(tree_dict, fig_size=(100, 100), make_image=SOURCES_PATH + '2miltest/tree.png')
    # draw_tree(
    #     dict_from_file(SOURCES_PATH + '2miltest/subtree.txt'),
    #     fig_size=(8, 8),
    #     make_image=SOURCES_PATH + '2miltest/subtree.png'
    # )


def twenty_nodes_test():
    bt = BinaryTree()
    subtree = BinaryTree()

    bt.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'tree.txt'))
    subtree.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'subtree.txt'))
    # bt.random_insertion(10, 12, 20)

    # bt.print_full_tree()

    # -----------TIME MEASURING-------------
    output_file_name = '20nodes_output.txt'
    with open(SOURCES_PATH + output_file_name, 'w') as output_file:
        start_time = time.perf_counter()
        nodes = bt.find_subtrees(subtree.root)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        output_file.write(f'Function find_subtrees Took {total_time*1000:.3f} ms or {total_time:.6f} s\n')

        for node in nodes:
            output_file.write(str(node.id) + '\n')
    # --------------------------------------

    # bt.export_tree_with_ids_to_file(SOURCES_PATH + 'tree20nodes.txt')
    # subtree.export_tree_with_ids_to_file(SOURCES_PATH + 'subtree3nodes.txt')
    # draw_tree(dict_from_file(SOURCES_PATH + 'tree.txt'), make_image=SOURCES_PATH + 'testSubtreeFinding1.png')
    # draw_tree(dict_from_file(SOURCES_PATH + 'subtree.txt'), make_image=SOURCES_PATH + 'testSubtreeFinding2.png')


def test_insertion():
    bt = BinaryTree()

    # -----------TIME MEASURING-------------
    start_time = time.perf_counter()
    bt.random_insertion(100, 1000, 2 * 10**6)
    end_time = time.perf_counter()
    total_time = end_time - start_time

    print(f'Function random_insertion for 2 mil Took {total_time * 1000:.3f} ms or {total_time:.6f} s\n')
    # -------------------------------------

    # -----------TIME MEASURING-------------
    start_time = time.perf_counter()
    bt.read_tree_from_dict(dict_from_file(SOURCES_PATH + '2miltest/tree.txt'))
    end_time = time.perf_counter()
    total_time = end_time - start_time

    print(f'Function read_tree for 2 mil Took {total_time * 1000:.3f} ms or {total_time:.6f} s\n')
    # -------------------------------------
