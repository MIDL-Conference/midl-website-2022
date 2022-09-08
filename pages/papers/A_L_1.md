---
title: "Regularizing Brain Age Prediction via Gated Knowledge Distillation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Regularizing Brain Age Prediction via Gated Knowledge Distillation

#### Yanwu Yang, Guo Xutao, Chenfei Ye, Yang Xiang, Ting Ma

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=nxA2bZff3iQ">PDF</a>
- <a href="https://openreview.net/forum?id=nxA2bZff3iQ">Reviews</a>

<p>
    <span class="abstract">
        The brain age has been proven to be a phenotype of relevance to cognitive performance and brain disease. Recently, brain age estimation accuracy has been greatly improved by using deep learning. However, deep neural networks with millions of parameters may incur overfitting and suffer from poor generalizations, especially for insufficient brain imaging data. This paper presents a novel regularization method that penalizes the predictive distribution using knowledge distillation and introduces additional knowledge to reinforce the learning process. During knowledge distillation, we propose a gated distillation mechanism to enable the student model to attentively learn meaningful knowledge from the teacher model, given the assumption that a teacher might not always be correct. Moreover, to enhance the capability of knowledge transfer, the hint representation similarity is also adopted to regularize the model for training. Our evaluation on a cohort of 3655 subjects from four public datasets with ages range of 16-92, demonstrates that our proposed method improves the prediction performance over a series of well-established models, where the mean absolute error of the estimated ages is reduced to 2.129 years.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Wednesday 6th July<br>Poster Session 1.1 - onsite 15:20 - 16:20, virtual 11:00 - 12:00 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
{{ macros.video("https://video.midl.io/2022/long/16.mp4") }}
