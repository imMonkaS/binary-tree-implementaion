from tree import BinaryTree
from utils import SOURCES_PATH, dict_from_file, draw_tree
import time


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