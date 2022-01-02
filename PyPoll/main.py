#import libraries
import csv
import os

#read file and make calculations
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #reads the head row first
    total_number_votes = 0
    list_names_candidates = []
    list_percentage_votes = []
    list_number_votes = []
    for row in csvreader:

#select winner
winner = list_names_candidates[0]
for i in range(len(list_percentage_votes)-1):
    if list_percentage_votes[i+1] > list_number_votes[i]:
        winner = list_names_candidates[i+1]

#Print to the terminal
print("Election Results")
print("--------------------")
print("Total Votes: {}".format(total_number_votes))
print("--------------------")
for i in range(len(list_names_candidates))
    print("%s: %.3f%% (%d)\n" % (list_names_candidates[i],list_percentage_votes[i], list_number_votes[i]))
print("--------------------")
print("Winner: {}",.format(winner))
print("--------------------")

#Export a text file with the results