# This folder contains all necessary scripts to create and analyse the dataset used in this study.

## All of these scripts are controlled by the three main scripts:
1. create\_dataset.py
2. analyse\_pronoun\_data.py
3. generate\_analysis\_csv.py
4. visualise\_data.py

## create_dataset.py
### Usage:
> python3 create_dataset.py [length]

### Dependencies:
- remove_extraneous_info.py
- clean_up_data.py

### Description:

This script converts the raw dataset to a pre-processed one that can be analysed by the other scripts. It removes non-Dutch tweets, removes language tags and remove undesired data.

This script relies on the 'list_filepaths_data_raw.txt' file to tell it which files it needs to read as input, which have to be in a 'Dataset_Raw' folder. It will automatically put the output files into the 'Dataset' folder (which has to be made beforehand).

The [length] parameter determines how many lines will the output.

## analyse_pronoun_data.py
### Usage:
> python3 analyse_pronoun_data.py [list_filepaths] [detailed_mode]

### Description:

This script prints a full pronoun analysis of every file in the processed dataset. Counting first person pronouns, overall pronouns and tokens.

The [list_filepaths] parameter is meant for 'list_filepaths_data.txt', which contains the filepaths to the processed dataset created by 'create_dataset.py'.

The [detailed_mode] parameter determines whether or not the output text will contain a list of lines that contain the detected FPSPs. It can either be True or False.

This script relies on 'list_pronouns.txt', which contains all the pronouns that the script checks for for its overall pronoun detection.

## generate_analysis_csv.py
### Usage:
> python3 generate_analysis_csv.py [list_filepaths]

### Description:

This script does the same as 'analyse_pronoun_data.py', but formats it as a .csv file instead.

The [list_filepaths] parameter is meant for 'list_filepaths_data.txt', which contains the filepaths to the processed dataset created by 'create_dataset.py'.

This script relies on 'list_pronouns.txt', which contains all the pronouns that the script checks for for its overall pronoun detection.

## visualise_data.py
### Usage:
> python3 visualise_data.py [data_csv]

### Description:

This script plots the .csv file created by 'generate_analysis_csv.py'.

The [data_csv] parameter is meant for the .csv file created by 'generate_analysis_csv.py'.

Note: This script makes use of Pandas.
