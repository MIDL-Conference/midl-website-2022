---
title: "AdwU-Net: Adaptive Depth and Width U-Net for Medical Image Segmentation by Differentiable Neural Architecture Search"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# AdwU-Net: Adaptive Depth and Width U-Net for Medical Image Segmentation by Differentiable Neural Architecture Search

#### Ziyan Huang, Zehua Wang, zhikai yang, Lixu Gu

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=kF-d1SKWJpS">PDF</a>
- <a href="https://openreview.net/forum?id=kF-d1SKWJpS">Reviews</a>

<p>
    <span class="abstract">
        The U-Net and its variants are proved as the most successful architectures in the medical image segmentation domain. However, the optimal configuration of the hyperparameters in U-Net structure such as depth and width remain challenging to adjust manually due to the diversity of medical image segmentation tasks. In this paper, we propose AdwU-Net, which is an efficient neural architecture search framework to search the optimal task-specific depth and width in the U-Net backbone. Specifically, an adaptive depth and width block is designed and applied hierarchically in U-Net. In each block, the optimal number of convolutional layers and channels in each layer are directly learned from data. To reduce the computational costs and alleviate the memory pressure, we conduct an efficient architecture search and reuse the network weights of different depth and width options in a differentiable manner. Extensive experiments on three subsets of the MSD dataset show that our method significantly outperforms not only the manually scaled U-Net but also other state-of-the-art architectures. Our code is publicly available at https://github.com/Ziyan-Huang/AdwU-Net.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Wednesday 6th July<br>Poster Session 1.1 - onsite 15:20 - 16:20, virtual 11:00 - 12:00 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
{{ macros.video("https://video.midl.io/2022/long/74.mp4") }}
