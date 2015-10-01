from grouped_data_sets import GroupedDataSets

class DataSet(object):

    # Could cache views?

    # Constructs a new data set.
    def __init__(self, contents):
        self.__contents = contents

    # Returns the contents of this data set.
    def contents(self):
        return self.__contents
    items = contents
    elements = contents

    # Return DataSetColumn?
    def project(self, property_name):
        m = map(lambda p: getattr(p, property_name), self.__contents)
        return DataSet(m) # need to update the "type" of the dataset.

    # Applies a given transformation function to this data set, possibly
    # converting it into something which isn't a data set.
    def transform(self, transformation):
        return transformation(self)

    # How can we safely achieve this?
    def group_by(self, property_name):
        groups = {}
        for point in self.__contents:
            v = getattr(point, property_name)
            if groups.has_key(v):
                groups[v].append(point)
            else:
                groups[v] = [point]
        groups = { k: DataSet(g) for k, g in groups.iteritems() }
        return GroupedDataSets(groups)
