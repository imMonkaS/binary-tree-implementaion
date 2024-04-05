import math
import random

import matplotlib.pyplot as plt
import networkx as nx

from typing import Tuple, Dict, List, Union, Optional

from tree import BinaryTree

SOURCES_PATH = 'app/sources/'


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc: Union[int, float] = 0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def draw_tree(
        tree: Dict[Union[int, str], List[Tuple[int, Union[int, str]]]],
        show_tree: bool = False,
        fig_size: Tuple[int, int] = (12, 12),
        show_ids: bool = False,
        make_image: Optional[str] = None,
        node_color: str = 'cyan',
        layout: str = 'n-ary'
) -> None:
    """
    Рисует дерево

    Args:
        tree: словарь дерева
        show_tree: Покажет дерево во время выполнения кода
        fig_size: размер холста
        show_ids: покажет Идшники нод
        make_image: Сделать изображение, указать путь до файла
        node_color: Цвет ноды (задний фон)
        layout:
            Как вывести (strict: с соблюдением структуры бинарного дерева;
            hierarchy: красивый вывод через мат. функцию, нашел его на одном форуме,
            не использовал для лабы, но он красивый, мне понравился, поэтому оставил;
            если ничего не написать: обычный вывод, назвал его n-ary;)

    Returns:
        None
    """

    graph = nx.DiGraph()
    parent_w_alone_child = set()

    id_to_value = {1: f'1: {tree["root_value"]}' if show_ids else tree["root_value"]}
    for node_id, children in list(tree.items())[1:]:
        if len(children) == 1:
            parent_w_alone_child.add((node_id, children[0][0]))
        for child in children:
            if child[0] not in id_to_value.keys():
                id_to_value[child[0]] = f'{child[0]}: {child[1]}' if show_ids else child[1]
            graph.add_edge(node_id, child[0])

    for node in graph.nodes():
        if node % 2 == 0:
            graph.nodes[node]['child_status'] = 'left'  # assign even to be left
        else:
            graph.nodes[node]['child_status'] = 'right'  # and odd to be right

    # default layout
    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')

    if layout == 'strict':
        for parent, child in parent_w_alone_child:
            pos[child] = (pos[parent][0] - 20, pos[child][1])
    elif layout == 'hierarchy':
        pos = hierarchy_pos(graph, 1, width = 2*math.pi, xcenter=0)
        pos = {u: (r * math.cos(theta), r * math.sin(theta)) for u, (theta, r) in pos.items()}

    plt.figure(figsize=fig_size)
    nx.draw(graph, pos, with_labels=True, node_color=node_color, arrows=False, labels=id_to_value)
    if make_image is not None:
        plt.savefig(make_image)
    if show_tree:
        plt.show()


def dict_from_file(filename: str) -> Dict:
    """
    Считывает файл и конвертирует его в словарь

    Args:
        filename:

    Returns:
        Dict
    """
    try:
        with open(filename, 'r') as f:
            try:
                tree_dict = eval(f.read())
            except Exception as e:
                raise e
    except Exception as e:
        raise e
    return tree_dict


def randomly_generate_tree_and_subtree_files(
        tree_nodes_amount: int,
        subtree_nodes_amount: int,
        tree_output_name: str,
        subtree_output_name: str,
        tree_image_name: str = None,
        subtree_image_name: str = None,
        start: int = 0,
        end: int = 100,
        show_ids: bool = True
):
    bt = BinaryTree()
    subtree = BinaryTree()

    bt.random_insertion(start, end, tree_nodes_amount)
    subtree.random_insertion(start, end, subtree_nodes_amount)

    bt.export_tree_to_file(tree_output_name)
    subtree.export_tree_to_file(subtree_output_name)

    if tree_image_name is not None:
        draw_tree(
            dict_from_file(tree_output_name),
            fig_size=(10, 10),
            make_image=tree_image_name,
            show_ids=show_ids
        )
    if subtree_image_name is not None:
        draw_tree(
            dict_from_file(subtree_output_name),
            fig_size=(8, 8),
            make_image=subtree_image_name,
            show_ids=show_ids
        )
