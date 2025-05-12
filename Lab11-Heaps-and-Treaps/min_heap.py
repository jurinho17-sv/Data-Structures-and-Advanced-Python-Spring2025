# min_heap.py

"""
CS 034 - Data Structures and Advanced Python
Lab 11: Heaps and Treaps
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 11th, 2025

GitHub repo:
"""

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # Using heapq to insert item into the heap
        # heapq maintains min-heap property automatically
        heapq.heappush(self.heap, item)

    def remove_min(self):
        # Using heapq to remove and return the smallest item
        # Returns None if heap is empty
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def peek_min(self):
        # Return the smallest item without removing it
        # Returns None if heap is empty
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        # Helper method to get the size of the heap
        return len(self.heap)

    def is_empty(self):
        # Helper method to check if heap is empty
        return len(self.heap) == 0