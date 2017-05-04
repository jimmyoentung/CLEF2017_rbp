"""
Created by Jimmy (April 2017)
Implementation of Rank-Biased Precision based on: "Rank-Biased Precision for Measurement of Retrieval Effectiveness",
Moffat, A. and Zobel, J., ACM Transactions on Information Systems, Vol. 27, No. 1, Article 2, December 2008.
"""

from collections import namedtuple

# declare run structure
Rbp = namedtuple("Rbp", "persist, q, d, score, err")


def compute_rbp(query_ids, runs, qrels, persists, depth):
    t_rbp = []

    if depth == 0:
        label_d = "full"
    else:
        label_d = str(depth)

    for q_id in query_ids:
        # if depth == 0 then check all ranks, else check up to the specified depth
        if depth == 0:
            qruns = [q for q in runs if q.q_id == q_id]
        else:
            qruns = [q for q in runs if q.q_id == q_id and q.rank <= depth]

        d = len(qruns)

        # for each persistence value
        for p in persists:
            temp_rbp = 0
            temp_err = 0

            # calculate rbp for each query using current persitence value
            for q in qruns:
                qrel_key = q.q_id + "*" + q.doc_id
                try:
                    if qrels[qrel_key] > 0:
                        temp_rbp += (qrels[qrel_key] * pow(p, q.rank - 1))
                except:
                    temp_err += pow(p, q.rank - 1)
            score = (1 - p) * temp_rbp
            err_score = pow(p, d) + (1 - p) * temp_err
            t_rbp.append(Rbp(p, q_id, label_d, score, err_score))

    # calculate average rbp score for each persistence value
    all_rbp = []
    for p in persists:
        rbps = [r for r in t_rbp if r.persist == p]

        temp_rbp = 0
        temp_err = 0
        for r in rbps:
            temp_rbp += r.score
            temp_err += r.err

        all_rbp.append(Rbp(p, "all", label_d, temp_rbp/len(query_ids), temp_err/len(query_ids)))

    return t_rbp, all_rbp
