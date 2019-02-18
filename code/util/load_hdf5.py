import h5py

def load_hdf5(path): 
    """ 
    Load HDF5 file from filepath. Store contents in dictionary.
    """
    return {key:item[:] for key, item in h5py.File(path, 'r').items()}