# Created by Jimmy (April 2017)

from collections import namedtuple

# declare run structure
rbp = namedtuple("rbp", "persist, q, d, score, err")


def compute_rbp(query_ids, runs, qrels, persists, depth):
    t_rbp = []
    for q_id in query_ids:

        # if depth == 0 then check all ranks, else check up to the depth
        if depth == 0:
            qruns = [q for q in runs if q.q_id == q_id]
        else:
            qruns = [q for q in runs if q.q_id == q_id and q.rank <= depth]

        d = len(qruns)

        for p in persists:
            tempRbp = 0
            tempErr = 0
            for q in qruns:
                qrel_key = q.q_id + "*" + q.doc_id
                if qrel_key in qrels:
                    if qrels[qrel_key] > 0:
                        tempRbp += (1 * pow(p, q.rank - 1))
                else:
                    tempErr += pow(p, q.rank - 1)
            score = (1 - p) * tempRbp
            err_score = pow(p, d) + (1 - p) * tempErr
            t_rbp.append(rbp(p, q_id, depth, score, err_score))

    return t_rbp
