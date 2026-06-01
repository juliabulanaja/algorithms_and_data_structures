class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail  

class PhoneBook:
    def __init__(self, m):
        self.contacts = [None] * m
        self.mod = m
        self.p = 1_000_000_007
        self.x = 263

    def hash(self, data):
        return sum([ord(c) * self.x**i for i, c in enumerate(data)]) % self.p % self.mod

    def add(self, data):
        hash_data = self.hash(data)
        contact = self.contacts[hash_data]
        
        if contact is None:
            new_node = Node(data)
            self.contacts[hash_data] = DoublyLinkedList(new_node, new_node)
        else:
            
            current_node = contact.head
            while current_node:
                if current_node.data == data:
                    return 
                current_node = current_node.next
            
            new_node = Node(data)
            new_node.next = contact.head
            contact.head.prev = new_node
            contact.head = new_node


    def find(self, data):
        hash_data = self.hash(data)
        contact = self.contacts[hash_data]

        if contact:
            current_node = contact.head
            while current_node:
                if current_node.data == data:
                    print('yes')
                    return
                current_node = current_node.next
        print('no')

    def delete(self, data):
        hash_data = self.hash(data)
        contact = self.contacts[hash_data]

        if not contact:
            return

        current_node = contact.head
        while current_node:

            if current_node.data == data:

                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    contact.head = current_node.next


                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    contact.tail = current_node.prev
     

                if contact.head is None:
                    self.contacts[hash_data] = None
                return

            current_node = current_node.next
                
    def check(self, i):
        index = int(i)

        contact = self.contacts[index]
        if index >= len(self.contacts) or self.contacts[index] is None:
            print('')
            return

        output = ''
        current_node = contact.head
        while current_node:
            output += ' ' + current_node.data
            current_node = current_node.next
        print(output.strip())

    # def print(self):
        
    #     for i in range(m):
            
    #         output = ''
    #         contact = self.contacts[i]
    #         if contact == 0:
    #             print(0)
    #             continue

    #         current_node = contact.head
    #         while current_node:
    #             output += ' ' + current_node.data
    #             current_node = current_node.next

    #         print(output.strip())
    #     print("__________________________")



if __name__ == "__main__":
    m = int(input()) # the number of buckets
    n = int(input()) # the number of queries 𝑁

    queries = []
    for _ in range(n):
        queries.append(input())
    # print(queries)
    # m = 3
    # queries = ['check 0', 'find help', 'add help', 'add del', 'add add', 'find add', 'find del', 'del del', 'find del', 'check 0', 'check 1', 'check 2']

    phone_book = PhoneBook(m)
    
    for q in queries:
        action, *args = q.split(' ')
        # print(q)  
        if action == 'add':
            phone_book.add(*args)  
        elif action == 'check':
            phone_book.check(*args) 
        elif action == 'del':
            phone_book.delete(*args) 
        elif action == 'find':
            phone_book.find(*args) 

        # phone_book.print()
