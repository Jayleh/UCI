import csv
import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyPoll\\raw_data', 'election_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as dictionary
    elect_data = csv.DictReader(csv_file, delimiter=',')

    # Create lists
    voter_id = []
    candidates = set()

    # Loop to count rows
    # row_count = sum(1 for row in elect_data)
    for row in elect_data:
        # Append voter ids to list
        voter_id.append(row['Voter ID'])
        candidates.add(row['Candidate'])

    # Declare variables
    total_votes = len(voter_id)
    candidates = sorted(list(candidates))
    cand_dict = {}

    print(candidates)

    # Instantiate candidate counts
    cand0_count = 0
    cand1_count = 0
    cand2_count = 0
    cand3_count = 0

    # Assign variables for candidates
    for i, cand in enumerate(candidates):
        # Add key value pairs to candidate dictionary
        cand_dict["cand%d" % i] = cand

    for row in elect_data:
        if cand_dict['cand0'] == row['Candidate']:
            cand0_count += 1
        elif cand_dict['cand1'] == row['Candidate']:
            cand1_count += 1
        elif cand_dict['cand2'] == row['Candidate']:
            cand2_count += 1
        elif cand_dict['cand3'] == row['Candidate']:
            cand3_count += 1

    print(cand0_count)
    print(cand1_count)
    print(cand2_count)
    print(cand3_count)
    print(cand_dict['cand0'])

    # Print results
    print("Election Results\n------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
