"""
Implementation of Quick Sort algorithm.

This module provides functions to perform the Quick Sort algorithm on lists of comparable elements.
"""

def quicksort(arr, low=None, high=None, stats=None):
    """
    Sort an array using the Quick Sort algorithm.
    
    Args:
        arr: The array to be sorted
        low: Starting index (default: 0)
        high: Ending index (default: len(arr)-1)
        stats: Dictionary to track performance statistics (optional)
        
    Returns:
        None (the array is sorted in-place)
    """
    # Initialize stats dictionary if not provided
    if stats is None:
        stats = {'comparisons': 0, 'swaps': 0}
    
    # Initialize low and high if not provided
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get the pivot position
        pivot_position = partition(arr, low, high, stats)
        
        # Sort the sub-arrays independently
        quicksort(arr, low, pivot_position - 1, stats)
        quicksort(arr, pivot_position + 1, high, stats)
    
    return stats


def partition(arr, low, high, stats):
    """
    Partition the array and return the position of the pivot.
    
    Args:
        arr: The array to be partitioned
        low: Starting index
        high: Ending index
        stats: Dictionary to track performance statistics
        
    Returns:
        The position of the pivot element
    """
    # Select the rightmost element as pivot
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        stats['comparisons'] += 1  # Count comparison
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats['swaps'] += 1  # Count swap
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    stats['swaps'] += 1  # Count swap
    return i + 1


if __name__ == "__main__":
    # Example usage
    test_array = [10, 7, 8, 9, 1, 5]
    print(f"Original array: {test_array}")
    
    stats = quicksort(test_array)
    print(f"Sorted array: {test_array}")
    print(f"Performance stats: {stats}")
    
    # Test with a larger random array
    import random
    large_array = random.sample(range(1, 1001), 100)  # 100 random numbers
    print(f"\nSorting an array of {len(large_array)} random elements...")
    stats = quicksort(large_array.copy())
    print(f"Performance stats: {stats}")