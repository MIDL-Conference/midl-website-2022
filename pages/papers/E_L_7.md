---
title: "Position Regression for Unsupervised Anomaly Detection"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Position Regression for Unsupervised Anomaly Detection

#### Florentin Bieder, Julia Wolleb, Robin Sandkuehler, Philippe C. Cattin

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=myJkK4u93g">PDF</a>
- <a href="https://openreview.net/forum?id=myJkK4u93g">Reviews</a>

<p>
    <span class="abstract">
        In recent years, anomaly detection has become an essential field in medical image analysis.  Most current anomaly detection methods for medical images are based on image reconstruction.  In this work, we propose a novel anomaly detection approach based on coordinate regression.  Our method estimates the position of patches within a volume, and is trained only on data of healthy subjects.  During inference, we can detect and localize anomalies by considering the error of the position estimate of a given patch.  We apply our method to 3D CT volumes and evaluate it on patients with intracranial haemorrhages and cranial fractures. The results show that our method performs well in detecting these anomalies.  Furthermore, we show that our method requires less memory than comparable approaches that involve image reconstruction.  This is highly relevant for processing large 3D volumes, for instance, CT or MRI scans. The code will be publicly available.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Friday 8th July<br>Poster Session 3.1 - onsite 15:20 - 16:20, virtual 11:00 - 12:00 (UTC+2)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

[% / %]


---
<!-- { macros.presentation('', '', 720, 450) } -->
