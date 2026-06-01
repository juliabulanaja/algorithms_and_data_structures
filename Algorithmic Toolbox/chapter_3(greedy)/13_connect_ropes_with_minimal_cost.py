import heapq


def connect_ropes(ropes: list): # O(nlogn)

    heapq.heapify(ropes) # O(n)
    total_cost = 0
    
    while len(ropes) > 1: # O(n)
        first = heapq.heappop(ropes) # O(logn)
        second = heapq.heappop(ropes) # O(logn)

        connection_cost = first + second
        total_cost += connection_cost

        heapq.heappush(ropes, connection_cost) # O(logn)

        
    return total_cost


ropes = [1, 3, 5, 11]
ropes = [2, 3, 4, 6]
ropes = [10, 4, 7]
ropes = [1, 2, 2, 2, 3, 4]
ropes = [4, 3, 2, 6] # 29
ropes = [4, 2, 7, 6, 9]


result = connect_ropes(ropes)
print(result)