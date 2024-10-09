

def create_queue():
    return []

def enqueue(queue, new_item):
    queue.append(new_item)

def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

customers = create_queue()
print(customers)

enqueue(customers, 'Ben Bitdiddle')
enqueue(customers, 'Joe Smith')
enqueue(customers, 'Alyssa Abernathy')
print(customers)

next_customer = dequeue(customers)
print('The next customer is : ' + next_customer)

next_customer = dequeue(customers)
next_customer = dequeue(customers)
next_customer = dequeue(customers)

if next_customer:
    print('The next customer is : ' + next_customer)
else:
    print('There are no more customers')


print(customers)
