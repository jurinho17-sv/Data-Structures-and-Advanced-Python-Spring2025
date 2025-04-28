"""
CS 034 - Data Structures and Advanced Python
Lab 9: Trees
Group 14: Ju Ho Kim, Sangmin Kim
Date: April 27, 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Lab9-Trees
"""

class Node:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        value: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ========== Part 1: Binary Tree Construction & Traversals ==========

def create_sample_tree():
    """
    Creates a sample binary tree with the structure:
         A
        / \
       B   C
      / \   \
     D   E   F
    
    Returns:
        The root node of the sample tree
    """
    # Create nodes
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')
    
    return root

def preorder_traversal(node, result=None):
    """
    Performs a preorder traversal (Root -> Left -> Right) on the binary tree.
    
    Args:
        node: The current node being visited
        result: List to store the traversal result
        
    Returns:
        List containing the values in preorder traversal order
    """
    if result is None:
        result = []
    
    if node:
        # Visit the root node first
        result.append(node.value)
        # Then traverse the left subtree
        preorder_traversal(node.left, result)
        # Finally traverse the right subtree
        preorder_traversal(node.right, result)
    
    return result

def inorder_traversal(node, result=None):
    """
    Performs an inorder traversal (Left -> Root -> Right) on the binary tree.
    
    Args:
        node: The current node being visited
        result: List to store the traversal result
        
    Returns:
        List containing the values in inorder traversal order
    """
    if result is None:
        result = []
    
    if node:
        # First traverse the left subtree
        inorder_traversal(node.left, result)
        # Then visit the root node
        result.append(node.value)
        # Finally traverse the right subtree
        inorder_traversal(node.right, result)
    
    return result

def postorder_traversal(node, result=None):
    """
    Performs a postorder traversal (Left -> Right -> Root) on the binary tree.
    
    Args:
        node: The current node being visited
        result: List to store the traversal result
        
    Returns:
        List containing the values in postorder traversal order
    """
    if result is None:
        result = []
    
    if node:
        # First traverse the left subtree
        postorder_traversal(node.left, result)
        # Then traverse the right subtree
        postorder_traversal(node.right, result)
        # Finally visit the root node
        result.append(node.value)
    
    return result

# ========== Part 2: Binary Search Tree (BST) Implementation ==========

class BST:
    """
    Binary Search Tree implementation with insert, search, and remove operations.
    """
    def __init__(self):
        """Initialize an empty BST"""
        self.root = None
    
    def insert(self, value):
        """
        Inserts a new value into the BST, maintaining BST properties.
        
        Args:
            value: Value to insert into the tree
        """
        # Create a helper function for recursive insertion
        def _insert_recursive(node, value):
            # If we've reached a leaf node, create and return a new node
            if node is None:
                return Node(value)
            
            # Traverse left if value is less than current node
            if value < node.value:
                node.left = _insert_recursive(node.left, value)
            # Traverse right if value is greater than current node
            elif value > node.value:
                node.right = _insert_recursive(node.right, value)
            # If value already exists, we'll just return the current node
            
            return node
        
        # Start the recursive insertion from the root
        self.root = _insert_recursive(self.root, value)
        print(f"Inserted {value} into the BST")
    
    def search(self, value):
        """
        Searches for a value in the BST.
        
        Args:
            value: Value to search for
            
        Returns:
            True if value is found, False otherwise
        """
        # Create a helper function for recursive search
        def _search_recursive(node, value):
            # Base case: value not found or empty tree
            if node is None:
                return False
            
            # Found the value
            if node.value == value:
                return True
            
            # Recursive search: left if value < node.value, right otherwise
            if value < node.value:
                return _search_recursive(node.left, value)
            else:
                return _search_recursive(node.right, value)
        
        # Start the recursive search from the root
        found = _search_recursive(self.root, value)
        if found:
            print(f"Value {value} was found in the BST.")
        else:
            print(f"Value {value} was NOT found in the BST.")
        return found
    
    def inorder(self):
        """
        Performs an inorder traversal of the BST.
        
        Returns:
            List of values in sorted order
        """
        result = inorder_traversal(self.root, [])
        print("Inorder traversal (sorted order):", result)
        return result
    
    def remove(self, value):
        """
        Removes a node with the given value from the BST.
        
        Args:
            value: Value to remove
            
        Returns:
            True if value was removed, False if not found
        """
        # Flag to track if removal was successful
        self.was_removed = False
        
        # Helper function to find the minimum value node in a subtree
        def find_min(node):
            current = node
            # Keep going left to find the minimum value
            while current.left is not None:
                current = current.left
            return current
        
        # Recursive function to remove a node
        def _remove_recursive(node, value):
            # Base case: value not found
            if node is None:
                return None
            
            # Find the node to remove by traversing the tree
            if value < node.value:
                node.left = _remove_recursive(node.left, value)
            elif value > node.value:
                node.right = _remove_recursive(node.right, value)
            else:
                # Node found - handle three cases
                self.was_removed = True
                
                # Case 1: Node with no children (leaf node)
                if node.left is None and node.right is None:
                    print(f"Removing node {value} with no children")
                    return None
                
                # Case 2: Node with only one child
                elif node.left is None:
                    print(f"Removing node {value} with one child (right)")
                    return node.right
                elif node.right is None:
                    print(f"Removing node {value} with one child (left)")
                    return node.left
                
                # Case 3: Node with two children
                else:
                    print(f"Removing node {value} with two children")
                    # Find the inorder successor (smallest node in right subtree)
                    successor = find_min(node.right)
                    # Replace current node's value with successor's value
                    node.value = successor.value
                    # Remove the successor (which will be either case 1 or 2)
                    node.right = _remove_recursive(node.right, successor.value)
            
            return node
        
        # Start recursive removal from the root
        self.root = _remove_recursive(self.root, value)
        
        if self.was_removed:
            print(f"Successfully removed {value} from the BST")
        else:
            print(f"Value {value} not found in the BST")
        
        return self.was_removed

# ========== Part 3: AVL Tree Implementation (Extra Credit) ==========

class AVLNode(Node):
    """
    A node in an AVL tree that keeps track of its height.
    """
    def __init__(self, value):
        super().__init__(value)
        self.height = 1  # Height of a new leaf node is 1

class AVLTree:
    """
    Self-balancing AVL tree implementation with automatic balancing.
    """
    def __init__(self):
        """Initialize an empty AVL tree"""
        self.root = None
    
    def height(self, node):
        """Get the height of a node (None has height 0)"""
        if node is None:
            return 0
        return node.height
    
    def balance_factor(self, node):
        """Calculate the balance factor of a node"""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        """Update the height of a node based on its children"""
        if node is None:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def rotate_right(self, y):
        """
        Perform a right rotation on node y
                y                  x
               / \                / \
              x   T3   -->      T1   y
             / \                    / \
            T1  T2                 T2  T3
        """
        print(f"Performing right rotation on node {y.value}")
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        # Return new root
        return x
    
    def rotate_left(self, x):
        """
        Perform a left rotation on node x
              x                    y
             / \                  / \
            T1  y      -->       x   T3
               / \              / \
              T2  T3           T1  T2
        """
        print(f"Performing left rotation on node {x.value}")
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
    
    def insert(self, value):
        """Insert a value into the AVL tree and rebalance"""
        
        def _insert_recursive(node, value):
            # Standard BST insert
            if node is None:
                print(f"Inserted leaf node with value {value}")
                return AVLNode(value)
            
            if value < node.value:
                node.left = _insert_recursive(node.left, value)
            elif value > node.value:
                node.right = _insert_recursive(node.right, value)
            else:
                # Duplicate values not allowed
                return node
            
            # Update height of current node
            self.update_height(node)
            
            # Get the balance factor to check if rebalancing is needed
            balance = self.balance_factor(node)
            
            # Left-Left Case (LL)
            if balance > 1 and value < node.left.value:
                print(f"Left-Left case detected at node {node.value}")
                return self.rotate_right(node)
            
            # Right-Right Case (RR)
            if balance < -1 and value > node.right.value:
                print(f"Right-Right case detected at node {node.value}")
                return self.rotate_left(node)
            
            # Left-Right Case (LR)
            if balance > 1 and value > node.left.value:
                print(f"Left-Right case detected at node {node.value}")
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            
            # Right-Left Case (RL)
            if balance < -1 and value < node.right.value:
                print(f"Right-Left case detected at node {node.value}")
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            
            # Node is balanced
            return node
        
        # Start recursive insertion from root
        self.root = _insert_recursive(self.root, value)
        print(f"Inserted {value} into the AVL tree with balancing")
    
    def inorder(self):
        """Inorder traversal for the AVL tree"""
        result = []
        
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        
        _inorder(self.root)
        print("Inorder traversal of AVL tree (sorted order):", result)
        return result
    
    def print_tree(self, node=None, level=0, is_first_call=True):
        """Print the AVL tree structure with indentation"""
        if is_first_call and node is None:
            node = self.root
            print("AVL Tree Structure:")
        
        if node is not None:
            # Print right branch (top part of the tree)
            self.print_tree(node.right, level + 1, False)
            
            # Print current node
            print(' ' * 4 * level + '-> ' + str(node.value) + 
                  f" (h={node.height}, bf={self.balance_factor(node)})")
            
            # Print left branch (bottom part of the tree)
            self.print_tree(node.left, level + 1, False)


# ========== Main Function to Run All Required Tests ==========

def main():
    print("\n" + "="*70)
    print("Lab 9: Trees - Group 14(Ju Ho Kim, Sangmin Kim) - CS 034 - April 27, 2025".center(70))
    print("="*70 + "\n")
    
    # ---- Part 1: Binary Tree Construction & Traversals ----
    print("\nPart 1: Binary Tree Construction & Traversals")
    print("-" * 50)
    
    # Create the sample tree
    tree = create_sample_tree()
    
    # Perform traversals and print results
    print("Preorder traversal:", preorder_traversal(tree))
    print("Inorder traversal:", inorder_traversal(tree))
    print("Postorder traversal:", postorder_traversal(tree))
    
    # ---- Part 2: Binary Search Tree (BST) Operations ----
    print("\nPart 2: Binary Search Tree (BST) Operations")
    print("-" * 50)
    
    # Create a BST and insert values
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    print("Inserting values:", values)
    for value in values:
        bst.insert(value)
    
    # Verify BST with inorder traversal (should be sorted)
    bst.inorder()
    
    # Search for values
    print("\nSearching for values:")
    bst.search(40)  # Should be found
    bst.search(100)  # Should not be found
    bst.search(60)  # Should be found
    
    # Remove nodes of different types
    print("\nTesting node removal:")
    
    # Remove leaf node (20)
    bst.remove(20)
    bst.inorder()  # Verify removal
    
    # Remove node with one child (30)
    bst.remove(30)
    bst.inorder()  # Verify removal
    
    # Remove node with two children (50 - root)
    bst.remove(50)
    bst.inorder()  # Verify removal
    
    # ---- Part 3: AVL Tree Implementation (Extra Credit) ----
    print("\nPart 3: AVL Tree Implementation (Extra Credit)")
    print("-" * 50)
    
    # Create an AVL tree and insert the same values
    avl = AVLTree()
    
    print("Inserting values into AVL tree:", values)
    for value in values:
        avl.insert(value)
        # Don't print tree after each insertion to avoid excessive output
    
    # Verify the tree is balanced and in sorted order
    avl.inorder()
    
    print("\nFinal AVL tree structure:")
    avl.print_tree()


if __name__ == "__main__":
    main()