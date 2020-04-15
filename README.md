# election_results
Created a python script for analyzing election results.

## Data
A set of poll data called [election_data.csv](election_results/Resources/election_data.csv), which is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

## Steps Taken
* Calculated the total number of votes cast by adding each Voter ID to a list `voterIDs` and finding the length of the list.
* Created a list `candidates` of candidates that recieved votes by adding the `Candidate` value for each vote to a list and finding the unique elements of the list.
* Calculated the number of votes for each candidate and added these totals to a list `voteCnt`.
