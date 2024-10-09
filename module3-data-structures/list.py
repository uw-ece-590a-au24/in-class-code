
def create_linked_list():
    return {
        'head': None,
        'size': 0
    }

def create_node(data):
    return {
        'data': data,
        'next': None
    }

def get_data_from_node(node):
    return node['data']

def get_next_from_node(node):
    return node['next']

def add_item(list, item):
    new_node = create_node(item)
    new_node['next'] = list['head']
    list['head'] = new_node
    list['size'] += 1

def remove_item(list, value):
    next_node = list['head']
    prev_node = None
    while next_node:
        if get_data_from_node(next_node) == value:
            # print("Delete this node!! " + get_data_from_node(next_node))
            # print("The previous node was " + get_data_from_node(prev_node))
            if prev_node:
                prev_node['next'] = next_node['next']
            else:
                list['head'] = next_node['next']
            list['size'] -= 1
        prev_node = next_node
        next_node = get_next_from_node(next_node)

def print_list(list):
    print('Printing list: {} elems', list['size'])
    next_node = list['head']
    while next_node:
        print(get_data_from_node(next_node))
        next_node = get_next_from_node(next_node)

my_ll = create_linked_list()
print(my_ll)

add_item(my_ll, 'ace of spades')
add_item(my_ll, 'king of hearts')
add_item(my_ll, 'queen of clubs')
add_item(my_ll, 'two of spades')
print_list(my_ll)

remove_item(my_ll, 'two of spades')
print("\n\n\n")
print_list(my_ll)