# Created by Jimmy (April 2017)

import run
import qrel
import persist
import rbp
import time

# read parameters
runs_path = "/Volumes/Data/Phd/Data/clef2016_topFiles/clef2016_top_01000003_25.0"
qrels_path = "/Volumes/Data/Phd/Data/clef2016_eval/task1.qrels.30Aug"
persists_string = ""
depth = 0

startTime=time.time()

# load runs and qresl into the respected list
runs, query_ids = run.load_runs(runs_path)
qrels = qrel.load_qrels(qrels_path)
persists = persist.load_persist(persists_string)

rbps = rbp.compute_rbp(query_ids, runs, qrels, persists, depth)

for rbp in rbps:
    print("p= {0:.2f} q= {1} d= {2} rbp= {3:.4f} + {4:.4f}".format(rbp.persist, rbp.q, rbp.d, rbp.score, rbp.err))


print (" Duration ", time.time()-startTime)