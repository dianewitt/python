## PyPoll

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import os
import csv
import collections

csv_path = os.path.join('Resources', 'election_data.csv')
text_path = os.path.join("Analysis", "election_results.txt")

csv_file_name = 'election_data.csv'
txt_file_name = 'election_reslts.txt'

candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
total_votes = 0
pct_candidate_votes = 0
num_candidate_votes =0
win_most_votes = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for votes in csv_reader:
        if votes['Candidate'] == 'Khan': # Using DictReader the key is the column name, then searches for 'word'
            candidate1_votes += 1 # Totals the number of times 'word' is found in column 'Candidate
    
        if votes['Candidate'] == 'Correy': # Using DictReader the key is the column name, then searches for 'word'
            candidate2_votes += 1 # Totals the number of times 'word' is found in column 'Candidate
    
        if votes['Candidate'] == 'Li': # Using DictReader the key is the column name, then searches for 'word'
            candidate3_votes += 1 # Totals the number of times 'word' is found in column 'Candidate

        if votes['Candidate'] == "O'Tooley": # Using DictReader the key is the column name, then searches for 'word'
            candidate4_votes += 1 # Totals the number of times 'word' is found in column 'Candidate

    total_votes = candidate1_votes + candidate2_votes + candidate3_votes + candidate4_votes
    candidate1_pct = candidate1_votes/total_votes*100
    candidate2_pct = candidate2_votes/total_votes*100
    candidate3_pct = candidate3_votes/total_votes*100
    candidate4_pct = candidate4_votes/total_votes*100
   
    # Formats variables before printing
    total_votes = "{:,.0f}".format(total_votes)
    candidate1_votes = "{:,.0f}".format(candidate1_votes)
    candidate2_votes = "{:,.0f}".format(candidate2_votes)
    candidate3_votes = "{:,.0f}".format(candidate3_votes)
    candidate4_votes = "{:,.0f}".format(candidate4_votes)
    candidate1_pct = "{:,.0f}%".format(candidate1_pct)
    candidate2_pct = "{:,.0f}%".format(candidate2_pct)
    candidate3_pct = "{:,.0f}%".format(candidate3_pct)
    candidate4_pct = "{:,.0f}%".format(candidate4_pct)
    
    win_most_votes = "{:,.0f}".format(win_most_votes)

    # Prints to terminal
    print(f"Election Results")
    print(f"Total Votes Cast: {total_votes}")
    print(f"Votes for Khan: {candidate1_votes}, {candidate1_pct}")
    print(f"Votes for Correy: {candidate2_votes}, {candidate2_pct}")
    print(f"Votes for Li: {candidate3_votes}, {candidate3_pct}")
    print(f"Votes for O'Tooley: {candidate4_votes}, {candidate4_pct}")
    print(f"Candidate With Most Votes: {win_most_votes}")

with open (text_path, "w", newline='') as csvfile:
    text_writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    # Prints to election_results.txt
    text_writer.writerow(['Election Results'])
    text_writer.writerow(['Total Votes Cast: ',total_votes])
    #text_writer.writerow(['Candidates With Votes: ',candidate_votes])
    text_writer.writerow(['Candidate Vote Percent: ',pct_candidate_votes])
    text_writer.writerow(['Candidate Vote Total: ',num_candidate_votes])
    text_writer.writerow(['Candidate With Most Votes: ',win_most_votes])