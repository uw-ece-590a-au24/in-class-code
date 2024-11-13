
my_hashtable = [None] * 5
num_items_in_table = 0

def hash(hashtable, key: int):
    return key % len(hashtable)


def resize(old_hashtable):
    print("Resizing")
    new_hashtable = [None] * (len(old_hashtable) * 2)
    num_items_in_table = 0
    for bucket in old_hashtable:
        if bucket:
            for item in bucket:
                put(new_hashtable, item[0], item[1])

    return new_hashtable


def put(hashtable, key, value):
    global num_items_in_table
    print(f'Inserting {key} ')
    load_factor = num_items_in_table / len(hashtable)
    if load_factor > .75:
        hashtable = resize(hashtable)
        print('New Resized Hashtable: ')
        print(hashtable)
        print(f'Now inserting {key} into new hashtable')
    index = hash(hashtable, key)
    if not hashtable[index]:
        hashtable[index] = []
    hashtable[hash(hashtable, key)].append((key, value))
    num_items_in_table += 1
    # print('New Resized Hashtable After the next insert: ')
    # print(hashtable, end='\n\n\n')
    return hashtable

def get(hashtable, key):
    data_list = hashtable[hash(hashtable, key)]
    for item in data_list:
        if item[0] == key:
            return item
    return None


print(my_hashtable)
my_hashtable = put(my_hashtable, 3, 3)
my_hashtable = put(my_hashtable, 4, 4)
my_hashtable = put(my_hashtable, 15, 15)
my_hashtable = put(my_hashtable, 42, 42)
my_hashtable = put(my_hashtable, 20, 20)


print(my_hashtable)

print(get(my_hashtable, 20))