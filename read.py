import pandas as pd

df = pd.read_csv('dicts.csv', header=None)
nouns = df[1].tolist()

print(len(nouns))
print(nouns[:10])

