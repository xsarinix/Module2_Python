import csv
from decimal import Decimal
budget_path="budget_data.csv"
with open(budget_path, newline="") as budget_data:
    budget_reader=csv.reader(budget_data, delimiter=",")
    pl_list=[]
    mon_list=[]
    end=[]
    start=[]
    next(budget_reader,None)
    for row in budget_reader:
        pl_conv=int(row[1])
        pl_list.append(pl_conv)
        end.append(pl_conv)
        start.append(pl_conv)
        mon_list.append(row[0])
    months=len(mon_list)
    total_net=sum(pl_list)
    max_pl=max(pl_list)
    min_pl=min(pl_list)
    max_mon=mon_list[pl_list.index(max_pl)]
    min_mon=mon_list[pl_list.index(min_pl)]
end.pop(0)
last_index=len(pl_list)-1
start.pop(last_index)
total_change=sum(end)-sum(start)
avg_change=round(Decimal(total_change/last_index),2)
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_net}")     
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_mon} (${max_pl})")
print(f"Greatest Decrease in Profits: {min_mon} (${min_pl})")  
output=open("budget_output.txt","w+")
output.write("Financial Analysis")
output.write("\n")
output.write("--------------------------------")
output.write("\n")
output.write(f"Total Months: {months}")
output.write("\n")
output.write(f"Total: ${total_net}")
output.write("\n")
output.write(f"Average Change: ${avg_change}")
output.write("\n")
output.write(f"Greatest Increase in Profits: {max_mon} (${max_pl})")
output.write("\n")
output.write(f"Greatest Decrease in Profits: {min_mon} (${min_pl})")
output.close()