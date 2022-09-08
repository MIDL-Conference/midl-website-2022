---
title: "Adaptive Gradient Triplet Loss with Automatic Margin Learning for Forensic Medical Image Matching"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Adaptive Gradient Triplet Loss with Automatic Margin Learning for Forensic Medical Image Matching

#### Khanh Nguyen, Hoang Huy Nguyen, Aleksei Tiulpin

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=LgO9mFejtNN">PDF</a>
- <a href="https://openreview.net/forum?id=LgO9mFejtNN">Reviews</a>

<p>
    <span class="abstract">
        This paper tackles the challenge of forensic medical image matching (FMIM) using deep neural networks (DNNs). We investigate Triplet loss (TL), which is probably the most well-known loss for this problem. TL aims to enforce closeness between similar and enlarge the distance between dissimilar data points in the image representation space extracted by a DNN. Although TL has been shown to perform well, it still has limitations, which we identify and analyze in this work. Specifically, we first introduce AdaTriplet -- an extension of TL that aims to adapt loss gradients according to the levels of difficulty of negative samples. Second, we also introduce AutoMargin -- a technique to adjust hyperparameters of margin-based losses such as TL and AdaTriplet dynamically during training. The performance of our loss is evaluated on a new large-scale benchmark for FMIM, which we have constructed from the Osteoarthritis Initiative cohort. The codes allowing replication of our results have been made publicly available at \url{https://github.com/Oulu-IMEDS/AdaTriplet}.
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
{{ macros.video("https://video.midl.io/2022/short/34.mp4") }}
