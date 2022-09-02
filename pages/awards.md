---
title: "Awards"
---

{% from "_macros.html" import paper, button, youtube %}


## Best Paper Award

The **MIDL 2022 best paper award** recognizes the highest quality full-length paper presented at the conference.

### Best Paper Award - Winner
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_3.html">VORTEX: Physics-Driven Data Augmentations Using Consistency Training for Robust Accelerated MRI Reconstruction</a>
    </span>
    <span class="authors"> Arjun D Desai, Beliz Gunel, Batu Ozturkler, Harris Beg, Shreyas Vasanawala, Brian Hargreaves, Christopher Re, John M. Pauly, Akshay Chaudhari</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=WjwUeGh0yMK">pdf</a></li><li><a href="https://openreview.net/forum?id=WjwUeGh0yMK">reviews</a></li></ul><span class="abstract">
      Deep neural networks have enabled improved image quality and fast inference times for various inverse problems, including accelerated magnetic resonance imaging (MRI) reconstruction. However, such models require extensive fully-sampled ground truth datasets, which are difficult to curate and are sensitive to distribution drifts. In this work, we propose applying physics-driven data augmentations for consistency training that leverage our domain knowledge of the forward MRI data acquisition process and MRI physics to achieve improved data efficiency and robustness to clinically-relevant distribution drifts. Our approach, termed VORTEX, (1) demonstrates strong improvements over supervised baselines with and without data augmentation in robustness to signal-to-noise ratio change and motion corruption in data-limited regimes; (2) considerably outperforms state-of-the-art purely image-based data augmentation techniques and self-supervised reconstruction methods on both in-distribution and out-of-distribution data; and (3) enables composing heterogeneous image-based and physics-driven data augmentations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>

### Best Paper Award - Runner-up


<p><div class="None poster">
    <span class="title">
      <a href="papers/A2.html">Learning Shape Reconstruction from Sparse Measurements with Neural Implicit Functions</a>
    </span>
    <span class="authors"> Tamaz Amiranashvili, David Lüdke, Hongwei Li, Bjoern Menze, Stefan Zachow</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=UuHtdwRXkzw">pdf</a></li><li><a href="https://openreview.net/forum?id=UuHtdwRXkzw">reviews</a></li></ul><span class="abstract">
      Reconstructing anatomical shapes from sparse or partial measurements relies on prior knowledge of shape variations that occur within a given population. Such shape priors are learned from example shapes, obtained by segmenting volumetric medical images. For existing models, the resolution of a learned shape prior is limited to the resolution of the training data. However, in clinical practice, volumetric images are often acquired with highly anisotropic voxel sizes, e.g.\ to reduce image acquisition time in MRI or radiation exposure in CT imaging. The missing shape information between the slices prohibits existing methods to learn a high-resolution shape prior. We introduce a method for high-resolution shape reconstruction from sparse measurements without relying on high-resolution ground truth for training. Our method is based on neural implicit shape representations and learns a continuous shape prior only from highly anisotropic segmentations. Furthermore, it is able to learn from shapes with a varying field of view and can reconstruct from various sparse input configurations. We demonstrate its effectiveness on two anatomical structures: vertebra and femur, and successfully reconstruct high-resolution shapes from sparse segmentations, using as few as three orthogonal slices.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>

<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_11.html">Differentiable Boundary Point Extraction for Weakly Supervised Star-shaped Object Segmentation</a>
    </span>
    <span class="authors"> Robin Camarasa, Hoel Kervadec, Daniel Bos, Marleen de Bruijne</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=whpBn0oadz">pdf</a></li><li><a href="https://openreview.net/forum?id=whpBn0oadz">reviews</a></li></ul><span class="abstract">
      Although Deep Learning is the new gold standard in medical image segmentation, the annotation burden limits its expansion to clinical practice.  We also observe a mismatch between annotations required by deep learning methods designed with pixel-wise optimization in mind and clinically relevant annotations designed for biomarkers extraction (diameters, counts, etc.). Our study proposes a first step toward bridging this gap, optimizing vessel segmentation based on its diameter annotations. To do so we propose to extract boundary points from a star-shaped segmentation in a differentiable manner. This differentiable extraction allows reducing annotation burden as instead of the pixel-wise segmentation only the two annotated points required for diameter measurement are used for training the model. Our experiments show that training based on diameter is efficient; produces state-of-the-art weakly supervised segmentation; and performs reasonably compared to full supervision. 
oindent Our code is publicly available:url{https:anonymous.4open.sciencerBoundary-Point-Extraction-F163}
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>