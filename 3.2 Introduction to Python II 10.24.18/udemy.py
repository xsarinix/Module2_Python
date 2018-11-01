import csv
import pandas
csvpath=web_starter.csv
colnames=[]
title=[]
price=[]
sub_count=[]
review_num=[]
length=[]
with open('web_starter.csv', newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=","
    for line in csvreader.readlines():
        array=line.split(',')
        first_item=array[0]
    num_columns=len(array)
