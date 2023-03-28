# File name: create_dataset.py
# Function: Concatenation of clean_up_data.py and remove_extraneous_info.py
# to allow batch functionality. It creates an output for every file specified
# in list_filepaths_data_raw.txt and stores those outputs in the Dataset folder.
# Also creates list_filepaths_data.txt for use in analyse_pronoun_data.py.
# Finally, the length of the output files can be determined through sys.argv[1].
# Author: C. Van der Deen, s4092597
# Date: 20-03-2023

import sys
from remove_extraneous_info import *


def main():
    list_output_filepaths = []
    with open("list_filepaths_data_raw.txt", 'r') as filepaths_data_raw:
        for filepath_raw in filepaths_data_raw:
            filepath_out = "../Dataset/" + filepath_raw[-9:-1]
            text_output = remove_extraneous_info(filepath_raw[:-1], int(sys.argv[1]))
            with open(filepath_out, 'w') as filepath_output:
                print(text_output, file=filepath_output)
            list_output_filepaths += [filepath_out]
    with open("list_filepaths_data.txt", 'w') as output_filepaths_holder:
        for item in list_output_filepaths:
            print(item, file=output_filepaths_holder)


if __name__ == "__main__":
    main()
