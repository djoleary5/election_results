# Dennis O'Leary
# Election Results

import os
import csv

# input file path
csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data
voterIDs = []
candidates = []
voteCounts = []

# set initial values
i = 0
j = 0
k = 0
win = 0

# open input file, remove header row and loop through the remaining rows
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # add each voter ID to list 'voterIDs'; it's length is the total number of votes
        voterIDs.append(row[0])
        # add the candidate for each vote to a list
        candidates.append(row[2])

# remove duplicates from candidate list
candidates = list( dict.fromkeys(candidates))

#loop through candidates list 
while i < (len(candidates)):
    # open input file, remove header row and loops through the remaining rows
    with open(csvpath, newline= "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        voteCnt = 0
        for row in csvreader:
            # count the number of votes for each candidate
            if candidates[i] == row[2]:
                voteCnt = voteCnt + 1
    # add vote count for each cadidate to list            
    voteCounts.append(voteCnt)
    i = i + 1

# print output in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(voterIDs)))
print("-------------------------")
# loop and print results for each canditate and stores the index of the highest vote count
while j < (len(candidates)):
    if voteCounts[j] > win:
        win = voteCounts[j]
        winCand = j
    pct = ((voteCounts[j])/(sum(voteCounts)))*100
    pct = round(pct, 2)
    print(candidates[j] + ": " + str(pct) + "%  (" + str(voteCounts[j]) + ")")
    j = j + 1
print("-------------------------")
# uses the index of the highest vote count to return the name of the winning candidate
print("Winner:  " + candidates[winCand])
print("-------------------------")