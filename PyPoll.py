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

#open the elction results and read the file.
with open(file_to_load) as election_data:
        #To do: read and analyze the data here
        #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        #print the header row.
    headers = next(file_reader)
    print(headers)