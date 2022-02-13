"""Generate Markov text from text files."""

from random import choice, random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read().replace("\n", " ")

    return text_string

# print(open_and_read_file("green-eggs.txt"))
    
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words)-2):
    # Looping through the words from the first word to the second-to-last word so that we don't try to make a bigram with a single word
        # To make sure we look for the subsequent word only if there is one
        key = (words[i], words[i+1])
        # Creating the bigram tuple of adjacent words
        value = words[i + 2]
        # Creating a value that represents the subsequent word of the tuple 
        if key in chains:
        # If the bigram is already in the dictionary, add the next word to the list of next words
            chains[key].append(value)
        else:
        # If the bigram isn't already in the dictionary, then create the dictionary
            chains[key] = [value]
    return chains           
                
 


def make_text(chains):
    """Return text from chains."""

    words = []

    list_of_keys = list(chains.keys())

    random_tuple = choice(list_of_keys)

    random_value = choice(chains[random_tuple])

    while random_tuple in chains.keys():
        
        if words==[]:
            words.append(random_tuple[0])
            words.append(random_tuple[1])
            words.append(random_value)
            random_tuple = (words[-2], words[-1])

        else:
            new_value = choice(chains[random_tuple])
    
            words.append(new_value)
            random_tuple = (words[-2], words[-1])

    return ' '.join(words)

# print(make_text(make_chains(open_and_read_file("green-eggs.txt"))))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
