import os
import csv
csvpath=os.path.join('netflix_ratings.csv')
with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    title=input("Which movie do you want to watch? ")
    for row in csvreader:
        if title==
'''
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
'''
