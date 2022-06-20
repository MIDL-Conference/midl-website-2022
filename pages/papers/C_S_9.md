---
title: "Image-to-image translation trained on unrelated histopathology data helps for Domain Generalization"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Image-to-image translation trained on unrelated histopathology data helps for Domain Generalization

#### Marin Scalbert, Maria Vakalopoulou, Florent Couzinie-Devy

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=Ps_PWSvJkOI">PDF</a>
- <a href="https://openreview.net/forum?id=Ps_PWSvJkOI">Reviews</a>

<p>
    <span class="abstract">
        Histopathology Whole Slide Images (WSIs) present large illumination or color variations due to protocol variability (scanner, staining). This can strongly harm the generalization performances of deep learning algorithms. To address this problem, we propose to train a multi-domain image-to-image translation (I2IT) model on WSIs from The Cancer Genome Atlas Program (TCGA) and use it for data augmentation. Using TCGA WSIs from different cancer types has several advantages: our data augmentation method can be used for tasks where data is small, the I2IT model does not need to be relearned for each task and the variability of TCGA protocols is high leading to better robustness. The method efficiency is assessed on the Camelyon17 WILDS dataset where we outperform sophisticated data augmentations and domain generalization methods. Results also confirms that training the I2IT model on unrelated histopathology data is much more efficient for generalization than training it on the training data of the domain generalization (DG) task.
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
<!-- { macros.presentation('', '', 720, 450) } -->
