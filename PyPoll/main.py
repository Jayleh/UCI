import csv
import os


# os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
# csv_path = os.path.join(os.getcwd(), 'PyPoll\\0 raw_data', 'election_data_1.csv')

# Set csv path
csv_path = os.path.join('0 raw_data', 'election_data_1.csv')


# Path to write to text file
# txt_path = os.path.join(os.getcwd(), 'PyPoll\\Election Results', 'election_data_1.txt')
txt_path = os.path.join('Election Results', 'election_data_1.txt')

with open(csv_path) as csv_file, open(txt_path, 'w') as txt_file:
    elect_data = csv.DictReader(csv_file)

    # Assign variables
    total_votes = 0
    candidate_options = []
    candidate_votes = {}
    winning_count = 0
    winner = ""
    voter_summary = []

    for row in elect_data:
        # Increment total votes
        total_votes += 1

        # Assign candidate row values to a variable to loop with
        candidate_name = row['Candidate']

        if candidate_name not in candidate_options:
            # Append candidate name if not in candidate options list
            candidate_options.append(candidate_name)

            # Assign candidate_votes dict key and instantiate each candidates' total votes
            candidate_votes[candidate_name] = 0

        # Increment each candidates' votes
        candidate_votes[candidate_name] += 1

    # Print to console
    print("Election Results\n-----------------------")
    print(f"Total Votes: {total_votes}\n-----------------------")

    # Write to text file
    txt_file.write("Election Results\n-----------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n-----------------------\n")

    # Loop through candiate_votes dictionary
    for candidate in candidate_votes:
        # Use get method to grab each candidate's vote count
        votes = candidate_votes.get(candidate)

        # Calculate vote percentages
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winner
        if votes > winning_count:
            winning_count = votes
            winner = candidate

        # Append summary of each voter to voter summary list
        voter_summary.append(f"{candidate}: {vote_percentage:.1f}% ({votes})")

    # For loop to print voter summary from list
    for voter in voter_summary:
        print(voter, end='\n')
        txt_file.write(voter + '\n')

    # Declare winner
    winner = f"-----------------------\nWinner: {winner}\n"

    # Print winner to console
    print(winner)

    # Write winner to text file
    txt_file.write(winner)
