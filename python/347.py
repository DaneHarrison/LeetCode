from collections import Counter
from typing import List
import heapq


def run(list: List[int], k: int) -> List[int]:
    counts = Counter(list)
    topK = heapq.nlargest(k, counts.keys(), key=counts.get)
    
    return topK


# heapq.heapify is a min heap by default
# put numbers in a by negative value to get a max heap
# heapq.nlargest
# heapq.nsmallest(n, list of values to peg as "label", key=how largest is defined)