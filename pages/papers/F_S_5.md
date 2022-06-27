---
title: "Graph Attention Network for Prostate Cancer Lymph Node Invasion Prediction"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Graph Attention Network for Prostate Cancer Lymph Node Invasion Prediction

#### Maxence Larose, Nawar Touma, Nicolas Raymond, Danahé LeBlanc, Fatemeh Rasekh, Bertrand Neveu, Hélène Hovington, Martin Vallières, Frédéric Pouliot, Louis Archambault

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=zIpx-MISaIA">PDF</a>
- <a href="https://openreview.net/forum?id=zIpx-MISaIA">Reviews</a>

<p>
    <span class="abstract">
        This work proposes the use of a graph attention network (GAT) model combining radiomics and clinical data to improve the performance and interpretability of lymph node invasion (LNI) prediction in high-grade prostate cancer (PCa). Experiments were conducted using an in-house dataset of 170 high-grade PCa (Gleason $\geq8$), each with FDG-PET/CT images acquired prior to prostatectomy. To ensure interpretable connections between patients, the graph structure was constructed by merging the most important radiomic shape-based CT feature and first-order intensity-based PET feature to the clinically relevant features. The performance of the GAT model was compared to random forest (RF) and support vector machine (SVM) classifiers. On the 30 patients test set, the models reached {AUC=0.765, bACC= 0.705}, {AUC=0.748, bACC=0.66} and {AUC=0.725,bACC=0.725} for the GAT, RF and SVM models respectively. Even though SVM achieved higher balanced accuracy than GAT, the predictions made by the latter are more interpretable through the graph structure and attention mechanism.
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
<!-- { macros.presentation('', '', 720, 450) } -->
