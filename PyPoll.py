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

# 2. Total list of candidates.
candidate_options = []

# 3. Create an empty dictionary with candidate and votes.
candidate_votes = {}
# 4. Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

        # Print candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # tracking candidates vote count.
            candidate_votes[candidate_name] = 0
        # Add candidates votes against their name
        candidate_votes[candidate_name] += 1
        
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes (one decimal).
    print(f"{candidate_name} : received {vote_percentage:.1f} % of the vote.")
     #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
         print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# Print candidate votes dictionary
#print(candidate_votes)        
# Print the candidate list.
#print(candidate_options)
# 3. Print the total votes.
#print(total_votes)