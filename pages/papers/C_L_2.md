---
title: "Unsupervised Domain Adaptation through Shape Modeling for Medical Image Segmentation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Unsupervised Domain Adaptation through Shape Modeling for Medical Image Segmentation

#### Yuan Yao, Fengze Liu, Zongwei Zhou, Yan Wang, Wei Shen, Alan Yuille, Yongyi Lu

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=CwXCs6HObSw">PDF</a>
- <a href="https://openreview.net/forum?id=CwXCs6HObSw">Reviews</a>

<p>
    <span class="abstract">
        Shape information is a strong and useful prior in segmenting organs in medical image. However, most current deep learning based segmentation algorithms don’t take shape information into consideration, which can lead to bias towards texture. We aim at modeling shape explicitly and use it to help medical image segmentation. Previous methods proposed variational autoencoder (VAE) based models to learn the distribution of shape for a certain organ, and used it to automatically evaluate the quality of a segmentation prediction by fitting it into the learned shape distribution. Based on which we aim at incorporating VAE into current segmentation pipelines. Specifically, we propose a new unsupervised domain adaptation pipeline based on a pseudo loss and a VAE reconstruction loss under a teacher-student learning paradigm. Both losses are optimized simultaneously and in return, boosts the segmentation task performance. Extensive experiments on three public Pancreas segmentation datasets as well as one in-house Pancreas segmentation dataset demonstrate the effectiveness of our method in challenging unsupervised domain adaptation scenario for medical image segmentation. We hope this work will advance shape analysis and geometric learning in medical imaging.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Thursday 7th July<br>Poster Session 2.1 - onsite 15:20 - 16:20, virtual 11:00 - 12:00 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->
