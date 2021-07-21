#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentate of votes each candidate won
#4. The total number of votes each candidate won
#5 The winner of the election based on popular vote

# Assign a variable for thefile to load and the path.
file_to_load = 'Resources/election_results.csv'
#Open the election resuts and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis.
    print(election_data)
#Close the file.
election_data.close()

import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file.
with open(file_to_load) as eletion_data:
    #print the file object.
    print(election_data)

#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to file 
open(file_to_save, "w")

#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the with statement open the file as a text
with open(file_to_save, "w") as txt_file:
     #write some data to the file.
    txt_file.write("Counties in the Election\n----------\nArapahoe\nDenver\nJefferson")

#add our depenencies
import csv
import os
#assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. initiaize a total vote counter.
total_votes = 0 
#candidate options
candidate_options = []
#1. declare the empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file.
with open(file_to_load) as election_data:
        #To do: read and analyze the data here
        #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        #print the header row.
    headers = next(file_reader)
    #Print each row in the csv file
    for row in file_reader:
        # 2. add to the total vote count.
        total_votes += 1
        # print the candidate name from each row.
        candidate_name = row[2]
        #if the candidate does not match any exiting candidates...
        if candidate_name not in candidate_options:
        #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. being tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#determine the percentage of votes for each candidate by looping through the counts
#1. iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #determine winning vote count and candidate
        #determin if the votes is greater than the winning count.
    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        #4 print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        winning_candidate_summary = ( 
            f"--------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------\n")
        print(winning_candidate_summary)



