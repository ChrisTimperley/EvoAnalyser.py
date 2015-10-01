class GroupedDataSets(object):
    
    # We should know what we're grouped by.

    # And perhaps what transformations have been applied to the whole group.

    # Constructs a new collection of dataset groups.
    def __init__(self, groups):
        self.__groups = groups

    # Performs an identical projection on the data set of each groups.
    def project(self, property_name):
        gs = map(lambda g: g.project(property_name), self.__groups)
        return GroupedDataSets(gs)

    # Returns the groups, along with their values, in the form of a dictionary.
    def groups(self):
        return self.__groups

    # Transforms this collection of grouped data sets into a single data set.
    # 
    # WARNING: Not order preserving (at the moment).
    def collapse(self):
        pass
