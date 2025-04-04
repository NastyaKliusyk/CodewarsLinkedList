class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def parse(s):
    if s.lower() == "null":
        return None

    nodes = s.split(" -> ")

    head = None
    current = None
    
    for value in nodes:

        if value.lower() == "none":
            break

        new_node = Node(int(value))
        if head is None:
            head = new_node
        else:
            current.next = new_node
        current = new_node
    
    return head
