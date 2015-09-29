import numpy

from collections import Counter
from intermediate import Intermediate

def occurrences(problem, inters, sid):
    size = float(len(inters))
    hashed = map(lambda i: i.hash_state(problem, sid), inters)
    return dict(Counter(hashed))

def site_entropy(problem, inters, sid):
    count = occurrences(problem, inters, sid)
    size = float(sum(count.values()))
    freqs = map(lambda c: c / size, count.values())
    return abs(reduce(lambda h, px: px * numpy.log2(px), freqs, 0.0))

def site_entropies(problem, patches):
    inters = map(lambda p: Intermediate.from_patch(problem, p), patches)
    pstmts = problem.statements()
    return [site_entropy(problem, inters, sid) for sid in pstmts]
