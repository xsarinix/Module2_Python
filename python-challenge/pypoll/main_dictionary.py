import csv
from decimal import Decimal

# this cell creates a dictionary of of names and voter IDs
# which can be used to not only tally votes, but check for duplicates

# this cell also creates dictionaries of counties and votes
# which can be also be used to tally results by county

election_data_path="election_data.csv"
candidate_results={}
county_results={}
with open(election_data_path, newline='') as election_data_file:
    election_reader=csv.reader(election_data_file, delimiter=",")
    next(election_reader)
    for row in election_reader:
        candidate_name=row[2]
        voter_id=row[0]
        county=row[1]
        county_results.setdefault(county,[]).append(candidate_name)
        candidate_results.setdefault(candidate_name,[]).append(voter_id)


# this cell prints results for the solution involving dictionaries
# and writes to .txt file

total_candidates=len(list(candidate_results))
candidate_list=list(candidate_results)
total_votes=0
winner_count=0
for indiv in list(candidate_results):
    vote_list=candidate_results[indiv]
    total_votes=total_votes+len(vote_list) 
output=open("election_results.txt","w+")
print("Election Results")
output.write("Election Results\n")
print("-------------------------")
output.write("-------------------------\n")
print(f"Total votes: {total_votes}")
output.write(f"Total votes: {total_votes}\n")
print("-------------------------")
output.write("-------------------------\n")
for name in candidate_list:
    vote_list=candidate_results[name]
    vote_tally=len(vote_list)
    vote_pct=vote_tally/total_votes
    vote_pct_conv=round(Decimal(100*vote_pct),2)
    if vote_tally > winner_count:
        winner_count=vote_tally
        winner_name=name
    print(f"{name}: {vote_pct_conv}% ({vote_tally}) \n")
    output.write(f"{name}: {vote_pct_conv}% ({vote_tally}) \n")
print("-------------------------")
output.write("-------------------------\n")
print(f"Winner: {winner_name}")
output.write(f"Winner: {winner_name}\n")
print("-------------------------")
output.write("-------------------------\n")

output.close()