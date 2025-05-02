# avl_tree.py

"""
CS 034 - Data Structures and Advanced Python
Lab 10: Balanced Trees
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 1st, 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab10-BalancedTrees
"""

class AVLNode:
    """
    Node class for AVL Tree implementation
    """
    def __init__(self, key):
        """
        Initialize a new AVL Tree node
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key          # Value stored in the node
        self.left = None        # Left child reference
        self.right = None       # Right child reference
        self.height = 1         # Height of node in the tree (leaf nodes have height 1)
        
    def __str__(self):
        """String representation of the node"""
        return str(self.key)


class AVLTree:
    """
    AVL Tree implementation with automatic balancing
    
    This implementation is useful for:
    - Managing player rankings in a competitive video game leaderboard
    """
    
    def __init__(self):
        """Initialize an empty AVL Tree"""
        self.root = None        # Root node of the tree
        self.rotation_count = 0 # Track the number of rotations performed
    
    def height(self, node):
        """
        Get the height of a node (None nodes have height 0)
        
        Args:
            node: The node to get height from
            
        Returns:
            int: Height of the node or 0 if node is None
        """
        if node is None:
            return 0
        return node.height
    
    def balance_factor(self, node):
        """
        Calculate balance factor of a node (left subtree height - right subtree height)
        
        Args:
            node: The node to calculate balance factor for
            
        Returns:
            int: Balance factor of the node
        """
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        """
        Update the height of a node based on its children's heights
        
        Args:
            node: The node to update height for
        """
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def right_rotate(self, y):
        """
        Perform right rotation on node y
        
        Args:
            y: The node to rotate
            
        Returns:
            AVLNode: New root after rotation
        """
        # Track rotation
        self.rotation_count += 1
        
        # Store references
        x = y.left
        T3 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T3
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        # Return new root
        return x
    
    def left_rotate(self, x):
        """
        Perform left rotation on node x
        
        Args:
            x: The node to rotate
            
        Returns:
            AVLNode: New root after rotation
        """
        # Track rotation
        self.rotation_count += 1
        
        # Store references
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        # Return new root
        return y
    
    def insert(self, key):
        """
        Insert a new key into the AVL Tree
        
        Args:
            key: The value to insert
        """
        # Perform standard BST insertion
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """
        Recursively insert a key into the AVL Tree
        
        Args:
            node: Current node being considered
            key: The value to insert
            
        Returns:
            AVLNode: New root after insertion
        """
        # Standard BST insertion
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            # Duplicate keys not allowed
            return node
        
        # Update height of current node
        self.update_height(node)
        
        # Get balance factor to check if node became unbalanced
        balance = self.balance_factor(node)
        
        # Left heavy cases (balance > 1)
        if balance > 1:
            # Left-Left Case
            if key < node.left.key:
                return self.right_rotate(node)
            # Left-Right Case
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        # Right heavy cases (balance < -1)
        if balance < -1:
            # Right-Right Case
            if key > node.right.key:
                return self.left_rotate(node)
            # Right-Left Case
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        
        # Return unchanged node if no rotation was performed
        return node
    
    def get_height(self):
        """
        Get the height of the entire tree
        
        Returns:
            int: Height of the tree or 0 if tree is empty
        """
        return self.height(self.root)
    
    def get_rotation_count(self):
        """
        Get the total number of rotations performed
        
        Returns:
            int: Total rotation count
        """
        return self.rotation_count
    
    def print_tree(self):
        """Print the tree structure"""
        if self.root is None:
            print("Empty Tree")
            return
        
        print("AVL Tree Structure:")
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
        if node is not None:
            print("  " * level + prefix + str(node.key) + 
                  f" (height: {node.height}, balance: {self.balance_factor(node)})")
            
            if node.left is not None or node.right is not None:
                if node.left:
                    self._print_tree_recursive(node.left, level + 1, "L: ")
                else:
                    print("  " * (level + 1) + "L: None")
                    
                if node.right:
                    self._print_tree_recursive(node.right, level + 1, "R: ")
                else:
                    print("  " * (level + 1) + "R: None")


# Example usage (when running this file directly)
if __name__ == "__main__":
    # Create a new AVL Tree
    avl = AVLTree()
    
    # Insert some test values
    test_values = [10, 20, 30, 40, 50, 25]
    for val in test_values:
        avl.insert(val)
        print(f"Inserted {val}")
        avl.print_tree()
    
    print(f"Final tree height: {avl.get_height()}")
    print(f"Total rotations performed: {avl.get_rotation_count()}")