import visualisation.storage as storage

def visualise(visualisation, data, options = {}):
    return storage.retrieve(visualisation)().draw(data, options)
