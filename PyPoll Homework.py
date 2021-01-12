#!/usr/bin/env python
# coding: utf-8

# In[118]:


#import budget data
import os 
import csv


# In[119]:


#create a path
csvpath=os.path.join("..","Resources","election_data.csv")


# In[120]:


#Create list to store data 
number_votes=0
candidate_list=[]
vote_count={}
vote_percent=[]

#to open the file
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csvheader=next(csvreader)
    
#total votes cast    
    for row in csvreader:
        
        #vote count 
        number_votes+=1
        
        #pull candidate from list 
        candidate=(row[2])
        
        if candidate in candidate_list:
            #candidate_index=candidate_list.index(candidate)
            vote_count[candidate]=vote_count[candidate]+1
        
        else:
            candidate_list.append(candidate)
            vote_count[candidate]=1
        
#finding percentage votes

percentage=[]
highest_votes = 0
winner=""


for i in range(len(candidate_list)):
    candidate=candidate_list[i]
    votes=vote_count.get(candidate)
    vote_percentage=round(votes/number_votes*100,2)
    percentage.append(vote_percentage)
    if highest_votes<votes:
        highest_votes=votes
        winner=candidate
print(highest_votes,winner,percentage)

     

    
    


# In[128]:


with open("Output.txt","w") as txt:
    output=(f"Election Results\n"
           f"-------------------------\n"
            f"Total Votes: {str(number_votes)}\n"
            f"-------------------------\n"
           )
    print(output)
    txt.write(output)
    for i in range(len(candidate_list)):
        output1=f"{candidate_list[i]}: {str(percentage[i])}% ({str(vote_count[candidate_list[i]])})\n"
        print(f"{candidate_list[i]}: {str(percentage[i])}% ({str(vote_count[candidate_list[i]])})")
        txt.write(output1)
    output2=(f"-------------------------\n"
             f"Winner: {winner}\n"
             f"-------------------------")
    txt.write(output2)
    print(output2)
    
        
        
            

