
def create_linked_list():
    return {
        'head': None,
        'size': 0,
        'tail': None
    }

def get_llist_head(linked_list):
    return linked_list['head']

def set_llist_head(linked_list, new_head):
    linked_list['head'] = new_head

def get_llist_size(linked_list):
    return linked_list['size']

def set_llist_size(linked_list, new_size):
    linked_list['size'] = new_size

def get_llist_tail(linked_list):
    return linked_list['tail']

def set_llist_tail(linked_list, new_tail):
    linked_list['tail'] = new_tail

def create_node(data):
    return {
        'data': data,
        'next': None,
        'prev': None
    }

def get_data_from_node(node):
    return node['data']

def get_next_from_node(node):
    return node['next']

def get_prev_from_node(node):
    return node['prev']

## Adds item at the head of the list
def add_item(list, item):
    new_node = create_node(item)
    new_node['next'] = list['head']
    if list['size'] > 0:
        list['head']['prev'] = new_node
    list['head'] = new_node
    list['size'] += 1

## Adds item at the end of the list
def add_item_at_end(list, item):
    new_node = create_node(item)

    if get_llist_size(list) == 0:
        set_llist_head(list, new_node)
        set_llist_tail(list, new_node)
        set_llist_size(list, 1)
        return

    ## Tell the last node to point to the new node
    if get_llist_tail(list):
        get_llist_tail(list)['next'] = new_node

    ## Tell the new node to point to the last node
    new_node['prev'] = get_llist_tail(list)

    ## Tell the list that the new node is now the last node
    set_llist_tail(list, new_node)

    set_llist_size(list, get_llist_size(list) + 1)


def remove_item(list, value):
    next_node = get_llist_head(list)
    while next_node:
        if get_data_from_node(next_node) == value:
            if next_node['prev']:
                next_node['prev']['next'] = next_node['next']
            else:
                ## The node we are removing is at the head of the list
                # list['head'] = next_node['next']
                set_llist_head(list, get_next_from_node(next_node))
            if not next_node['next']:
                ## The node we are removing is at the tail of the list
                set_llist_tail(list, next_node['prev'])
            list['size'] -= 1
        next_node = get_next_from_node(next_node)

def print_list(list):
    print('Printing list: {} elems'.format(list['size']))
    next_node = list['head']
    while next_node:
        print(get_data_from_node(next_node))
        next_node = get_next_from_node(next_node)

my_ll = create_linked_list()
print(my_ll)

add_item_at_end(my_ll, 'ace of spades')
add_item_at_end(my_ll, 'king of hearts')
add_item_at_end(my_ll, 'queen of clubs')
add_item_at_end(my_ll, 'two of spades')
print_list(my_ll)

remove_item(my_ll, 'ace of spades')
print("\n\n\n")
print_list(my_ll)

add_item_at_end(my_ll, 'seven of clubs')
print("\n\n\n")
print_list(my_ll)


#
# remove_item(my_ll, 'two of spades')
# print("\n\n\n")
# print_list(my_ll)
#
# add_item_at_end(my_ll, 'seven of clubs')
# print("\n\n\n")
# print_list(my_ll)