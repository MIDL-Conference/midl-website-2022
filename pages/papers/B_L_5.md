---
title: "TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces

#### Andrew Hoopes, Juan Eugenio Iglesias, Bruce Fischl, Douglas Greve, Adrian V Dalca

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=-JiHeZNDY3a">PDF</a>
- <a href="https://openreview.net/forum?id=-JiHeZNDY3a">Reviews</a>

<p>
    <span class="abstract">
        Mesh-based reconstruction of the cerebral cortex is a fundamental component in brain image analysis. Classical, iterative pipelines for cortical modeling are robust but often time-consuming, mostly due to expensive procedures that involve topology correction and spherical mapping. Recent attempts to address reconstruction with machine learning methods have accelerated some components in these pipelines, but they still require slow processing steps to enforce topological constraints to comply with known anatomical structure. In this work, we introduce a novel learning-based strategy, TopoFit, which rapidly fits a topologically-correct surface to the white-matter tissue boundary. We design a joint network with image and graph convolutions and an efficient symmetric distance loss to learn to predict accurate deformations that map a template mesh to subject-specific anatomy. This technique encompasses the work of current mesh correction, fine-tuning, and inflation steps and, as a result, offers a $150\times$ faster solution to cortical surface reconstruction compared to traditional approaches. We demonstrate that TopoFit is robust to common failure modes, such as white-matter tissue hypointensities, and is $1.8\times$ more accurate than current state-of-the-art deep-learning strategy. 
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
{{ macros.video("https://video.midl.io/2022/long/137.mp4") }}

{{ macros.video("https://video.midl.io/2022/live/137.mp4") }}