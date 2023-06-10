def print_subsets(s, current_subset, index):
    if index == len(s):
        print(current_subset)
        return

    print_subsets(s, current_subset, index + 1)  # Exclude current character
    print_subsets(s, current_subset + s[index], index + 1)  # Include current character


def print_all_subsets(s):
    print_subsets(s, "", 0)


# Test Examples
print_all_subsets("abc")
print_all_subsets("abcd")
