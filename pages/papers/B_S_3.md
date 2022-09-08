---
title: "The do's and don'ts of reinforcement learning for tractography"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# The do's and don'ts of reinforcement learning for tractography

#### Antoine Theberge, Christian Desrosiers, Pierre-marc Jodoin, Maxime Descoteaux

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=H7xbw-1MVPg">PDF</a>
- <a href="https://openreview.net/forum?id=H7xbw-1MVPg">Reviews</a>

<p>
    <span class="abstract">
        Tractography is the process of virtually reconstructing the white matter structure of the brain in a non-invasive manner. To tackle the various known problems of tractography, deep learning has been proposed, but the lack of well curated diverse datasets makes neural networks incapable of generalizing well on unseen data. Recently, deep reinforcement learning (RL) has been shown to effectively learn the tractography procedure without reference streamlines. While the performances reported were competitive, the proposed framework is complex and little is  known on the role and impact of its multiple parts. In this work, we thoroughly explore the different components of the proposed framework through seven experiments on two datasets and shed light on their impact. Our goal is to guide researchers eager to explore the possibilities of deep RL for tractography by exposing what works and what does not work with this category of approach. We find that directionality is crucial for the agents to learn the tracking procedure and that the input signal and the seeding strategy offer a trade-offs in connectivity vs. volume.
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
{{ macros.video("https://video.midl.io/2022/short/42.mp4") }}
