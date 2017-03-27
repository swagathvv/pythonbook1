from downey_anagram import *
import shelve

def store_anagrams(filename, anagram_file):
    anagram_dict = all_anagrams(anagram_file)
    anagram_shelve = shelve.open(filename)

    for key in anagram_dict.keys():
        anagram_shelve[key] = anagram_dict[key]

    anagram_shelve.close()


def read_anagrams(filename, a_word):
    anagram_shelve = shelve.open(filename)

    sig = signature(a_word)
    return anagram_shelve[sig]
