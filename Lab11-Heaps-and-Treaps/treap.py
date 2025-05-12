# treap.py

"""
CS 034 - Data Structures and Advanced Python
Lab 11: Heaps and Treaps
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 11th, 2025

GitHub repo:
"""

import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def rotate_left(self, root):
        # Implement left rotation logic
        # The right child becomes the new root
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def rotate_right(self, root):
        # Implement right rotation logic
        # The left child becomes the new root
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def insert(self, root, key):
        # Insert node using BST rules
        # Apply rotations based on priority
        if root is None:
            return TreapNode(key)
        
        # BST insertion
        if key < root.key:
            root.left = self.insert(root.left, key)
            # Maintain heap property - rotate if child has higher priority
            if root.left.priority > root.priority:
                root = self.rotate_right(root)
        else:
            root.right = self.insert(root.right, key)
            # Maintain heap property - rotate if child has higher priority
            if root.right.priority > root.priority:
                root = self.rotate_left(root)
        
        return root

    def search(self, root, key):
        # Search for a key using BST logic
        if root is None:
            return False
        
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def insert_key(self, key):
        # Public method to insert a key
        self.root = self.insert(self.root, key)

    def search_key(self, key):
        # Public method to search for a key
        return self.search(self.root, key)