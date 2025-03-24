"""
Generate test datasets for sorting algorithm evaluation.

This script creates various types of datasets as described in the design document:
1. Random Integer Arrays
2. Nearly Sorted Arrays
3. Reverse Sorted Arrays
4. Arrays with Duplicate Values
5. Constant Arrays
"""

import random
import os
import json

# Create data directory if it doesn't exist
os.makedirs('datasets', exist_ok=True)

def generate_random_array(size, min_val=-10000, max_val=10000):
    """Generate an array of random integers."""
    return random.sample(range(min_val, max_val+1), min(size, max_val-min_val+1))

def generate_nearly_sorted_array(size, percent_unsorted=10):
    """Generate a nearly sorted array (only a small percentage is out of order)."""
    # Create a sorted array
    arr = list(range(size))
    
    # Calculate how many elements to swap
    num_swaps = int(size * percent_unsorted / 100)
    
    # Perform random swaps
    for _ in range(num_swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def generate_reverse_sorted_array(size):
    """Generate an array sorted in descending order."""
    return list(range(size, 0, -1))

def generate_array_with_duplicates(size, unique_percent=20):
    """Generate an array with many duplicate values."""
    # Calculate number of unique values
    num_unique = max(1, int(size * unique_percent / 100))
    
    # Generate unique values
    unique_values = random.sample(range(-1000, 1000), num_unique)
    
    # Create array with duplicates
    arr = []
    for _ in range(size):
        arr.append(random.choice(unique_values))
    
    return arr

def generate_constant_array(size, value=42):
    """Generate an array where all elements have the same value."""
    return [value] * size

def save_dataset(dataset, filename):
    """Save a dataset to a JSON file."""
    with open(f'datasets/{filename}', 'w') as f:
        json.dump(dataset, f)
    print(f"Saved {len(dataset)} elements to datasets/{filename}")

# Generate datasets of various sizes
sizes = [100, 1000, 10000]
for size in sizes:
    # Random arrays
    save_dataset(generate_random_array(size), f'random_{size}.json')
    
    # Nearly sorted arrays
    save_dataset(generate_nearly_sorted_array(size), f'nearly_sorted_{size}.json')
    
    # Reverse sorted arrays
    save_dataset(generate_reverse_sorted_array(size), f'reverse_sorted_{size}.json')
    
    # Arrays with duplicates
    save_dataset(generate_array_with_duplicates(size), f'duplicates_{size}.json')
    
    # Constant arrays
    save_dataset(generate_constant_array(size), f'constant_{size}.json')

# Special test cases
save_dataset([], 'empty.json')  # Empty array
save_dataset([42], 'single.json')  # Single element
save_dataset([7, 3], 'two_elements.json')  # Two elements

print("All datasets generated successfully!")