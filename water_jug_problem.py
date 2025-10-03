# ---------------------------
# Water Jug Problem using BFS
# ---------------------------

from collections import deque

def water_jug(x_cap, y_cap, target):
    # Start state (both jugs empty)
    start = (0, 0)

    # Queue for BFS
    queue = deque([start])

    # Visited states to avoid repeating
    visited = set([start])

    print("Starting BFS to solve Water Jug Problem")
    print("Jug capacities:", x_cap, "and", y_cap, "Target:", target)
    print()

    while queue:
        (x, y) = queue.popleft()
        print("Current state:", (x, y))

        # Check goal
        if x == target or y == target:
            print("\nReached target state:", (x, y))
            return True

        # All possible next moves
        possible_states = [
            (x_cap, y),        # Fill X
            (x, y_cap),        # Fill Y
            (0, y),            # Empty X
            (x, 0),            # Empty Y
            # Pour X → Y
            (max(0, x - (y_cap - y)), min(y_cap, y + x)),
            # Pour Y → X
            (min(x_cap, x + y), max(0, y - (x_cap - x)))
        ]

        # Process each possible state
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                print("  Adding new state:", state)

    print("\nNo solution found!")
    return False


# ---------------------------
# Run Example
# ---------------------------
water_jug(4, 3, 2)
