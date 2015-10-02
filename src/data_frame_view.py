from tabulate import tabulate

class DataFrameViewIterator(object):

    """
    Constructs a new iterator for a given data frame view.
    """
    def __init__(self, view):
        self.__view = view
        self.__i = 0
        self.__limit = view.size()

    """
    Returns the next record from the attached data frame view.
    """
    def next(self):
        if self.__i >= self.__limit:
            raise StopIteration
        else:
            f, j = self.__view.__members[self.__i]
            f = self.__view.__frames[f]
            record = {k: f.__columns[k][j] for k in self.__view.__source_columns}
            yield record

class DataFrameView(object):

    # DataFrames: [a, b, c]
    # Rows: [(df, i), ...]

    """
    Constructs a new data frame view.

    :param frames:  the data frames that hold the data in this view.
    :param members: a list of the members of this view, each given as a tuple,
                    specifying the ID of their source data frame and their
                    internal ID within that frame.
    :param columns: the names of the columns included from the original
                    data frames in this view.
    """
    def __init__(self, frames, members, columns):
        self.__frames = frames
        self.__source_columns = columns
        self.__members = members
        self.__size = len(self.__members)

    # virtual columns?
  
    """
    Returns the size of this data frame view, measured by the number of records
    it contains.
    """
    def size(self):
        return self.__size

    """
    Constructs and returns a new iterator for this view.
    """
    def __iter__(self):
        return DataFrameViewIterator(self)

    """
    Constructs a tabular form of this view and returns it as a string.
    """
