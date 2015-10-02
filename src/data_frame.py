import copy

from data_frame_view import DataFrameView
from tabulate import tabulate

class DataFrame(object):

    # Each DataFrame needs a unique ID.

    @staticmethod
    def build(records):
        df = DataFrame()
        for record in records:
            df.__append(record)
        return df

    # Constructs a new data frame.
    def __init__(self):
        self.__size = 0
        self.__columns = {'_uid': []}
        self.__column_names = []

    # Inserts a given (parsed) JSON record into this data frame.
    def __append(self, record):
       
        # Record the UID of this record.
        self.__columns['_uid'].append(self.__size)

        # Insert each column from the record into the data frame.
        # If the column doesn't exist, a new (partial) column is created.
        for cn, cv in record.iteritems():
            if self.__columns.has_key(cn):
                self.__columns[cn].append(cv)
            else:
                self.__column_names.append(cn)
                self.__columns[cn] = ([None] * self.__size) + [cv]
                # MARK COLUMN AS PARTIAL (if this isn't the first record).

        # For each column in the data frame that isn't touched by this record,
        # add a "None" entry for that column and ensure the column is marked
        # as partial.
        for cn in (set(self.__column_names) - set(record.keys())):
            self.__column_names.append(cn)
            self.__columns[cn].append(None)
            # MARK COLUMN AS PARTIAL

        # Increment the size of this data frame.
        self.__size += 1

        return self

    # Returns an iterator over the rows of this data frame.
    def iterator(self):
        pass

    # Retrieves a column with a given name from this data frame.
    def column(self, name):
        contents = [(0, i) for i in range(self.__size)]
        return DataFrameView([self], contents, [name])

    # Returns a view of this data-set, 
    def attach(self, name):
        pass

    # Transforms this data-frame into a string table.
    def tabulate(self, show_uid = False):
        cols = copy.copy(self.__column_names)
        cols = ['_uid'] + cols if show_uid else cols
        table = [[self.__columns[cn][i] for cn in cols] for i in range(self.__size)]
        return tabulate(table, headers=cols)
