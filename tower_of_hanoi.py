# ---------------------------
# Tower of Hanoi
# ---------------------------

def tower_of_hanoi(n, source, helper, destination):
    # Base case: if only 1 disk, just move it
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Step 1: Move n-1 disks from source to helper
    tower_of_hanoi(n-1, source, destination, helper)
    
    # Step 2: Move the biggest disk
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from helper to destination
    tower_of_hanoi(n-1, helper, source, destination)

# ---------------------------
# Run with 3 disks
# ---------------------------
tower_of_hanoi(3, "A", "B", "C")
