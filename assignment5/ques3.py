class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    start = None

    def add_at_end(self, data):
        node = Node(data)
        if self.start == None:
            self.start = node
            self.end = node

        else:
            self.end.next = node
            self.end = node

    def display(self):
        tmp = self.start
        while tmp != None:
            print(tmp.data)
            tmp = tmp.next

    def adding_between_twoNumber(self,num1,num2, value):
        node = Node(value)
        tmp = self.start
        while tmp != None:
            if tmp.data == num1 and tmp.next.data == num2:
                tmp1 = tmp.next
                tmp.next = node
                node.next = tmp1
                break
            tmp = tmp.next    

    def delete_element(self, num):
        tmp = self.start
        if tmp.data == num:
            self.start = tmp.next
        while tmp != None:
            if tmp.next.data == num:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next

    def search_element(self, value):
        tmp = self.start
        flag = 0
        while tmp != None:
            if tmp.data == value:
                print("value found")
                flag = 1
                break
            tmp = tmp.next
        if flag == 0:
            print("value not found")
            
    def reverse_linkList(self):
        prev = None
        current = self.start
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.start = prev
                

linked_list = Linked_list()
linked_list.add_at_end(3)
linked_list.add_at_end(4)
linked_list.add_at_end(5)
linked_list.add_at_end(6)
linked_list.add_at_end(7)
linked_list.display()
linked_list.adding_between_twoNumber(4, 5, 8)
linked_list.display()
linked_list.delete_element(5)
linked_list.display()
linked_list.search_element(7)
linked_list.display()
linked_list.reverse_linkList()
linked_list.display()
