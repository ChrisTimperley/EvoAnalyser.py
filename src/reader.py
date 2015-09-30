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
    return json.loads("{" + s + "}")

# Parses the contents of the environment section of a log file.
def parse_environment(s):
    return json.loads("{" + s + "}")

# Parses the contents of the problem section of a log file.
def parse_problem(s):
    return json.loads("{" + s + "}")

# Parses the contents of the search section of a log file.
def parse_search(s):
    pass
