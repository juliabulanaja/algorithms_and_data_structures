import heapq

def schedule(jobs: list, m: int):
    threads = [(0, i) for i in range(m)]
    heapq.heapify(threads)

    for j in jobs:
        th_time, th_id = heapq.heappop(threads)
        print(f"{th_id} {th_time}")
        th_time += j
        heapq.heappush(threads, (th_time, th_id))
        

if __name__ == "__main__":
    m, n = [int(i) for i in input().split(' ')] # n - threads, m - jobs
    jobs = [int(i) for i in input().split(' ')]

    # m = 2
    # jobs = [1, 2, 3, 4, 5]
    schedule(jobs, m)

