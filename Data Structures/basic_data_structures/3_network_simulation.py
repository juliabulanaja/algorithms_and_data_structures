from collections import deque


def solve_problem(packets: list, S: int):
    stack = deque()
    current_time = 0

    for p in packets:
        start_time = p[0]
        end_time = p[1]

        if len(stack) == S:
            if stack[0] <= start_time:
                stack.popleft()
            else:
                print(-1)
                continue

        current_time = max(current_time, start_time)
        print(current_time)
        current_time += end_time
        stack.append(current_time)



if __name__ == "__main__":

    S, n = [int(i) for i in input().strip().split(' ')]
    packets = []
    for i in range(n):
        packet = tuple(int(i) for i in input().strip().split(' '))
        packets.append(packet)



    # S = 1
    # n = 2
    # packets = [(0, 1), (1, 1)]

    solve_problem(packets, S)

