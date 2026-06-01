from collections import deque


class MaxStack:
    def __init__(self):
        self.stack = deque()

    def push(self, number):
        last_max = self.stack[-1][1] if self.stack else number
        self.stack.append((number, max(number, last_max)))
    
    def pop(self):
        if self.stack:
            self.stack.pop()

    def get_max(self):
        if not self.stack:
            return None
        return self.stack[-1][1]    

    


def solve_problem(commands: list[str]):
    q = MaxStack()

    for c in commands:
        if c.startswith('push'):
            _, number = c.split(' ')
            q.push(int(number))
        elif c.startswith('pop'):
            q.pop()
        elif c.startswith('max'):
            print(q.get_max())




if __name__ == "__main__":
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(input())


    # commands = ['push 2', 'push 1', 'max', 'pop', 'max']
    solve_problem(commands)