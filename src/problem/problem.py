class Problem(object):
    
    """
    Creates a new object for a given problem instance.
    """
    def __init__(self, name):
        self.__name = name

    """
    Returns the name of this problem instance.
    """
    def name(self):
        return self.__name

    """
    Returns the name of this problem type.
    """
    def type_name(self):
        return self.__class__.class_name()
