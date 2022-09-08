---
title: "Domain Generalization for Retinal Vessel Segmentation with Vector Field Transformer"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Domain Generalization for Retinal Vessel Segmentation with Vector Field Transformer

#### Dewei Hu, Hao Li, Han Liu, Ipek Oguz

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=mB_V8ThxY8Z">PDF</a>
- <a href="https://openreview.net/forum?id=mB_V8ThxY8Z">Reviews</a>

<p>
    <span class="abstract">
        Domain generalization has become a heated topic in the literature of deep learning. It has great impact on medical image analysis as the inconsistency of data distribution is prevalent in most of the medical data modalities due to the image acquisition techniques. In this study, we investigate a novel pipeline that generalizes the retinal vessel segmentation across color fundus photography and OCT angiography images. We hypothesize that the scaled minor eigenvector of the Hessian matrix can sufficiently represent the vessel by vector flow. This vector field can be regarded as a common domain for different modalities as it is very similar even for data that follows vastly different intensity distributions. We describe two additional contributions of our work. First, we leverage the uncertainty in the latent space of the auto-encoder to synthesize enhanced vessel maps to augment the training data. Then we propose a transformer network to extract features from the vector field. In comprehensive experiments, we show that our model can work in cross-modality fashion.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Friday 8th July<br>Poster Session 3.2 - onsite 11:00 - 12:00, virtual 15:20 - 16:20 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
{{ macros.video("https://video.midl.io/2022/long/113.mp4") }}
