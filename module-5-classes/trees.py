
def create_linked_list():
    return {'head': None, 'tail': None, 'size':0}


def create_ll_node(data):
    return {'payload': data, 'prev_node': None, 'next_node': None}

def append(list, new_node):
    pass


class TreeNode:
    def __init__(self, data):
        self.payload = data
        self.left_child = None
        self.right_child = None
        self.parent = None


    def setLeftChild(self, left_node):
        self.left_child = left_node
        left_node.setParent(self)

    def setRightChild(self, right_node):
        self.right_child = right_node
        right_node.setParent(self)

    def getLeftChild(self):
        return self.left_child

    def getRightChild(self):
        return self.right_child


    def setParent(self, new_parent):
        self.parent = new_parent

    def printNode(self):
        print(self.payload)

    def __str__(self):
        return self.payload

    def insert_to_bst(self, value):
        if value < self.payload:
            self.left_child.insert_to_bst(value)
        else:
            self.right_child.insert_to_bst(value)


## Declaring our nodes
root = TreeNode('Joe Smith')
jane = TreeNode('Jane')
dan = TreeNode('Dan')
alec = TreeNode('Alec')
madz = TreeNode('Madyson')
zoe = TreeNode('Zoe')


## Build our tree
root.setLeftChild(jane)
root.setRightChild(dan)

jane.setLeftChild(alec)
jane.setRightChild(madz)

dan.setLeftChild(zoe)

## Print out some nodes to test if it looks like it's doing the right thing
# root.printNode()
# root.getLeftChild().printNode()
# root.getRightChild().printNode()


def print_tree(root_node):
    if root_node:
        print(root_node)
        print_tree(root_node.getLeftChild())
        print_tree(root_node.getRightChild())

def print_tree_v2(root_node):
    stack = [root_node]

    while len(stack) > 0:
        cur_node = stack.pop()
        print(cur_node)
        if cur_node.getRightChild():
            stack.append(cur_node.getRightChild())
        if cur_node.getLeftChild():
            stack.append(cur_node.getLeftChild())

def print_tree_v3(root_node):
    queue = [root_node]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node)
        if cur_node.getLeftChild():
            queue.append(cur_node.getLeftChild())
        if cur_node.getRightChild():
            queue.append(cur_node.getRightChild())






print_tree_v3(root)