---
title: "SZLoc: A Multi-resolution Architecture for Automated Epileptic Seizure Localization from Scalp EEG"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# SZLoc: A Multi-resolution Architecture for Automated Epileptic Seizure Localization from Scalp EEG

#### Jeff Craley, Emily Johnson, Christophe C Jouny, David Hsu, Raheel Ahmed, Archana Venkataraman

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=yGgZ3iPrkJT">PDF</a>
- <a href="https://openreview.net/forum?id=yGgZ3iPrkJT">Reviews</a>

<p>
    <span class="abstract">
        We propose an end-to-end deep learning framework for epileptic seizure localization from scalp electroencephalography (EEG). Our architecture, SZLoc, extracts multi-resolution information via local (single channel) and global (cross-channel) CNN encodings. These interconnected representations are fused using a transformer layer. Leveraging its multi-resolution outputs, SZLoc derives three clinically interpretable outputs: electrode-level seizure activity, seizure onset zone localization, and identification of the EEG signal intervals that contribute to the final localization. From an optimization standpoint, we formulate a novel multi-task ensemble of loss functions to train SZLoc using inexact spatial and temporal labels of seizure onset. In this manner, SZLoc automatically learns phenomena at finer resolutions than the training labels. We validate our SZLoc framework and training paradigm on a clinical EEG dataset of 34 focal epilepsy patients. As compared to other deep learning baseline models, SZLoc achieves robust inter-patient seizure localization performance. We also demonstrate generalization of SZLoc to a second cohort of 16 epilepsy patients with different seizure characteristics and recorded at a different site. Taken together, SZLoc extends beyond the traditional paradigm of seizure detection by providing clinically relevant seizure localization information from coarse and inexact training labels.
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
{{ macros.video("https://video.midl.io/2022/long/75.mp4") }}
