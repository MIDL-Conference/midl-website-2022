---
title: "Attention-Guided Prostate Lesion Localization and Grade Group Classification with Multiple Instance Learning"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Attention-Guided Prostate Lesion Localization and Grade Group Classification with Multiple Instance Learning

#### Ekaterina Redekop, Karthik V. Sarma, Adam Kinnaird, Anthony Sisk, Steven S. Raman, Leonard S. Marks, William Speier, Corey W. Arnold

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=QDJhkKy5x4q">PDF</a>
- <a href="https://openreview.net/forum?id=QDJhkKy5x4q">Reviews</a>

<p>
    <span class="abstract">
        Prostate lesion localization is a component of the prostate magnetic resonance imaging (MRI) routine evaluation. Localization is essential for targeted biopsy by enabling registration with real-time ultrasound. Most previous work on prostate cancer localization was focused on classification or segmentation assuming availability of radiological annotations. In this work we propose to use unsipervised attention-based multiple instance learning (MIL) method in an application for the prediction and localization of clinically significant prostate cancer. We train our model end-to-end with only image-level labels instead of relying on expensive pixel-level annotations. We extend MIL method by operating both on patches and the whole size image to learn local and global features which further improves classification and localization performance. To better leverage the relationships between multi-modal data we use an architecture with multiple encoding paths, where each path processing one image modality respectively. The model was developed on dataset containing 986 multiparametric prostate MRI and achieved 0.75 ±0.03 AUROC using 3-fold cross-validation in prostate cancer Grade Group classification.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Friday 7th July<br>Poster Session 3.2 - onsite 11:00 - 12:00, virtual 15:20 - 16:20 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->
