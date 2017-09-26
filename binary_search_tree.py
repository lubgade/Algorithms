# Node object
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree object
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                # print "Right available for: %s" % current.right.value
                self.insert_helper(current.right, new_val)
            else:
                # print "No right inserting node"
                current.right = Node(new_val)
        else:
            # print "current>new_val"
            if current.left:
                # print "Left available for: %s" % current.left.value
                self.insert_helper(current.left, new_val)
            else:
                # print "No left inserting node"
                current.left = Node(new_val)

    def search_helper(self, current, find_val):
        # print "current.value: %s" % current.value
        if current:
            if current.value == find_val:
                print "current==find_val"
                return True
            elif current.value < find_val:
                print "current.value<find_val"
                # print current.right.value
                print find_val
                self.search_helper(current.right, find_val)

            else:
                print "current.value>find_val"
                # print current.left.value
                self.search_helper(current.left, find_val)

        else:
            return False

def lca(root, n1, n2):
    while root is not None:
        if root is None:
            return None
        elif n1 < root.data and n2 < root.data:
            root = root.left
        elif n1 > root.data and n2 > root.data:
            root = root.right
        else:
            break
    return root.data


        
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.right.left = Node(10)
root.right.right = Node(14)

t = lca(root, 10, 14)
print "Least common ancestor is: %s" % t


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
tree.search(6)
# Should be False
tree.search(1)