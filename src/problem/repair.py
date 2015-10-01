import storage
from problem import Problem

# - Repair
class Repair(Problem):

    @staticmethod
    def load(definition):
       return Repair(definition['enclosure'])

    # Constructs a repair problem.
    def __init__(self, enclosure):
        self.enclosure = enclosure
        self.sids = self.enclosure.keys()
        self.max_sid = self.sids[-1]
        self.size = len(self.sids)

        # Generate the lines for the problem.
        self.lines = reduce(lambda lines, sid: lines + self.lines_within(sid),
                            self.top_level_statements(),
                            [])

# Register this problem class.
storage.register("repair", Repair)
