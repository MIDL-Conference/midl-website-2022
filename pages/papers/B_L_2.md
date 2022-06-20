---
title: "FBNETGEN: Task-aware GNN-based fMRI Analysis via Functional Brain Network Generation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# FBNETGEN: Task-aware GNN-based fMRI Analysis via Functional Brain Network Generation

#### Xuan Kan, Hejie Cui, Joshua Lukemire, Ying Guo, Carl Yang

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=oWFphg2IKon">PDF</a>
- <a href="https://openreview.net/forum?id=oWFphg2IKon">Reviews</a>

<p>
    <span class="abstract">
        Functional magnetic resonance imaging (fMRI) is one of the most commonly used imaging modalities to investigate brain functions. Recent studies in neuroscience stress the great potential of functional brain networks constructed from fMRI data for clinical predictions. Traditional functional brain networks, however, are noisy and unaware of downstream prediction tasks, while also incompatible with the recent powerful deep learning models of graph neural networks (GNNs). In order to fully unleash the power of GNNs in network-based fMRI analysis, we develop FBNETGEN, a task-aware and interpretable fMRI analysis framework via deep brain network generation. In particular, we formulate (1) prominent region of interest (ROI) features extraction, (2) brain networks generation, and (3) clinical predictions with GNNs in an end-to-end trainable model under the guidance of particular prediction tasks. Along with the process, the key novel component is the graph generator which learns to transform raw time-series features into task-oriented brain networks. Our learnable graphs also provide unique interpretations by highlighting prediction-related brain regions. Comprehensive experiments on two datasets, i.e., the recently released and currently largest publicly available fMRI dataset Adolescent Brain Cognitive Development (ABCD), and the widely-used dataset PNC, prove the superior effectiveness and interpretability of FBNETGEN. The implementation is available at https://github.com/Wayfear/FBNETGEN.
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
