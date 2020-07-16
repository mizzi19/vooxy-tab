import csv
import time
import pandas as pd
import numpy as np

df = pd.read_csv('list.csv', index_col=[0])
df.loc['Sandro Mizzi','present'] = 'True'
print (df)



name = input(f'\nPlease enter name :  ')

match = df[df.index.str.match(name)].index
counter = 1
for n in match:
    print (f'{counter}. {n}')
    counter +=1
choice_from_match = int(input ('Please enter number '))

name_from_choice = match[(choice_from_match-1)]
(df.loc[name_from_choice,'proxy']) = 'True'

print (df)


#
# df.loc[1,'Name'] = 'a'
# df.loc[3,'present'] = True
#
# check = input ('enter name')

# match = df[df['Name'].str.contains('Sa')]
#
# print(match)
#
# selection = input ('select index')
#
#
# match.loc[selection,'proxy'] = True
#
# match.to_csv('final')
#
# # print(new)
# #print(match)
# print(df)
#
#
#
#
