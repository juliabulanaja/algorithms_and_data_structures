import heapq


def merge_tables(n, rows, queries):
    pointers = [i for i in range(n)]
    current_max = max(rows)

    for d, s in queries:
        d -= 1
        s -= 1

        destination = pointers[d] 
        source = s 

        while pointers[s] != s:
            s = pointers[s]
        
        node = s

        while pointers[source] != source:   
            next_source = pointers[source]
            pointers[source] = node
            source = next_source


        while pointers[d] != d:
            d = pointers[d]

        if s != d:
            pointers[s] = destination
            rows[d] += rows[s]
            current_max = max(current_max, rows[d])
        print(current_max)


if __name__ == "__main__":
    n, m = [int(i) for i in input().split(' ')] # n - the number of tables and m - the number of merge queries
    rows = [int(i) for i in input().split(' ')] 
    queries = []

    for _ in range(m):
        destination, source = [int(i) for i in input().split(' ')]
        queries.append((destination, source))


    # n, m = 5, 5
    # rows = [1, 1, 1, 1, 1]
    # queries = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]
    merge_tables(n, rows, queries)
