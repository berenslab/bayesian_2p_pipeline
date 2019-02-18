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

def generate_contrasts(h_clusters):
    """
    Use cluster frequencies to generate an orthogonal contrast code.
    """
    cluster_freq = compute_cluster_freq(h_clusters)

    maxclust, n_rois = h_clusters.shape
    
    contrast_code = np.zeros([maxclust - 1, n_rois])

    for i_node in range(maxclust - 1):
        change_mask = np.diff(cluster_freq, axis = 0)[i_node, :] != 0

        row_freq = cluster_freq[i_node + 1, change_mask] 
        row_freq = 1 / row_freq
        row_freq[0] *= - 1

        i_cluster = np.arange(maxclust)

        for itx, cluster in enumerate(i_cluster[change_mask]):
            cluster_mask = h_clusters[i_node + 1, :] == cluster
            contrast_code[i_node, cluster_mask] = row_freq[itx]
            
    return contrast_code
