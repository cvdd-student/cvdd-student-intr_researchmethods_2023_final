# File name: generate_analysis_csv.py
# Function:
# Author: C. Van der Deen, s4092597
# Date: 20-03-2023

import sys


def detect_fpp(filepath):
    '''Tokenises previously prepared text and prints the amount of times
    "ik", "mij", "mijn" or "me" appears in said text.
    If flag_detailed_mode is set to true, it also prints which lines in the
    text caused the counters to increase.'''
    accum_line = 0
    counter_ik = 0
    counter_mij = 0
    counter_mijn = 0
    counter_me = 0
    for line in filepath:
        list_tokens = line.split(" ")
        for token in list_tokens:
            if token == "ik":
                counter_ik += 1
            if token == "mij":
                counter_mij += 1
            if token == "mijn":
                counter_mijn += 1
            if token == "me":
                counter_me += 1
            accum_line += 1
    counter_fpp_total = counter_ik + counter_mij + counter_mijn + counter_me
    str_csv_formatted = str(counter_ik) + ","
    str_csv_formatted += str(counter_mij) + ","
    str_csv_formatted += str(counter_mijn) + ","
    str_csv_formatted += str(counter_me) + ","
    str_csv_formatted += str(counter_fpp_total) + ","
    return str_csv_formatted


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
    str_csv_formatted = str(counter_pronouns) + ","
    str_csv_formatted += str(counter_tokens)
    return str_csv_formatted


def main():
    flag_first_line_passed = False
    str_csv_out = "year,amt_ik,amt_mij,amt_mijn,amt_me,amt_fpp,"
    str_csv_out += "amt_pronoun,amt_token\n"
    path_list_filepaths = sys.argv[1]
    with open(path_list_filepaths, 'r') as filepaths:
        for line in filepaths:
            if flag_first_line_passed is True:
                str_csv_out += "\n"
            str_csv_out += line[-9:-5]
            str_csv_out += ","
            with open(line[:-1], 'r') as file_tweets:
                str_csv_out += detect_fpp(file_tweets)
            with open(line[:-1], 'r') as file_tweets:
                str_csv_out += count_pronouns_and_tokens(file_tweets)
            flag_first_line_passed = True
    print(str_csv_out)


main()
