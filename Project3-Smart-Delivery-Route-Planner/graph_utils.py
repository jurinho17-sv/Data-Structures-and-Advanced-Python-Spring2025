# graph_utils.py

"""
CS 034 - Data Structures and Advanced Python
Project 3 - Smart Delivery Route Planner
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 23th, 2025

GitHub repo: https://github.com/jurinho17-sv/Data-Structures-and-Advanced-Python-Spring2025/tree/main/Project3-Smart-Delivery-Route-Planner
"""

"""
Graph utilities for Smart Delivery Route Planner
Handles graph construction and path-finding algorithms
"""

import csv
import heapq
from collections import deque


def main():
    """Test the graph utility functions"""
    # Build graph from sample input
    graph = build_graph('sample_input.csv')
    print("Graph structure:", graph)
    
    # Test route checking
    print("\nRoute possible from A to F?", is_route_possible(graph, 'A', 'F'))
    print("Route possible from A to Z?", is_route_possible(graph, 'A', 'Z'))
    
    # Test shortest path
    distance, path = find_shortest_path(graph, 'A', 'F')
    print(f"\nShortest path from A to F: {path} (distance: {distance})")


def build_graph(filename):
    """
    Build a graph from a CSV file containing road network data
    
    Args:
        filename (str): Path to CSV file with columns: source, destination, distance
        
    Returns:
        dict: Graph as adjacency list with distances
    """
    graph = {}
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Extract data from each row
                source = row['source']
                destination = row['destination']
                distance = int(row['distance'])
                
                # Initialize nodes if not in graph
                if source not in graph:
                    graph[source] = {}
                if destination not in graph:
                    graph[destination] = {}
                
                # Add edges (undirected graph)
                graph[source][destination] = distance
                graph[destination][source] = distance
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return {}
    
    return graph


def is_route_possible(graph, start, end):
    """
    Check if a route exists between two locations using DFS
    
    Args:
        graph (dict): Graph representation
        start (str): Starting location
        end (str): Destination location
        
    Returns:
        bool: True if route exists, False otherwise
    """
    # Check if nodes exist in graph
    if start not in graph or end not in graph:
        return False
    
    # Initialize visited set and stack for DFS
    visited = set()
    stack = [start]
    
    # Perform DFS
    while stack:
        current = stack.pop()
        
        # Found the destination
        if current == end:
            return True
        
        # Mark as visited
        visited.add(current)
        
        # Add unvisited neighbors to stack
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    # No route found
    return False


def find_shortest_path(graph, start, end):
    """
    Find shortest path between two locations using Dijkstra's algorithm
    
    Args:
        graph (dict): Graph representation
        start (str): Starting location
        end (str): Destination location
        
    Returns:
        tuple: (distance, path) where path is a list of nodes
    """
    # Check if nodes exist
    if start not in graph or end not in graph:
        return (float('inf'), [])
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Skip if already visited
        if current in visited:
            continue
            
        visited.add(current)
        
        # Found destination
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            return (distances[end], path)
        
        # Check neighbors
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            # Update if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return (float('inf'), [])


def plan_delivery(graph, depot, deliveries):
    """
    Plan optimal delivery route using greedy nearest neighbor approach
    
    Args:
        graph (dict): Graph representation
        depot (str): Starting depot location
        deliveries (list): List of delivery locations
        
    Returns:
        tuple: (total_distance, route) where route includes depot and all deliveries
    """
    # Verify all locations exist and are reachable
    for location in [depot] + deliveries:
        if location not in graph:
            return (float('inf'), [])
    
    for delivery in deliveries:
        if not is_route_possible(graph, depot, delivery):
            return (float('inf'), [])
    
    # Initialize route and unvisited deliveries
    route = [depot]
    unvisited = set(deliveries)
    current = depot
    total_distance = 0
    
    # Visit each delivery using nearest neighbor
    while unvisited:
        nearest = None
        nearest_distance = float('inf')
        
        # Find nearest unvisited delivery
        for delivery in unvisited:
            distance, _ = find_shortest_path(graph, current, delivery)
            if distance < nearest_distance:
                nearest = delivery
                nearest_distance = distance
        
        # Add nearest to route
        if nearest:
            route.append(nearest)
            total_distance += nearest_distance
            current = nearest
            unvisited.remove(nearest)
    
    return (total_distance, route)


if __name__ == "__main__":
    main()