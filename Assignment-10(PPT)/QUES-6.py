def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1

    moves = 0

    # Move n-1 disks from source to auxiliary rod
    moves += tower_of_hanoi(n - 1, source, auxiliary, destination)

    # Move the remaining largest disk from source to destination rod
    print("move disk", n, "from rod", source, "to rod", destination)
    moves += 1

    # Move the n-1 disks from auxiliary rod to destination rod
    moves += tower_of_hanoi(n - 1, auxiliary, destination, source)

    return moves

# Example usage
N = 3
total_moves = tower_of_hanoi(N, 1, 3, 2)
print(total_moves)
