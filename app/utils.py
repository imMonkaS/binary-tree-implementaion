import matplotlib.pyplot as plt
import networkx as nx

from typing import Tuple, Dict, List, Union, Optional

SOURCES_PATH = 'app/sources/'


def draw_tree(
        tree: Dict[Tuple[int, Union[int, str]], List[Tuple[int, Union[int, str]]]],
        show_tree: bool = False,
        fig_size: Tuple[int, int] = (12, 12),
        show_ids: bool = False,
        make_image: Optional[str] = None
):
    graph = nx.DiGraph()

    id_to_value = {}

    for node, children in tree.items():
        if node[0] not in id_to_value.keys():
            id_to_value[node[0]] = f'{node[0]}: {node[1]}' if show_ids else node[1]
        for child in children:
            if child[0] not in id_to_value.keys():
                id_to_value[child[0]] = f'{child[0]}: {child[1]}' if show_ids else child[1]
            graph.add_edge(node[0], child[0])

    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')
    plt.figure(figsize=fig_size)
    nx.draw(graph, pos, with_labels=True, arrows=False, labels=id_to_value)
    if make_image is not None:
        plt.savefig(make_image)
    if show_tree:
        plt.show()


def dict_from_file(filename: str) -> Dict:
    try:
        with open(filename, 'r') as f:
            try:
                tree_dict = eval(f.read())
            except Exception as e:
                raise e
    except Exception as e:
        raise e
    return tree_dict
