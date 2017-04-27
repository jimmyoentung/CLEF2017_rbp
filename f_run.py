# Created by Jimmy (April 2017)

import os
from collections import namedtuple


# declare run structure
run = namedtuple("run", "q_id,iter,doc_id,rank,score,run_id")


def load_runs(run_path):
    temp = []
    query_ids = []
    if not os.path.exists(run_path):
        raise NameError("Path to Run file not found!")

    with open(run_path, 'r') as infile:
        for line in infile:
            parts = line.split()
            temp.append(run(parts[0], parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            query_ids.append(parts[0])

    # get only unique query ids
    query_ids = list(set(query_ids))
    query_ids.sort()

    return temp, query_ids

