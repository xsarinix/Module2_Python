import os
import csv
csvpath="cereal.csv"
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvpath, delimiter=',')
    for row in csvreader.readlines():
        next(csvreader,None) if row == 1 else print(csvreader)