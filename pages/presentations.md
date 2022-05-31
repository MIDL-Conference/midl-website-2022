---
title: "Oral Presentations"
---

{% from "_macros.html" import paper %}

# Scientific program

## Wednesday 6th July
<a id="oral1-1"></a><h3>Oral Session 1.1 - 10:00 - 10:40 (UTC+2)</h3>
[% .papers %]
{{ paper('Left Ventricle Contouring in Cardiac Images Based on Deep Reinforcement Learning',
        'Sixing Yin, Yameng Han, Judong Pan, Yining Wang, Shufang Li',
        openreview='https://openreview.net/forum?id=2CakDDr9e9L',
        pdf='https://openreview.net/pdf?id=2CakDDr9e9L',
        id='A1',
        paper='papers/A1.html',
        <!-- proceedings='', -->
        <!-- video='', -->
        abstract='Assessment of the left ventricle segmentation in cardiac magnetic resonance imaging (MRI) is of crucial importance for cardiac disease diagnosis. However, conventional manual segmentation is a tedious task that requires excessive human effort, which makes automated segmentation highly desirable in practice to facilitate the process of clinical diagnosis. In this paper, we propose a novel reinforcement-learning-based framework for left ventricle contouring, which mimics how a cardiologist outlines the left ventricle along a specific trajectory in a cardiac image. Following the algorithm of proximal policy optimization (PPO), we train a policy network, which makes a stochastic decision on the agent's movement according to its local observation such that the generated trajectory matches the true contour of the left ventricle as much as possible. Moreover, we design a deep learning model with a customized loss function to generate the agent's landing spot (or coordinate of its initial position on a cardiac image). The experiment results show that the coordinate of the generated landing spot is sufficiently close to the true contour and the proposed reinforcement-learning-based approach outperforms the existing U-net model even with limited training set.')
}}
{{ paper('Learning Shape Reconstruction from Sparse Measurements with Neural Implicit Functions',
        'Tamaz Amiranashvili, David Lüdke, Hongwei Li, Bjoern Menze, Stefan Zachow',
        openreview='https://openreview.net/forum?id=UuHtdwRXkzw',
        pdf='hhttps://openreview.net/pdf?id=UuHtdwRXkzw',
        id='A2',
        paper='papers/A2.html',
        <!-- proceedings='', -->
        <!-- video='', -->
        abstract='Reconstructing anatomical shapes from sparse or partial measurements relies on prior knowledge of shape variations that occur within a given population. Such shape priors are learned from example shapes, obtained by segmenting volumetric medical images. For existing models, the resolution of a learned shape prior is limited to the resolution of the training data. However, in clinical practice, volumetric images are often acquired with highly anisotropic voxel sizes, e.g. to reduce image acquisition time in MRI or radiation exposure in CT imaging. The missing shape information between the slices prohibits existing methods to learn a high-resolution shape prior. We introduce a method for high-resolution shape reconstruction from sparse measurements without relying on high-resolution ground truth for training. Our method is based on neural implicit shape representations and learns a continuous shape prior only from highly anisotropic segmentations. Furthermore, it is able to learn from shapes with a varying field of view and can reconstruct from various sparse input configurations. We demonstrate its effectiveness on two anatomical structures: vertebra and distal femur, and successfully reconstruct high-resolution shapes from sparse segmentations, using as few as three orthogonal slices.')
}}
{{ paper('Are 2.5D approaches superior to 3D deep networks in whole brain segmentation?',
        'Saikat Roy, David Kügler, Martin Reuter',
        openreview='https://openreview.net/forum?id=Ob62JPB_CDF',
        pdf='https://openreview.net/pdf?id=Ob62JPB_CDF',
        id='A3',
        paper='papers/A3.html',
        <!-- proceedings='', -->
        <!-- video='', -->
        abstract='Segmentation of 3D volumes with a large number of labels, small convoluted structures, and lack of contrast between various structural boundaries is a difficult task. While recent methodological advances across many segmentation tasks are dominated by 3D architectures, currently the strongest performing method for whole brain segmentation is FastSurferCNN, a 2.5D approach. To shed light on the nuanced differences between 2.5D and various 3D approaches, we perform a thorough and fair comparison and suggest a spatially-ensembled 3D architecture. Interestingly, we observe training memory intensive 3D segmentation on full-view images does not outperform the 2.5D approach. A shift to training on patches even while evaluating on full-view solves these limitations of both memory and performance limitations at the same time. We demonstrate significant performance improvements over state-of-the-art 3D methods on both Dice Similarity Coefficient and especially average Hausdorff Distance measures across five datasets. Finally, our validation across variations of neurodegenerative disease states and scanner manufacturers, shows we outperform the previously leading 2.5D approach FastSurferCNN demonstrating robust segmentation performance in realistic settings.')
}}
[% / %]
<a id="oral1-2"></a><h3>Oral Session 1.2 - 13:20 - 14:00 (UTC+2)</h3>
