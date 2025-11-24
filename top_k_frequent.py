import collections
import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements in an array.
    Uses Hash Map for O(N) counting and a Min-Heap for O(N log K) efficiency.
    """

    freq_map = collections.Counter(nums)
    
    min_heap = []
    
    for num, count in freq_map.items():
        
        heapq.heappush(min_heap, (count, num))
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = [item[1] for item in min_heap]
    
    return result

print(f"Test Case 1: {topKFrequent([1,1,1,2,2,3], 2)}") # النتيجة المتوقعة: [1, 2]
print(f"Test Case 2: {topKFrequent([4,1,-1,2,-1,2,3], 2)}") # النتيجة المتوقعة: [-1, 2]