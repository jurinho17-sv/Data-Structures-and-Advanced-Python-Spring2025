# tests.py

"""
CS 034 - Data Structures and Advanced Python
Lab 11: Heaps and Treaps
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 11th, 2025

GitHub repo:
"""

from min_heap import MinHeap
from treap import Treap

def test_min_heap():
    """Test MinHeap implementation"""
    print("=== Testing MinHeap ===")
    
    # Create MinHeap instance
    heap = MinHeap()
    
    # Test insertion
    test_values = [5, 3, 8, 1, 9, 2, 7]
    print(f"Inserting values: {test_values}")
    for val in test_values:
        heap.insert(val)
    
    # Test peek_min
    print(f"Peek min (should be 1): {heap.peek_min()}")
    
    # Test remove_min
    print("Removing elements in min order:")
    while not heap.is_empty():
        print(heap.remove_min(), end=" ")
    print("\n")

def test_treap():
    """Test Treap implementation"""
    print("=== Testing Treap ===")
    
    # Create Treap instance
    treap = Treap()
    
    # Test insertion
    test_keys = [5, 3, 8, 1, 9, 2, 7]
    print(f"Inserting keys: {test_keys}")
    for key in test_keys:
        treap.insert_key(key)
    
    # Test search
    search_keys = [3, 6, 9, 10]
    print("\nSearch results:")
    for key in search_keys:
        result = treap.search_key(key)
        print(f"Key {key}: {'Found' if result else 'Not found'}")
    
    # Print treap structure (for visualization)
    print("\nTreap structure (in-order traversal):")
    print_inorder(treap.root)
    print()

def print_inorder(root, level=0):
    """Helper function to print treap structure"""
    if root:
        print_inorder(root.right, level + 1)
        print("  " * level + f"Key: {root.key}, Priority: {root.priority}")
        print_inorder(root.left, level + 1)

if __name__ == "__main__":
    test_min_heap()
    print()
    test_treap()