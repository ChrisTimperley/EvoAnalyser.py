import json

# Splits the contents of a log file into each of its sections.
def split_log_into_sections(s):
    i_meta = s.find('[meta]')
    i_environment = s.find('[environment]', i_meta)
    i_problem = s.find('[problem]', i_environment)
    i_search = s.find('[search]', i_problem)

    s_meta = s[i_meta:i_environment].strip()
    s_environment = s[i_environment:i_problem].strip()
    s_problem = s[i_problem:i_search].strip()
    s_search = s[i_search].strip()

    return s_meta, s_environment, s_problem, s_search

# Parses the contents of the meta section of a log file.
def parse_meta(s):
    print "- parsing meta section."

    # Remove the header and parse as a JSON object.
    s = s[7:]
    return json.loads(s)

# Parses the contents of the environment section of a log file.
def parse_environment(s):
    print "- parsing environment section."

    # Remove the header and parse as a JSON object.
    s = s[14:]
    return json.loads(s)

# Parses the contents of the problem section of a log file.
def parse_problem(s):
    print "- parsing problem section."

    # Remove the header and parse as a JSON object.
    s = s[10:]
    return json.loads(s)

# Parses the contents of the search section of a log file.
def parse_search(s):
    print "- parsing search section."
    return s

# Reads a given log file.
def read_log(fn):
    print "Opening log file: %s" % (fn)

    # Open the log file and read each of its sections to separate strings.
    with open(fn, "r") as f:
        print "Opened log file: %s" % (fn)
        meta, environment, problem, search = split_log_into_sections(f.read())
        print "Split log file into sections."

    # Parse each of the sections of the file.
    meta = parse_meta(meta)
    environment = parse_environment(environment)
    problem = parse_problem(problem)
    search = parse_search(search)

    print "Finished parsing sections."

read_log("test.log")
