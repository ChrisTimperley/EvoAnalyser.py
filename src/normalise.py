

# Process backwards at each index?

def normalise(fixes, problem):

    # Group the fixes by the SIDs on which they operate.
    # Also record their position in the patch.
    groups = {}
    for i, fix in enumerate(fixes):
        if fix.location in groups:
            groups[fix.location] = [(i, fix)]
        else
            groups[fix.location] += (i, fix)

    # Find the (affected) children for each SID.
    sids = groups.keys()
    children = {sid: sids.intersection(problem.children(sid)) for sid in sids}

    # Order the groups such that those at the start of the program come first.
    # This ensures that parents are processed before their children, potentially
    # saving time.
    sids.sort()
    for sid in sids:
    
        # Process the fixes in reverse order.
        for gi, (pi, fix) in enumerate(reverse(groups[sid])):
            
            # If replacement occurs, discard all fixes at this SID before this
            # operation, and destroy all changes made to each of its children
            # (before this operation).
            if fix.replacement?
                groups[sid] = groups[sid][gi:]
                for c in children:
                    groups[c] = filter(lambda (cfi, cf): cfi > pi, groups[c])

            # If this statement is a delete, then for now we can no longer
            # address it or its children.
            if fix.deletion?
                groups[sid] = [(pi, fix)]
                for c in children:
                    groups[c] = []

    # Form a canonical patch by adding each group from left to right.
    patch = reduce(lambda p, sid: p + map(lambda (i, f): f, groups[sids]),
                   sids, [])

    print patch
