# Lab 12: Set ADT Design Document

## Class Diagram (UML)

### Set Class
```
+----------------------------+
|           Set              |
+----------------------------+
| - elements: dict           |
+----------------------------+
| + __init__()               |
| + add(element)             |
| + remove(element)          |
| + contains(element)        |
| + union(otherSet)          |
| + intersection(otherSet)   |
| + difference(otherSet)     |
| + __len__()                |
| + __str__()                |
| + __iter__()               |
+----------------------------+
```

### EnrollmentManager Class
```
+-----------------------------------+
|        EnrollmentManager          |
+-----------------------------------+
| - courseA: Set                    |
| - courseB: Set                    |
+-----------------------------------+
| + __init__(fileA, fileB)          |
| + load_course_data(filename)      |
| + students_in_both()              |
| + students_only_in_A()            |
| + students_only_in_B()            |
| + all_students()                  |
| + display_statistics()            |
+-----------------------------------+
```

## Pseudocode for Set Operations

### Initialization
```
FUNCTION __init__():
    self.elements = empty dictionary
END FUNCTION
```

### Add
```
FUNCTION add(element):
    IF element is not NULL THEN
        SET self.elements[element] = True
    END IF
END FUNCTION
```

### Remove
```
FUNCTION remove(element):
    IF self.contains(element) THEN
        REMOVE element from self.elements
    ELSE
        RAISE KeyError("Element not in set")
    END IF
END FUNCTION
```

### Contains
```
FUNCTION contains(element):
    RETURN element in self.elements
END FUNCTION
```

### Union
```
FUNCTION union(otherSet):
    result = new Set()
    
    FOR each element in self:
        result.add(element)
    END FOR
    
    FOR each element in otherSet:
        result.add(element)
    END FOR
    
    RETURN result
END FUNCTION
```

### Intersection
```
FUNCTION intersection(otherSet):
    result = new Set()
    
    FOR each element in self:
        IF otherSet.contains(element) THEN
            result.add(element)
        END IF
    END FOR
    
    RETURN result
END FUNCTION
```

### Difference
```
FUNCTION difference(otherSet):
    result = new Set()
    
    FOR each element in self:
        IF NOT otherSet.contains(element) THEN
            result.add(element)
        END IF
    END FOR
    
    RETURN result
END FUNCTION
```

## Data-flow Sketch

```
+----------------+     +----------------+
| courseA.csv    |     | courseB.csv    |
+----------------+     +----------------+
        |                     |
        v                     v
+-----------------------------------------+
|        EnrollmentManager                |
| 1. Load files into Set objects          |
| 2. Apply set operations                 |
| 3. Generate statistics                  |
+-----------------------------------------+
        |
        v
+--------------------------------------------------+
| Output:                                          |
| - Students in both courses (intersection)        |
| - Students only in A (difference A-B)            |
| - Students only in B (difference B-A)            |
| - All students (union)                           |
+--------------------------------------------------+
```

## Implementation Rationale

### Underlying Structure Choice

I've chosen to implement the Set ADT using a Python dictionary for the following reasons:

1. **Performance**: Dictionaries in Python provide O(1) average-case time complexity for lookups, insertions, and deletions, making them ideal for set operations.

2. **Simplicity**: Using a dictionary with elements as keys allows for a straightforward implementation without needing to develop a custom hashing mechanism.

3. **Edge Cases**: Dictionaries naturally handle edge cases like duplicates (keys are unique) and provide efficient membership testing.

4. **Memory Efficiency**: By using the elements as keys and storing a simple True value, we optimize memory usage while maintaining functionality.

### Trade-offs

- **Ordering**: This implementation doesn't maintain insertion order. If ordering matters, we could use OrderedDict instead of a regular dictionary.

- **Element Types**: Elements must be hashable to be used as dictionary keys. This restricts the types of elements that can be stored in our Set.

- **Iteration Performance**: Iterating through all elements is O(n), which affects the performance of set operations like union, intersection, and difference.

### Alternative Approaches Considered

1. **List-based implementation**: Simple but would have O(n) lookup time, making set operations inefficient.

2. **Using Python's built-in set**: Would be more efficient but would defeat the educational purpose of implementing our own Set ADT.

3. **Binary Search Tree**: Would provide O(log n) operations but adds complexity and is overkill for this application.

## Author

**Group 14 (Ju Ho Kim, Sangmin Kim)**  
CS 034 - Data Structures and Advanced Python  
Spring 2025