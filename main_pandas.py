import csv
import time
import pandas as pd
import numpy as np
import os

def clear():
    os.system('cls')


def write_to_csv(name,present='empty',proxy='empty'):
    with open('day_data.csv', newline='', mode='a') as database:
        timestamp_event = time.asctime( time.localtime(time.time()) )
        csv_writer = csv.writer(database,delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
        csv_writer.writerow([timestamp_event,name,present,proxy])

def save_to_final():
    df.to_csv(r'updated_attendance.csv')


df = pd.read_csv('list.csv', index_col=[0])
# df.loc['Sandro Mizzi','present'] = 'True'
print (df)


clear()
name = input(f'\nPlease enter name :  ')
match = df[df.index.str.match(name)].index
counter = 1
for n in match:
    print (f'{counter}. {n}')
    counter +=1
choice_from_match = int(input ('Please enter number '))
name_from_choice = match[(choice_from_match-1)]


clear()
attendance_proxy_choice = int(input (f'\nWhat do you want to edit from {name_from_choice} \n1. Change attendance \n2. Fill in proxy \n3. Back\n'))
print (attendance_proxy_choice,type(attendance_proxy_choice))
print (df.loc[name_from_choice, 'present'])

if attendance_proxy_choice == 1:
    if (df.loc[name_from_choice, 'present']) == False:
        (df.loc[name_from_choice, 'present']) = True
        print(df.loc[name_from_choice, 'present'])

        write_to_csv(name_from_choice, df.loc[name_from_choice, 'present'], df.loc[name_from_choice, 'proxy'])
    elif(df.loc[name_from_choice, 'present']) == True:
        (df.loc[name_from_choice, 'present']) = False
        write_to_csv(name_from_choice, df.loc[name_from_choice, 'present'], df.loc[name_from_choice, 'proxy'])

clear()
print (df.loc[name_from_choice])
save_to_final()

