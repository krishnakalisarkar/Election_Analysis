## Deliverable 1
#----------------------
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
#------------------------------------------------------------------------------
# Initialize a total vote counter.
total_votes = 0
#-------------------------------------------------------------------------------
# 1: Creating a county list and county votes dictionary.

county_options = [] # list to hold the county names.
county_votes = {}   # Dictionary to hold the county votes.
#-----------------------------------------------------------------------------
# 2: Track the largest county and county voter turnout.
#-----------------------------------------------------------------------------
winning_county = ""     # County name with largest turnout.
winning_countyvotes = 0  # County votes with largest turnout
winning_percentage = 0  # Percentage of county votes with respect to the total votes.
#--------------------------------------------------------------------------------
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the 2 headers
    header = next(reader)
    header = next(reader)
    #print(header)
    #For each row in the CSV file.
    for row in reader:
        #Add to the total vote count
        total_votes += 1    # Total votes casted.
        #print(total_votes)
        # 3. Get the county name from each row.
        county_name = row[1]    # County names in the list.
        #print(county_name)
        # 4a. If the county does not match any existing county add it to the county list
        if county_name not in county_options:
            # 4b. Add the candidate name to the candidate list.
            county_options.append(county_name)
            #print(county_options)
            # 4c.Tracking the county's vote count.
            county_votes[county_name] = 0
        # 5. Add a vote to that county's vote count.
        county_votes[county_name] += 1
        #print(county_votes)
    # 6a. Write a for loop to get the county from the county dictionary.
    for county in county_votes.keys():
        print(county)
    # 6b. Retrieve the county vote count.
    for votes in county_votes.values():
        print(votes)
    with open(file_to_save, "w") as txt_file:   
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"County Votes :\n")
        print(election_results)
        txt_file.write(election_results)
    # 6c. Calculate the percentage of votes for the county.
        for county_name in county_votes:
            votes = county_votes[county_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # 6d. Print the county results to the terminal.
            print(county_results)    
            txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
            if (votes > winning_countyvotes) and (vote_percentage > winning_percentage):
                winning_countyvotes = votes
                winning_county = county_name
            
            #7. Print the county with the largest turnout to the terminal.
            largest_turnout_county = (
                f"-------------------------\n"
                f"Largest County turnout : {winning_county}\n"
                f"-------------------------------\n")
        print(largest_turnout_county)
        txt_file.write(largest_turnout_county)
        txt_file.close()
        
    #----------------------------------------------------------------------------------------------------"
   # Candidate options and candidate votes
    candidate_options = []
    candidate_votes = {}
    # Track the winning candidate, vote count, and percentage.
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    
    # Open the election results and read the file.
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        # Read the header row.
        headers = next(file_reader)
        headers = next(file_reader)
        # Print each row in the CSV file.
        for row in file_reader:
            
            # Get the candidate name from each row.
            candidate_name = row[2]
            #If the candidate does not match any existing candidate add it the candidate list.
            if candidate_name not in candidate_options:
                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0
                # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
        #print(candidate_options)
        #print(candidate_votes)
        with open(file_to_save, "a") as txt_file:
                   
            for candidate_name in candidate_votes:
                # Retrieve vote count and percentage.
                votes = candidate_votes[candidate_name]
                vote_percentage = (float(votes) / float(total_votes)) * 100
                # Print each candidate, their voter count, and percentage to the terminal.
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")                                           
                # Print each candidate, their voter count, and percentage to the terminal.
                print(candidate_results)
                txt_file.write(candidate_results)
                # Determine winning vote count, winning percentage, and candidate.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_candidate = candidate_name
                    winning_percentage = vote_percentage   
                    winning_candidate_summary = (
                        f"-------------------------\n"
                        f"\nWinner: {winning_candidate}\n"
                        f"\nWinning Vote Count: {winning_count:,}\n"
                        f"\nWinning Percentage: {winning_percentage:.1f}%\n"
                        f"\n-------------------------\n")
            print(winning_candidate_summary)
            txt_file.write(winning_candidate_summary)
            txt_file.close()
