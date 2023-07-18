def reversed_sentence(sentence):
    words = sentence.split()
    reversed= words[::-1]
    reversed_sentence = ' '.join(reversed)
    return reversed_sentence 



sentence = 'i am a boy'
print(reversed_sentence(sentence=sentence))