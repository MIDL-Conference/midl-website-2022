---
title: "SPA: Shape-Prior Variational Autoencoders for Unsupervised Brain Pathology Segmentation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# SPA: Shape-Prior Variational Autoencoders for Unsupervised Brain Pathology Segmentation

#### Cosmin I. Bercea, Benedikt Wiestler, Daniel Rueckert, Shadi Albarqouni

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=mB_V8ThxY8Z">PDF</a>
- <a href="https://openreview.net/forum?id=mB_V8ThxY8Z">Reviews</a>

<p>
    <span class="abstract">
        Deep unsupervised representation learning for brain pathology segmentation is of great interest for medical imaging, as it does not require extensive annotations for training and allows the detection of unseen pathologies. While recent approaches proposed to model the distribution of healthy brain Magnetic Resonance Imaging (MRI) using variational autoencoders, we propose to model the pixel distribution of the healthy brain by introducing a shape-prior based on the brain tissue distribution.  To this end, we propose Shape-Prior variational Autoencoders (SPA) to disentangle the generative factors of brain MRI, namely cerebrospinal fluid (CSF), gray matter (GM), and white matter (WM). Our method obtains interpretable latent representations, providing pixel-wise tissue probability maps. We evaluated the proposed method on MRIs of 538 patients from six data-sets containing demyelinating lesions, small vessel disease, and tumors. Experimental results indicate that our method is capable of disentangling the generative brain MR factors and avoiding the reconstruction of anomalous regions, leading to better lesion detection performance.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Thursday 7th July<br>Poster Session 2.2 - onsite 11:00 - 12:00, virtual 15:20 - 16:20 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->

{% import "_macros.html" as macros %}

# On the Pitfalls of Using the Residual as Anomaly Score

#### Felix Meissen, Benedikt Wiestler, Georgios Kaissis, Daniel Rueckert

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=ZsoHLeupa1D">PDF</a>
- <a href="https://openreview.net/forum?id=ZsoHLeupa1D">Reviews</a>

<p>
    <span class="abstract">
        Many current state-of-the-art methods for anomaly detection in medical images rely on calculating a residual image between a potentially anomalous input image and its ("healthy") reconstruction. As the reconstruction of the unseen anomalous region should be erroneous, this yields large residuals as a score to detect anomalies in medical images. However, this assumption does not take into account residuals resulting from imperfect reconstructions of the machine learning models used. Such errors can easily overshadow residuals of interest and therefore strongly question the use of residual images as scoring function. Our work explores this fundamental problem of residual images in detail. We theoretically define the problem and thoroughly evaluate the influence of intensity and texture of anomalies against the effect of imperfect reconstructions in a series of experiments.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Friday 8th July<br>Poster Session 3.1 - onsite 15:20 - 16:20, virtual 11:00 - 12:00 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->
