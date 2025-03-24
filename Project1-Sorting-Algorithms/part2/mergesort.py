"""
Implementation of Merge Sort algorithm.

This module provides functions to perform the Merge Sort algorithm on lists of comparable elements.
"""

def mergesort(arr, stats=None):
    """
    Sort an array using the Merge Sort algorithm.
    
    Args:
        arr: The array to be sorted
        stats: Dictionary to track performance statistics (optional)
        
    Returns:
        The sorted array
    """
    # Initialize stats dictionary if not provided
    if stats is None:
        stats = {'comparisons': 0, 'swaps': 0}
    
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = mergesort(left_half, stats)
    right_half = mergesort(right_half, stats)
    
    # Merge the sorted halves
    return merge(left_half, right_half, stats)


def merge(left, right, stats):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
        stats: Dictionary to track performance statistics
        
    Returns:
        A merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller to the result
    while i < len(left) and j < len(right):
        stats['comparisons'] += 1  # Count comparison
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        stats['swaps'] += 1  # Count move operation
    
    # Add any remaining elements (only one of these loops will execute)
    while i < len(left):
        result.append(left[i])
        i += 1
        stats['swaps'] += 1  # Count move operation
    
    while j < len(right):
        result.append(right[j])
        j += 1
        stats['swaps'] += 1  # Count move operation
    
    return result


if __name__ == "__main__":
    # Example usage
    test_array = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {test_array}")
    
    stats = {'comparisons': 0, 'swaps': 0}
    sorted_array = mergesort(test_array, stats)
    print(f"Sorted array: {sorted_array}")
    print(f"Performance stats: {stats}")
    
    # Test with a larger random array
    import random
    large_array = random.sample(range(1, 1001), 100)  # 100 random numbers
    stats = {'comparisons': 0, 'swaps': 0}
    print(f"\nSorting an array of {len(large_array)} random elements...")
    sorted_large = mergesort(large_array, stats)
    print(f"Performance stats: {stats}")