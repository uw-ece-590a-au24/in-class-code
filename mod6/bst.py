
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
        if self.left_child:
            left_node.setParent(self)

    def setRightChild(self, right_node):
        self.right_child = right_node
        if self.right_child:
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
        return str(self.payload)

    def insert_to_bst(self, value):
        if value < self.payload:
            if self.left_child:
                return self.left_child.insert_to_bst(value)
            else:
                self.left_child = TreeNode(value)
                self.left_child.setParent(self)
                return self.left_child
        else:
            if self.right_child:
                return self.right_child.insert_to_bst(value)
            else:
                self.right_child = TreeNode(value)
                self.right_child.setParent(self)
                return self.right_child

    def remove_from_bst(self):
        if not self.left_child and not self.right_child:
            ## No children
            if self.parent.payload < self.payload:
                self.parent.setRightChild(None)
            else:
                self.parent.setLeftChild(None)
            return
        if not (self.left_child and self.right_child):
            print('Removing node with one child')
            new_child = self.left_child if self.left_child else self.right_child
            if self.parent.payload < self.payload:
                ## This node is the right child
                self.parent.setRightChild(new_child)
            else:
                self.parent.setLeftChild(new_child)
            return
        ## If we have 2 children
        replacement = self.right_child.find_smallest_child()
        self.payload = replacement.payload
        if not replacement.left_child and not replacement.right_child:
            ## NO children; remove successor from parent
            replacement.remove_from_bst()
        if replacement.right_child:
            replacement.payload = replacement.right_child.payload
            replacement.right_child = None



    # ## Assume
    # def choose_successor(self):
    #     if self.right_child:
    #         ### Find the smallest of the right child
    #         ## This is our "in-order successor"
    #         return self.right_child.find_smallest_child()
    #         pass
    #     else:
    #         ## Find the largest of the left child
    #
    #         pass

    def find_smallest_child(self):
        ## Return node that holds smallest child of this node
        if self.left_child:
            return find_smallest_child(self.left)
        return self

def print_tree(root_node, level = 0):
    for i in range(level):
        print('-', end='')
    if root_node:
        print(root_node)
        print_tree(root_node.getLeftChild(), level + 1)
        print_tree(root_node.getRightChild(), level + 1)
    else:
        print('X')

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



bst = TreeNode(24)
has_two_children = bst.insert_to_bst(15)
bst.insert_to_bst(5)
bst.insert_to_bst(7)

one_child_node = bst.insert_to_bst(42)
bst.insert_to_bst(18)
bst.insert_to_bst(1)
bst.insert_to_bst(37)

last_leaf = bst.insert_to_bst(52)

print_tree(bst)

print("\n\n\n=========")

has_two_children.remove_from_bst()

# last_leaf.remove_from_bst()
#
# one_child_node.remove_from_bst()





print_tree(bst)