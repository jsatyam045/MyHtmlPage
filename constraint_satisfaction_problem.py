import itertools

# Variables (regions on the map)
variables = ["A", "B", "C"]

# Colors available
colors = ["Red", "Blue", "Yellow"]

# Generate all possible assignments (Cartesian product)
all_assignments = itertools.product(colors, repeat=len(variables))

# Function to check constraints
def is_valid(assignment):
    A, B, C = assignment  # unpack the tuple
    if A == B:   # A and B must be different
        return False
    if B == C:   # B and C must be different
        return False
    if A == C:   # A and C must be different
        return False
    return True

# Print valid solutions
for assignment in all_assignments:
    if is_valid(assignment):
        solution = dict(zip(variables, assignment))
        print("Valid coloring of the map:", solution)
