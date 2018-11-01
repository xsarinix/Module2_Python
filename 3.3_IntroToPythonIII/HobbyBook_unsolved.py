import random
personal={"Name": "Sarah", "Age": "30", "Hobbies": ["Soccer","Hiking","Cooking","Dog Walks"], "Times": ["615am","645am","830am","1200pm"]}
print(f'{personal["Name"]} has {len(personal["Hobbies"])} hobbies and sometimes wakes up at {personal["Times"][random.randint(1, len(personal["Times"]))]}.')