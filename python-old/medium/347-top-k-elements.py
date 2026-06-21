from collections import Counter
import heapq

def topKFrequent(self, nums, k):
    counts = Counter(nums)
    topK = heapq.nlargest(k, counts.keys(), key=counts.get)

    return topK