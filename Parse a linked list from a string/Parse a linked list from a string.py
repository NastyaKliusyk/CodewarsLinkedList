class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None":
        return None

    elements = s.split(" -> ")
    elements.pop()

    head = Node(int(elements[0]))
    current = head

    for value in elements[1:]:
        current.next = Node(int(value))
        current = current.next
    
    return head

