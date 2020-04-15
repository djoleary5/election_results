# election_results
Created a python script for analyzing election results.

## Data
A set of poll data called [election_data.csv](election_results/Resources/election_data.csv), which is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

## Steps Taken
* Calculated the total number of votes cast by adding each Voter ID to a list `voterIDs` and finding the length of the list.
* Created a list `candidates` of candidates that recieved votes by adding the `Candidate` value for each vote to a list and finding the unique elements of the list.
* Calculated the number of votes for each candidate and added these totals to a list `voteCnt`.
* Calcuated the percentage of the votes won by each candidate along with the name of the winning candidate.
* Printed the output in the terminal:
    ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
* Created a text file [output.txt](output.txt) and wrote the output into the file. 
