# The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The total number of votes each candidate won.
#4. The percentage of votes each candidate won.
#5. The winner of the election based on popular vote.

# Assign a variable for the file path to load.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read file.
election_data = open(file_to_load)
# To do: perform analysis.
# Close the file.
election_data.close()
with open(file_to_load) as election_data:   
    # To do: perform analysis.
    print(election_data)
import csv
import os
# 1.Assign a variable for the file to load and the file.
file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Print the file object
    print(election_data)
# 2.Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Hello World")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
# Write three counties to the file
    txt_file.write("Counties in the election\n----------------------------------\nArapahoe\nDenver\nJefferson")

# # Add our dependencies.# #
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # 2. Add the total vote count.
        total_votes += 1
# 3. Print the total votes.
print(total_votes)

