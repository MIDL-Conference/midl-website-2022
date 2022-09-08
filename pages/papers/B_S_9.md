---
title: "On the performance of learned and fixed-framelet shrinkage networks for low-dose CT denoising"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# On the performance of learned and fixed-framelet shrinkage networks for low-dose CT denoising

#### Luis Albert Zavala Mondragon, Peter H.N. de With, Fons van der Sommen

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=WGLqD0zHXy9">PDF</a>
- <a href="https://openreview.net/forum?id=WGLqD0zHXy9">Reviews</a>

<p>
    <span class="abstract">
        The recently introduced wavelet shrinkage networks (WSNs) are models with a performance close to state-of-the-art CT denoising CNNs, but they are faster and have less parameters. Here, we compare elements of two WSNs. The DHSN2 where the encoding-decoding (ED) path is composed by fixed convolution filters/framelets and the noise reduction is achieved through a CNN in the skip connection. Alternatively, the LWFSN where the ED path is learned and denoising is achieved by an ensemble of semi-hard thresholds. Although both models have been used for CT denoising, heterogeneities in data partitioning, training strategies and overall design, do not allow for direct evaluation of the benefits of having a trainable ED path and using a more elaborated design of a shrinkage CNN. This paper compares these issues by evaluating WSNs under common conditions. Our results show that the configuration with the best trade-off between performance and total trainable parameters is the combination of a learned framelet in the ED path with a simple thresholding layer in the skip connection. In addition, we observe that the CNN with fixed ED improves the most from using a CNN in the skip connection, but a careful design is required of the intermediate CNN to avoid extreme increases in trainable parameters
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
{{ macros.video("https://video.midl.io/2022/short/27.mp4") }}
