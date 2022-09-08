---
title: "CAD-RADS Scoring using Deep Learning and Task-Specific Centerline Labeling"
page_class: "paper"
---

{% import "_macros.html" as macros %}

# CAD-RADS Scoring using Deep Learning and Task-Specific Centerline Labeling

#### Felix Denzinger, Michael Wels, Oliver Taubmann, Mehmet Akif Gülsün, Max Schöbinger, Florian André, Sebastian Buss, Johannes Görich, Michael Suehling, Andreas Maier, Katharina Breininger

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="">Proceedings</a>
- <a href="https://openreview.net/pdf?id=vVPMifME8b">PDF</a>
- <a href="https://openreview.net/forum?id=vVPMifME8b">Reviews</a>

<p>
    <span class="abstract">
        With coronary artery disease (CAD) persisting to be one of the leading causes of death worldwide, interest in supporting physicians with algorithms to speed up and improve diagnosis is high. In clinical practice, the severeness of CAD is often assessed with a coronary CT angiography (CCTA) scan and manually graded with the CAD-Reporting and Data System (CAD-RADS) score.  The clinical questions this score assesses are whether a patient has CAD or not (rule-out) and whether he has severe CAD or not (hold-out). In this work, we reach new state-of-the-art performance for automatic CAD-RADS scoring from CCTA. We propose using severity-based label encoding, test time augmentation (TTA) and model ensembling for a task-specific deep learning architecture. Furthermore, we introduce a novel task- and model-specific, heuristic coronary segment labeling, which subdivides coronary trees into consistent parts across patients. It is fast, robust, and easy to implement. We were able to raise the previously reported area under the receiver operating characteristic curve (AUC) from 0.914 to 0.942 in the rule-out and from 0.921 to 0.950 in the hold-out task respectively.
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
{{ macros.video("https://video.midl.io/2022/long/44.mp4") }}
