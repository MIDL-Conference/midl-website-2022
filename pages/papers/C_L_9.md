---
title: "On learning adaptive acquisition policies for undersampled multi-coil MRI reconstruction"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# On learning adaptive acquisition policies for undersampled multi-coil MRI reconstruction

#### Tim Bakker, Matthew J. Muckley, Adriana Romero-Soriano, Michal Drozdzal, Luis Pineda

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=eAkOp9Oet5y">PDF</a>
- <a href="https://openreview.net/forum?id=eAkOp9Oet5y">Reviews</a>

<p>
    <span class="abstract">
        Most current approaches to undersampled multi-coil MRI reconstruction focus on learning the reconstruction model for a fixed, equidistant acquisition trajectory. In this paper, we study the problem of joint learning of the reconstruction model together with acquisition policies. To this end, we extend the End-to-End Variational Network with learnable acquisition policies that can adapt to different data points. We validate our model on a coil-compressed version of the large scale undersampled multi-coil \fastMRI dataset using two undersampling factors: $4\times$ and $8\times$. Our experiments show that we are able to outperform the learnable non-adaptive and handcrafted equidistant strategies for both acceleration factors, with an observed improvement up to $\sim 3\%$ in SSIM, suggesting that potentially-adaptive $k$-space acquisition trajectories can improve reconstructed image quality for larger acceleration factors. However, and perhaps surprisingly, our best performing policies learn to be explicitly non-adaptive.
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
{{ macros.video("https://video.midl.io/2022/long/112.mp4") }}
