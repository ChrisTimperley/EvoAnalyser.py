# A dictionary is used to store registered visualisations.
__visualisations = {}

# Registers a provided visualisation using a given name.
def register(name, cls):
    print "- registering visualisation: %s" % (name)
    if __visualisations.has_key(name):
        raise Exception("Failed to register visualisation: key already defined (%s)" % (name))
    __visualisations[name] = cls

# Retrives a visualisation with a given name.
def retrieve(name):
    if not __visualisations.has_key(name):
        raise Exception("Failed to find visualisation: %s" % (name))
    return __visualisations[name]
