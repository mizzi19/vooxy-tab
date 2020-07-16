import csv
import time
import pandas as pd
import numpy as np

def find_the_correct(name):
    with open('list.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        count = 1
        name_matches = []

        for row in reader:
            if name in row[1]:
                print(count, row[1:])
                name_matches.append(row)
                count += 1
    number_match = int(input (f' there are {(count-1)} matches, please choose one : '))
    choice = (name_matches[(number_match-1)])
    choice_data = choice
    print (choice [1:2])
    return choice_data


def write_to_csv(data,present='empty',proxy='empty'):
    with open('day_data.csv', newline='', mode='a') as database:
        timestamp_event = time.asctime( time.localtime(time.time()) )
        name = data[1]

        csv_writer = csv.writer(database,delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
        csv_writer.writerow([timestamp_event,name,present,proxy])




name = input('Enter Name or part thereof :  ')

choice_data = find_the_correct(name)
edit_choice = int(input (f' what do you want to modify? \n 1. Attendance \n 2. Proxy \n'))

if edit_choice==1:
    present = input(f'Is {choice_data[1]} present? ')
    proxy =''
    write_to_csv(choice_data, present, proxy)
elif edit_choice==2:
    proxy = input(f'did you leave a proxy?')
    write_to_csv(choice_data, choice_data[3], proxy)