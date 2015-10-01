class GroupedDataSets(object):
    
    # We should know what we're grouped by.

    # And perhaps what transformations have been applied to the whole group.

    # Constructs a new collection of dataset groups.
    def __init__(self, groups):
        self.__groups = groups

    # Performs an identical projection on the data set of each groups.
    def project(self, property_name):
        gs = {k: g.project(property_name) for k, g in self.__groups.iteritems() }
        return GroupedDataSets(gs)

    # Returns the groups, along with their values, in the form of a dictionary.
    def groups(self):
        return self.__groups

    def pairs(self):
        return self.__groups.iteritems()

    # Performs an identical transformation on each of the groups within this
    # data set.
    #
    # This is more like a reduction, but unfortunately "reduce" seems not only
    # to involve reducing a data-set to a single value, but a particular way
    # in performing that operation.
    def transform(self, transformation):
        gs = {k: g.transform(transformation) for k, g in self.__groups.iteritems() }
        return GroupedDataSets(gs)

    # Transforms this collection of grouped data sets into a single data set.
    # 
    # WARNING: Not order preserving (at the moment).
    def collapse(self):
        pass
