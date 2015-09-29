# Used to store information about a given individual within the population.
#
# TODO: Compute normalised fitness, along with more fitness details.
class Individual:
   
    def __init__(self, problem, position, parents, patch, fitness):
        self.parents = parents
        self.position = position
        self.patch = patch
        self.canonical_patch = patch.normalise(problem)
        self.fitness = fitness

    # Composes the information about this individual into a string.
    def to_string(self, **kwds):
        fmt = "%d; %s; %s; %s; %f"
        args = [self.position,
                ', '.join(map(str, self.parents)),
                self.patch.to_string(),
                self.canonical_patch.to_string(),
                self.fitness]

        if kwds.has_key("lines"):
            fmt += "; %s"
            args.append(', '.join(map(str, kwds["lines"])))

        if kwds.has_key("distance_to_origin"):
            fmt += "; %f"
            args.append(float(kwds["distance_to_origin"]))

        return fmt % tuple(args)
