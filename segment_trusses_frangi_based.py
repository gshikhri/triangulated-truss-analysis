import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import io, filters, morphology, measure
from scipy import ndimage
from skimage.color import label2rgb
import os

matplotlib.use('Qt5Agg')

in_folder = 'wireframe-tubes'

for _, _, filenames in os.walk(in_folder):
    for file in filenames[:]:
        truss_image = io.imread(os.path.join(in_folder, file))[128:640, 128:640]

        thresh = filters.threshold_otsu(truss_image)
        binary = truss_image > thresh
        morphed_image = morphology.remove_small_objects(morphology.remove_small_holes(binary))
        edges = filters.frangi(morphed_image)
        dilated_edges = morphology.binary_dilation(edges)

        labelled_image = measure.label(dilated_edges)

        fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
        ax[0][0].imshow(truss_image)
        ax[0][1].imshow(morphed_image)
        ax[1][0].imshow(edges)
        ax[1][1].imshow(dilated_edges)
        ax[1][1].imshow(label2rgb(labelled_image, image=truss_image, bg_label=0))
        fig.suptitle(file)
        plt.show()



# fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
# ax[0].imshow(labelled_image)

# labelled_image[labelled_image <=1] = 0
# labelled_image[labelled_image >=2] = 1

# ax[1].imshow(labelled_image)

# ax[2].imshow(morphology.skeletonize(labelled_image))

# plt.show()

# io.imsave(os.path.splitext(file_name)[0] + str('_skeleton.tif'), morphology.skeletonize(labelled_image))
a = 2