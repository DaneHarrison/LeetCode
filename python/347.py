from typing import List
import heapq


def run(list: List[int], k: int) -> List[int]:
    max_heap = [-n for n in list]
    largest = []
    
    heapq.heapify(max_heap)
    
    for _ in range(k):
        largest.append(heapq.heappop(max_heap))
   
    return largest


# heapq.heapify is a min heap by default
# put numbers in a by negative value to get a max heap