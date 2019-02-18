import numpy as np

def compute_cluster_freq(h_clusters):
    """
    Compute the frequency of each cluster at each layer of the hierarchy.
    """
    maxclust = h_clusters.shape[0]
    cluster_freq = np.zeros([maxclust, maxclust])
    
    for itx in range(maxclust):
        cluster_row = h_clusters[itx, :]
        
        for cluster_id in np.unique(cluster_row):
            cluster_freq[itx, :] = np.histogram(h_clusters[itx, :], bins = np.arange(maxclust + 1))[0]
            
    return cluster_freq