from cProfile import label
import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import io, filters, morphology, measure, feature, future, segmentation, util
from scipy import ndimage
from skimage.color import label2rgb
import os
import numpy as np
import pandas as pd
from functools import partial
from sklearn.ensemble import RandomForestClassifier
from scipy import ndimage

matplotlib.use('Qt5Agg')

in_folder = 'wireframe-tubes'

for _, _, filenames in os.walk(in_folder):
    for file in filenames[-2:-1]:
        truss_image = io.imread(os.path.join(in_folder, file))
        blur_truss_image = ndimage.gaussian_filter(truss_image, sigma=5)

        thresh = filters.threshold_otsu(blur_truss_image)
        binary = truss_image > thresh
        morphed_image = morphology.remove_small_objects(morphology.remove_small_holes(binary))

        clear = segmentation.clear_border(~morphed_image)
        modified_binary = morphology.binary_erosion(clear, np.ones(shape=(2, 2)))

        edges = filters.frangi(~modified_binary)

        eroded_edges = morphology.binary_erosion(edges, np.ones(shape=(12, 12)))

        labelled_image = measure.label(eroded_edges)
        
        binary_labelled = np.where(labelled_image != 0, 1, 0)
        
        # fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(10, 8))
        # ax[0][0].imshow(truss_image)
        # ax[0][1].imshow(binary_labelled)
        # ax[1][0].imshow(label2rgb(labelled_image, image=truss_image, bg_label=0))
        # ax[1][1].imshow(label2rgb(morphology.skeletonize(binary_labelled), image=truss_image, bg_label=0))
        # fig.suptitle(file)
        # fig.tight_layout()
        # plt.show()

        # now I will use the binary labelled image to create the skeletons 
        # that can be then used for the watershed

        markers = measure.label(morphology.skeletonize(eroded_edges))
        labels = segmentation.watershed(eroded_edges, markers)
        plt.imshow(segmentation.mark_boundaries(truss_image, labels))
        plt.show()
        


a = 2
