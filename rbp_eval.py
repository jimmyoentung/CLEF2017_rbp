# Created by Jimmy (April 2017)

import f_run
import f_qrel
import f_persist
import f_rbp

# read parameters
runs_path = "/Volumes/Data/Phd/Data/clef2016_topFiles/clef2016_top_01000003_25.0"
qrels_path = "/Volumes/Data/Phd/Data/clef2016_eval/task1.qrels.30Aug"
persists_string = ""
depth = 0

# load runs and qresl into the respected list
runs, query_ids = f_run.load_runs(runs_path)
qrels = f_qrel.load_qrels(qrels_path)
persists = f_persist.load_persist(persists_string)

rbps = f_rbp.compute_rbp(query_ids, runs, qrels, persists, depth)

for rbp in rbps:
    print(str(rbp.persist) + " " + rbp.q + " " + str(rbp.d) + " " + str(rbp.score) + " + " + str(rbp.err))



#for q in query_ids:
#    print(q)

#print(qrels["103001*0*clueweb12-0112wb-68-25181"])


#print(query_ids)
