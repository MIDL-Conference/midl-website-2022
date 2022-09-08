---
title: "SynthMap: a generative model for synthesis of 3D datasets for quantitative MRI parameter mapping of myelin water fraction"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# SynthMap: a generative model for synthesis of 3D datasets for quantitative MRI parameter mapping of myelin water fraction

#### Serge Vasylechko, Simon Keith Warfield, Sila Kurugol, Onur Afacan

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=qWkGHtDCATs">PDF</a>
- <a href="https://openreview.net/forum?id=qWkGHtDCATs">Reviews</a>

<p>
    <span class="abstract">
        We present a generative model for synthesis of large scale 3D datasets for quantitative MRI parameter mapping of myelin water fraction (MWF). Training robust neural networks for estimation of quantitative MRI parameters requires large amounts of data. Conventional approaches to tackling data scarcity use spatial augmentations, which may not capture a broad range of possible variations when only a very small initial dataset is available. Furthermore, conventional non linear least squares (NNLS) based methods for MWF estimation are highly sensitive to noise, which means that high quality ground truth MWF parameters are not available for supervised training. Instead of using the noisy NNLS based estimates of MWF parameters from limited real data, we propose to leverage the biophysical model that describes how the MRI signals arise from the underlying tissue parameters to synthetically generate a wide variety of high quality data of the corresponding signals and corresponding parameters for training any CNN based architecture. Our model samples parameter values from a range of naturally occurring prior values for each tissue type. To capture spatial variation, the generative signal decay model is combined with a generative spatial model conditioned on generic tissue segmentations. We demonstrate that our synthetically trained neural network provides superior accuracy over conventional NNLS based methods under the constraints of naturally occuring noise as well as on synthetic low SNR images. Our source code is available at: https://github.com/sergeicu/synthmap
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
{{ macros.video("https://video.midl.io/2022/long/245.mp4") }}
