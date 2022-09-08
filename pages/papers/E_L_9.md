---
title: "Orientation Estimation of Abdominal Ultrasound Images with Multi-Hypotheses Networks"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Orientation Estimation of Abdominal Ultrasound Images with Multi-Hypotheses Networks

#### Timo Horstmann, Oliver Zettinig, Wolfgang Wein, Raphael Prevost

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=1gsauv2B7Ar">PDF</a>
- <a href="https://openreview.net/forum?id=1gsauv2B7Ar">Reviews</a>

<p>
    <span class="abstract">
        Ultrasound imaging can provide valuable information to clinicians during interventions, in particular when fused with other modalities. Multi-modal image registration algorithms however require a somewhat accurate initialization, which is particularly difficult to estimate for ultrasound images as their orientation is arbitrary and their content ambiguous (limited field of view, artifacts, etc.). In this work, we train neural networks to predict the absolute orientation of ultrasound frames, but also to produce a confidence for each prediction. This allows us to select only the most confident frames in the clip. Our networks are trained to produce multiple hypotheses using a simple yet overlooked meta-loss that is specifically designed to capture the ambiguity of the input data.  We show on several abdominal ultrasound datasets that multi-hypotheses networks provide better uncertainty estimates than Monte-Carlo dropout while being more efficient than network ensembling. Generic, easy to implement and able to quantify both data ambiguity and out-of-distribution samples, they represent a preferable alternative to traditional baselines for uncertainty estimation. Our method produces on a clinical test estimates within $20^{\circ}$ of the true orientation, which we can use to improve the accuracy of a subsequent registration algorithm down to less than $10^{\circ}$.
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
{{ macros.video("https://video.midl.io/2022/long/186.mp4") }}
