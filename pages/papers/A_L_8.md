---
title: "Hybrid Ladder Transformers with Efficient Parallel-Cross Attention for Medical Image Segmentation"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Hybrid Ladder Transformers with Efficient Parallel-Cross Attention for Medical Image Segmentation

#### Haozhe Luo, Yu Changdong, Raghavendra Selvan

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=swvVpnzro9q">PDF</a>
- <a href="https://openreview.net/forum?id=swvVpnzro9q">Reviews</a>

<p>
    <span class="abstract">
        Deep convolutional neural networks (CNNs) have been widely used for medical image segmentation and have shown large performance improvements compared to model-based methods in recent years. Due to the inductive biases of CNNs that primarily focus on extracting features from local image neighbourhoods, they lack information about long-range dependencies in images. Transformer-based architectures that use self-attentive mechanisms to encode long-range dependencies and learn more global representations could have the potential of bridging the gap with CNNs. Most existing transformer-based network architectures for computer vision tasks are large (in number of parameters) and  require large-scale datasets for training. However, the relatively small number of data samples in medical imaging compared to the datasets for vision applications makes it difficult to effectively train transformers for medical imaging applications. This motivates us to investigate a hybrid transformer-based approach for medical image of segmentation tasks and we propose a hybrid transformer model that works in conjunction with a CNN. We propose to use learnable global attention heads along with the traditional convolutional segmentation network architecture to encode long-range dependencies. Specifically, in our proposed architecture the local information extracted by the convolution operations and the global information learned by the self-attention mechanisms are fused using bi-directional cross attention during the encoding process, resulting in what we call a hybrid ladder transformer (HyLT). We evaluate the proposed network on two different medical image segmentation datasets.  The results show that it achieves better results than the relevant CNN- and transformer-based architectures.
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
{{ macros.video("https://video.midl.io/2022/long/146.mp4") }}
