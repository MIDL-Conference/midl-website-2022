---
title: "Transfer Learning Promotes Robust Parametric Mapping of Diffusion Encoded MR Fingerprinting"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Transfer Learning Promotes Robust Parametric Mapping of Diffusion Encoded MR Fingerprinting

#### Alan Finkelstein, Congyu Liao, Xiaozhi Cao, Jianhui Zhong

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=pCusj-HT_bi">PDF</a>
- <a href="https://openreview.net/forum?id=pCusj-HT_bi">Reviews</a>

<p>
    <span class="abstract">
        MR fingerprinting (MRF) is a framework to simultaneously quantify multiple tissue properties. Acquisition parameters are varied pseudo-randomly and each signal evolution is matched with a dictionary of simulated entries. However, dictionary methods are computationally and memory intensive. Deep learners (DL) are capable of mapping complex MRF signal evolutions to a quantitative parametric space, reducing the computational requirements and reconstruction time; yet fail to perform as well in the setting of noise. Drawing from natural language processing (NLP) we proposed a transfer learning (TL) model to improve MRF parametric estimates with realistic noise levels. The weights of a network trained on clean data are used to instantiate the weights of a noisy model. The model is constrained to learn noise invariant features, by freezing the last layer. Signal evolutions were modeled using a recurrent neural network (RNN) to reconstruct T1, T2, and the apparent diffusion coefficient (ADC). Compared to a model trained with noise, but without TL our approached resulted in a 15% reduction in mean squared error (MSE). Monte Carlo simulations performed at varying SNR (10-60 dB) showed our method yielded losses comparable to the clean model at higher SNRs and proved more robust in the setting of noise at lower SNRs.
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
