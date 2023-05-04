# get fib sequence

# nterms = int(input("How many terms? (Please input a number >= 1) ")) # takes too much time when running

nterms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < nterms:
#   print(n1)
   nth = n1 + n2
   n1 = n2
   n2 = nth
   count += 1

# the number of syllables in each line: 5, 8, 13, 21, 34, 21, 13, 8

# count the pronouncing
import pronouncing

word = str(input("Please input a word which have you favourite pronounce!!"))

pronunciation_list = pronouncing.phones_for_word(word)
pronouncing.syllable_count(pronunciation_list[0])

import sys
!{sys.executable} -m pip install pronouncing

import pronouncing as pr 
import random

wordPr = pr.phones_for_word(word) [0] # output a string
#print(wordPr)

words1 = pr.search(wordPr)
words2 = pr.search(wordPr + "$")
words3 = pr.search("^" + wordPr)

# My initial idea was just using similar words that satisfy above conditions; 
# however, for some words, there are only 2-3 words in the list, thus I add a pronouncing stress similar condition

phones_list = pronouncing.phones_for_word(word)
prStress = pronouncing.stresses(phones_list[0])
words4 = pronouncing.search_stresses("0101")

words = [*words1, *words2, *words3, *words4] # words: list
#words = [*words1, *words2, *words3]

# print(words)

# count the syllable of the words with similar pronouncing
all_phones = []
for item in words:
    phone_list = pr.phones_for_word(item)
    phones = phone_list[0]
#    print(item, phones.split(), pronouncing.syllable_count(phone_list[0]))
    all_phones.extend(phones.split())

text_a = open("Jorge Luis Borges: Selected Poems.txt").read()
text_b = ' '.join(words)

import sys
!{sys.executable} -m pip install markovify

import markovify
generator_a = markovify.Text(text_a, well_formed=False, state_size=3)
generator_b = markovify.Text(text_b, well_formed=False, state_size=3) 
combo = markovify.combine([generator_a, generator_b], [0.1, 0.9])

for i in range(8):
    print(combo.make_sentence())