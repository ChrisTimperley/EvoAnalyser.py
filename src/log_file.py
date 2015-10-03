import json

# LogFile objects are used to store the contents of a log file in a common
# format.
class LogFile:

    # Parses the meta section of a log file.
    @staticmethod
    def __parse_meta(s):
        return json.loads(s[7:])

    # Parses the data section of a log file.
    @staticmethod
    def __parse_data(meta, s):
        rows = map(lambda p: json.loads(p), s[7:].split('\n'))

        # This is quite inefficient, but for now, it's not so bad.
        # We could store LogFile UIDs, then compute these columns
        # on the fly?
        for row in rows:
            row['program'] = meta['program']
            row['seed'] = meta['seed']
            row['problem'] = meta['problem']['name']

        return rows

    # Splits the contents of a log file into its two sections.
    @staticmethod
    def __split_into_sections(s):
        i_meta = s.find('[meta]')
        i_data = s.find('[data]', i_meta)
        s_meta = s[i_meta:i_data].strip()
        s_data = s[i_data:].strip()
        return s_meta, s_data

    # Reads a log file at a given location and returns it, formatted as LogFile
    # object.
    @staticmethod
    def read(fn):
        print "Opening log file: %s" % (fn)

        # Open the log file and read each of its sections to separate strings.
        with open(fn, "r") as f:
            print "Opened log file: %s" % (fn)
            meta, data = LogFile.__split_into_sections(f.read())
            print "Split log file into sections."

        # Parse each of the sections of the file and merge them into an object.
        meta = LogFile.__parse_meta(meta)
        return LogFile(meta, LogFile.__parse_data(meta, data))

    # Constructs a new log file from the parsed contents of its two sections.
    def __init__(self, meta, data):
        self.meta = meta
        self.data = data
