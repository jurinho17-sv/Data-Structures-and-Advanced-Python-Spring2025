"""
Implementation of Quick Sort algorithm.

This module provides functions to perform the Quick Sort algorithm on lists of comparable elements.
"""

def quicksort(arr, low=None, high=None):
    """
    Sort an array using the Quick Sort algorithm.
    
    Args:
        arr: The array to be sorted
        low: Starting index (default: 0)
        high: Ending index (default: len(arr)-1)
        
    Returns:
        None (the array is sorted in-place)
    """
    # Initialize low and high if not provided
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get the pivot position
        pivot_position = partition(arr, low, high)
        
        # Sort the sub-arrays independently
        quicksort(arr, low, pivot_position - 1)
        quicksort(arr, pivot_position + 1, high)


def partition(arr, low, high):
    """
    Partition the array and return the position of the pivot.
    
    Args:
        arr: The array to be partitioned
        low: Starting index
        high: Ending index
        
    Returns:
        The position of the pivot element
    """
    # Select the rightmost element as pivot
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Example usage
    test_array = [10, 7, 8, 9, 1, 5]
    print(f"Original array: {test_array}")
    
    quicksort(test_array)
    print(f"Sorted array: {test_array}")
