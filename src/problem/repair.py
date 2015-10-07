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

    # Constructs a repair problem.
    def __init__(self, definition):
        super(Repair, self).__init__(definition['name'])
        self.__ideal_fitness = float(definition['ideal_fitness'])
        self.enclosure = definition['enclosure'].iteritems()
        self.enclosure = dict(map(lambda (k, p): (int(k), p), self.enclosure))
        self.sids = self.enclosure.keys()
        self.max_sid = self.sids[-1]
        self.size = len(self.sids)

        # Compute the list of immediate children for each statement.
        self.__immediate_children = dict({sid: [] for sid in self.sids})
        for sid in self.sids:
            pid = self.enclosure[sid]
            if pid > 0:
                self.__immediate_children[pid].append(sid)

        # Compute the list of all children for each statement.
        self.__children = dict({sid: [] for sid in self.sids})
        for sid in self.sids:
            q = self.__immediate_children[sid][:]
            while q:
                nxt = q.pop(0)
                q += self.__immediate_children[nxt]
                self.__children[sid].append(nxt)

        # Compute the size of each statement.
        self.__size_of = dict({sid: len(children) + 1 for (sid, children) in self.__children.iteritems()})

        # Generate the lines for the problem.
        self.lines = reduce(lambda lines, sid: lines + self.lines_within(sid),
                            self.top_level_statements(),
                            [])

    # Returns the ideal fitness value for this problem.
    def ideal_fitness(self):
        return self.__ideal_fitness

    # Determines whether some given fitness value is ideal for this problem.
    def is_ideal_fitness(self, fitness):
        return fitness >= self.__ideal_fitness

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

    # Returns the "size" of a statement at a given SID.
    def size_of(self, sid):
        return self.__size_of[sid]

    # Returns a list of the immediate children of a statement at a given SID.
    def immediate_children(self, sid):
        return self.__immediate_children[sid]

    # Returns a list of all the children of a statement at a given SID,
    # recursively.
    def children(self, sid):
        return self.__children[sid]

# Register this problem class.
storage.register(Repair)
