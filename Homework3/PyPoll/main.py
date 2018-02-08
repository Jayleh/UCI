import csv
import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyPoll\\0 raw_data', 'election_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as dictionary
    elect_data = csv.DictReader(csv_file, delimiter=',')

    # Create lists/dictionaries
    voter_id = []
    candidates = set()
    cand_dict = {}

    # Loop to count rows
    # Can also do row_count = sum(1 for row in elect_data)
    for row in elect_data:
        # Append voter ids to list
        voter_id.append(row['Voter ID'])
        candidates.add(row['Candidate'])

    # Create sorted list of unique candidates
    candidates = sorted(list(candidates))

    # Create candidate dictionary
    for i, cand in enumerate(candidates):
        # Add key value pairs to candidate dictionary
        cand_dict["cand%d" % i] = cand

    # Read csv file again
    with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

        # Read csv file as dictionary
        elect_data = csv.DictReader(csv_file, delimiter=',')

        # Instantiate candidate counts
        cand0_count = 0
        cand1_count = 0
        cand2_count = 0
        cand3_count = 0

        for row in elect_data:
            if row['Candidate'] == cand_dict['cand0']:
                cand0_count += 1
            elif row['Candidate'] == cand_dict['cand1']:
                cand1_count += 1
            elif row['Candidate'] == cand_dict['cand2']:
                cand2_count += 1
            elif row['Candidate'] == cand_dict['cand3']:
                cand3_count += 1

        # Declare variables
        total_votes = len(voter_id)
        cand0_percentage = round((cand0_count / total_votes)*100, 1)
        cand1_percentage = round((cand1_count / total_votes)*100, 1)
        cand2_percentage = round((cand2_count / total_votes)*100, 1)
        cand3_percentage = round((cand3_count / total_votes)*100, 1)

        '''
        cand_perc_vote_dict = {cand_dict['cand0']: [cand0_percentage, cand0_count],
                               cand_dict['cand1']: [cand1_percentage, cand1_count],
                               cand_dict['cand2']: [cand2_percentage, cand2_count],
                               cand_dict['cand3']: [cand3_percentage, cand3_count]}
        '''

        # Create candidate votes list
        cand_votes = [cand0_count, cand1_count, cand2_count, cand3_count]

        # for value in cand_dict:
        #     cand_perc_vote_dict[cand_dict[f'{value}']] = 123

        max_vote = max(cand_votes)

        index = -1
        for i in cand_votes:
            index += 1
            if i == max_vote:
                # Declare winner
                winner = candidates[index]

        # Print results
        print("Election Results\n------------------------")
        print(f"Total Votes: {total_votes}")
        print("------------------------")
        print(cand_dict['cand0'] + f": {cand0_percentage}% ({cand0_count})")
        print(cand_dict['cand1'] + f": {cand1_percentage}% ({cand1_count})")
        print(cand_dict['cand2'] + f": {cand2_percentage}% ({cand2_count})")
        print(cand_dict['cand3'] + f": {cand3_percentage}% ({cand3_count})")
        print("------------------------")
        print(f"Winner: {winner}\n------------------------")

        # Declare text file path
        txt_path = os.path.join(os.getcwd(), 'PyPoll\\Election Results', 'election_data_1.txt')

        with open(txt_path, 'w') as txt_file:

            txt_file.write("Election Results\n------------------------\n")
            txt_file.write(f"Total Votes: {total_votes}\n")
            txt_file.write("------------------------\n")
            txt_file.write(cand_dict['cand0'] + f": {cand0_percentage}% ({cand0_count})\n")
            txt_file.write(cand_dict['cand1'] + f": {cand1_percentage}% ({cand1_count})\n")
            txt_file.write(cand_dict['cand2'] + f": {cand2_percentage}% ({cand2_count})\n")
            txt_file.write(cand_dict['cand3'] + f": {cand3_percentage}% ({cand3_count})\n")
            txt_file.write("------------------------\n")
            txt_file.write(f"Winner: {winner}\n------------------------")
