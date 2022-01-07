#import libraries
import csv
import os

#read file and make calculations
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #reads the head row first
    total_number_votes = 0 #variable that holds total number of votes
    dict_candidates = {} #dictionary for the candidates and their number of votes
    for row in csvreader:
        name = row[2]
        total_number_votes += 1
        if name in dict_candidates: #if candidate is already in the list, increase their number of votes
            dict_candidates[name] += 1
        else: #if candidate is not in the list, then add candidate
            dict_candidates[name] = 1

#select winner
winner_votes = 0
for key in dict_candidates.keys():
    if dict_candidates[key] > winner_votes: #compare votes
        winner = key
        winner_votes = dict_candidates[key]


#Print to the terminal
print("Election Results")
print("--------------------")
print("Total Votes: {}".format(total_number_votes))
print("--------------------")
for key in dict_candidates.keys():
    percentage_votes = (dict_candidates[key]/total_number_votes) * 100
    print("%s: %.3f%% (%d)\n" % (key,percentage_votes,dict_candidates[key]))
print("--------------------")
print("Winner: {}".format(winner))
print("--------------------")

#Export a text file with the results
with open("output_PyPoll.txt", 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Votes: {}\n".format(total_number_votes))
    txtfile.write("--------------------\n")
    for key in dict_candidates.keys():
        percentage_votes = (dict_candidates[key]/total_number_votes) * 100
        txtfile.write("%s: %.3f%% (%d)\n" % (key,percentage_votes,dict_candidates[key]))
    txtfile.write("--------------------\n")
    txtfile.write("Winner: {}\n".format(winner))
    txtfile.write("--------------------\n")