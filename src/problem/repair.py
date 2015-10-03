import storage
from problem import Problem

# - Repair
class Repair(Problem):

    """
    Returns the name of this problem class.
    """
    @staticmethod
    def class_name():
        return "repair"

    @staticmethod
    def load(definition):
       return Repair(definition['enclosure'])

    # Constructs a repair problem.
    def __init__(self, definition):
        super(Repair, self).__init__(definition['name'])
        self.enclosure = definition['enclosure']
        self.sids = self.enclosure.keys()
        self.max_sid = self.sids[-1]
        self.size = len(self.sids)

        # Generate the lines for the problem.
        self.lines = reduce(lambda lines, sid: lines + self.lines_within(sid),
                            self.top_level_statements(),
                            [])

    # Determines whether a statement with a given SID is a top-level
    # statement (i.e. it has no parent).
    def is_top_level(self, sid):
      return self.enclosure[sid] == 0

    # Returns a list of the SIDs for all top-level statements for this problem.
    def top_level_statements(self):
        return filter(self.is_top_level, self.sids)

    # Returns a list of all the lines added to the program by the statement
    # at a given SID. Implementation could be faster, but there isn't really
    # much point in optimisation.
    def lines_within(self, pid):
        lines = [pid]
        for cid in self.immediate_children(pid):
            lines.extend(self.lines_within(cid))
        return lines

    # Returns a list of all the ancestors of the statement at a given SID.
    def ancestors(self, sid):
        pid = self.parent(sid)
        return [pid] + self.ancestors(pid) if pid else []

    # Returns the SID of the parent of a statement at a given SID.
    # If that statement has no parent, 0 is returned.
    def parent(self, sid):
        return self.enclosure[sid]
  
    # Returns a list of the immediate children of a statement at a given SID.
    def immediate_children(self, sid):
        return filter(lambda pid: self.enclosure[pid] == sid, self.sids)

    # Returns a list of all the children of a statement at a given SID,
    # recursively.
    def children(self, sid):
        c = self.immediate_children(sid)
        return reduce(lambda c, sid: c + self.children(sid), c, c) 

# Register this problem class.
storage.register(Repair)
