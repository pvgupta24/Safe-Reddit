import pandas as pd
from sys import argv

def isToxic():
    df = pd.read_csv('ans.csv')

    s = pd.Series(df['post_id'])
    return (argv[1] in s)
