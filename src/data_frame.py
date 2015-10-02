import copy

class DataFrame(object):

    # This static variable is used to hold the unique ID to be used by the
    # next record that is inserted into any data frame. Used to maintain
    # natural ordering.
    __next_uid = 0

    # Returns the next unique identifier.
    @staticmethod
    def __uid():
        n = DataFrame.__next_uid
        DataFrame.__next_uid += 1
        return n

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
        self.__columns['_uid'].append(DataFrame.__uid())

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

    # Retrieves a column with a given name from this data frame.
    def column(self, name):
        pass

    # Returns the contents of this data frame as an array of rows, including
    # its headers.
    def table(self, show_uid = False):
        cols = copy.copy(self.__column_names)
        cols = ['_uid'] + cols if show_uid else cols
        return [cols] + \
            [[self.__columns[cn][i] for cn in cols] for i in range(self.__size)]
