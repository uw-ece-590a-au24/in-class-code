

class Heap():
    def __init__(self):
        self.data = []

    def insert(self, value):
        ## Put the new value at the end/last leaf of the tree
        self.data.append(value)
        new_value_index = len(self.data) - 1

        ## Bubble it up until it's in the right place
        ## Compare the node to it's parent, if the parent is smaller, swap
        parent_index = int((new_value_index - 1) / 2)

        if self.data[parent_index] < self.data[new_value_index]:
            ## swap
            val = self.data[parent_index]
            self.data[parent_index] = self.data[new_value_index]
            self.data[new_value_index] = val

        pass



    def get_min(self):
        pass

def print_tree(heap, cur_node= 0, level = 0):

    if (cur_node >= len(heap)):
        return
    for i in range(level):
        print('-', end='')
    print(heap[cur_node])
    left_child = (cur_node * 2) + 1
    right_child = left_child + 1
    print_tree(heap, left_child, level + 1)
    print_tree(heap, right_child, level + 1)

heap = Heap()
heap.insert(25)
heap.insert(3)
heap.insert(9)

print_tree(heap.data)