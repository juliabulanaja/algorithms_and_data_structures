import random
import heapq
from time import perf_counter


deadline_max = 40
n = 10 ** 1
jobs = [(random.randint(15, 100), random.randint(1, deadline_max)) for _ in range(n)]
jobs = [(50, 2), (30, 2), (15, 3), (20, 1), (25, 1)]
# print(jobs)



def schedule_jobs(jobs: list[tuple]) -> list[tuple]:

    jobs = sorted(jobs, key=lambda x: (x[1], -x[0])) # nlog(n)
    print(jobs)

    result = []
    slot = 0

    for profit, deadline in jobs: # O(n)

        if slot == deadline:
            index, (min_profit_in_result, _) = min(enumerate(result), key=lambda x: x[1][0]) # O(n)

            if profit > min_profit_in_result:
                result[index] = (profit, deadline)
    
        if slot < deadline:
            result.append((profit, deadline))
            slot += 1

    return sum(i[0] for i in result)


def schedule_jobs_heap(jobs: list[tuple]) -> list[tuple]:

    jobs = sorted(jobs, key=lambda x: (x[1], -x[0])) # nlog(n)

    result = []
    slot = 0

    for profit, deadline in jobs: # O(n)

        if slot == deadline:
            min_value = result[0]

            if profit > min_value[0]:
                heapq.heapreplace(result, (profit, deadline))

    
        if slot < deadline:
            heapq.heappush(result, (profit, deadline))
            slot += 1

    return sum(i[0] for i in result)

if __name__ == "__main__":

    start = perf_counter()
    result1 = schedule_jobs(jobs)
    print(f"time execution is {perf_counter() - start}")

    start = perf_counter()
    result2 = schedule_jobs_heap(jobs)
    print(f"time execution is {perf_counter() - start}")

    print(result1 == result2)