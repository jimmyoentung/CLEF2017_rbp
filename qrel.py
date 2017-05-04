"""
Created by Jimmy (April 2017)
Load and validate qrels data
"""

import os


def load_qrels(qrels_path, relevance_threshold):
    # create empty dictionary to hold the qrels data. key: q_id*doc_id. value: relevance score
    temp = dict()
    if not os.path.exists(qrels_path):
        raise NameError("Path to qrels file not found!")

    with open(qrels_path, 'r') as infile:
        for line in infile:
            parts = line.split()
            key = parts[0] + "*" + parts[2]
            if int(parts[3]) >= relevance_threshold:
                relevance_score = 1
            else:
                relevance_score = 0
            temp[key] = relevance_score

    return temp
