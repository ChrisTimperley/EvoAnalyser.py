import json

# LogFile objects are used to store the contents of a log file in a common
# format.
class LogFile:

    # Parses the meta section of a log file.
    def __parse_meta(s):
        print "- parsing meta section."
        return json.loads(s[7:])

    # Parses the environment section of a log file.
    def __parse_environment(s):
        print "- parsing environment section."
        return json.loads(s[14:])

    # Parses the problem section of a log file.
    def __parse_problem(s):
        print "- parsing problem section."
        return json.loads(s[10:])

    # Parses the search section of a log file.
    def __parse_search(s):
        print "- parsing search section."
        return map(json.loads, s[9:].split('\n'))

    # Splits the contents of a log file into each of its sections.
    def __split_into_sections(s):
        i_meta = s.find('[meta]')
        i_environment = s.find('[environment]', i_meta)
        i_problem = s.find('[problem]', i_environment)
        i_search = s.find('[search]', i_problem)

        s_meta = s[i_meta:i_environment].strip()
        s_environment = s[i_environment:i_problem].strip()
        s_problem = s[i_problem:i_search].strip()
        s_search = s[i_search:].strip()

        return s_meta, s_environment, s_problem, s_search

    # Reads a log file at a given location and returns it, formatted as LogFile
    # object.
    @staticmethod
    def read(fn):
        print "Opening log file: %s" % (fn)

        # Open the log file and read each of its sections to separate strings.
        with open(fn, "r") as f:
            print "Opened log file: %s" % (fn)
            meta, environment, problem, search = __split_into_sections(f.read())
            print "Split log file into sections."

        # Parse each of the sections of the file and merge them into an object.
        return LogFile(__parse_meta(meta),
                       __parse_environment(environment),
                       __parse_problem(problem),
                       __parse_seach(search))

    # Constructs a new log file from the parsed contents of each of its
    # sections.
    def __init__(self, meta, environment, problem, search):
        self.meta = meta
        self.environment = environment
        self.problem = problem
        self.search = search