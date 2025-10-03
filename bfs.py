# ---------------------------
# Breadth First Search (BFS)
# ---------------------------

def bfs_traverse(graph, start):
    visited = set()        # to keep track of visited nodes
    queue = []             # queue to process nodes
    order = []             # to store the BFS order

    print("Starting BFS from:", start)

    # Step 1: mark start as visited + put in queue
    visited.add(start)
    queue.append(start)
    print("Visited:", visited)
    print("Queue:", queue)

    # Step 2: keep running until queue is empty
    while len(queue) > 0:
        # take the first node from queue
        node = queue.pop(0)
        print("\nDequeued:", node)

        # visit the node
        order.append(node)
        print("Order so far:", order)

        # check its neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # mark visited
                queue.append(neighbor)     # enqueue
                print("  Added neighbor:", neighbor)
                print("  Visited now:", visited)
                print("  Queue now:", queue)

    print("\nFinal BFS Order:", order)
    return order


# ---------------------------
# Example Graph
# ---------------------------
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# ---------------------------
# Run BFS
# ---------------------------
bfs_traverse(graph, "A")
