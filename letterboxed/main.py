from nltk.corpus import words

# wordlist = [word.lower() for word in words.words()]
wordlist = words.words()

print(f"There are {len(wordlist)} words in the corpus")

# Setup grid
sides = []
for i in range(4):
    side = [c for c in input("Please enter side:")]
    sides.append(side)

print("The sides are ", sides)

#sides = [['i', 'l', 'p'], ['u', 'r', 'n'], ['s', 'o', 'a'], ['h', 't', 'd']]

# use possible letters to filter wordlist
from itertools import chain

letters = set("".join(chain.from_iterable(sides)))
# print(f"All letters {letters}")

# if a word has a letter not in letters, then we need to discard it from wordlist
wordlist = [word for word in wordlist if all([l in letters for l in word])]

print(f"There {len(wordlist)} words with only the appropriate letters")


# use bigrams to filter wordlist
from itertools import permutations

bad_bigrams = []
for i in range(4):
    bad_bigrams.extend(["".join(p) for p in permutations(sides[i], 2)])
    
# print(f"Bad bigrams are {bad_bigrams}")

wordlist = [word for word in wordlist if not any([bbg in word for bbg in bad_bigrams])]

print(f"There are {len(wordlist)} words with appropriate bigrams")

# for each word left, work through the algorithm 
wordlist.sort(key=lambda x: len(set(x)), reverse=True)

possible_solutions = 0
solved = False
for word in wordlist:
    letters_needed = letters.difference(set(word))
    starting_letter = word[-1]
    possible_solves = [word for word in wordlist if word.startswith(starting_letter) and all([l in word for l in letters_needed])]
    if possible_solves:
        print(f"A solution is {word}-{possible_solves[0]}")
        possible_solutions += 1

print(f"Found {possible_solutions-1} other possible 2-word solutions")
    

# print("Now tell me the starting letter and the letters you need")
# starting_letter = input("What is the starting letter of the next word: ")
# other_letters = [l for l in input("What are the other letters you need: ")]

# wordlist = [word for word in wordlist if word.startswith(starting_letter) and all([l in word for l in other_letters])]
# print(f"Any of these {len(wordlist)} words should finish the job:")
# print(wordlist)