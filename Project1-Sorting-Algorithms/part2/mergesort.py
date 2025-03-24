"""
Implementation of Merge Sort algorithm.

This module provides functions to perform the Merge Sort algorithm on lists of comparable elements.
"""

def mergesort(arr):
    """
    Sort an array using the Merge Sort algorithm.
    
    Args:
        arr: The array to be sorted
        
    Returns:
        The sorted array
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = mergesort(left_half)
    right_half = mergesort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        A merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    # Example usage
    test_array = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {test_array}")
    
    sorted_array = mergesort(test_array)
    print(f"Sorted array: {sorted_array}")
