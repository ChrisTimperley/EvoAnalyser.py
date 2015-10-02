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

    # column names.
    # row IDs.
    # virtual columns?
