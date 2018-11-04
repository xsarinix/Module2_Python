import csv
from decimal import Decimal

# this section creates a short list of names and a long list of votes

election_data_path="election_data.csv"
candidate_list=[]
candidate_votes=[]
with open(election_data_path, newline='') as election_data_file:
    election_reader=csv.reader(election_data_file, delimiter=",")
    next(election_reader)
    for row in election_reader:
        candidate_name=row[2]
        candidate_votes.append(candidate_name)
        if not candidate_name in candidate_list:
            candidate_list.append(candidate_name)

# this cell prints results and writes to .txt file

total_candidates=len(candidate_list)
total_votes=len(candidate_votes)
winner_count=0
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
    vote_tally=candidate_votes.count(name)
    vote_pct=vote_tally/total_votes
    vote_pct_conv=round(Decimal(100*vote_pct),2)
    if vote_tally > winner_count:
        winner_count=vote_tally
        winner_name=name
    print(f"{name}: {vote_pct_conv}% ({vote_tally})")
    output.write(f"{name}: {vote_pct_conv}% ({vote_tally}) \n")
print("-------------------------")
output.write("-------------------------\n")
print(f"Winner: {winner_name}")
output.write(f"Winner: {winner_name}\n")
print("-------------------------")
output.write("-------------------------\n")

output.close()