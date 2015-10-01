# A dictionary is used to store registered representations.
__representations = {}

# Registers a provided representation using a given name.
def register(name, cls):
    print "- registering visualisation: %s" % (name)
    if __representations.has_key(name):
        raise Exception("Failed to register representation: key already defined (%s)" % (name))
    __representations[name] = cls

# Retrives a representation with a given name.
def retrieve(name):
    if not __representations.has_key(name):
        raise Exception("Failed to find representation: %s" % (name))
    return __representations[name]
