# if its length is strictly more than 10 characters.
# write down the first and the last letter of a word 
# between them we write the number of letters between the first and the last letters

# INPUT
# First line contains an integer n (1 ≤ n ≤ 100).
# Each of the following n lines contains one word.
# All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters

# OUTPUT
# Print n lines
# The i-th line should contain the result of replacing of the i-th word from the input data

num_words = int(input())

arr_words = []

for x in range(num_words):
    arr_words.append(input())

arr_words_translated = []

for word in arr_words:
    if len(word) > 10:
        first_char = word[0]
        last_char = word[len(word) - 1]
        length_center_word = len(word) - 2
        
        arr_words_translated.append(first_char + str(length_center_word) + last_char)
    else:
        arr_words_translated.append(word)

for word in arr_words_translated:
    print(word)