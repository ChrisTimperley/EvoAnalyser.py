# EvoAnalyser.py

Performs framework-independent visualisation and analysis of genetic algorithm
log files.

## Log Format

The framework-independent log file for a given run is split into two sections:

* `[meta]`, describes the environment in which the run was performed, the
  problem it covered, and other meta-level details about the run.
* `[data]`, contains a number of observations, or data points, describing
  (part of) the state of the search at given moments in time. These
  observations are given as a sequence of flexibly-structured JSON documents.

### `[meta]` section

The information provided in this section guides the analyser on how to parse
the observations in the `[data]` section of the file. This contents of this
section are specified by a JSON file, which should contain (at least some of)
the properties below:

* `os`, a short description of the operating system used during the run.
* `seed`, the random seed used during the run.
* `datetime`, the date and time that the run was started.
* `program`, the program, or framework, that was used to perform the run.

### Algorithm Section

Provides a description of the genetic algorithm being used to solve the
problem, along with its components and relevant parameter values. The
information in this section of the file is used to guide the interpretation
of the rest of the file.

### Problem Section

This section identifies the type of problem being solved, and provides its
relevant details (based on the type of the problem and the search method in
use).

### Data Section

The data section is composed of a sequence of "points" from the search. The
meaning and structure of these points depends on the type of algorithm used by
the run.

For an evolutionary algorithm, each of these points is used to represent an
individual at a given position with the population (and possibly a given deme
within that population) at a given generation. Each point would contain the
following information (where fields marked with an asterix are optional):

* `uid`
* `position`
* `generation`
* `*deme`
* `*parents`
* `genome`
* `fitness`
