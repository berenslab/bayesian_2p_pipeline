import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_roi(data, ax = False, cmap_roi = 'hls', cmap_bkg = 'viridis'):
    """
    Plot mean fluorescent image with superimposed ROI mask.    
    """
    mean_image = data['wDataCh0'].mean(axis = -1)
    roi_image = data['ROIs']

    i_rois = np.unique(roi_image)
    i_rois = i_rois[i_rois != 1]
    n_rois = len(i_rois)

    roi_rgba = np.zeros(list(roi_image.shape) + [4,])
    roi_rgba[roi_image != 1, :] = 1
    roi_colours = sns.color_palette(cmap_roi, n_rois)

    for itx, roi in enumerate(i_rois):
        roi_rgba[roi_image == roi, :] = list(roi_colours[itx]) + [1,]

    imshow_p = {
        'origin': 'lower',
        'interpolation': 'nearest'
    }

    if not ax:
        fig, ax = plt.subplots(1)

    ax.imshow(mean_image, cmap = cmap_bkg,  **imshow_p)
    ax.imshow(roi_rgba, **imshow_p)

    ax.grid(False)
    ax.set_xticklabels([]);
    ax.set_yticklabels([]);