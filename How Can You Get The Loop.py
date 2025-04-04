class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    if not node or not node.next:
        return 0

    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_length = 1
            current = slow.next
            while current != slow:
                loop_length += 1
                current = current.next
            return loop_length
    
    return 0
