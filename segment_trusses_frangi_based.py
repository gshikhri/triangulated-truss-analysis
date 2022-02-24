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

        thresh = filters.threshold_otsu(truss_image)
        binary = truss_image > thresh
        morphed_image = morphology.remove_small_objects(morphology.remove_small_holes(binary))

        edges = filters.frangi(morphed_image)
        eroded_edges = morphology.binary_erosion(edges, np.ones(shape=(10, 10)))

        labelled_image = measure.label(eroded_edges)

        regions = measure.regionprops_table(label_image=labelled_image, \
            intensity_image=truss_image, properties=('label', 'area'))
        df = pd.DataFrame(regions)
        outlier_range = np.quantile(df['area'], [0, 1])
        bad_labels = df[~df['area'].between(*outlier_range)].dropna()['label'].to_numpy().astype(np.int16)
        for i in list(bad_labels):
            labelled_image = np.where(labelled_image == i, 0, labelled_image)
        
        binary_labelled = np.where(labelled_image != 0, 1, 0)
        
        fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(10, 8))
        ax[0].imshow(truss_image)
        ax[1].imshow(binary_labelled)
        ax[2].imshow(label2rgb(labelled_image, image=truss_image, bg_label=0))
        fig.suptitle(file)
        fig.tight_layout()
        plt.show()

        # fig, ax = plt.subplots()
        # ax.imshow(label2rgb(morphology.skeletonize(binary_labelled), image=truss_image, bg_label=0))
        # fig.suptitle(file)
        # plt.show()

a = 2
