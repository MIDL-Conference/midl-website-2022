---
title: "Interpretable Prediction of Lung Squamous Cell Carcinoma Recurrence With Self-supervised Learning"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Interpretable Prediction of Lung Squamous Cell Carcinoma Recurrence With Self-supervised Learning

#### Weicheng Zhu, Carlos Fernandez-Granda, Narges Razavian

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=QBg9YNm26FF">PDF</a>
- <a href="https://openreview.net/forum?id=QBg9YNm26FF">Reviews</a>

<p>
    <span class="abstract">
        Lung squamous cell carcinoma (LSCC) has a high recurrence and metastasis rate. Factors influencing recurrence and metastasis are currently unknown and there are no distinct histopathological or morphological features indicating the risks of recurrence and metastasis in LSCC. Our study focuses on the recurrence prediction of LSCC based on H&E-stained histopathological whole-slide images (WSI). Due to the small size of LSCC cohorts in terms of patients with available recurrence information, standard end-to-end learning with various convolutional neural networks for this task tends to overfit. Also, the predictions made by these models are hard to interpret. Histopathology WSIs are typically very large and are therefore processed as a set of smaller tiles. In this work, we propose a novel conditional self-supervised learning (SSL) method to learn representations of WSI at the tile level first, and leverage clustering algorithms to identify the tiles with similar histopathological representations. The resulting representations and clusters from self-supervision are used as features of a survival model for recurrence prediction at the patient level. Using two publicly available datasets from TCGA and CPTAC, we show that our LSCC recurrence prediction survival model outperforms both LSCC pathological stage-based approach and machine learning baselines such as multiple instance learning. The proposed method also enables us to explain the recurrence histopathological risk factors via the derived clusters. This can help pathologists derive new hypotheses regarding morphological features associated with LSCC recurrence.
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
