import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import io, filters, morphology, feature, measure
from scipy import ndimage
from skimage.color import label2rgb

matplotlib.use('Qt5Agg')

in_folder = 'test_images'
file_name = 'tube dimer10.tif'

truss_image = io.imread(os.path.join(in_folder, file_name))

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
ax[0][0].imshow(truss_image)

thresh = filters.threshold_otsu(truss_image)
binary = truss_image > thresh

morphed_image = morphology.remove_small_objects(morphology.remove_small_holes(morphology.binary_opening(binary)))
ax[0][1].imshow(morphed_image)

edges = feature.canny(morphed_image)
ax[1][0].imshow(edges)

ax[1][1].imshow(label2rgb(measure.label(ndimage.binary_fill_holes(edges)), image=truss_image))

plt.show()

a = 2