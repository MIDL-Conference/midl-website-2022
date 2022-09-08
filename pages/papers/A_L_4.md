---
title: "Left Ventricle Contouring in Cardiac Images Based on Deep Reinforcement Learning"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Left Ventricle Contouring in Cardiac Images Based on Deep Reinforcement Learning

#### Sixing Yin, Yameng Han, Judong Pan, Yining Wang, Shufang Li

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=2CakDDr9e9L">PDF</a>
- <a href="https://openreview.net/forum?id=2CakDDr9e9L">Reviews</a>

<p>
    <span class="abstract">
        Assessment of the left ventricle segmentation in cardiac magnetic resonance imaging (MRI) is of crucial importance for cardiac disease diagnosis. However, conventional manual segmentation is a tedious task that requires excessive human effort, which makes automated segmentation highly desirable in practice to facilitate the process of clinical diagnosis. In this paper, we propose a novel reinforcement-learning-based framework for left ventricle contouring, which mimics how a cardiologist outlines the left ventricle along a specific trajectory in a cardiac image. Following the algorithm of proximal policy optimization (PPO), we train a policy network, which makes a stochastic decision on the agent's movement according to its local observation such that the generated trajectory matches the true contour of the left ventricle as much as possible. Moreover, we design a deep learning model with a customized loss function to generate the agent's landing spot (or coordinate of its initial position on a cardiac image). The experiment results show that the coordinate of the generated landing spot is sufficiently close to the true contour and the proposed reinforcement-learning-based approach outperforms the existing U-net model even with limited training set.
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
{{ macros.video("https://video.midl.io/2022/long/61.mp4") }}
