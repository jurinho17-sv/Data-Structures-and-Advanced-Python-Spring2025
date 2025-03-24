"""
Implementation of Insertion Sort algorithm.

This module provides functions to perform the Insertion Sort algorithm on lists of comparable elements.
"""

def insertionsort(arr):
    """
    Sort an array using the Insertion Sort algorithm.
    
    Args:
        arr: The array to be sorted
        
    Returns:
        None (the array is sorted in-place)
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertionsort_with_binary_search(arr):
    """
    Sort an array using the Insertion Sort algorithm with binary search optimization.
    This variant uses binary search to find the position where the element should be inserted,
    which can reduce the number of comparisons.
    
    Args:
        arr: The array to be sorted
        
    Returns:
        None (the array is sorted in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Find the position where key should be inserted using binary search
        position = binary_search(arr, key, 0, i - 1)
        
        # Shift all elements after position to right
        for j in range(i - 1, position - 1, -1):
            arr[j + 1] = arr[j]
            
        # Insert key at the correct position
        arr[position] = key


def binary_search(arr, key, low, high):
    """
    Use binary search to find the position where key should be inserted.
    
    Args:
        arr: The array to search within
        key: The value to find the insertion position for
        low: The lower bound of the search range
        high: The upper bound of the search range
        
    Returns:
        The position where key should be inserted
    """
    if high <= low:
        if key > arr[low]:
            return low + 1
        else:
            return low
    
    mid = (low + high) // 2
    
    if key == arr[mid]:
        return mid + 1
    elif key > arr[mid]:
        return binary_search(arr, key, mid + 1, high)
    else:
        return binary_search(arr, key, low, mid - 1)


if __name__ == "__main__":
    # Example usage of regular insertion sort
    test_array1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array1}")
    
    insertionsort(test_array1)
    print(f"Sorted array (regular insertion sort): {test_array1}")
    
    # Example usage of insertion sort with binary search
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {test_array2}")
    
    insertionsort_with_binary_search(test_array2)
    print(f"Sorted array (insertion sort with binary search): {test_array2}")
