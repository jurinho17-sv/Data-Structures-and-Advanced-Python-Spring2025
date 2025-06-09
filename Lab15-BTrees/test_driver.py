# test_driver.py

"""
CS 034 - Data Structures and Advanced Python
Lab 15 - B-Trees Test Driver
Author: Ju Ho Kim, Sangmin Kim
Date: June. 8th. 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab15-BTrees

Test program to demonstrate B-Tree operations with random integers
"""

import random
from btree import BTree


def main():
    """Main test function to demonstrate B-Tree operations"""
    
    print("=" * 60)
    print("     B-TREE TEST DRIVER")
    print("=" * 60)
    
    # Create a new B-Tree
    tree = BTree()
    
    # Generate 15-20 random integers between 1 and 100
    num_values = random.randint(15, 20)
    random_integers = []
    
    # Generate unique random integers
    while len(random_integers) < num_values:
        value = random.randint(1, 100)
        if value not in random_integers:
            random_integers.append(value)
    
    print(f"\nGenerating {num_values} random integers:")
    print(f"Random integers: {random_integers}")
    
    # Insert all values into the B-Tree
    print("\n" + "-" * 60)
    print("INSERTING VALUES INTO B-TREE")
    print("-" * 60)
    
    for value in random_integers:
        tree.insert(value)
    
    # Perform in-order traversal
    print("\n" + "-" * 60)
    print("IN-ORDER TRAVERSAL")
    print("-" * 60)
    tree.inOrderTraversal()
    
    # Test search operations
    print("\n" + "-" * 60)
    print("SEARCH OPERATIONS")
    print("-" * 60)
    
    # Search for some values that exist
    search_values = []
    # Pick 3 random values from our list
    for i in range(3):
        if i < len(random_integers):
            search_values.append(random_integers[i])
    
    # Also search for some values that don't exist
    not_exist = [200, 201, 202]  # Values outside our range
    
    print("\nSearching for values that exist:")
    for value in search_values:
        result = tree.contains(value)
        print(f"  contains({value}): {result}")
    
    print("\nSearching for values that don't exist:")
    for value in not_exist:
        result = tree.contains(value)
        print(f"  contains({value}): {result}")
    
    # Bonus: Display tree structure
    print("\n" + "-" * 60)
    print("BONUS: TREE STRUCTURE VISUALIZATION")
    print("-" * 60)
    tree.print_tree()
    
    # Additional test: Verify sorted order
    print("\n" + "-" * 60)
    print("VERIFICATION")
    print("-" * 60)
    
    # Sort the original list and compare
    sorted_list = sorted(random_integers)
    print(f"Original list sorted: {sorted_list}")
    print("The in-order traversal should match the sorted list above!")
    
    print("\n" + "=" * 60)
    print("     TEST COMPLETED SUCCESSFULLY!")
    print("=" * 60)


def simple_test():
    """
    Simple test with known values for debugging
    Useful for understanding how the tree works
    """
    print("\n" + "=" * 60)
    print("     SIMPLE TEST WITH KNOWN VALUES")
    print("=" * 60)
    
    tree = BTree()
    
    # Insert specific values to see splitting behavior
    test_values = [10, 20, 30, 40, 50, 25, 60, 70, 80]
    
    print(f"\nInserting values in order: {test_values}")
    print("-" * 40)
    
    for value in test_values:
        tree.insert(value)
    
    print("\nFinal tree structure:")
    tree.print_tree()
    
    print("\nIn-order traversal:")
    tree.inOrderTraversal()


if __name__ == "__main__":
    # Run the main test
    main()
    
    # Uncomment the line below to also run the simple test
    # simple_test()