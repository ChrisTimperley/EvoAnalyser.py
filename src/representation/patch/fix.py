# Used to represent a single atomic fix within a candidate patch.
class Fix(object):

    # Calculates the precedence level of a given operation (e.g. deletion,
    # replacement, insertion). A lower level indicates a higher priority,
    # i.e. an operator with a precedence of 0 must be executed before an
    # operator with a precedence of 1.
    @staticmethod
    def op_precedence(op):
         return ({
            "delete":   0,
            "replace":  1,
            "insert":   2
        })[op]

    # Constructs a patch fix object from a log file definition.
    @staticmethod
    def load(definition):

        # Find the type of the fix.
        typ = ({
            "a": "insert",
            "r": "replace",
            "d": "delete"
        })[definition[0]]

        # Extract the location and surrogate SIDs.
        args = map(int, definition[2:-1].split(","))
        
        # Record the location SID of the fix.
        location = args[0]
        
        # Find the surrogate SID, if there is one.
        # If there isn't, then record the surrogate SID as None.
        surrogate = None if typ == "delete" else args[1]
        
        # Build the object.
        return Fix(typ, location, surrogate)

    # Constructs a patch fix object from its properties. 
    def __init__(self, typ, location, surrogate):
        self.typ = typ
        self.location = location
        self.surrogate = surrogate

    # Writes a fix object to a string.
    def to_string(self):

        # Produce the short fix type identifier.
        typ_short = ({
            "insert": "a",
            "replace": "r",
            "delete": "d"
        })[self.typ]

        # Compute the fix arguments.
        args = [self.location]
        if self.typ != "delete":
            args.append(self.surrogate)
        args = ",".join(map(str, args))

        # Put everything together into a string definition.
        return "%s(%s)" % (typ_short, args)

    # Calculates the precedence of the operator used by this fix. 
    def operator_precedence(self):
        return Fix.op_precedence(self.typ)
        
    # Compares this fix to another to determine which should be performed first.
    def __cmp__(self, other):
        
        # If the two fixes operate at different locations, the one that
        # operates at an earlier index comes first.
        if self.location != other.location:
            return cmp(self.location, other.location)

        # If the two fixes operate at the same location, then compare them
        # according to their operator precedence.
        else:
            return cmp(self.operator_precedence(), other.operator_precedence())


