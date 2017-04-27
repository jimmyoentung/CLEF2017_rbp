# Created by Jimmy (April 2017)

import os


def load_qrels(qrels_path):
    # create empty dictionary to hold the qrels data. key: q_id*doc_id. value: relevance score
    temp = dict()
    if not os.path.exists(qrels_path):
        raise NameError("Path to qrels file not found!")

    with open(qrels_path, 'r') as infile:
        for line in infile:
            parts = line.split()
            key = parts[0] + "*" + parts[2]
            temp[key] = int(parts[3])

    return temp
