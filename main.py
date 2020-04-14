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

