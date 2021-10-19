sentence = input('Enter your sentence to count the words: ').strip()

word_counter = 1
for char in sentence:
    if char == ' ':
        word_counter += 1
        
print('Number of your Words: ', word_counter)