#Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# read the file object with the reader function
    file_reader = csv.reader(election_data)
    # read and print header row
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. print total number of votes
print(total_votes)
        

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

#write some data to the file
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")




# 1. The total number of votes casted
# 2. A complete list of candidates who received votes
# 3. the precentage of votes each candidate won
# 4. The total number of votes eachcandidate won
# 5. The winner of the election based on the popular vote



    