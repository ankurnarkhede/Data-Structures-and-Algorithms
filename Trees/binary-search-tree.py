class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if (data <= node.data):
            if (node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if (node.right != None):
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if (self.root != None):
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if (data == node.data):
            return node
        elif (data < node.data and node.left != None):
            return self._find(data, node.left)
        elif (data > node.data and node.right != None):
            return self._find(data, node.right)

    def height(self, node):
        if (node == None):
            return 0
        else:
            return (1 + max(tree.height(node.left), tree.height(node.right)))

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self, order='in_order'):
        if (self.root != None):
            if (order == 'in_order'):
                self.in_order(self.root)
            elif (order == 'pre_order'):
                self.pre_order(self.root)
            elif (order == 'post_order'):
                self.post_order(self.root)

    def in_order(self, node):
        if (node != None):
            self.in_order(node.left)
            print(str(node.data) + ' ')
            self.in_order(node.right)

    def pre_order(self, node):
        if (node != None):
            print(str(node.data) + ' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if (node != None):
            self.post_order(node.left)
            self.post_order(node.right)
            print(str(node.data) + ' ')

    def max_on_path(self, start_node, end):
        # finding maximum value on path between startnode and end
        maximum = 0
        while start_node.data != end:
            if start_node.data > end:
                maximum = max(maximum, start_node.data)
                start_node = start_node.left
            elif start_node.data < end:
                maximum = max(maximum, start_node.data)
                start_node = start_node.right
        return max(maximum, end)

    def lca(self, x, y):
        # finding the lowest common ancestor
        p = self.root
        while (p.data > x and p.data > y) or (p.data < x and p.data < y):
            if x < p.data and y < p.data:
                p = p.left
            elif x > p.data and y > p.data:
                p = p.right
        return p

    # Given a non-empty binary
    # search tree, return the node
    # with minum key value
    # found in that tree. Note that the
    # entire tree does not need to be searched


    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

        # Given a binary search tree and a key, this function
        # delete the key and returns the new root


    def deleteNode(self, root, key):

        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(key > root.key):
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's
            # content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)

        return root


#    3
# 0     4
#   2      8
tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
tree.printTree('post_order')
print(tree.getRoot().data)
print('finding 2:', end='')
print((tree.find(2)))
print('finding 10:', end='')
print(tree.find(10))
tree.deleteTree()
tree.printTree('post_order')
print('bbye')
