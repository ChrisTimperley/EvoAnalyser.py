# This class is used to contain the meta-data for a given data set.
# This meta-data provides a context for the data, and instructs the system how
# to parse and analyse it.
class Meta(object):

    # problem
    # algorithm
    # environment

# Challenge, how do we combine data-sets with different meta-information?
class Problem(object):

    @staticmethod
    def load(definition):
        # Forward to appropriate load method.
        pass

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


