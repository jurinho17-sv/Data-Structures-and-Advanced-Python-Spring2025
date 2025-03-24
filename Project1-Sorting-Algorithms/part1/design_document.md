# Sorting Algorithms Project Plan
**Advanced Python Programming and Data Structures**
**Spring 2025**

## 1. Algorithm Selection and Rationale (15 points)

Our team (Group 14) has selected the following sorting algorithms for implementation and analysis:

### Quick Sort
**Rationale:** Quick Sort is an efficient, divide-and-conquer algorithm that serves as a standard for comparison-based sorting. It offers average-case time complexity of O(n log n), making it suitable for large datasets. While its worst-case performance is O(n²), proper pivot selection strategies can mitigate this weakness. Quick Sort is widely used in practice due to its efficient cache utilization and adaptability to various data types.

### Merge Sort
**Rationale:** Merge Sort provides consistent O(n log n) performance regardless of input data characteristics, making it reliable for critical applications where predictable performance is essential. Unlike Quick Sort, it guarantees O(n log n) even in worst-case scenarios. Though it requires additional O(n) space complexity, this trade-off is often acceptable for its stability and consistent performance. Merge Sort is particularly effective for linked lists and external sorting applications.

### Heap Sort
**Rationale:** Heap Sort combines the space efficiency of in-place sorting with guaranteed O(n log n) time complexity in all cases. Its use of the heap data structure demonstrates an important application of priority queues. While typically slower than well-implemented Quick Sort in practice due to cache locality issues, Heap Sort provides excellent worst-case guarantees without Quick Sort's pathological cases, making it valuable for systems requiring consistent performance bounds.

### Insertion Sort
**Rationale:** Despite its O(n²) worst-case complexity, Insertion Sort excels with small datasets (n < 20) or nearly-sorted data, where it can approach O(n) performance. Its simplicity, low overhead, and adaptive nature make it ideal as a final step in more complex algorithms (like Quick Sort's partition handling). Insertion Sort is also stable, preserving the relative order of equal elements, which is crucial for certain applications.

## 2. Detailed Pseudocode and Flowcharts (20 points)

### Quick Sort

**Pseudocode:**
ALGORITHM QuickSort(arr, low, high)
    IF low < high THEN
        // Find the partition index
        pivotIndex ← Partition(arr, low, high)
        
        // Recursively sort elements before and after partition
        QuickSort(arr, low, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, high)
    END IF
END ALGORITHM

ALGORITHM Partition(arr, low, high)
    // Choose rightmost element as pivot
    pivot ← arr[high]
    
    // Index of smaller element
    i ← low - 1
    
    FOR j ← low TO high - 1 DO
        // If current element is smaller than or equal to pivot
        IF arr[j] ≤ pivot THEN
            // Increment index of smaller element
            i ← i + 1
            Swap arr[i] and arr[j]
        END IF
    END FOR
    
    Swap arr[i + 1] and arr[high]
    RETURN i + 1
END ALGORITHM


**Flowchart for Quick Sort:**
┌─────────────────────┐
│ QuickSort(arr,low,high) │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   low < high?       │
└──────────┬──────────┘
           ↓
     ┌─────┴─────┐
     │           │
    Yes          No
     │           │
     ↓           ↓
┌─────────────────────┐    ┌─────────────────────┐
│pivotIndex←Partition()│    │       Return        │
└──────────┬──────────┘    └─────────────────────┘
           ↓
┌─────────────────────┐
│QuickSort(arr,low,   │
│     pivotIndex-1)   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│QuickSort(arr,       │
│pivotIndex+1,high)   │
└─────────────────────┘



### Merge Sort

**Pseudocode:**
ALGORITHM MergeSort(arr, left, right)
    IF left < right THEN
        // Find the middle point to divide the array
        middle ← (left + right) / 2
        
        // Recursively sort first and second halves
        MergeSort(arr, left, middle)
        MergeSort(arr, middle + 1, right)
        
        // Merge the sorted halves
        Merge(arr, left, middle, right)
    END IF
END ALGORITHM

ALGORITHM Merge(arr, left, middle, right)
    // Calculate sizes of subarrays
    n1 ← middle - left + 1
    n2 ← right - middle
    
    // Create temporary arrays
    Create arrays L[n1] and R[n2]
    
    // Copy data to temporary arrays
    FOR i ← 0 TO n1 - 1 DO
        L[i] ← arr[left + i]
    END FOR
    
    FOR j ← 0 TO n2 - 1 DO
        R[j] ← arr[middle + 1 + j]
    END FOR
    
    // Merge the temporary arrays back
    i ← 0, j ← 0, k ← left
    
    WHILE i < n1 AND j < n2 DO
        IF L[i] ≤ R[j] THEN
            arr[k] ← L[i]
            i ← i + 1
        ELSE
            arr[k] ← R[j]
            j ← j + 1
        END IF
        k ← k + 1
    END WHILE
    
    // Copy remaining elements of L[], if any
    WHILE i < n1 DO
        arr[k] ← L[i]
        i ← i + 1
        k ← k + 1
    END WHILE
    
    // Copy remaining elements of R[], if any
    WHILE j < n2 DO
        arr[k] ← R[j]
        j ← j + 1
        k ← k + 1
    END WHILE
END ALGORITHM


**Flowchart for Merge Sort:**
┌─────────────────────┐
│ MergeSort(arr,left,right) │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    left < right?    │
└──────────┬──────────┘
           ↓
     ┌─────┴─────┐
     │           │
    Yes          No
     │           │
     ↓           ↓
┌─────────────────────┐    ┌─────────────────────┐
│middle←(left+right)/2│    │       Return        │
└──────────┬──────────┘    └─────────────────────┘
           ↓
┌─────────────────────┐
│MergeSort(arr,left,  │
│       middle)       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│MergeSort(arr,       │
│  middle+1,right)    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Merge(arr,left,     │
│   middle,right)     │
└─────────────────────┘



### Heap Sort

**Pseudocode:**
ALGORITHM HeapSort(arr)
    n ← length(arr)
    
    // Build max heap
    FOR i ← n/2 - 1 TO 0 (step -1) DO
        Heapify(arr, n, i)
    END FOR
    
    // Extract elements from heap one by one
    FOR i ← n - 1 TO 0 (step -1) DO
        // Move current root to end
        Swap arr[0] and arr[i]
        
        // Call max heapify on reduced heap
        Heapify(arr, i, 0)
    END FOR
END ALGORITHM

ALGORITHM Heapify(arr, n, i)
    // Initialize largest as root
    largest ← i
    left ← 2*i + 1
    right ← 2*i + 2
    
    // If left child is larger than root
    IF left < n AND arr[left] > arr[largest] THEN
        largest ← left
    END IF
    
    // If right child is larger than largest so far
    IF right < n AND arr[right] > arr[largest] THEN
        largest ← right
    END IF
    
    // If largest is not root
    IF largest ≠ i THEN
        Swap arr[i] and arr[largest]
        
        // Recursively heapify the affected sub-tree
        Heapify(arr, n, largest)
    END IF
END ALGORITHM


**Flowchart for Heap Sort:**
┌─────────────────────┐
│    HeapSort(arr)    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     n ← len(arr)    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│Build max heap:      │
│For i←n/2-1 down to 0│
│  Heapify(arr,n,i)   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│Extract elements:    │
│For i←n-1 down to 0: │
│  Swap arr[0],arr[i] │
│  Heapify(arr,i,0)   │
└─────────────────────┘



### Insertion Sort

**Pseudocode:**
ALGORITHM InsertionSort(arr)
    n ← length(arr)
    
    FOR i ← 1 TO n - 1 DO
        key ← arr[i]
        j ← i - 1
        
        // Move elements greater than key one position ahead
        WHILE j ≥ 0 AND arr[j] > key DO
            arr[j + 1] ← arr[j]
            j ← j - 1
        END WHILE
        
        arr[j + 1] ← key
    END FOR
END ALGORITHM


**Flowchart for Insertion Sort:**
┌─────────────────────┐
│  InsertionSort(arr) │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     n ← len(arr)    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ FOR i ← 1 TO n-1    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    key ← arr[i]     │
│    j ← i - 1        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ WHILE j≥0 AND       │
│   arr[j] > key      │
└──────────┬──────────┘
           ↓
     ┌─────┴─────┐
     │           │
    Yes          No
     │           │
     ↓           ↓
┌─────────────────────┐    ┌─────────────────────┐
│arr[j+1] ← arr[j]    │    │  arr[j+1] ← key     │
│j ← j - 1            │    └──────────┬──────────┘
└──────────┬──────────┘               │
           │                          │
           └──────────────────────────┘


## 3. Planned Datasets and Test Cases (15 points)

To thoroughly evaluate the performance and correctness of our sorting algorithms, we have designed the following datasets and test cases:

### Dataset Types

1. **Random Integer Arrays**
   - Description: Arrays filled with randomly generated integers
   - Sizes: 100, 1,000, 10,000, and 100,000 elements
   - Value Range: [-10000, 10000]
   - Purpose: Evaluate average-case performance for each algorithm
   - Example: `[42, -17, 999, 3, ...]`

2. **Nearly Sorted Arrays**
   - Description: Arrays that are 90% sorted (only 10% of elements are out of order)
   - Sizes: 100, 1,000, 10,000, and 100,000 elements
   - Purpose: Test adaptive behavior of algorithms like Insertion Sort
   - Generation Method: Start with a sorted array, then swap random pairs for 10% of the array length
   - Example: `[1, 2, 4, 3, 5, 6, 7, 9, 8, 10, ...]`

3. **Reverse Sorted Arrays**
   - Description: Arrays sorted in descending order
   - Sizes: 100, 1,000, 10,000, and 100,000 elements
   - Purpose: Evaluate worst-case behavior for some algorithms
   - Example: `[100, 99, 98, ..., 3, 2, 1]`

4. **Arrays with Duplicate Values**
   - Description: Arrays with many repeated elements (80% of elements are duplicates)
   - Sizes: 100, 1,000, 10,000, and 100,000 elements
   - Purpose: Assess performance with non-unique keys and algorithm stability
   - Example: `[5, 2, 5, 7, 2, 5, 2, 7, ...]`

5. **Constant Arrays**
   - Description: Arrays where all elements have the same value
   - Sizes: 100, 1,000, 10,000, and 100,000 elements
   - Purpose: Test edge case behavior
   - Example: `[42, 42, 42, 42, ...]`

### Test Cases

| Test ID | Dataset Type      | Size    | Expected Outcome | Special Considerations                   |
|---------|-------------------|---------|------------------|------------------------------------------|
| TC1     | Random Integers   | 100     | Sorted Array     | Baseline performance test                |
| TC2     | Random Integers   | 10,000  | Sorted Array     | Stress test for all algorithms           |
| TC3     | Random Integers   | 100,000 | Sorted Array     | Performance differentiation test         |
| TC4     | Nearly Sorted     | 10,000  | Sorted Array     | Should favor Insertion Sort             |
| TC5     | Reverse Sorted    | 10,000  | Sorted Array     | Worst case for Quick Sort with rightmost pivot |
| TC6     | Duplicates        | 10,000  | Sorted Array     | Tests stability of algorithms           |
| TC7     | Constant Array    | 10,000  | Sorted Array     | Edge case test                           |
| TC8     | Empty Array       | 0       | Empty Array      | Edge case test                           |
| TC9     | Single Element    | 1       | Same Array       | Edge case test                           |
| TC10    | Two Elements      | 2       | Sorted Array     | Minimal comparison test                  |

### Validation Methods

For each test case, we will:
1. Verify correctness by comparing the output to Python's built-in `sorted()` function
2. Measure runtime using the `time` module for practical performance metrics
3. Count key operations (comparisons and swaps) to validate theoretical complexity
4. Generate visualization of sorted vs. unsorted arrays for demonstration purposes

### Performance Metrics Collection

We will record the following metrics for each algorithm and test case:
- Execution time (in milliseconds)
- Number of comparisons performed
- Number of swaps/moves performed
- Memory usage (peak additional memory required)

This comprehensive set of datasets and test cases will allow us to thoroughly evaluate the strengths and weaknesses of each sorting algorithm across various real-world scenarios.

