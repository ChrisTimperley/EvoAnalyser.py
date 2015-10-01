import visualisation.storage as storage

def visualise(data, visualisation, options):
    storage.retrieve(visualisation)(data).draw(options)
