import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv(sys.argv[1], index_col='year', low_memory=False)
    df = df.sort_values(by=['year'], ascending =True)
    df['perc_ik'] = df['amt_ik'] / df['amt_pronoun'] * 100
    df['perc_mij'] = df['amt_mij'] / df['amt_pronoun'] * 100
    df['perc_mijn'] = df['amt_mijn'] / df['amt_pronoun'] * 100
    df['perc_me'] = df['amt_me'] / df['amt_pronoun'] * 100
    plt.plot(df['perc_ik'], label="Percentage 'ik'")
    plt.plot(df['perc_mij'], label="Percentage 'mij'")
    plt.plot(df['perc_mijn'], label="Percentage 'mijn'")
    plt.plot(df['perc_me'], label="Percentage 'me'")
    plt.xlabel("Year")
    plt.ylabel("Percentage within overall pronouns")
    plt.legend()
    plt.show()
    print(df)


main()
