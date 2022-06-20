---
title: "CAiD: Context-Aware Instance Discrimination for Self-supervised Learning in Medical Imaging"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# CAiD: Context-Aware Instance Discrimination for Self-supervised Learning in Medical Imaging

#### Mohammad Reza Hosseinzadeh Taher, Fatemeh Haghighi, Michael Gotway, Jianming Liang

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=PNAdmb_Ujf">PDF</a>
- <a href="https://openreview.net/forum?id=PNAdmb_Ujf">Reviews</a>

<p>
    <span class="abstract">
        Recently, self-supervised instance discrimination methods have achieved significant success in learning visual representations from unlabeled natural images. However, given the marked differences between natural and medical images, the efficacy of instance-based objectives, focusing on the most discriminative global feature in the image (i.e., cycle in bicycle), remains unknown in medical imaging. Our preliminary analysis showed that high global similarity of medical images in terms of anatomy hampers instance discrimination methods in capturing a set of distinct features, negatively impacting their performance on medical downstream tasks. To alleviate this limitation, we have developed a simple yet effective self-supervised framework, called Context-Aware instance Discrimination (CAiD). CAiD aims to improve instance discrimination learning by providing finer and more discriminative information encoded from diverse local context of unlabeled medical images. We conduct a systematic analysis to investigate the utility of the learned features from a three-pronged perspective: (i) generalizability and transferability, (ii) separability in the embedding space, and (iii) reusability. Our extensive experiments demonstrate that CAiD (1) enriches representations learned from existing instance discrimination methods; (2) delivers more discriminative features by adequately capturing finer contextual information from individual medial images; and (3) improves reusability of low/mid-level features compared to standard instance discriminative methods. As open science, all codes and pre-trained models are available on our GitHub page: https://github.com/JLiangLab/CAiD.
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
