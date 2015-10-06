from representation import Representation
from _patch.fix import Fix
from _patch.intermediate import Intermediate
import storage

# Used to represent a candidate patch for a given program.
class Patch(Representation):

    # Generates a patch from a log file definition.
    @staticmethod
    def load(definition):
        if definition == "original":
            return Patch([])
        else:
            return Patch(map(Fix.load, definition.split(" ")))

    # Converts this patch to a human-readable string.
    def to_s(self):
        return self.to_string()

    # Converts a given intermediate representation to its minimal canonical
    # patch.
    @staticmethod
    def from_inter(problem, inter):

        # Create a list to hold the fixes comprising the patch.
        fixes = []

        # Generate the fixes from left to right.
        for sid in problem.sids:
            if inter.altered(sid):

                # Check if this statement was destroyed by an edit at this SID,
                # and not a deletion at an ancestor.
                if inter.destroyed(sid) and (not inter.destroyed_by_ancestor(problem, sid)):
                    fixes.append(Fix("delete", sid, None))
                
                # Must have been either replaced, inserted at, or both.
                else:

                    # Check if a replacement has occurred.
                    if inter.replaced(sid):
                        fixes.append(Fix("replace", sid, inter.states[sid][0]))

                    # Add any insertions.
                    fixes.extend([Fix("insert", sid, ins) for ins in inter.insertions(sid)])

        return Patch(fixes)

    # Constructs a patch from a sequence of atomic fixes.
    def __init__(self, fixes, canonical=False):
        self.fixes = fixes
        self.__is_canonical = canonical

    # Computes and returns the length of this patch.
    def length(self):
        return len(self.fixes)

    # Converts this patch (in its unmodified form) to a string definition.
    def to_string(self):
        if self.fixes:
            return " ".join(map(lambda f: f.to_string(), self.fixes))
        else:
            return "original"

    # Computes the line manifest for the program produced by this patch.
    # (we shouldn't look at the entire program, only the differences).
    def to_lines(self, problem):
      return Intermediate.from_patch(problem, self).to_lines(problem)

    # Computes the edit distance between this patch and another.
    def distance(self, other):
        return 0

    # Returns a hashed form of this patch.
    def __hash__(self):
        return hash(self.to_string())

    # Determines whether this patch is equivalent to some given object.
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.fixes == other.fixes

    # Computes the normal form of this patch.
    def normalise(self, problem):

        # Check if the patch has already been normalised.
        if self.__is_canonical:
            return self
        
        # Group the fixes by the SIDs on which they operate.
        # Also record their position in the patch.
        groups = {}
        for i, fix in enumerate(self.fixes):
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
        return Patch(fixes, True)
    
storage.register("patch", Patch)
