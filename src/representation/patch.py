import storage

class Patch(Representation):
    
    @staticmethod
    def read(definition):
        pass

    def __init__(self):

storage.register("patch", Patch)
