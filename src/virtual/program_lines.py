class ProgramLines(VirtualColumn):

    def requirements(self):
        meta.problem.uses_genome("patch")

    def compute_row(self, row):
        return genome.to_lines(meta.problem)
