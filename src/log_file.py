import pandas as pd
import json
import problem
import representation
import distance as dist

# LogFile objects are used to store the contents of a log file in a common
# format.
class LogFile:

    # Parses the meta section of a log file.
    @staticmethod
    def __parse_meta(s):
        meta = json.loads(s[7:])
        meta['problem'] = problem.Repair(meta['problem'])
        return meta

    # Parses the data section of a log file.
    @staticmethod
    def __parse_data(meta, s):
        problem = meta['problem'] # for now
        max_fitness = float(problem.ideal_fitness())
        rows = map(lambda p: json.loads(p), s[7:].split('\n'))

        # This is quite inefficient, but for now, it's not so bad.
        # We could store LogFile UIDs, then compute these columns
        # on the fly?
        for row in rows:
            row['genome'] = representation.Patch.load(row['genome'])
            row['canonical'] = row['genome'].normalise(problem) # better to make this a lazy column.
            #row['lines'] = row['canonical'].to_lines(meta['problem'])
            row['distance_to_origin'] = dist.distance_to_origin(problem, row['canonical'])
            row['ideal'] = problem.is_ideal_fitness(row['fitness'])
            row['program'] = meta['program']
            row['seed'] = meta['seed']
            row['problem'] = meta['problem'].name()
            row['normalised_fitness'] = row['fitness'] / max_fitness

        return pd.DataFrame(rows)

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
        print "Loading log file: %s" % fn

        # Open the log file and read each of its sections to separate strings.
        with open(fn, "r") as f:
            meta, data = LogFile.__split_into_sections(f.read())

        # Parse each of the sections of the file and merge them into an object.
        meta = LogFile.__parse_meta(meta)
        log = LogFile(meta, LogFile.__parse_data(meta, data))
        print "Loaded log file:  %s" % fn
        return log

    # Constructs a new log file from the parsed contents of its two sections.
    def __init__(self, meta, data):
        self.meta = meta
        self.data = data
