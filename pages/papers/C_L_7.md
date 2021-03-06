---
title: "Domain adaptation through anatomical constraints for 3d human pose estimation under the cover"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# Domain adaptation through anatomical constraints for 3d human pose estimation under the cover

#### Alexander Bigalke, Lasse Hansen, Jasper Diesel, Mattias P Heinrich

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=iCTU7EQipC">PDF</a>
- <a href="https://openreview.net/forum?id=iCTU7EQipC">Reviews</a>

<p>
    <span class="abstract">
        Domain adaptation has the potential to overcome the expensive or even infeasible labeling of target data by transferring knowledge from a labeled source domain. In this work, we address domain adaptation in the context of point cloud-based 3D human pose estimation, whose clinical applicability is severely limited by a lack of labeled training data. Unlike the mainstream approach of domain-invariant feature learning, we propose to guide the learning process in the target domain through weak supervision, based on prior knowledge about human anatomy. We embed this prior knowledge into a novel loss function that encourages network predictions to match the statistics of an anatomically plausible skeleton. Specifically, we formulate three loss functions that penalize asymmetric limb lengths, implausible joint angles, and implausible bone lengths. We evaluate the method on a public lying pose dataset (SLP), adapting from uncovered patients in the source to covered patients in the target domain. Our method outperforms diverse state-of-the-art domain adaptation techniques and improves the baseline model by 25% while reducing the gap to a fully supervised model by 52%. Source code is available at https://github.com/multimodallearning/da-3dhpe-anatomy.
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
<!-- { macros.presentation('', '', 720, 450) } -->
