hashtable = [None] * 5
num_items_in_hashtable = 0

def oa_hash(key):
    return key % len(hashtable)

def resize():
    pass

def put(key):
    global num_items_in_hashtable
    if num_items_in_hashtable >= len(hashtable):
        print("Hashtable is full. ")
        return
    which_bucket = oa_hash(key)
    offset = 0
    while hashtable[(which_bucket + offset) % len(hashtable)]:
        offset += 1

    hashtable[(which_bucket + offset) % len(hashtable)] = key
    num_items_in_hashtable += 1
    return


def get(key):
    which_bucket = oa_hash(key)
    offset = 0
    while hashtable[(which_bucket + offset) % len(hashtable)] != key:
        offset += 1
        if offset >= len(hashtable):
            return False
    return True


put(1)
put(2)

print(hashtable)
put(11)
put(21)
put(31)
print(hashtable)


print(get(31))