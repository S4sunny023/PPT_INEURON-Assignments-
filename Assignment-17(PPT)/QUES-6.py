def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    current = 0

    while len(friends) > 1:
        current = (current + k - 1) % len(friends)
        friends.pop(current)

    return friends[0]


print(findTheWinner(5, 2)) 
