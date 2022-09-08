---
title: "Learning Strategies for Contrast-agnostic Segmentation via SynthSeg for Infant MRI data"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Learning Strategies for Contrast-agnostic Segmentation via SynthSeg for Infant MRI data

#### Ziyao Shang, Md Asadullah Turja, Eric Feczko, Audrey Houghton, Amanda Rueter, Lucille A Moore, Kathy Snider, Timothy Hendrickson, Paul Reiners, Sally Stoyell, Omid Kardan, Monica Rosenberg, Jed T Elison, Damien A Fair, Martin Andreas Styner

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=MOYTPAvLluZ">PDF</a>
- <a href="https://openreview.net/forum?id=MOYTPAvLluZ">Reviews</a>

<p>
    <span class="abstract">
        Longitudinal studies of infants' brains are essential for research and clinical detection of Neurodevelopmental Disorders. However, for infant brain MRI scans, effective deep learning-based  segmentation frameworks exist only within small age intervals due the large image intensity and contrast changes that take place in the early postnatal stages of development. However, using different segmentation frameworks or models at different age intervals within the same longitudinal data set would cause segmentation inconsistencies and age-specific biases. Thus, an age-agnostic segmentation model for infants' brains is needed. In this paper, we present "Infant-SynthSeg", an extension of the contrast-agnostic SynthSeg segmentation framework applicable to MRI data of infant at ages within the first year of life. Our work mainly focuses on extending learning strategies related to synthetic data generation and augmentation, with the aim of creating a method that employs training data capturing features unique to infants' brains during this early-stage development. Comparison across different learning strategy settings, as well as a more-traditional contrast-aware deep learning model (NN-Unet) are presented. Our experiments show that our trained Infant-SynthSeg models show consistently high segmentation performance on MRI scans of infant brains throughout the first year of life. Furthermore, as the model is trained on ground truth labels at different ages, even labels that are not present at certain ages (such as cerebellar white matter at 1 month) can be appropriately segmented via Infant-SynthSeg across the whole age range. Finally, while Infant-SynthSeg shows consistent segmentation performance across the first year of life, it is outperformed by age-specific deep learning models trained for a specific narrow age range.
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
{{ macros.video("https://video.midl.io/2022/long/134.mp4") }}
