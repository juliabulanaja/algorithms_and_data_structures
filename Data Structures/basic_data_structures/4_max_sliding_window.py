from collections import deque


def solve_problem(m, numbers): # with suffix and prefix
    n = len(numbers)
    prefixes = []
    suffixes = numbers[:]
    intervals = []

    for i in range(n):
        j = i % m
        if j == 0:
            value = numbers[i]
        else:
            value = max(numbers[i], prefixes[i-1])
        prefixes.append(value)

    for i in range(n):
        j = i % m
        if j == 0:
            value = suffixes[n-i-1]
        else:
            value = max(suffixes[n-i-1], suffixes[n-i])
        suffixes[n-i-1] = value

    i = 0
    while i < (n - m + 1):
        intervals.append(max(prefixes[i+m-1], suffixes[i]))
        i += 1
    return ' '.join(map(str, intervals))



def solve_problem_dequeue(m, numbers): # with own class
    dequeue_window = Dequeue()

    result = []
    start = 0
    end = m - 1

    for i, num in enumerate(numbers):
        
        dequeue_window.enqueue(num, i)

        if i == end:

            result.append(dequeue_window.max.value)
            start += 1
            end += 1
            dequeue_window.dequeue(start)
    return ' '.join(map(str, result))


class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.start = None
        self.end = None
        self.max = None

    
    def enqueue(self, num, index):
        new_item = Item(num, index)

        if self.head == None:
            self.start = index
            self.head = new_item
            self.tail = new_item
            self.max = new_item

        if num >= self.max.value:
            self.head = new_item
            self.tail = new_item
            self.max = new_item

        else:
            prev_item = self.tail
            while prev_item:
                if num <= prev_item.value:
                    break
                else:
                    prev_item = prev_item.prev_item         

            if prev_item == None:
                self.head = new_item
                self.max = new_item
            else:
                prev_item.next_item = new_item
                new_item.prev_item = prev_item
            self.tail = new_item
     
        self.end = index

    def dequeue(self, new_start):
        if new_start > self.head.index:
            self.head = self.head.next_item
            self.start = new_start
            self.max = self.head


class Item:
    def __init__(self, value, index, prev_item=None, next_item=None):
        self.value = value
        self.index = index
        self.prev_item = prev_item
        self.next_item = next_item


class WindowDeque:
    def __init__(self):
        self.deque = deque()

    def push(self, value, index):
        while self.deque and self.deque[-1][0] <= value:
            self.deque.pop()
        self.deque.append((value, index))
      
    def pop(self, index):
        if self.deque[0][1] < index:
            self.deque.popleft()

    def max(self):
        return self.deque[0][0]


def solve_problem_dequeue2(m, numbers): # with deque from collections
    queue = WindowDeque()

    result = []
    start = 0
    end = m - 1

    for index, number in enumerate(numbers):
        
        queue.push(number, index)

        if index == end:
            result.append(queue.max())
            start += 1
            end += 1
            queue.pop(start)
    return ' '.join(map(str, result))


class WindowStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def max(self):
        in_max = self.stack_in[-1][1]
        out_max = self.stack_out[-1][1] if self.stack_out else in_max
        return max(in_max, out_max)

    def push(self, number):
        last_max = self.stack_in[-1][1] if self.stack_in else number
        self.stack_in.append((number, max(number, last_max)))

    def move(self):
        for _ in range(len(self.stack_in)):
            number = self.stack_in[-1][0]
            last_max = self.stack_out[-1][1] if self.stack_out else number
            self.stack_out.append((number, max(number, last_max)))
            self.stack_in.pop()

    def pop(self):
        if not self.stack_out:
            self.move()
        self.stack_out.pop()


def solve_problem_stack(m, numbers): # with 2 stacks    
    window = WindowStack()
    result = []

    for i, number in enumerate(numbers):

        window.push(number)

        if i >= m - 1:

            result.append(window.max())

            # print("out: ", window.stack_out)
            # print("in: ", window.stack_in)
            # print("result ", result)
            # print("_" * 30)


            window.pop()
    return ' '.join(map(str, result))
            







if __name__ == "__main__":
    n = int(input())
    numbers = [int(i) for i in input().split()]
    m = int(input())


    # numbers = [2, 7, 3, 1, 5, 2, 6, 2] # 7 7 5 6 6
    # m = 4

    # result = solve_problem(m, numbers)
    # print(result)

    # result2 = solve_problem_dequeue(m, numbers)
    # print(result2)

    
    # result3 = solve_problem_dequeue2(m, numbers)
    # print(result3)

    result4 = solve_problem_stack(m, numbers)
    print(result4)


