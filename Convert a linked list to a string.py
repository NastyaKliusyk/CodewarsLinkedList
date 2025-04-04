class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    result = ""
    while node is not None:
        result += str(node.data) + " -> "
        node = node.next
    result += "None"
    return result
