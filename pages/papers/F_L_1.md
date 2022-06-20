---
title: "MedSelect: Selective Labeling for Medical Image Classification Using Meta-Learning"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# MedSelect: Selective Labeling for Medical Image Classification Using Meta-Learning

#### Akshay Smit, Damir Vrabac, Yujie He, Andrew Y. Ng, Andrew Beam, Pranav Rajpurkar

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=GgLjvwvB8yF">PDF</a>
- <a href="https://openreview.net/forum?id=GgLjvwvB8yF">Reviews</a>

<p>
    <span class="abstract">
        We propose a selective labeling method using meta-learning for medical image interpretation in the setting of limited labeling resources. Our method, MedSelect, consists of a trainable deep learning model that uses image embeddings  to select   images to label, and a non-parametric classifier that uses cosine similarity to classify unseen images. We demonstrate that MedSelect learns an effective selection strategy outperforming baseline selection strategies across seen and unseen medical conditions for chest X-ray interpretation. We also perform an analysis of the selections performed by MedSelect comparing the distribution of latent embeddings and clinical features, and find significant differences compared to the strongest performing baseline. Our method is broadly applicable across medical imaging tasks where labels are expensive to acquire.
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
