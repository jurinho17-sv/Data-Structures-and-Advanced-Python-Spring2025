"""
Implementation of Heap Sort algorithm.

This module provides functions to perform the Heap Sort algorithm on lists of comparable elements.
"""

def heapsort(arr):
    """
    Sort an array using the Heap Sort algorithm.
    
    Args:
        arr: The array to be sorted
        
    Returns:
        None (the array is sorted in-place)
    """
    n = len(arr)
    
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call heapify on the reduced heap
        heapify(arr, i, 0)


def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr: The array representing the heap
        n: Size of the heap
        i: Index of the root of the subtree to heapify
        
    Returns:
        None (the heap is modified in-place)
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Heapify the affected sub-tree
        heapify(arr, n, largest)


if __name__ == "__main__":
    # Example usage
    test_array = [12, 11, 13, 5, 6, 7]
    print(f"Original array: {test_array}")
    
    heapsort(test_array)
    print(f"Sorted array: {test_array}")
