from representation.patch import Patch, Fix
from log_file import *

# We need a test problem.
log = LogFile.read('../examples/gcd/0.log')
problem = log.meta['problem']

def normalise(patch, problem):

    fixes = patch.fixes

    # Group the fixes by the SIDs on which they operate.
    # Also record their position in the patch.
    groups = {}
    for i, fix in enumerate(fixes):
        if not fix.location in groups:
            groups[fix.location] = [(i, fix)]
        else:
            groups[fix.location].append((i, fix))

    # Find the (affected) children for each SID.
    sids = set(groups.keys())
    children = {sid: sids.intersection(set(problem.children(sid))) for sid in sids}

    # Order the groups such that those at the start of the program come first.
    # This ensures that parents are processed before their children, potentially
    # saving time.
    sids = sorted(sids)
    for sid in sids:
    
        # Process the fixes in reverse order.
        for gi, (pi, fix) in enumerate(reversed(groups[sid])):
            
            # If replacement occurs, discard all fixes at this SID before this
            # operation, and destroy all changes made to each of its children
            # (before this operation).
            if fix.is_replacement():
                groups[sid] = groups[sid][gi:]
                for c in children[sid]:
                    groups[c] = filter(lambda (cfi, cf): cfi > pi, groups[c])

            # If this statement is a delete, then for now we can no longer
            # address it or its children.
            if fix.is_deletion():
                groups[sid] = [(pi, fix)]
                for c in children[sid]:
                    groups[c] = []

    # Form a canonical patch by adding each group from left to right.
    fixes = reduce(lambda p, sid: p + map(lambda (i, f): f, groups[sid]),
                   sids, [])
    return Patch(fixes)

# Normalise a test patch.
test_patch = Patch.load('d(9) r(1,5) r(8,13) r(5,7) d(4) a(2,14) r(1,10) d(2)')

normalised = normalise(test_patch, problem)
print normalised.to_s()
