sentence = input('Sentence: ')
words = sentence.split()

shouted = 0
for word in words:
  if word.isupper():
    shouted = shouted + 1
print(f'Number of shouted words: {shouted}')
