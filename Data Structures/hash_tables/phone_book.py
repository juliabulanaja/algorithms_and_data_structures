class PhoneBook:
    def __init__(self):
        self.contacts = [0] * 10 ** 7

    def hash(self, phone):
        return int(phone) % 10 ** 8

    def add(self, phone, name):
        hash_number = self.hash(phone)
        self.contacts[hash_number] = name

    def find(self, phone):
        hash_number = self.hash(phone)
        if self.contacts[hash_number] != 0:
            print(self.contacts[hash_number])
        else:
            print('not found') 

    def remove(self, phone):
        hash_number = self.hash(phone)
        self.contacts[hash_number] = 0

    


if __name__ == "__main__":
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(input())

    # commands = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911', 'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']

    phone_book = PhoneBook()


    for command in commands:
        action, *args = command.split(' ')

        if action == 'add':
            phone_book.add(*args)   
        elif action == 'find':
            phone_book.find(*args) 
        elif action == 'del':
            phone_book.remove(*args) 
        


