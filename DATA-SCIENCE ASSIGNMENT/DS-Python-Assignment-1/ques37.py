def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence






input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(input_sentence)
print("Reversed sentence:", reversed_sentence)
