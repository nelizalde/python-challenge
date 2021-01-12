#!/usr/bin/env python
# coding: utf-8

# In[33]:


#import budget data
import os 
import csv

#create path
csvpath=os.path.join('Homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv')

#to open the file
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csvheader=next(csvreader)
    firstrow=next(csvreader)
    previousmonth=int(firstrow[1])
    
#Lists to store data 
    total_months=[]
    total_net=[]
    change=[]
    greatestprofit=0
    greatestmonth=""
    greatestloss=0
    monthloss=""

#append total months and net
    for row in csvreader:
        total_months.append(row[0])
        total_net.append(int(row[1]))
        profitchange=int(row[1])-previousmonth
        change.append(profitchange)
        
        if profitchange > greatestprofit:
            greatestprofit=profitchange
            greatestmonth=row[0]
            
        if profitchange<greatestloss:
            greatestloss=profitchange
            monthloss=row[0]
        
        previousmonth=int(row[1])
        
#average change

average=round(sum(change)/len(change),2)

output=(f"Financial Analysis\n"

#print statements
f"--------------------------\n"
f"total Months: {len(total_months)+1}\n"
f"Total: ${sum(total_net)+int(firstrow[1])}\n"
f"Average  Change: ${average}\n"
f"Greatest Increase in Profits: {greatestmonth} (${greatestprofit})\n"
f"Greatest Decrease in Profits: {monthloss} (${greatestloss})")

print(output)

with open ("output.txt","w") as txtfile:
    txtfile.write(output)





