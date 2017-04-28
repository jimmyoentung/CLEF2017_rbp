# Created by Jimmy (April 2017)

import os
from collections import namedtuple

# declare qrel structure
Qrel = namedtuple("Qrel", "q_id, doc_id, relevance")


def load_qrels(qrels_path):
    temp = []

    if not os.path.exists(qrels_path):
        raise NameError("Path to qrels file not found!")

    with open(qrels_path, 'r') as infile:
        for line in infile:
            parts = line.split()
            temp.append(Qrel(parts[0], parts[2], int(parts[3])))

    return temp


'''
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
'''