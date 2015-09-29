# Contains details about the given problem being solved by the EA.
class Problem:

    # Constructs the details of a problem from a string definition.
    @staticmethod
    def from_string(s):
        
        # Build the enclosure information.
        lines = (s.split('\n'))[3:-1]
        lines = map(lambda l: tuple(map(int, l.split(': '))), lines)
        enclosure = dict(lines)

        # Build the problem object.
        return Problem(enclosure)

    # Constructs a problem definition from its properties.
    def __init__(self, enclosure):
        self.enclosure = enclosure
        self.max_sid = self.statements()[-1]
        self.size = len(self.enclosure) - 1
        self.generations = []
        self.max_fitness = 12
        self._lines = reduce(lambda lines, sid: lines + self.lines_within(sid),
                             self.top_level_statements(),
                             [])

    # Determines whether a given fitness value is ideal.
    def is_ideal_fitness(self, fitness):
        return fitness >= self.max_fitness

    def lines(self):
        return self._lines

    # Returns a list of the IDs of each of the statements in this problem.
    def statements(self):
        return self.enclosure.keys()

    # Returns the number of statements for the current problem.
    def num_statements(self):
        return self.size

    # Determines whether a statement with a given SID is a top-level
    # statement (i.e. it has no parent).
    def is_top_level(self, sid):
      return self.enclosure[sid] == 0

    # Returns a list of the SIDs for all top-level statements for this problem.
    def top_level_statements(self):
        return filter(self.is_top_level, self.statements())

    # Generates the list of lines for this problem, in their original
    # unmodified form.
    def to_lines(self):
        return reduce(lambda lines, sid: lines + self.lines_within(sid),
                      self.top_level_statements(),
                      [])

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
        return filter(lambda pid: self.enclosure[pid] == sid, self.statements())

    # Returns a list of all the children of a statement at a given SID,
    # recursively.
    def children(self, sid):
        
        # Find the children for each immediate child recursively.
        c = self.immediate_children(sid)
        return reduce(lambda c, sid: c + self.children(sid), c, c) 
