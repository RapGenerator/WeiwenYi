
import pandas as pd

data = pd.read_csv('data/data.csv', header=-1)
data.columns=['lyrics','class']

for name, group in data.groupby('class'):
        # print (name)
        # print (group)
        group.to_csv('data/class/%s.csv'%(name))