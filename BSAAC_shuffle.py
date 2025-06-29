"""
Take in a CSV file with a list of BSAAC members consisting of their names and committees, shuffle them, and create
groups of 6 members. 
"""

import csv
import random
import sys

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            entries = []
            csv_reader = csv.reader(file)
            for row in csv_reader:
                entries.append(row)
            return entries
    except FileNotFoundError:
        print("file not found ):")
    except Exception as e:
        print("some other error")
    
def create_dict(entries):
    dictionary = {}
    for entry in entries:
        name = entry[0]
        committee = entry[1]
        if committee not in dictionary:
            dictionary[committee] = []
        dictionary[committee].append(name)
    for committee in dictionary:
        random.shuffle(dictionary[committee])
    return dictionary

def create_groups(dictionary, entries):
    index = 0
    groups = {}
    while index < len(entries):
        group = []
        for committee in dictionary:
            if len(dictionary[committee]) > 0:
                group.append(dictionary[committee].pop(0))
                index += 1
        if len(group) < 6:
            for committee in dictionary:
                while len(dictionary[committee]) > 0 and len(group) < 6:
                    group.append(dictionary[committee].pop(0))
                    index += 1
        groups[f'Group {index//6}'] = group
    return groups

def main(args):
    first = read_file(args)
    dictionary = create_dict(first)
    groups = create_groups(dictionary, first)
    for group in groups:
        print(f"{group}: {groups[group]}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a CSV file as an argument.")