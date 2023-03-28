# File name: clean_up_data.py
# Function: Take a tab-separated .TXT file as input
# containing the language and text of a Tweet, then
# filter for Dutch Tweets, remove the language tag,
# and finally print 500 random Tweets.
# NOTE: For the sake of reproducable research, the RNG
# seed was set to 2597.
# Author: C. Van der Deen, s4092597
# Date: 14-03-2023

import sys
from random import *


def clean_up(txt_import, str_lang, int_output_length):
    '''Callable version of main() for use in other scripts.'''
    seed(2597)
    text_process = lines_filter_language(txt_import, str_lang)
    return randomise_and_cut_down(text_process, int_output_length)


def randomise_and_cut_down(str_input, desired_length):
    '''Takes a text input and return a certain amount
    of randomised lines from it, the amount specified by
    desired_length.'''
    str_new = ""
    list_input = str_input.split("\n")
    list_output = []
    list_rng_numbers = []
    while desired_length != 0:
        rng_int = randrange(len(list_input))
        if rng_int not in list_rng_numbers:
            list_rng_numbers += [rng_int]
            desired_length = desired_length - 1
    for entry in list_rng_numbers:
        str_new += list_input[entry]
        if entry != list_rng_numbers[-1]:
            str_new += "\n"
    return str_new


def lines_filter_language(file_data, str_language):
    '''Filter a language tag from a text input for language
    specified through str_language, then remove that tag and
    return the filtered string.'''
    str_cleaned_text = ""
    for line in file_data:
        if line[0:2] == str_language:
            str_cleaned_text += line[3:]
    return str_cleaned_text


def main():
    seed(2597)
    path_import = sys.argv[1]
    lines_processed = ""
    with open(path_import, 'r') as data:
        lines_processed = lines_filter_language(data, "nl")
    print(randomise_and_cut_down(lines_processed, 500))


if __name__ == "__main__":
    main()
