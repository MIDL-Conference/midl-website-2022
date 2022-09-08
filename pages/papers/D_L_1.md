---
title: "Speckle and Shadows: Ultrasound-specific Physics-based Data Augmentation Applied to Kidney Segmentation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Speckle and Shadows: Ultrasound-specific Physics-based Data Augmentation Applied to Kidney Segmentation

#### Rohit Singla, Cailin Ringstrom, Ricky Hu, Victoria Lessoway, Janice Reid, Chris Nguan, Robert Rohling

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=E_KsfOoVf9D">PDF</a>
- <a href="https://openreview.net/forum?id=E_KsfOoVf9D">Reviews</a>

<p>
    <span class="abstract">
        Data augmentation techniques are frequently used to prevent overfitting, enhance generalizability, and overcome limited amounts of data. This data-oriented approach commonly includes domain-agnostic techniques of geometric transformations, colour space changes, and generative adversarial networks. However, leveraging domain-specific traits in aug- mentations may yield further improvements. We propose three new contributions to ultrasound augmentation: zoom, artificial shadowing, and speckle parameter maps. We first present zoom, a modification on scale which maintains the ultrasound beam shape. We then characterize acoustic shadows within abdominal ultrasound images, and formulate a method to introduce artificial shadows in a realistic manner into existing images. Finally, we transform B-mode ultrasound images into speckle parameter maps based on the Nakagami distribution to represent spatial structures not obvious in conventional B-mode. The three augmentations are evaluated in training a fully supervised network and a contrastive learning network for multi-class intra-organ semantic segmentation. Our preliminary results demonstrate the benefit of using zoom and speckle maps as augmentation, and the challenges presented by acoustic shadowing, in segmentation.
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
{{ macros.video("https://video.midl.io/2022/long/37.mp4") }}
