import csv

# Set up variables to store data
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

# Open the CSV file and read data
with open(r"C:\Users\aspen\osu\homework\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    next(csvreader)
    # Loop through each row of data
    for row in csvreader:
        # Increment total vote count
        total_votes += 1
        # Get the candidate's name
        candidate = row[2]
        # Add the candidate to the dictionary if they don't exist
        if candidate not in candidates:
            candidates[candidate] = 0
        # Increment the candidate's vote count
        candidates[candidate] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    # Calculate the percentage of votes
    vote_percentage = votes / total_votes * 100
    # Print the candidate's name, vote percentage, and vote count
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    # Check if this candidate has the highest vote count so far
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open(r"C:\Users\aspen\osu\homework\python-challenge\PyPoll\Resources\election_data.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes
        vote_percentage = votes / total_votes * 100
        # Write the candidate's name, vote percentage, and vote count to the file
        file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")