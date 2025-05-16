# Set.py

"""
CS 034 - Data Structures and Advanced Python
Lab 12: Implementing and Applying the Set ADT
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 15th, 2025

GitHub repo:
"""

class Set:
    """
    A custom implementation of the Set abstract data type (ADT) using a dictionary
    as the underlying data structure.
    
    This implementation provides efficient O(1) average case operations for adding,
    removing and checking membership.
    """
    
    def __init__(self):
        """
        Initialize an empty set using a dictionary as the underlying structure.
        """
        # Using a dictionary with elements as keys for O(1) operations
        self.elements = {}
    
    def add(self, element):
        """
        Add an element to the set if it's not already present.
        
        Args:
            element: The element to add to the set (must be hashable)
        """
        # Using dictionary, we store the element as a key with a True value
        if element is not None:
            self.elements[element] = True
    
    def remove(self, element):
        """
        Remove an element from the set.
        
        Args:
            element: The element to remove
            
        Raises:
            KeyError: If the element is not in the set
        """
        if self.contains(element):
            del self.elements[element]
        else:
            raise KeyError(f"Element '{element}' not in set")
    
    def contains(self, element):
        """
        Check if an element exists in the set.
        
        Args:
            element: The element to check
            
        Returns:
            bool: True if the element is in the set, False otherwise
        """
        return element in self.elements
    
    def union(self, other_set):
        """
        Return a new set that is the union of this set and the other set.
        
        Args:
            other_set: Another Set object
            
        Returns:
            Set: A new set containing all elements from both sets
        """
        # Create a new set to store the result
        result = Set()
        
        # Add all elements from this set
        for element in self:
            result.add(element)
        
        # Add all elements from the other set
        for element in other_set:
            result.add(element)
        
        return result
    
    def intersection(self, other_set):
        """
        Return a new set that is the intersection of this set and the other set.
        
        Args:
            other_set: Another Set object
            
        Returns:
            Set: A new set containing only elements that are in both sets
        """
        # Create a new set to store the result
        result = Set()
        
        # Add elements that are in both sets
        for element in self:
            if other_set.contains(element):
                result.add(element)
        
        return result
    
    def difference(self, other_set):
        """
        Return a new set that is the difference of this set and the other set.
        
        Args:
            other_set: Another Set object
            
        Returns:
            Set: A new set containing elements that are in this set but not in the other set
        """
        # Create a new set to store the result
        result = Set()
        
        # Add elements that are in this set but not in the other set
        for element in self:
            if not other_set.contains(element):
                result.add(element)
        
        return result
    
    def __len__(self):
        """
        Return the number of elements in the set.
        
        Returns:
            int: The number of elements
        """
        return len(self.elements)
    
    def __str__(self):
        """
        Return a string representation of the set.
        
        Returns:
            str: A string representation of the set
        """
        if not self.elements:
            return "Set{}"
        
        items = ", ".join(str(element) for element in self.elements)
        return f"Set{{{items}}}"
    
    def __iter__(self):
        """
        Allow iteration through the set elements.
        
        Returns:
            iterator: An iterator over the set elements
        """
        # Return an iterator over the keys (elements) of the dictionary
        return iter(self.elements)