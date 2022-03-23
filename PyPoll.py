#Add our dependencies.
import csv
import os

#Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize an accumulator variable to count votes.
total_votes = 0

#Candidate Options. (Declaring a new list.) 
candidate_options = []

#Candidate Votes. (Initialize a dictionary)
candidate_votes = {}

#Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    #and print the header row to check
    # print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count. (same as total_votes= total_votes + 1)
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]
        
        #If the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count. Set each candidates count to 0.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
   
#Using the with statement open the file as a text file and save results to it.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElections Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)


    #Determine ethe percentage of votes for each candidate by looping through the counts.
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes)/ float(total_votes) * 100

        #Print each candidate, their voter count, and percetage to the terminal
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine the winning count and candidate.
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name 

    #Print out winning candidate summary.
    winning_candidate_summary = (
        f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's name to the text file. 
    txt_file.write(winning_candidate_summary)
