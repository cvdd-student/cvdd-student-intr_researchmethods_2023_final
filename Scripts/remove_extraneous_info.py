# File name: remove_extraneous_info.py
# Function: Takes a file containing lines of text,
# uses clean_up_data.py to clean it, removes
# mentions, links and unwanted characters from the lines
# and finally make all letter lowercase.
# Author: C. Van der Deen, s4092597
# Date: 20-03-2023

import sys
from random import *
from clean_up_data import *


def upper_to_lower(str_input):
    '''Changes all uppercase characters into
    lowercase character for a given string.'''
    str_output = ""
    chars_lower = "abcdefghijklmnopqrstuvwxyz"
    chars_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in str_input:
        char_to_add = ""
        if char in chars_upper:
            for i in range(len(chars_upper)):
                if char == chars_upper[i]:
                    char_to_add = chars_lower[i]
        else:
            char_to_add = char
        str_output += char_to_add
    return str_output


def remove_mentions_and_links(str_input):
    '''Tokenises a given string input and removes
    any Twitter mentions, links and Retweet markers.'''
    str_output = ""
    list_lines = str_input.split("\n")
    for line in list_lines:
        str_building_line = ""
        list_tokens = line.split(" ")
        for token in list_tokens:
            if "@" not in token:
                if "http" not in token:
                    if token != "":
                        if token != "RT":
                            str_building_line += token
                            str_building_line += " "
        str_output += str_building_line[0:-1]
        if line != list_lines[-1]:
            str_output += "\n"
    return str_output


def remove_unwanted_characters(str_input):
    '''Removes any character from a string that is not
    specified in the desired_characters string, then 
    returns the result.'''
    desired_characters = "-0123456789@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \n"
    str_output = ""
    for char in str_input:
        if char in desired_characters:
            str_output += char
    return str_output


def remove_extraneous_info(path_input, len_desired):
    '''Callable version of main() for use in other scripts.'''
    str_input_data = ""
    with open(path_input, 'r') as data:
        str_input_data = clean_up(data, "nl", len_desired)
    str_input_data = remove_unwanted_characters(str_input_data)
    str_input_data = remove_mentions_and_links(str_input_data)
    return upper_to_lower(str_input_data)


def main():
    str_input_data = ""
    with open(sys.argv[1], 'r') as data:
        str_input_data = clean_up(data, "nl", int(sys.argv[2]))
    str_input_data = remove_unwanted_characters(str_input_data)
    str_input_data = remove_mentions_and_links(str_input_data)
    print(upper_to_lower(str_input_data))


if __name__ == "__main__":
    main()
