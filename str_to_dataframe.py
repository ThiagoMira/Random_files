import csv

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd

with open('file.csv', 'r') as csv_file:
    file = csv_file.read()

DATA = StringIO(file)

df = pd.read_csv(DATA, sep=",")

print(df.head())
