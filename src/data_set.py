class DataSet(object):

    # Could cache views?

    # Constructs a new data set.
    def __init__(self, contents):
        self.__contents = contents

    # Returns the contents of this data set.
    def contents(self):
        return self.__contents

    #
    def project(self, property_name):
        m = map(lambda p: getattr(p, property_name), self.__contents)
        return DataSet(m) # need to update the "type" of the dataset.

    # How can we safely achieve this?
    def group_by(self, property_name):
        groups = {}
        for point in self.__contents:
            v = getattr(point, property_name)
            if groups.has_key(v):
                groups[v].append(point)
            else:
                groups[v] = [point]
        return None
