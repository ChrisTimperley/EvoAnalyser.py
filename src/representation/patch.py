import storage

# Used to represent a single atomic fix within a candidate patch.
class Fix(object):

    # Calculates the precedence level of a given operation (e.g. deletion,
    # replacement, insertion). A lower level indicates a higher priority,
    # i.e. an operator with a precedence of 0 must be executed before an
    # operator with a precedence of 1.
    @staticmethod
    def op_precedence(op):
         return ({
            "delete":   0,
            "replace":  1,
            "insert":   2
        })[op]

    # Constructs a patch fix object from a log file definition.
    @staticmethod
    def load(definition):

        # Find the type of the fix.
        typ = ({
            "a": "insert",
            "r": "replace",
            "d": "delete"
        })[definition[0]]

        # Extract the location and surrogate SIDs.
        args = map(int, definition[2:-1].split(","))
        
        # Record the location SID of the fix.
        location = args[0]
        
        # Find the surrogate SID, if there is one.
        # If there isn't, then record the surrogate SID as None.
        surrogate = None if typ == "delete" else args[1]
        
        # Build the object.
        return Fix(typ, location, surrogate)

    # Constructs a patch fix object from its properties. 
    def __init__(self, typ, location, surrogate):
        self.typ = typ
        self.location = location
        self.surrogate = surrogate

    # Writes a fix object to a string.
    def to_string(self):

        # Produce the short fix type identifier.
        typ_short = ({
            "insert": "a",
            "replace": "r",
            "delete": "d"
        })[self.typ]

        # Compute the fix arguments.
        args = [self.location]
        if self.typ != "delete":
            args.append(self.surrogate)
        args = ",".join(map(str, args))

        # Put everything together into a string definition.
        return "%s(%s)" % (typ_short, args)

    # Calculates the precedence of the operator used by this fix. 
    def operator_precedence(self):
        return Fix.op_precedence(self.typ)
        
    # Compares this fix to another to determine which should be performed first.
    def __cmp__(self, other):
        
        # If the two fixes operate at different locations, the one that
        # operates at an earlier index comes first.
        if self.location != other.location:
            return cmp(self.location, other.location)

        # If the two fixes operate at the same location, then compare them
        # according to their operator precedence.
        else:
            return cmp(self.operator_precedence(), other.operator_precedence())

# Used to hold the intermediate representation of a given patch.
class Intermediate(object):

    # Generates the null intermediate representation for the given problem.
    @staticmethod
    def from_problem(problem):
        states = dict([(sid, [sid]) for sid in problem.statements()])
        return Intermediate(states)

    # Generates an intermediate representation from a given patch.
    @staticmethod
    def from_patch(problem, patch):
        rep = Intermediate.from_problem(problem)        
        for fix in patch.fixes:
            rep.apply_fix(problem, fix)
        return rep

    # Constructs an intermediate representation from a sequence of states for
    # each of its addressable statements.
    def __init__(self, states):
        self.states = states

    # Hashes the state of the program at a given SID.
    def hash_state(self, problem, sid):

        # If the site has been destroyed, return 0.
        if self.destroyed(sid):
            return 0

        # Otherwise transform the state into a base-10 number.
        base = problem.max_sid
        return reduce(lambda h, (i, s): h + s * pow(base, i),
                      enumerate(self.states[sid]), 0)

    # Applies an atomic fix to this intermediate representation.
    def apply_fix(self, problem, fix):
        if fix.typ == "delete":
            for loc in ([fix.location] + problem.children(fix.location)):
                self.states[loc] = [0]
        elif fix.typ == "insert":
            if self.states[fix.location] == [0]:
                self.states[fix.location] = [fix.surrogate]
            else:
                self.states[fix.location].append(fix.surrogate)

        elif fix.typ == "replace":
            self.states[fix.location] = [fix.surrogate]
            for loc in problem.children(fix.location):
                self.states[loc] = [0]

    # Determines whether a statement at a given SID has been altered by the
    # changes in this intermediate representation.
    def altered(self, sid):
        return self.states[sid] != [sid] # changed from sid to [sid]

    # Determines whether the root statement at a given SID has been altered by
    # the changes in this intermediate representation.
    def altered_root(self, sid):
        return self.states[sid][0] != sid

    # Determines whether a replacement has taken place at a given SID. 
    def replaced(self, sid):
        return (not self.destroyed(sid)) and self.states[sid][0] != sid

    # Returns a list of the statements inserted at a given SID.
    def insertions(self, sid):
        return self.states[sid][1:]

    # Determines whether a statement at a given SID has been destroyed by the
    # changes in this intermediate representation.
    def destroyed(self, sid):
        return self.states[sid] == [0]

    # Determines whether a statement at a given SID has been destroyed by the
    # deletion or replacement of one of its ancestors.
    def destroyed_by_ancestor(self, problem, sid):
        for ancestor in problem.ancestors(sid):
            if self.replaced(ancestor) or self.destroyed(ancestor):
                return True
        return False

    # Generates the list of lines comprising this program.
    def to_lines(self, problem):
        lines = []

        # Find all the top-level statements.
        q = filter(problem.is_top_level, problem.statements())[::-1]
        while q:
            nxt = q.pop()

            # Only process this SID if there are statements there.
            if self.states[nxt] != [0]:

                # Check if the root statement has been replaced.
                if self.altered_root(nxt):
                    lines.extend(problem.lines_within(self.states[nxt][0]))

                # If not, process the children of this statement.
                else:
                    lines.append(nxt)
                    q.extend(problem.immediate_children(nxt)[::-1])

                # Process each insertion performed at this SID.
                for ins_id in self.states[nxt][1:]:
                    lines.extend(problem.lines_within(ins_id))

        return lines

    # Produces a string definition of this intermediate state.
    # Useful for debugging.
    def to_string(self):
        s = ", ".join(["%d -> (%s)" % (sid, " ".join(map(str, s))) for sid, s in self.states[1:]])
        return "{%s}" % (s)

# Used to represent a candidate patch for a given program.
class Patch(Representation):

    # Generates a patch from a log file definition.
    @staticmethod
    def load(definition):
        if definition == "original":
            return Patch([])
        else:
            return Patch(map(Fix.from_string, definition.split(" ")))

    # Constructs a new patch from a sequence of edits.
    def __init__(self, edits):
        self.edits = edits

    # Converts this patch to a human-readable string.
    def to_s(self):
        pass

    # Converts a given intermediate representation to its minimal canonical
    # patch.
    @staticmethod
    def from_inter(problem, inter):

        # Create a list to hold the fixes comprising the patch.
        fixes = []

        # Generate the fixes from left to right.
        for sid in problem.statements():
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
    def __init__(self, fixes):
        self.fixes = fixes

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
        inter = Intermediate.from_patch(problem, self)
        return Patch.from_inter(problem, inter)

storage.register("patch", Patch)
