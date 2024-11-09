from unittest.mock import right


## Min Heap: The lowest value is most important
class Heap():
    def __init__(self):
        self.data = []

    def insert(self, value):
        ## Put the new value at the end/last leaf of the tree
        self.data.append(value)
        new_value_index = len(self.data) - 1

        ## If it's the first thing, just return
        if new_value_index == 0:
            return

        ## Bubble it up until it's in the right place
        ## Compare the node to it's parent, if the parent is smaller, swap
        parent_index = int((new_value_index - 1) / 2)

        while (self.data[parent_index] > self.data[new_value_index] and
               new_value_index > 0):
            ## swap
            val = self.data[parent_index]
            self.data[parent_index] = self.data[new_value_index]
            self.data[new_value_index] = val

            new_value_index = parent_index
            parent_index = int((new_value_index - 1) / 2)

    def get_min(self):
        result = self.data.pop(0)

        ###
        # result = self.data[0]
        # self.data[0] = self.data.pop()
        ###

        last_value = self.data.pop()
        self.data.insert(0, last_value)

        root_index = 0
        left_child_index = 1
        right_child_index = 2

        smallest_child_index = left_child_index if self.data[left_child_index] < self.data[right_child_index] else right_child_index

        while self.data[root_index] > self.data[smallest_child_index]:
            print(f'Swapping {self.data[root_index]} with child {self.data[smallest_child_index]}')
            val = self.data[root_index]
            self.data[root_index] = self.data[smallest_child_index]
            self.data[smallest_child_index] = val

            root_index = smallest_child_index
            left_child_index = root_index * 2 + 1
            right_child_index = left_child_index + 1

            if left_child_index > len(self.data) - 1:
                return result
            if right_child_index > len(self.data) - 1:
                smallest_child_index = left_child_index
            else:
                smallest_child_index = left_child_index if self.data[left_child_index] < self.data[right_child_index] else right_child_index

        return result





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
heap.data = [3, 5, 9, 11, 17,15, 10, 16, 19, 25]

highest_priority = heap.get_min()

print(highest_priority)

print(heap.data)
print_tree(heap.data)