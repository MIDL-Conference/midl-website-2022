---
title: "OptTTA: Learnable Test-Time Augmentation for Source-Free Medical Image Segmentation Under Domain Shift"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# OptTTA: Learnable Test-Time Augmentation for Source-Free Medical Image Segmentation Under Domain Shift

#### Devavrat Tomar, Guillaume Vray, Jean-Philippe Thiran, Behzad Bozorgtabar

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=B6HdQaY_iR">PDF</a>
- <a href="https://openreview.net/forum?id=B6HdQaY_iR">Reviews</a>

<p>
    <span class="abstract">
        As distribution shifts are inescapable in realistic clinical scenarios due to inconsistencies in imaging protocols, scanner vendors, and across different centers, well-trained deep models incur a domain generalization problem in unseen environments. Despite a myriad of model generalization techniques to circumvent this issue, their broad applicability is impeded as (i) source training data may not be accessible after deployment due to privacy regulations, (ii) the availability of adequate test domain samples is often impractical, and (iii) such model generalization methods are not well-calibrated, often making unreliable overconfident predictions. This paper proposes a novel learnable test-time augmentation, namely OptTTA, tailored specifically to alleviate large domain shifts for the source-free medical image segmentation task. OptTTA enables efficiently generating augmented views of test input, resembling the style of private source images and bridging a domain gap between training and test data. Our proposed method explores optimal learnable test-time augmentation sub-policies that provide lower predictive entropy and match the source model's internal batch normalization statistics without requiring access to training source samples. Thorough evaluation and ablation studies on challenging multi-center and multi-vendor MRI datasets of three anatomies have demonstrated the performance superiority of OptTTA over prior-arts test-time augmentation and model adaptation methods. Additionally, the generalization capabilities and effectiveness of OptTTA are evaluated in terms of aleatoric uncertainty and model calibration analyses. Our PyTorch code implementation is publicly available at https://github.com/devavratTomar/OptTTA.
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
{{ macros.video("https://video.midl.io/2022/long/18.mp4") }}

{{ macros.video("https://video.midl.io/2022/live/18.mp4") }}