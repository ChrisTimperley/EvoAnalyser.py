# Virtual column
class Canonical(object):
    
    # Check requirements are satisfied.
    def requires(data):

    def compute(data):
        return map(self.process, data.rows())

    def process(row):
       return row.column("genome").normalise(PROBLEM)
