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