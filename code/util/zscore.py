def zscore(ndarray, single = True):
    """
    Center data. Rescale to standard deviation.
    """

    ndarray -= ndarray.mean() 
    ndarray /= ndarray.std()
        
    return ndarray