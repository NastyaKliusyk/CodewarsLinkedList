class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes")
    
    first_head = None
    second_head = None
    first_tail = None
    second_tail = None

    current = head
    count = 1
    
    while current:
        if count % 2 != 0:
            if not first_head:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = first_tail.next
        else:
            if not second_head:
                second_head = current
                second_tail = current
            else:
                second_tail.next = current
                second_tail = second_tail.next

        current = current.next
        count += 1

    if first_tail:
        first_tail.next = None
    if second_tail:
        second_tail.next = None

    return Context(first_head, second_head)
