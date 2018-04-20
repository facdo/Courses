# 56 - Demostration of the interactive dictionary
# You type an english word and have its meaning printed out
# it might identify typos in the inputed word
# it works with mixed upper and lower case

# 57 - The data source
# the vocabulay dictionary will come from a .json file
# It is simpily a dictionary file, implemented in the form {"word": ["meaning"]}
# The file is already implemented and can be downloaded in the course class page
# Some words have multiple meanings, so the meaning is actually a list
# We have to load the .json file into a python dictionary, which can be easily
# acomlished by the load method from the json library, which receives a file
# like type of variable as an input
# 58 to 62

# 62  - calculating similarity between two words
# take into consideration user mistypes
# get words that are similar
# algorithm to compare the typed word with the keys in the .json file
# we can use a standad library called difflib
# get the ratio of similarity between two strings
# the first argument is used for sequences of words, to ignore spaces and special characters
# It is not our case, so we will pass None
# we need to compare it with all the words from the dictionary
# but it already has a build in find method to get the close matches from a list
# it is called get_close_matches ant it takes as an argument the word, the list, the number
# of matches and the ratio of similarity

# 63 - Make the program suggest a similar word for words not found

# 64 - 66 -  final optimizations of the program


# additional functionalities:
# - Adding new words
# - Adding new meanings to existing words
# - Acrynom detector

import json
from difflib import get_close_matches

# load the .json file into a data variable dictionary
data = json.load(open('data_mod.json','r'))

# returns the definition of a word or prompts the user to add more words to
# the data vocabulary, or more meanings to the existing words
def main_operation(word):
    word = word.lower()
    if word in data.keys():
        return promp_add_meaning(word)
    elif len(get_close_matches(word, data.keys(), 1, 0.75))>0:
        possible_word = get_close_matches(word, data.keys(), 1, 0.75)[0]
        check = input("Did you mean %s instead? Type Y or N: " % possible_word)
        if check.lower() == "y":
            return promp_add_meaning(possible_word)
        else:
            return prompt_add_word(word)
    elif word.isnumeric():
        return "Leaving program. See you later!"
    else:
        return prompt_add_word(word)

# displays the results for searching the word and checks if the user wants to add
# more meanings
def promp_add_meaning(word):
    more_meanings_check = input(print_list(data[word])+"\n"+
                                "Do you want to add another meaning to that word?"+
                                "Type Y or N: ")
    if more_meanings_check.lower() == "y":
        meaning = input("Please type the meaning for the word %s:\n" % word)
        add_new(word, meaning)
        return "The meaning for the word %s was added to the vocabulary." % word
    else:
        return "Ok. Try a new entry.\n\n"

# check if user wants to add new word
def prompt_add_word(word):
    add_check = input("Sorry, I don't know the word that you want.\n"
                    "Do you want to add %s to the vocabulary? Type Y or N: " % word)
    if add_check.lower() == 'y':
        meaning = input("Please type a meaning for that word:\n")
        add_new(word, meaning)
        return "The word %s was added! Thank you for the contribuition :)" % word
    else:
        return "Ok. Try a new entry.\n\n"

# adds new words or append new meanings to the data.json dictionary
def add_new(word, meaning):
    if word in data.keys():
        data[word].append(meaning)
    else:
        data[word] = []
        data[word].append(meaning)
    # inputs that into the .json data file
    with open('data_mod.json', 'w') as dic:
        dic.write(json.dumps(data))

# returns a nice string made from elements of a list
def print_list(lst):
    total_string = ''
    for index, el in enumerate(lst):
        total_string += "{} - {}\n".format(index+1, el)
    return total_string

# run program in a loop, exit when the user types a number
def run_loop():
    word = ''
    while not word.isnumeric():
        word = input("Please enter an english word, or a number to leave: ")
        print(main_operation(word))

# executes the program
run_loop()
