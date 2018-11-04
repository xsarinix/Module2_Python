
import csv
election_data_path="election_data.csv"
candidate_dict={}
with open(election_data_path, newline='') as election_data_file:
    election_reader=csv.reader(election_data_file, delimiter=",")
    next(election_reader, None)
    for row in election_reader:
        candidate_name=str(row[2])
        voter_id=row[0]
        candidate_dict[candidate_name]=voter_id
candidate_dict["Khan"]