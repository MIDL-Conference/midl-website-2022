---
title: "Camera Ready Instructions"
---
# Camera Ready Instructions

Dear authors, 

Congratulations again for your accepted papers at MIDL 2022. This webpage contains detailed instructions for submitting the camera-ready material for your manuscript. Please read the items below carefully and follow the instructions, as they are required for the publication of your paper in the PMLR proceedings. Once your final material is prepared according to the detailed instructions below, please upload a single zip file containing all the items on OpenReview by March 30th. To do so, please use the "Camera Ready Revision" button and then upload to the "Supplementary Material" field in the revision form.

## Detailed Instructions

Three different items need to be prepared for upload in OpenReview:

1) Your LaTex file for the JMLR Proceedings with the JMLR copyright form.

2) A compiled pdf of the camera ready version.

3) An individual bibfile entry for your paper. 

Items 1) and 3) will be submitted in the same zip file as "supplementary material".


### 1: LaTex submission:
-- Prepare your final version using the LaTex MIDL template (midl-fullpaper) available here:  [https://github.com/MIDL-Conference/MIDLLatexTemplate](https://github.com/MIDL-Conference/MIDLLatexTemplate)

-- After making sure that your project compiles correctly with the standard pdf-latex compiler, please include all the following items in a single zip folder latex project:

1. The main LaTex file, which should be named “surname22.tex”, where "surname" is replaced with the primary author's surname. The number 22 represents a 2-digit representation of the year of publication. This naming convention is necessary as per the PMLR format.  

2. The bibliography should be in a single .bib file and named “surname22.bib” with the same convention as above.

3. Within the “surname22.tex” tex file, the document class should be: \documentclass{midl}

4. You should also set the following variables before the \title command: \jmlryear{2022}
\jmlrworkshop{Full Paper -- MIDL 2022}

5. The bibliography should be included in the paper using the following command:  bibliography{surname22}

6. Please do NOT use the \begin{thebibliography} environment.

7. Do not use any \vskip or any other format/spacing altering commands. They will be removed  during compilation.

8. Please include the appendix and supplementary material in the camera-ready version.

9. Please ensure that your paper does not exceed the 8 page limit.

10. Include the main PDF and all the Figures in the zip folder.

11. Fill out and sign the PMLR Publication Agreement ([http://proceedings.mlr.press/pmlr-license-agreement.pdf](http://proceedings.mlr.press/pmlr-license-agreement.pdf)) and add it in PDF format to the zip folder as part of your latex project.


### 2. Camera ready PDF for OpenReview:

You also need to submit the final paper in PDF format in OpenReview using the "Camera Ready Revision" button and the “PDF” field by March 30th.

### 3. The paper bibfile entry:

The authors must create one @InProceedings entry for their paper. Save it in a text file named "bibentry.txt", and add it to the zip file containing your latex sources and the copyright form. This entry must have the following fields:

* title: The title of the paper
* author: The paper’s authors in “Lastname, Firstnames” format, separated by “and”. Do not use unicode characters, use the LaTeX equivalents.
* pages: The page numbers in “startpage–endpage” format
* abstract: The paper’s abstract. 
    * It can include maths in valid LaTeX.
    * Make sure there are no special characters in the abstract, such as those [arising from copying and pasting ligatures from the pdf](http://superuser.com/questions/375449/why-does-the-text-fi-get-cut-when-i-copy-from-a-pdf-or-print-a-document).
    * You can use   `<em>` tags for emphasis.
    * You can use `<b>` for bold.
    * You can use `<ul>` tags for bullets.
    * You can use `<ol>` for numerated lists.
* Other fields may also appear in the @InProceedings entries but will be ignored at present.


