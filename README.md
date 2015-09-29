# EvoAnalyser.py

Performs platform-independent visualisation and analysis of genetic algorithm
log files.

## Log Format

* Environment
* Algorithm
* Problem
* Initialisation
* Search

### Environment Section

Gives details of the machine used to carry out the search, including its
operating system. Also specifies the name of the framework, the random
seed used, and the date and time that the run started.

### Algorithm Section

Provides a description of the genetic algorithm being used to solve the
problem, along with its components and relevant parameter values. The
information in this section of the file is used to guide the interpretation
of the rest of the file.

### Problem Section

This section identifies the type of problem being solved, and provides its
relevant details (based on the type of the problem and the search method in
use).

### Search Section

This final section contains a detailed log of the search process.
