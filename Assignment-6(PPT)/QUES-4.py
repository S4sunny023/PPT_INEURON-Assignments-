def reverseWords(s):
    words = s.split()
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


s = "Let's take LeetCode contest"
print(reverseWords(s))  