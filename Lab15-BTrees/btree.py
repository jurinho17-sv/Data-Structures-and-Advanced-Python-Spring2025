# btree.py

"""
CS 034 - Data Structures and Advanced Python
Lab 15 - B-Trees
Author: Ju Ho Kim, Sangmin Kim
Date: June. 8th. 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab15-BTrees

Implementation of a 2-3-4 Tree (B-Tree) with dynamic node splitting
"""


class Node:
    """
    Node class for 2-3-4 Tree
    - Can hold 1, 2, or 3 keys
    - Can have 2, 3, or 4 children
    """
    
    def __init__(self, leaf=True):
        """
        Initialize a new node
        
        Args:
            leaf (bool): True if node is a leaf, False otherwise
        """
        self.keys = []        # List to store keys (max 3)
        self.children = []    # List to store child nodes (max 4)
        self.leaf = leaf      # Flag to indicate if node is a leaf
    
    def is_full(self):
        """Check if node has maximum number of keys (3)"""
        # A node is full when it has 3 keys
        if len(self.keys) == 3:
            return True
        else:
            return False


class BTree:
    """
    2-3-4 Tree implementation with self-balancing through node splitting
    """
    
    def __init__(self):
        """Initialize an empty B-Tree with a root node"""
        self.root = Node()  # Start with an empty leaf node as root
    
    def insert(self, key):
        """
        Insert a key into the B-Tree
        
        Args:
            key (int): The key to insert
        """
        # Check if root is full (has 3 keys)
        if self.root.is_full():
            # Create new root
            new_root = Node(leaf=False)  # New root is not a leaf
            # Make old root a child of new root
            new_root.children.append(self.root)
            # Split the old root
            self._split_child(new_root, 0)
            # Update root
            self.root = new_root
        
        # Now insert the key
        self._insert_non_full(self.root, key)
        print(f"Inserted {key}")
    
    def _insert_non_full(self, node, key):
        """
        Insert key into a node that is not full
        
        Args:
            node (Node): The node to insert into
            key (int): The key to insert
        """
        # Start from the rightmost key
        i = len(node.keys) - 1
        
        if node.leaf:
            # This is a leaf node - insert key here
            # Add space for new key
            node.keys.append(None)
            
            # Move keys to make room for new key
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i = i - 1
            
            # Insert the new key
            node.keys[i + 1] = key
        else:
            # This is not a leaf - find correct child
            # Find which child to go to
            while i >= 0 and key < node.keys[i]:
                i = i - 1
            i = i + 1  # This is the child we need
            
            # Check if that child is full
            if node.children[i].is_full():
                # Split the child
                self._split_child(node, i)
                # After split, we might need to go to next child
                if key > node.keys[i]:
                    i = i + 1
            
            # Continue inserting in the appropriate child
            self._insert_non_full(node.children[i], key)
    
    def _split_child(self, parent, index):
        """
        Split a full child node into two nodes
        
        Args:
            parent (Node): Parent of the node to split
            index (int): Index of child in parent's children list
        """
        # Get the full child that needs splitting
        full_child = parent.children[index]
        
        # Create new node for right half
        new_child = Node(leaf=full_child.leaf)
        
        # The middle key will move up to parent
        mid_key = full_child.keys[1]
        
        # Split the keys
        # Left child keeps first key
        left_keys = [full_child.keys[0]]
        # Right child gets last key
        right_keys = [full_child.keys[2]]
        
        # Update the keys
        full_child.keys = left_keys
        new_child.keys = right_keys
        
        # If not a leaf, also split the children
        if not full_child.leaf:
            # Left child keeps first 2 children
            left_children = [full_child.children[0], full_child.children[1]]
            # Right child gets last 2 children
            right_children = [full_child.children[2], full_child.children[3]]
            
            # Update the children
            full_child.children = left_children
            new_child.children = right_children
        
        # Insert middle key into parent
        parent.keys.insert(index, mid_key)
        # Insert new child into parent
        parent.children.insert(index + 1, new_child)
        
        print(f"Node split occurred at key: {mid_key}")
    
    def contains(self, key):
        """
        Check if a key exists in the B-Tree
        
        Args:
            key (int): The key to search for
            
        Returns:
            bool: True if key exists, False otherwise
        """
        # Start searching from root
        return self._search(self.root, key)
    
    def _search(self, node, key):
        """
        Recursively search for a key in the tree
        
        Args:
            node (Node): Current node to search
            key (int): Key to search for
            
        Returns:
            bool: True if found, False otherwise
        """
        # Look through all keys in current node
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i = i + 1
        
        # Check if we found the key
        if i < len(node.keys) and key == node.keys[i]:
            return True
        
        # If this is a leaf and we didn't find it, key doesn't exist
        if node.leaf:
            return False
        
        # Otherwise, search in the appropriate child
        return self._search(node.children[i], key)
    
    def inOrderTraversal(self):
        """Print all keys in sorted order"""
        print("\nIn-order traversal (sorted):")
        self._in_order_helper(self.root)
        print()  # New line after traversal
    
    def _in_order_helper(self, node):
        """
        Helper method for in-order traversal
        
        Args:
            node (Node): Current node to process
        """
        if node is not None:
            # Process each key in the node
            i = 0
            num_keys = len(node.keys)
            
            # For each key
            while i < num_keys:
                # First, visit left child (if not a leaf)
                if not node.leaf and i < len(node.children):
                    self._in_order_helper(node.children[i])
                
                # Then print the key
                print(node.keys[i], end=" ")
                
                # Move to next key
                i = i + 1
            
            # Finally, visit the rightmost child (if not a leaf)
            if not node.leaf and len(node.children) > num_keys:
                self._in_order_helper(node.children[num_keys])
    
    def print_tree(self):
        """
        (Bonus) Print tree structure level by level
        """
        print("\nTree Structure (Level-by-Level):")
        
        # Check if tree is empty
        if len(self.root.keys) == 0:
            print("Empty tree")
            return
        
        # We'll use a list as a queue to process nodes level by level
        # Each item is a tuple: (node, level_number)
        queue = []
        queue.append((self.root, 0))
        
        current_level = 0
        level_nodes = []
        
        # Process nodes until queue is empty
        while len(queue) > 0:
            # Remove first item from queue
            node, level = queue.pop(0)
            
            # If we've moved to a new level, print the previous level
            if level > current_level:
                print(f"Level {current_level}: {level_nodes}")
                current_level = level
                level_nodes = []
            
            # Add this node's keys to current level
            level_nodes.append(node.keys)
            
            # Add all children to queue (if not a leaf)
            if not node.leaf:
                for child in node.children:
                    queue.append((child, level + 1))
        
        # Don't forget to print the last level
        print(f"Level {current_level}: {level_nodes}")