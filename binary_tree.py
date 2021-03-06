class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - used to create a
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - used to create a
        recursive print solution."""
        if start:
            traversal += (str(start.value) + ",")
            #print traversal
            traversal = self.preorder_print(start.left, traversal)
            #print traversal
            traversal = self.preorder_print(start.right, traversal)
            #print traversal
        return traversal



def preorder(start, nodes):
    nodes.append(start.value);
    if start and start.left:
        preorder(start.left, nodes)
    if start and start.right:
        preorder(start.right, nodes)

    return nodes

def postorder(start, nodes):
    if start and start.left:
        postorder(start.left, nodes)
    if start and start.right:
        postorder(start.right, nodes)
    nodes.append(start.value)

    return nodes


def inorder(start, nodes):
    if start and start.left:
        inorder(start.left, nodes)
    nodes.append(start.value)
    if start and start.right:
        inorder(start.right, nodes)

    return nodes


            # Set up tree


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
# print tree.search(4)
# Should be False
# print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
print preorder(tree.root, [])
print postorder(tree.root, [])
print inorder(tree.root, [])