from tabulate import tabulate

class DataFrameViewIterator(object):

    """
    Constructs a new iterator for a given data frame view.
    """
    def __init__(self, view):
        self.view = view
        self.i = 0
        self.limit = view.size()

    """
    Returns the next record from the attached data frame view.
    """
    def next(self):
        if self.i >= self.limit:
            raise StopIteration()
        else:
            f, j = self.view.member(self.i)
            f = self.view.frames()[f]
            record = {k: f.cell(k, j) for k in self.view.source_columns()}
            self.i += 1
            return record
    __next__ = next

class DataFrameView(object):

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
    Returns the (frame id, inner id) tuple for the nth member of this view.
    """
    def member(self, n):
        return self.__members[n]

    """
    Returns a list of the column sources for this view.
    """
    def source_columns(self):
        return self.__source_columns

    """
    Returns a list of the data frame sources for this view.
    """
    def frames(self):
        return self.__frames

    """
    Constructs and returns a new iterator for this view.
    """
    def __iter__(self):
        return DataFrameViewIterator(self)

    """
    Constructs a tabular form of this view and returns it as a string.
    """
    def tabulate(self, show_uid=False):
        return tabulate(self)
