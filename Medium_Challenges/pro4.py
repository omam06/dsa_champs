def reverse_first(queue, k):
    if k < 0 or k > len(queue):
        return queue
    
    stack = []
    for i in range(k):
        firstitem = queue.pop(0)
        stack.append(firstitem)
    while stack != []:
        from_stack = stack.pop()
        queue.append(from_stack)
    
    for i in range(len(queue) - k):
        from_queue_again = queue.pop(0)
        queue.append(from_queue_again)
    return queue

print(reverse_first([10, 20, 30, 40, 50], 3))