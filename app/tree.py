import random


class Node:
    def __init__(self, value, _id):
        self.value = value
        self.id = _id
        self.left = None
        self.right = None

    def equals(self, other):
        if other is None:
            return False
        if self.value != other.value:
            return False
        left_equal = self.left.equals(other.left) if self.left and other.left else self.left is other.left
        right_equal = self.right.equals(other.right) if self.right and other.right else self.right is other.right
        return left_equal and right_equal


class BinaryTree:
    def __init__(self):
        self.root = None
        self.nodes_amount = 0

    def insert_node(self, value, node: Node):
        if node is None:
            self.nodes_amount += 1
            return Node(value, self.nodes_amount)
        if random.randint(0, 1):
            node.left = self.insert_node(value, node.left)
        else:
            node.right = self.insert_node(value, node.right)
        return node

    def insert(self, value):
        self.root = self.insert_node(value, self.root)

    def print_tree(self, node, indent=""):
        if node is not None:
            print(indent + str(node.value))
            self.print_tree(node.left, indent + "  ")
            self.print_tree(node.right, indent + "  ")

    def random_insertion(self, start: int, end: int, amount: int):
        values = [random.randint(start, end) for _ in range(amount)]
        for value in values:
            self.insert(value)

    def print_full_tree(self):
        self.print_tree(self.root)

    def export_tree(self, node):
        if node is None:
            return ""
        result = f"{node.value}: ["
        if node.left:
            result += f"{node.left.value}, "
        if node.right:
            result += f"{node.right.value}"
        result += "], "
        result += self.export_tree(node.left)
        result += self.export_tree(node.right)
        return result

    def export_tree_with_ids(self, node):
        if node is None:
            return ""
        result = f"({node.id}, {node.value}): ["
        if node.left:
            result += f"({node.left.id}, {node.left.value})"
        if node.right and node.left:
            result += ", "
        if node.right:
            result += f"({node.right.id}, {node.right.value})"
        result += "],\n"
        result += self.export_tree_with_ids(node.left)
        result += self.export_tree_with_ids(node.right)
        return result

    def export_tree_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.export_tree(self.root))

    def export_tree_with_ids_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write('{\n' + self.export_tree_with_ids(self.root) + '}')

    # def same(self, r: Node, s: Node):
    #     if r is None and s is None:
    #         return True
    #
    #     if r and s and r.value == s.value:
    #         return self.same(r.right, s.right) and self.same(r.left, s.left)
    #
    #     return False
    #
    # def is_subtree(self, root: Node, sub_root: Node) -> bool:
    #     if sub_root is None:
    #         return True
    #
    #     if root is None:
    #         return False
    #
    #     if self.same(root, sub_root):
    #         return True
    #     return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    def find_subtrees(self, subtree_structure):
        def dfs(node):
            if node is None:
                return []
            result = []
            if node.equals(subtree_structure):
                result.append(node)
            result.extend(dfs(node.left))
            result.extend(dfs(node.right))
            return result

        return dfs(self.root)

    def read_tree_from_dict(self, tree_dict):
        nodes = {}
        for node_id_value, children in tree_dict.items():
            node_id, value = node_id_value
            if node_id not in nodes:
                nodes[node_id] = Node(value, node_id)
            node = nodes[node_id]
            if children:
                left_child, right_child = children[0], children[1] if len(children) > 1 else None
                if left_child:
                    left_id, left_value = left_child
                    if left_id not in nodes:
                        nodes[left_id] = Node(left_value, left_id)
                    node.left = nodes[left_id]
                if right_child:
                    right_id, right_value = right_child
                    if right_id not in nodes:
                        nodes[right_id] = Node(right_value, right_id)
                    node.right = nodes[right_id]
        self.root = nodes[1]
