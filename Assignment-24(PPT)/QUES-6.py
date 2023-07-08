from collections import Counter

def top_k_frequent_words(words, k):
    word_count = Counter(words)

    def compare_words(word1, word2):
        count1 = word_count[word1]
        count2 = word_count[word2]
        if count1 == count2:
            return -1 if word1 < word2 else 1
        return count2 - count1

    return sorted(word_count.keys(), key=compare_words)[:k]

print(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2))


print(top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))

