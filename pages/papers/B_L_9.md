---
title: "Deep Learning Radiographic Assessment of Pulmonary Edema: Training with Serum Biomarkers"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Deep Learning Radiographic Assessment of Pulmonary Edema: Training with Serum Biomarkers

#### Justin Huynh, Samira Masoudi, Abraham Noorbakhsh, Amin Mahmoodi, Kyle Hasenstab, Micheal Pazzani, Albert Hsiao

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=NyxXpTbHUCJ">PDF</a>
- <a href="https://openreview.net/forum?id=NyxXpTbHUCJ">Reviews</a>

<p>
    <span class="abstract">
        A major obstacle faced when developing convolutional neural networks (CNNs) for medical imaging is the acquisition of training labels: most current approaches rely on manually prescribed labels from physicians, which are time consuming and labor intensive to attain. Clinical biomarkers, often measured alongside medical images and used in diagnostic workup, may provide a rich set of data that can be collected retrospectively and utilized to train diagnostic models. In this work, we focused on the blood serum biomarkers BNP and BNPP, indicative of acute heart failure (HF) and cardiogenic pulmonary edema, paired with the chest X-ray imaging modality. We investigated the potential for inferring BNP and BNPP from chest radiographs. For this purpose, a CNN was trained using 28090 radiographs to automatically infer BNP and BNPP, and achieved strong performance ($AUC=0.903$, $r=0.787$). Since radiographic features of pulmonary edema may not be visible on low resolution images, we also assessed the impact of image resolution on model learning and performance, comparing CNNs trained at five image sizes ($64\times64$ to $1024\times1024$). With comparable AUC values obtained at different resolutions, our experiments using three activation mapping techniques (saliency, Grad-CAM, XRAI) revealed considerable in-lung attention growth with increased resolution. The highest resolution models focus attention on the lungs, necessary for radiographic diagnosis of pulmonary edema. Our results emphasize the need to utilize radiographs of near-native resolution for optimal CNN performance, not fully captured by summary metrics like AUC.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Wednesday 6th July<br>Poster Session 1.2 - onsite 11:00 - 12:00, virtual 15:20 - 16:20 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->
