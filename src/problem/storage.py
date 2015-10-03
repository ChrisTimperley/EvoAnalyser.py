# A dictionary is used to store registered problem classes.
__problems = {}

# Registers a provided problem class under a given name.
def register(cls):
    name = cls.class_name()
    print "- registering problem class: %s" % (name)
    if __problems.has_key(name):
        raise Exception("Failed to register problem class: key already defined (%s)" % (name))
    __problems[name] = cls

# Retrives a problem class with a given name.
def retrieve(name):
    if not __problems.has_key(name):
        raise Exception("Failed to find problem class: %s" % (name))
    return __problems[name]
