# main.py

"""
Smart Delivery Route Planner - Main Program

CS 034 - Data Structures and Advanced Python
Project 3 - Smart Delivery Route Planner
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 23th, 2025

GitHub repo:
"""

from graph_utils import build_graph, is_route_possible, find_shortest_path, plan_delivery


def main():
    """Main program for Smart Delivery Route Planner"""
    print("=" * 50)
    print("   SMART DELIVERY ROUTE PLANNER")
    print("=" * 50)
    
    # Load road network
    filename = input("Enter road network file (default: sample_input.csv): ").strip()
    if not filename:
        filename = "sample_input.csv"
    
    print(f"\nLoading road network from {filename}...")
    graph = build_graph(filename)
    
    if not graph:
        print("Failed to load road network. Exiting.")
        return
    
    print(f"Successfully loaded {len(graph)} locations")
    print(f"Locations: {', '.join(sorted(graph.keys()))}")
    
    # Get depot location
    while True:
        depot = input("\nEnter depot location: ").strip().upper()
        if depot in graph:
            break
        print(f"Error: '{depot}' not found in network. Please try again.")
    
    # Get delivery locations
    while True:
        deliveries_input = input("Enter delivery stops (comma separated): ").strip().upper()
        deliveries = [loc.strip() for loc in deliveries_input.split(',')]
        
        # Validate all locations exist
        invalid = [loc for loc in deliveries if loc not in graph]
        if not invalid:
            break
        print(f"Error: Invalid locations: {', '.join(invalid)}. Please try again.")
    
    # Plan delivery route
    print("\nCalculating optimal route...")
    total_distance, route = plan_delivery(graph, depot, deliveries)
    
    if total_distance == float('inf'):
        print("Error: Unable to find a valid route to all deliveries.")
        return
    
    # Display results
    print("\n" + "=" * 50)
    print("DELIVERY PLAN")
    print("=" * 50)
    
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        distance, path = find_shortest_path(graph, start, end)
        print(f"{i + 1}. {start} → {end} ({distance} km)")
    
    print(f"\nTotal distance: {total_distance} km")
    print("=" * 50)


if __name__ == "__main__":
    main()