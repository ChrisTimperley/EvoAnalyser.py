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


