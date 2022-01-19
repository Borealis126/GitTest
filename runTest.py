import pandas as pd
import numpy as np

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
ages = list(range(10,15,1))
genders = ['M','F','F','M','F']
BabyDataSet = list(zip(names, ages, genders))
print(BabyDataSet)
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births', 'Genders'])

# print(df)
# print(df['Names'])
# print(df.Names)
# print(df[['Names', 'Genders']])
# print(df.iloc[0]) #Integer location
# for index, row in df.iterrows():
#     print(index, row['Name'])
print(df.loc[df['Genders'] == "M"])
# print(df.sort_values(['Births'], ascending=False))
# print(df['Births'])