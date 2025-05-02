# tree_comparison.py

"""
CS 034 - Data Structures and Advanced Python
Lab 10: Balanced Trees
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 1st, 2025

GitHub repo:
"""

import random
import time
from avl_tree import AVLTree
from red_black_tree import RedBlackTree

def compare_trees(values):
    """
    Compare AVL and Red-Black trees with the same input values
    
    Args:
        values: List of values to insert into both trees
    """
    # Create trees
    avl_tree = AVLTree()
    rb_tree = RedBlackTree()
    
    print("Starting comparison with values:", values)
    print("-" * 50)
    
    # Test AVL Tree
    print("AVL Tree Insertion:")
    avl_start_time = time.time()
    
    for val in values:
        avl_tree.insert(val)
    
    avl_end_time = time.time()
    avl_time = avl_end_time - avl_start_time
    
    # Test Red-Black Tree
    print("Red-Black Tree Insertion:")
    rb_start_time = time.time()
    
    for val in values:
        rb_tree.insert(val)
    
    rb_end_time = time.time()
    rb_time = rb_end_time - rb_start_time
    
    # Print tree structures
    print("\nFinal AVL Tree:")
    avl_tree.print_tree()
    
    print("\nFinal Red-Black Tree:")
    rb_tree.print_tree()
    
    # Print comparison results
    print("\nComparison Results:")
    print("-" * 50)
    print(f"AVL Tree:")
    print(f"  - Height: {avl_tree.get_height()}")
    print(f"  - Rotations: {avl_tree.get_rotation_count()}")
    print(f"  - Insertion Time: {avl_time:.6f} seconds")
    
    print(f"\nRed-Black Tree:")
    print(f"  - Height: {rb_tree.get_height()}")
    print(f"  - Rotations: {rb_tree.get_rotation_count()}")
    print(f"  - Insertion Time: {rb_time:.6f} seconds")


if __name__ == "__main__":
    # Generate 20 random integers between 1 and 100
    random.seed(42)  # For reproducibility
    random_values = [random.randint(1, 100) for _ in range(20)]
    
    # Run comparison
    compare_trees(random_values)