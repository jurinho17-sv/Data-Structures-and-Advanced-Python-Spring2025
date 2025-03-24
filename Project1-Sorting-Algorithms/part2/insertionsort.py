"""
Implementation of Insertion Sort algorithm.

This module provides functions to perform the Insertion Sort algorithm on lists of comparable elements.
"""

def insertionsort(arr, stats=None):
    """
    Sort an array using the Insertion Sort algorithm.
    
    Args:
        arr: The array to be sorted
        stats: Dictionary to track performance statistics (optional)
        
    Returns:
        None (the array is sorted in-place)
    """
    if stats is None:
        stats = {'comparisons': 0, 'swaps': 0}
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0:
            stats['comparisons'] += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                stats['swaps'] += 1
                j -= 1
            else:
                break
                
        # If we moved any elements, place key in the correct position
        if j + 1 != i:
            arr[j + 1] = key
            stats['swaps'] += 1
    
    return stats


def insertionsort_with_binary_search(arr, stats=None):
    """
    Sort an array using the Insertion Sort algorithm with binary search optimization.
    This variant uses binary search to find the position where the element should be inserted,
    which can reduce the number of comparisons.
    
    Args:
        arr: The array to be sorted
        stats: Dictionary to track performance statistics (optional)
        
    Returns:
        None (the array is sorted in-place)
    """
    if stats is None:
        stats = {'comparisons': 0, 'swaps': 0}
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Find the position where key should be inserted using binary search
        position = binary_search(arr, key, 0, i - 1, stats)
        
        # If position is the same as i, no need to move elements
        if position < i:
            # Shift all elements after position to right
            for j in range(i - 1, position - 1, -1):
                arr[j + 1] = arr[j]
                stats['swaps'] += 1
                
            # Insert key at the correct position
            arr[position] = key
            stats['swaps'] += 1
    
    return stats


def binary_search(arr, key, low, high, stats):
    """
    Use binary search to find the position where key should be inserted.
    
    Args:
        arr: The array to search within
        key: The value to find the insertion position for
        low: The lower bound of the search range
        high: The upper bound of the search range
        stats: Dictionary to track performance statistics
        
    Returns:
        The position where key should be inserted
    """
    while low <= high:
        mid = (low + high) // 2
        stats['comparisons'] += 1
        
        if key == arr[mid]:
            return mid + 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


if __name__ == "__main__":
    # Example usage of regular insertion sort
    test_array1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array1}")
    
    stats1 = insertionsort(test_array1.copy())
    print(f"Sorted array (regular insertion sort): {test_array1}")
    print(f"Performance stats (regular): {stats1}")
    
    # Example usage of insertion sort with binary search
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {test_array2}")
    
    stats2 = insertionsort_with_binary_search(test_array2.copy())
    print(f"Sorted array (insertion sort with binary search): {test_array2}")
    print(f"Performance stats (with binary search): {stats2}")
    
    # Test with a larger random array
    import random
    large_array = random.sample(range(1, 1001), 100)  # 100 random numbers
    
    # Regular insertion sort
    large_array_copy1 = large_array.copy()
    print(f"\nSorting an array of {len(large_array)} random elements with regular insertion sort...")
    stats_reg = insertionsort(large_array_copy1)
    print(f"Performance stats: {stats_reg}")
    
    # Insertion sort with binary search
    large_array_copy2 = large_array.copy()
    print(f"\nSorting with binary search optimization...")
    stats_bin = insertionsort_with_binary_search(large_array_copy2)
    print(f"Performance stats: {stats_bin}")
    print(f"Comparison reduction: {stats_reg['comparisons'] - stats_bin['comparisons']} comparisons")