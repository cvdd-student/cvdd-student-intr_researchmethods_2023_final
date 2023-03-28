# File name: analyse_pronoun_data.py
# Function: Prints the pronoun data of Dutch text files,
# specifically those provided in list_filepaths_data.txt.
# Specifically, it returns the frequency of both overall pronouns
# as well as first person pronouns (ik, mij, mijn, me).
# Author: C. Van der Deen, s4092597
# Date: 20-03-2023

import sys


def detect_fpp(filepath, flag_detailed_mode):
    '''Tokenises previously prepared text and prints the amount of times
    "ik", "mij", "mijn" or "me" appears in said text.
    If flag_detailed_mode is set to true, it also prints which lines in the
    text caused the counters to increase.'''
    accum_line = 0
    counter_ik = 0
    set_ik = set()
    counter_mij = 0
    set_mij = set()
    counter_mijn = 0
    set_mijn = set()
    counter_me = 0
    set_me = set()
    for line in filepath:
        accum_line += 1
        list_tokens = line.split(" ")
        for token in list_tokens:
            if token == "ik":
                set_ik.add(accum_line)
                counter_ik += 1
            if token == "mij":
                set_mij.add(accum_line)
                counter_mij += 1
            if token == "mijn":
                set_mijn.add(accum_line)
                counter_mijn += 1
            if token == "me":
                set_me.add(accum_line)
                counter_me += 1
    print("Amount of 'ik':", counter_ik)
    print("Amount of 'mij':", counter_mij)
    print("Amount of 'mijn':", counter_mijn)
    print("Amount of 'me':", counter_me)
    counter_fpp_total = counter_ik + counter_mij + counter_mijn + counter_me
    print("Overall amount of first person pronouns:", counter_fpp_total)
    if flag_detailed_mode is True:
        print("\nLines containing 'ik':", set_ik)
        print("\nLines containing 'mij':", set_mij)
        print("\nLines containing 'mijn':", set_mijn)
        print("\nLines containing 'me':", set_me)


def count_pronouns_and_tokens(filepath):
    '''Tokenises previously prepared text and prints the amount of times
    a Dutch pronoun appears in said text. The exact pronouns that were counted
    are specified in the list_pronouns.txt file.'''
    counter_pronouns = 0
    counter_tokens = 0
    set_pronouns = set()
    list_skippable_tokens = ["-", "\n"]
    with open("list_pronouns.txt", 'r') as file_pronouns:
        for item in file_pronouns:
            set_pronouns.add(item[0:-1])
    for line in filepath:
        list_tokens = line.split(" ")
        for token in list_tokens:
            if token not in list_skippable_tokens:
                counter_tokens += 1
            if token in set_pronouns:
                counter_pronouns += 1
    print("Overall amount of pronouns:", counter_pronouns)
    print("Overall amount of tokens:", counter_tokens)
    perc_pronouns = counter_pronouns / counter_tokens * 100
    print("Percentage of pronouns in tokens:", perc_pronouns)


def display_all_pronoun_data(filepath, flag_detailed_mode):
    '''Takes a text file as input, and runs detect_fpp() and
    count_pronouns_and_tokens(), making sure everything prints
    neatly.'''
    print("---------- Pronoun data for", filepath[0:-1], "----------\n")
    with open(filepath[0:-1], 'r') as data:
        detect_fpp(data, flag_detailed_mode)
    print("")
    with open(filepath[0:-1], 'r') as data:
        count_pronouns_and_tokens(data)
    print("")


def main():
    path_list_filepaths = sys.argv[1]
    with open(path_list_filepaths, 'r') as filepaths:
        for line in filepaths:
            display_all_pronoun_data(line, eval(sys.argv[2]))


if __name__ == "__main__":
    main()
