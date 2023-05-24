sentence = input('Sentence: ')
words = sentence.split()

shouted = 1
for word in words:
  if word.islower():
  shouted = shouted + 1
print(f'Number of shouted words: {shouted}')
