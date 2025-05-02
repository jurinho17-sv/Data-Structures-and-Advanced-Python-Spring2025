# red_black_tree.py

"""
CS 034 - Data Structures and Advanced Python
Lab 10: Balanced Trees
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 1st, 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab10-BalancedTrees
"""

class RBNode:
    """
    Node class for Red-Black Tree implementation
    """
    def __init__(self, key):
        """
        Initialize a new Red-Black Tree node
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key          # Value stored in the node
        self.left = None        # Left child reference
        self.right = None       # Right child reference
        self.parent = None      # Parent node reference
        self.is_red = True      # New nodes are always red
        
    def __str__(self):
        """String representation of the node"""
        color = "Red" if self.is_red else "Black"
        return f"{self.key} ({color})"


class RedBlackTree:
    """
    Red-Black Tree implementation with automatic balancing
    
    This implementation is useful for:
    - Storing and updating book ISBN numbers in a library database
    """
    
    def __init__(self):
        """Initialize an empty Red-Black Tree"""
        self.nil = RBNode(None)      # Sentinel node (NIL)
        self.nil.is_red = False      # NIL nodes are always black
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil         # Root starts as NIL
        self.rotation_count = 0      # Track the number of rotations performed
    
    def insert(self, key):
        """
        Insert a new key into the Red-Black Tree
        
        Args:
            key: The value to insert
        """
        # Create new red node
        new_node = RBNode(key)
        new_node.left = self.nil
        new_node.right = self.nil
        
        # Perform standard BST insertion
        y = self.nil
        x = self.root
        
        # Find the insertion position
        while x != self.nil:
            y = x
            if new_node.key < x.key:
                x = x.left
            elif new_node.key > x.key:
                x = x.right
            else:
                # Duplicate keys not allowed
                return
        
        # Set the parent of new node
        new_node.parent = y
        
        # If tree was empty, new node becomes root
        if y == self.nil:
            self.root = new_node
        # Otherwise, attach to the correct child position
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        
        # Fix Red-Black Tree properties
        self._fix_insertion(new_node)
    
    def _left_rotate(self, x):
        """
        Perform left rotation on node x
        
        Args:
            x: The node to rotate
        """
        # Track rotation
        self.rotation_count += 1
        
        # Store reference to right child
        y = x.right
        
        # Turn y's left subtree into x's right subtree
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        
        # Link x's parent to y
        y.parent = x.parent
        
        # Handle root case
        if x.parent == self.nil:
            self.root = y
        # Handle x as left child
        elif x == x.parent.left:
            x.parent.left = y
        # Handle x as right child
        else:
            x.parent.right = y
        
        # Put x on y's left
        y.left = x
        x.parent = y
    
    def _right_rotate(self, y):
        """
        Perform right rotation on node y
        
        Args:
            y: The node to rotate
        """
        # Track rotation
        self.rotation_count += 1
        
        # Store reference to left child
        x = y.left
        
        # Turn x's right subtree into y's left subtree
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        
        # Link y's parent to x
        x.parent = y.parent
        
        # Handle root case
        if y.parent == self.nil:
            self.root = x
        # Handle y as right child
        elif y == y.parent.right:
            y.parent.right = x
        # Handle y as left child
        else:
            y.parent.left = x
        
        # Put y on x's right
        x.right = y
        y.parent = x
    
    def _fix_insertion(self, k):
        """
        Fix Red-Black Tree properties after insertion
        
        Args:
            k: Newly inserted node
        """
        # Fix the tree until we reach the root or parent is black
        while k != self.root and k.parent.is_red:
            # Parent is left child of grandparent
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                
                # Case 1: Uncle is red - recolor only
                if uncle.is_red:
                    k.parent.is_red = False
                    uncle.is_red = False
                    k.parent.parent.is_red = True
                    k = k.parent.parent
                else:
                    # Case 2: Uncle is black, k is right child - left rotation
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    
                    # Case 3: Uncle is black, k is left child - right rotation
                    k.parent.is_red = False
                    k.parent.parent.is_red = True
                    self._right_rotate(k.parent.parent)
            # Parent is right child of grandparent (mirror cases)
            else:
                uncle = k.parent.parent.left
                
                # Case 1: Uncle is red - recolor only
                if uncle.is_red:
                    k.parent.is_red = False
                    uncle.is_red = False
                    k.parent.parent.is_red = True
                    k = k.parent.parent
                else:
                    # Case 2: Uncle is black, k is left child - right rotation
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    
                    # Case 3: Uncle is black, k is right child - left rotation
                    k.parent.is_red = False
                    k.parent.parent.is_red = True
                    self._left_rotate(k.parent.parent)
                    
        # Ensure root is always black
        self.root.is_red = False
    
    def get_height(self):
        """
        Get the height of the entire tree
        
        Returns:
            int: Height of the tree or 0 if tree is empty
        """
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        """
        Recursively calculate the height of a subtree
        
        Args:
            node: Root of the subtree
            
        Returns:
            int: Height of the subtree
        """
        if node == self.nil:
            return 0
        
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def get_rotation_count(self):
        """
        Get the total number of rotations performed
        
        Returns:
            int: Total rotation count
        """
        return self.rotation_count
    
    def print_tree(self):
        """Print the tree structure"""
        if self.root == self.nil:
            print("Empty Tree")
            return
        
        print("Red-Black Tree Structure:")
        self._print_tree_recursive(self.root, 0, "Root: ")
        print("\n")
    
    def _print_tree_recursive(self, node, level, prefix):
        """
        Recursively print the tree structure
        
        Args:
            node: Current node being printed
            level: Current level in the tree (for indentation)
            prefix: Text prefix to add before node value
        """
        if node != self.nil:
            color = "Red" if node.is_red else "Black"
            print("  " * level + prefix + str(node.key) + f" ({color})")
            
            if node.left != self.nil or node.right != self.nil:
                if node.left != self.nil:
                    self._print_tree_recursive(node.left, level + 1, "L: ")
                else:
                    print("  " * (level + 1) + "L: NIL")
                    
                if node.right != self.nil:
                    self._print_tree_recursive(node.right, level + 1, "R: ")
                else:
                    print("  " * (level + 1) + "R: NIL")


# Example usage (when running this file directly)
if __name__ == "__main__":
    # Create a new Red-Black Tree
    rb = RedBlackTree()
    
    # Insert some test values
    test_values = [10, 20, 30, 40, 50, 25]
    for val in test_values:
        rb.insert(val)
        print(f"Inserted {val}")
        rb.print_tree()
    
    print(f"Final tree height: {rb.get_height()}")
    print(f"Total rotations performed: {rb.get_rotation_count()}")