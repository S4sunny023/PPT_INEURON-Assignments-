def permutations(string):
    # Convert the string to a list of characters
    chars = list(string)
    n = len(chars)

    # Helper function to swap characters at two indices
    def swap(i, j):
        chars[i], chars[j] = chars[j], chars[i]

    # Recursive function to generate permutations
    def generate_permutations(start):
        if start == n - 1:
            # Base case: reached the last character, so we have a permutation
            print(''.join(chars))
        else:
            # Recursive case: generate permutations by swapping characters
            for i in range(start, n):
                swap(start, i)
                generate_permutations(start + 1)
                swap(start, i)  # Backtrack

    # Start generating permutations from the first character
    generate_permutations(0)

# Example usage
str = "cd"
permutations(str)
