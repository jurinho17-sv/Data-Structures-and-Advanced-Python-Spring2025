"""
Performance testing for sorting algorithms.

This script tests the performance of different sorting algorithms on various datasets
and collects metrics such as execution time, comparisons, and swaps.
"""

import time
import json
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Add the parent directory to the path so we can import the sorting modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import sorting algorithms
from part2.quicksort import quicksort
from part2.mergesort import mergesort
from part2.heapsort import heapsort
from part2.insertionsort import insertionsort, insertionsort_with_binary_search

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

def load_dataset(filename):
    """Load a dataset from a JSON file."""
    with open(os.path.join('datasets', filename), 'r') as f:
        return json.load(f)

def test_algorithm(algorithm, dataset, algo_name, dataset_name):
    """Test a sorting algorithm on a dataset and return performance metrics."""
    # Make a copy of the dataset to avoid modifying the original
    data_copy = dataset.copy()
    
    # Initialize stats dictionary
    stats = {'comparisons': 0, 'swaps': 0}
    
    # Measure execution time
    start_time = time.time()
    
    # Run the algorithm
    if algo_name in ['Quick Sort', 'Heap Sort', 'Insertion Sort', 'Insertion Sort (Binary)']:
        returned_stats = algorithm(data_copy, stats)
        if returned_stats:
            stats = returned_stats
    else:  # Merge Sort returns a new array
        algorithm(data_copy, stats)
    
    # Calculate execution time
    execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    
    return {
        'algorithm': algo_name,
        'dataset': dataset_name,
        'size': len(dataset),
        'time_ms': execution_time,
        'comparisons': stats['comparisons'],
        'swaps': stats['swaps']
    }

def run_performance_tests():
    """Run performance tests on all algorithms using all datasets."""
    results = []
    
    # Define algorithms to test
    algorithms = [
        (quicksort, 'Quick Sort'),
        (mergesort, 'Merge Sort'),
        (heapsort, 'Heap Sort'),
        (insertionsort, 'Insertion Sort'),
        (insertionsort_with_binary_search, 'Insertion Sort (Binary)')
    ]
    
    # Get all dataset files
    dataset_files = [f for f in os.listdir('datasets') if f.endswith('.json')]
    
    total_tests = len(algorithms) * len(dataset_files)
    test_count = 0
    
    # Run tests for each algorithm and dataset
    for algo_func, algo_name in algorithms:
        for dataset_file in dataset_files:
            test_count += 1
            dataset_name = dataset_file.replace('.json', '')
            print(f"Running test {test_count}/{total_tests}: {algo_name} on {dataset_name}")
            
            try:
                dataset = load_dataset(dataset_file)
                result = test_algorithm(algo_func, dataset, algo_name, dataset_name)
                results.append(result)
            except Exception as e:
                print(f"Error testing {algo_name} on {dataset_name}: {e}")
    
    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    
    # Save results to CSV
    df.to_csv('results/performance_results.csv', index=False)
    
    # Print summary table
    summary = df.groupby(['algorithm', 'dataset']).agg({
        'time_ms': 'mean',
        'comparisons': 'mean',
        'swaps': 'mean'
    }).reset_index()
    
    print("\nPerformance Summary:")
    print(tabulate(summary, headers='keys', tablefmt='grid'))
    
    return df

def generate_charts(results_df):
    """Generate charts to visualize performance results."""
    # Filter results for datasets of size 100, 1000, and 10000
    sizes = [100, 1000, 10000]
    filtered_df = results_df[results_df['size'].isin(sizes)]
    
    # Create execution time chart
    plt.figure(figsize=(12, 6))
    for size in sizes:
        size_df = filtered_df[filtered_df['size'] == size]
        time_pivot = size_df.pivot(index='algorithm', columns='dataset', values='time_ms')
        
        # Filter only main dataset types
        main_datasets = ['random', 'nearly_sorted', 'reverse_sorted', 'duplicates', 'constant']
        columns_to_keep = []
        for dataset in main_datasets:
            matching_cols = [col for col in time_pivot.columns if dataset in col]
            columns_to_keep.extend(matching_cols)
        
        time_pivot = time_pivot[columns_to_keep]
        
        ax = time_pivot.plot(kind='bar', figsize=(15, 6), title=f'Execution Time (ms) for Size {size}')
        ax.set_ylabel('Time (ms)')
        ax.set_xlabel('Algorithm')
        plt.tight_layout()
        plt.savefig(f'results/time_comparison_size_{size}.png')
    
    # Create comparisons chart
    plt.figure(figsize=(12, 6))
    for size in sizes:
        size_df = filtered_df[filtered_df['size'] == size]
        comp_pivot = size_df.pivot(index='algorithm', columns='dataset', values='comparisons')
        
        # Keep only main dataset types
        columns_to_keep = []
        for dataset in main_datasets:
            matching_cols = [col for col in comp_pivot.columns if dataset in col]
            columns_to_keep.extend(matching_cols)
        
        comp_pivot = comp_pivot[columns_to_keep]
        
        ax = comp_pivot.plot(kind='bar', figsize=(15, 6), title=f'Number of Comparisons for Size {size}')
        ax.set_ylabel('Comparisons')
        ax.set_xlabel('Algorithm')
        plt.tight_layout()
        plt.savefig(f'results/comparisons_size_{size}.png')
    
    # Algorithm comparison across sizes
    plt.figure(figsize=(12, 6))
    size_time = filtered_df.groupby(['algorithm', 'size']).agg({'time_ms': 'mean'}).reset_index()
    
    for algo in size_time['algorithm'].unique():
        algo_df = size_time[size_time['algorithm'] == algo]
        plt.plot(algo_df['size'], algo_df['time_ms'], marker='o', label=algo)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Dataset Size (log scale)')
    plt.ylabel('Time (ms) (log scale)')
    plt.title('Algorithm Performance vs Dataset Size')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('results/size_vs_time.png')

if __name__ == "__main__":
    print("Starting performance tests...")
    results = run_performance_tests()
    print("\nGenerating charts...")
    generate_charts(results)
    print("\nPerformance testing complete! Results saved to 'results' directory.")