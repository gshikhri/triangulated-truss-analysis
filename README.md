## triangulated-truss-analysis: Identify and label DNA origami based triangulated trusses from Electron microscopy images

DNA Origami based triangulated trusses [reported here](https://pubs.acs.org/doi/full/10.1021/acs.nanolett.6b00381), have been known to exhibit robust biophysical properties in solution (high persistence length)

Their bio-physical properties can be investigated from the electron micrographs. That would require using computer vision algorithms to identify (segment) individual structures from a wide field of view. This is here achieved using a combination of traditional computer vision algorithms:
- Adaptive thresholding
- Mathematical morphology (to create masks and skeletonized structures)
- Ridge detection filters
- Watershed segmentation

![](https://github.com/gshikhri/triangulated-truss-analysis/blob/main/instance_segmentation.png)

So far the algorithms can correctly segment trusses (some false positives when two trusses are touching). In future, I would like to implement RandomForest based pixel classifier for more robust segmentation. 

## Issues and questions
Triangulated-truss-analysis is a work in progress. If you need help or have suggestions or you want to report an issue, please do so in a reproducible example at the corresponding [GitHub page](https://github.com/gshikhri/triangulated-truss-analysis/issues).
