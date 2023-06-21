class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createNewLinkedList(list1, list2):
    newList = None
    tail = None

    while list1 is not None and list2 is not None:
        if list1.data >= list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next

        if newList is None:
            newList = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    while list1 is not None:
        new_node = Node(list1.data)
        list1 = list1.next

        tail.next = new_node
        tail = tail.next

    while list2 is not None:
        new_node = Node(list2.data)
        list2 = list2.next

        tail.next = new_node
        tail = tail.next

    return newList






