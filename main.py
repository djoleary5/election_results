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

# print output in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(voterIDs)))
print("-------------------------")