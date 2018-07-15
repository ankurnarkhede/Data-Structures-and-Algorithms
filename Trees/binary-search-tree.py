

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
            self.root = Node (data)
        else:
            self._add (data, self.root)

    def _add(self, data, node):
        if (data <= node.data):
            if (node.left != None):
                self._add (data, node.left)
            else:
                node.left = Node (data)
        else:
            if (node.right != None):
                self._add (data, node.right)
            else:
                node.right = Node (data)

    def find(self, data):
        if (self.root != None):
            return self._find (data, self.root)
        else:
            return None

    def _find(self, data, node):
        if (data == node.data):
            return node
        elif (data < node.data and node.left != None):
            return self._find (data, node.left)
        elif (data > node.data and node.right != None):
            return self._find (data, node.right)

    def height(self, node):
        if (node==None):
            return 0
        else:
            return ( 1 + max(tree.height(node.left), tree.height(node.right)) )



    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self, order='in_order'):
        if (self.root != None):
            if (order == 'in_order'):
                self.in_order (self.root)
            elif (order == 'pre_order'):
                self.pre_order (self.root)
            elif (order == 'post_order'):
                self.post_order (self.root)

    def in_order(self, node):
        if (node != None):
            self.in_order (node.left)
            print (str (node.data) + ' ')
            self.in_order (node.right)

    def pre_order(self, node):
        if (node != None):
            print (str (node.data) + ' ')
            self.pre_order (node.left)
            self.pre_order (node.right)

    def post_order(self, node):
        if (node != None):
            self.post_order (node.left)
            self.post_order (node.right)
            print (str (node.data) + ' ')

    def max_on_path(self, start_node, end):
        # finding maximum value on path between startnode and end
        maximum = 0
        while start_node.data != end:
            if start_node.data > end:
                maximum = max (maximum, start_node.data)
                start_node = start_node.left
            elif start_node.data < end:
                maximum = max (maximum, start_node.data)
                start_node = start_node.right
        return max (maximum, end)

    def lca(self, x, y):
        # finding the lowest common ancestor
        p = self.root
        while (p.data > x and p.data > y) or (p.data < x and p.data < y):
            if x < p.data and y < p.data:
                p = p.left
            elif x > p.data and y > p.data:
                p = p.right
        return p


#    3
# 0     4
#   2      8
tree = Tree ()

tree.add (3)
tree.add (4)
tree.add (0)
tree.add (8)
tree.add (2)
tree.printTree ()
tree.printTree ('post_order')
print (tree.getRoot ().data)
print ('finding 2:', end='')
print ((tree.find (2)))
print ('finding 10:', end='')
print (tree.find (10))
tree.deleteTree ()
tree.printTree ('post_order')
print ('bbye')
