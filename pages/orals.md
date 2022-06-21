---
title: "Oral and Poster Presentations"
---

{% from "_macros.html" import paper %}

<script>
function applyToList(list, fn) {
    for (var i = 0; i < list.length; i++) {
        fn(list[i], list);
    }
}

function hide(list) {
    applyToList(list, function(item) {
        item.style.display = "none";
    });
}

function show(list) {
    applyToList(list, function(item) {
        item.style.display = "block";
    });
}



function showListCategories() {
    var value = document.getElementById("listDisplayer").value;
    var allitems = document.getElementsByClassName("poster");
    var items = document.getElementsByClassName(value);

    // var items = itemList.getElementsByTagName("div");
    if (value === "all") {
        show(allitems);
        for (let i = 0; i < allitems.length; i++) {
            show(allitems[i].parentElement.parentElement);
            allitems[i].parentElement.style.display = "list-item";

        }
       
    } else {
        // hide all items by default
    
        hide(allitems);
        for (let i = 0; i < allitems.length; i++) {
            hide(allitems[i].parentElement);
            allitems[i].parentElement.style.display = "none";
        }
        show(items);
        for (let i = 0; i < items.length; i++) {
            show(items[i].parentElement);
            items[i].parentElement.style.display = "list-item";

            // items[i].parentElement.style.visibility = "visible";

        }

    }
};
</script>



# Scientific program

<select id="listDisplayer" onchange="showListCategories();">
    <option value="all" selected="selected">Show papers from all topics</option>
    <option value="xtai">Explainable AI</option>
    <option value="damg"> Domain Adaptation and Model Generalization</option>
    <option value="rs">Image Reconstruction and Synthesis</option>
    <option value="url">Unsupervised and Representation Learning</option>
    <option value="cad">Computer-Aided Detection and Diagnosis</option>
    <option value="lnl">Learning with Noisy Labels</option>
    <option value="reg">Registration</option>
    <option value="seg">Segmentation</option>
    <option value="del">Data-Efficient Learning </option>

</select>

## Wednesday 6th July

<p><a id="oral1-1"></a><h3>Oral Session 1.1: Segmentation I - 10:00 - 10:40 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/A1.html">Left Ventricle Contouring in Cardiac Images Based on Deep Reinforcement Learning</a>
    </span>
    <span class="authors"> Sixing Yin, Yameng Han, Judong Pan, Yining Wang, Shufang Li</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=2CakDDr9e9L">pdf</a></li><li><a href="https://openreview.net/forum?id=2CakDDr9e9L">reviews</a></li></ul><span class="abstract">
      Assessment of the left ventricle segmentation in cardiac magnetic resonance imaging (MRI) is of crucial importance for cardiac disease diagnosis. However, conventional manual segmentation is a tedious task that requires excessive human effort, which makes automated segmentation highly desirable in practice to facilitate the process of clinical diagnosis. In this paper, we propose a novel reinforcement-learning-based framework for left ventricle contouring, which mimics how a cardiologist outlines the left ventricle along a specific trajectory in a cardiac image. Following the algorithm of proximal policy optimization (PPO), we train a policy network, which makes a stochastic decision on the agent&apos;s movement according to its local observation such that the generated trajectory matches the true contour of the left ventricle as much as possible. Moreover, we design a deep learning model with a customized loss function to generate the agent&apos;s landing spot (or coordinate of its initial position on a cardiac image). The experiment results show that the coordinate of the generated landing spot is sufficiently close to the true contour and the proposed reinforcement-learning-based approach outperforms the existing U-net model even with limited training set.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/A2.html">Learning Shape Reconstruction from Sparse Measurements with Neural Implicit Functions</a>
    </span>
    <span class="authors"> Tamaz Amiranashvili, David Lüdke, Hongwei Li, Bjoern Menze, Stefan Zachow</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=UuHtdwRXkzw">pdf</a></li><li><a href="https://openreview.net/forum?id=UuHtdwRXkzw">reviews</a></li></ul><span class="abstract">
      Reconstructing anatomical shapes from sparse or partial measurements relies on prior knowledge of shape variations that occur within a given population. Such shape priors are learned from example shapes, obtained by segmenting volumetric medical images. For existing models, the resolution of a learned shape prior is limited to the resolution of the training data. However, in clinical practice, volumetric images are often acquired with highly anisotropic voxel sizes, e.g.\ to reduce image acquisition time in MRI or radiation exposure in CT imaging. The missing shape information between the slices prohibits existing methods to learn a high-resolution shape prior. We introduce a method for high-resolution shape reconstruction from sparse measurements without relying on high-resolution ground truth for training. Our method is based on neural implicit shape representations and learns a continuous shape prior only from highly anisotropic segmentations. Furthermore, it is able to learn from shapes with a varying field of view and can reconstruct from various sparse input configurations. We demonstrate its effectiveness on two anatomical structures: vertebra and femur, and successfully reconstruct high-resolution shapes from sparse segmentations, using as few as three orthogonal slices.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/A3.html">Are 2.5D approaches superior to 3D deep networks in whole brain segmentation?</a>
    </span>
    <span class="authors"> Saikat Roy, David Kügler, Martin Reuter</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Ob62JPB_CDF">pdf</a></li><li><a href="https://openreview.net/forum?id=Ob62JPB_CDF">reviews</a></li></ul><span class="abstract">
      Segmentation of 3D volumes with a large number of labels, small convoluted structures, and lack of contrast between various structural boundaries is a difficult task. While recent methodological advances across many segmentation tasks are dominated by 3D architectures, currently the strongest performing method for whole brain segmentation is FastSurferCNN, a 2.5D approach. To shed light on the nuanced differences between 2.5D and various 3D approaches, we perform a thorough and fair comparison and suggest a spatially-ensembled 3D architecture. Interestingly, we observe training memory intensive 3D segmentation on full-view images does not outperform the 2.5D approach. A shift to training on patches even while evaluating on full-view solves these limitations of both memory and performance limitations at the same time. We demonstrate significant performance improvements over state-of-the-art 3D methods on both Dice Similarity Coefficient and especially average Hausdorff Distance measures across five datasets. Finally, our validation across variations of neurodegenerative disease states and scanner manufacturers, shows we outperform the previously leading 2.5D approach FastSurferCNN demonstrating robust segmentation performance in realistic settings.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster1-1"></a><h3>Poster Session 1.1 : Onsite 15:20 - 16:20 , Virtual 11:00 - 12:00</h3>
<a id="long1-1"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_1.html">Regularizing Brain Age Prediction via Gated Knowledge Distillation</a>
    </span>
    <span class="authors"> Yanwu Yang, Guo Xutao, Chenfei Ye, Yang Xiang, Ting Ma</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=nxA2bZff3iQ">pdf</a></li><li><a href="https://openreview.net/forum?id=nxA2bZff3iQ">reviews</a></li></ul><span class="abstract">
      The brain age has been proven to be a phenotype of relevance to cognitive performance and brain disease. Recently, brain age estimation accuracy has been greatly improved by using deep learning. However, deep neural networks with millions of parameters may incur overfitting and suffer from poor generalizations, especially for insufficient brain imaging data. This paper presents a novel regularization method that penalizes the predictive distribution using knowledge distillation and introduces additional knowledge to reinforce the learning process. During knowledge distillation, we propose a gated distillation mechanism to enable the student model to attentively learn meaningful knowledge from the teacher model, given the assumption that a teacher might not always be correct. Moreover, to enhance the capability of knowledge transfer, the hint representation similarity is also adopted to regularize the model for training. Our evaluation on a cohort of 3655 subjects from four public datasets with ages range of 16-92, demonstrates that our proposed method improves the prediction performance over a series of well-established models, where the mean absolute error of the estimated ages is reduced to 2.129 years.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_2.html">Inference of captions from histopathological patches</a>
    </span>
    <span class="authors"> Masayuki Tsuneki, Fahdi Kanavati</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=9gKn7SDb83v">pdf</a></li><li><a href="https://openreview.net/forum?id=9gKn7SDb83v">reviews</a></li></ul><span class="abstract">
      Computational histopathology has made significant strides in the past few years, slowly getting closer to clinical adoption. One area of benefit would be the automatic generation of diagnostic reports from H&amp;E-stained whole slide images which would further increase the efficiency of the pathologists&apos; routine diagnostic workflows. In this study, we compiled a dataset of histopathological captions of stomach adenocarcinoma endoscopic biopsy specimens which we extracted from diagnostic reports and paired with patches extracted from the associated whole slide images. The dataset contains a variety of gastric adenocarcinoma subtypes. We trained a baseline attention-based model to predict the captions from features extracted from the patches and obtained promising results. We make the captioned dataset of 260K patches publicly available.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_3.html">Prior Guided Multitask Learning for Joint Optic Disc&frasl;Cup Segmentation and Fovea Detection</a>
    </span>
    <span class="authors"> Huaqing He, Li Lin, Zhiyuan Cai, Xiaoying Tang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=HU6-t9oKvRW">pdf</a></li><li><a href="https://openreview.net/forum?id=HU6-t9oKvRW">reviews</a></li></ul><span class="abstract">
      Fundus photography has been routinely used to document the presence and severity of various retinal degenerative diseases such as age-related macula degeneration, glaucoma, and diabetic retinopathy, for which the fovea, optic disc (OD), and optic cup (OC) are important anatomical landmarks. Identification of those anatomical landmarks is of great clinical importance. However, the presence of lesions, drusen, and other abnormalities during retinal degeneration severely complicates automatic landmark detection and segmentation. Most existing works treat the identification of each landmark as a single task and typically do not make use of any clinical prior information. In this paper, we present a novel method, named JOINED, for prior guided multi-task learning for joint OD/OC segmentation and fovea detection. An auxiliary branch for distance prediction, in addition to a segmentation branch and a detection branch, is constructed to effectively utilize the distance information from each image pixel to landmarks of interest. Our proposed JOINED pipeline consists of a coarse stage and a fine stage. At the coarse stage, we obtain the OD/OC coarse segmentation and the heatmap localization of fovea through a joint segmentation and detection module. Afterwards, we crop the regions of interest for subsequent fine processing and use predictions obtained at the coarse stage as additional information for better performance and faster convergence. Experimental results reveal that our proposed JOINED outperforms existing state-of-the-art approaches on the publicly-available GAMMA, PALM, and REFUGE datasets of fundus images. Furthermore, JOINED ranked the 5th on the OD/OC segmentation and fovea detection tasks in the GAMMA MICCAI 2021 challenge.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_4.html">Left Ventricle Contouring in Cardiac Images Based on Deep Reinforcement Learning</a>
    </span>
    <span class="authors"> Sixing Yin, Yameng Han, Judong Pan, Yining Wang, Shufang Li</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=2CakDDr9e9L">pdf</a></li><li><a href="https://openreview.net/forum?id=2CakDDr9e9L">reviews</a></li></ul><span class="abstract">
      Assessment of the left ventricle segmentation in cardiac magnetic resonance imaging (MRI) is of crucial importance for cardiac disease diagnosis. However, conventional manual segmentation is a tedious task that requires excessive human effort, which makes automated segmentation highly desirable in practice to facilitate the process of clinical diagnosis. In this paper, we propose a novel reinforcement-learning-based framework for left ventricle contouring, which mimics how a cardiologist outlines the left ventricle along a specific trajectory in a cardiac image. Following the algorithm of proximal policy optimization (PPO), we train a policy network, which makes a stochastic decision on the agent&apos;s movement according to its local observation such that the generated trajectory matches the true contour of the left ventricle as much as possible. Moreover, we design a deep learning model with a customized loss function to generate the agent&apos;s landing spot (or coordinate of its initial position on a cardiac image). The experiment results show that the coordinate of the generated landing spot is sufficiently close to the true contour and the proposed reinforcement-learning-based approach outperforms the existing U-net model even with limited training set.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_5.html">AdwU-Net: Adaptive Depth and Width U-Net for Medical Image Segmentation by Differentiable Neural Architecture Search</a>
    </span>
    <span class="authors"> Ziyan Huang, Zehua Wang, zhikai yang, Lixu Gu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kF-d1SKWJpS">pdf</a></li><li><a href="https://openreview.net/forum?id=kF-d1SKWJpS">reviews</a></li></ul><span class="abstract">
      The U-Net and its variants are proved as the most successful architectures in the medical image segmentation domain. However, the optimal configuration of the hyperparameters in U-Net structure such as depth and width remain challenging to adjust manually due to the diversity of medical image segmentation tasks. In this paper, we propose AdwU-Net, which is an efficient neural architecture search framework to search the optimal task-specific depth and width in the U-Net backbone. Specifically, an adaptive depth and width block is designed and applied hierarchically in U-Net. In each block, the optimal number of convolutional layers and channels in each layer are directly learned from data. To reduce the computational costs and alleviate the memory pressure, we conduct an efficient architecture search and reuse the network weights of different depth and width options in a differentiable manner. Extensive experiments on three subsets of the MSD dataset show that our method significantly outperforms not only the manually scaled U-Net but also other state-of-the-art architectures. Our code is publicly available at https://github.com/Ziyan-Huang/AdwU-Net.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_6.html">Region Aware Transformer for Automatic Breast Ultrasound Tumor Segmentation</a>
    </span>
    <span class="authors"> Xiner Zhu, Haoji Hu, Hualiang Wang, Jincao Yao, 李 伟 liwei, Di Ou, Dong Xu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=2bVDHzy7xwV">pdf</a></li><li><a href="https://openreview.net/forum?id=2bVDHzy7xwV">reviews</a></li></ul><span class="abstract">
      Although  Automatic  Breast  Ultrasound  (ABUS)  has  become  an  important  tool  to  detect breast cancer, computer-aided diagnosis requires accurate segmentation of tumors on ABUS. In this paper, we propose the Region Aware Transformer Network (RAT-Net) for tumor  segmentation  on  ABUS  images.   RAT-Net  incorporates  region  prior  information of tumors into network design.  The specially designed Region Aware Self-Attention Block(RASAB) and Region Aware Transformer Block (RATB) fuse the tumor region information into multi-scale features to obtain accurate segmentation.  To the best of our knowledge,it is the first time that tumor region distributions are incorporated into network architectures for ABUS image segmentation.  Experimental results on a dataset containing 84,480 ABUS images taken from 256 subjects show that RAT-Net outperforms other state-of-the-art methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_7.html">YAMU: Yet Another Modified U-Net Architecture for Semantic Segmentation</a>
    </span>
    <span class="authors"> Pranab Samanta, Nitin Singhal</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=RPFCw3VU6R9">pdf</a></li><li><a href="https://openreview.net/forum?id=RPFCw3VU6R9">reviews</a></li></ul><span class="abstract">
      Digital histopathology images must be examined accurately and quickly as part of a pathologist&apos;s clinical procedure. For histopathology image segmentation, different variants of U-Net and fully convolutional networks (FCN) are state-of-the-art. HistNet or histopathology network for semantic labelling in histopathology images, for example, is one of them. We improve our previously proposed model HistNet in this paper by introducing new skip pathways to the decoder stage to aggregate multiscale features and incorporate a feature pyramid to keep the contextual information. In addition, to boost performance, we employ a deep supervision training technique. We show that not only does the proposed design outperform the baseline, but it also outperforms state-of-the-art segmentation architectures with much fewer parameters.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_8.html">Hybrid Ladder Transformers with Efficient Parallel-Cross Attention for Medical Image Segmentation</a>
    </span>
    <span class="authors"> Haozhe Luo, Yu Changdong, Raghavendra Selvan</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=swvVpnzro9q">pdf</a></li><li><a href="https://openreview.net/forum?id=swvVpnzro9q">reviews</a></li></ul><span class="abstract">
      Deep convolutional neural networks (CNNs) have been widely used for medical image segmentation and have shown large performance improvements compared to model-based methods in recent years. Due to the inductive biases of CNNs that primarily focus on extracting features from local image neighbourhoods, they lack information about long-range dependencies in images. Transformer-based architectures that use self-attentive mechanisms to encode long-range dependencies and learn more global representations could have the potential of bridging the gap with CNNs. Most existing transformer-based network architectures for computer vision tasks are large (in number of parameters) and  require large-scale datasets for training. However, the relatively small number of data samples in medical imaging compared to the datasets for vision applications makes it difficult to effectively train transformers for medical imaging applications. This motivates us to investigate a hybrid transformer-based approach for medical image of segmentation tasks and we propose a hybrid transformer model that works in conjunction with a CNN. We propose to use learnable global attention heads along with the traditional convolutional segmentation network architecture to encode long-range dependencies. Specifically, in our proposed architecture the local information extracted by the convolution operations and the global information learned by the self-attention mechanisms are fused using bi-directional cross attention during the encoding process, resulting in what we call a hybrid ladder transformer (HyLT). We evaluate the proposed network on two different medical image segmentation datasets.  The results show that it achieves better results than the relevant CNN- and transformer-based architectures.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_9.html">Automatic Segmentation of Head and Neck Tumor: How Powerful Transformers Are?</a>
    </span>
    <span class="authors"> Ikboljon Sobirov, Otabek Nazarov, Hussain Alasmawi, Mohammad Yaqub</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=reIO5WfgbLd">pdf</a></li><li><a href="https://openreview.net/forum?id=reIO5WfgbLd">reviews</a></li></ul><span class="abstract">
      Cancer is one of the leading causes of death worldwide, and head and neck (H&amp;N) cancer is amongst the most prevalent types. Positron emission tomography and computed tomography are used to detect and segment the tumor region. Clinically, tumor segmentation is extensively time-consuming and prone to error. Machine learning, and deep learning in particular, can assist to automate this process, yielding results as accurate as the results of a clinician. In this research study, we develop a vision transformers-based method to automatically delineate H&amp;N tumor, and compare its results to leading convolutional neural network (CNN)-based models. We use multi-modal data of CT and PET scans to do this task. We show that the selected transformer-based model can achieve results on a par with CNN-based ones. With cross validation, the model achieves a mean dice similarity coefficient of 0.736, mean precision of 0.766 and mean recall of 0.766. This is only 0.021 less than the 2020 competition winning model in terms of the DSC score. This indicates that the exploration of transformer-based models is a promising research area.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_10.html">Attention Guided Deep Supervision Model for Prostate Segmentation in MultiSite Heterogeneous MRI Data</a>
    </span>
    <span class="authors"> Kuruparan Shanmugalingam, Arcot Sowmya, Daniel Moses, Erik Meijering</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=5RBBK1iTs2C">pdf</a></li><li><a href="https://openreview.net/forum?id=5RBBK1iTs2C">reviews</a></li></ul><span class="abstract">
      Prostate cancer and benign prostatic hyperplasia are common diseases in men and require early and accurate diagnosis for optimal treatment. Standard diagnostic tests such as the prostate-specific antigen test and digital rectal examination are inconvenient. Thus, non-invasive methods such as magnetic resonance imaging (MRI) and automated image analysis are increasingly utilised to facilitate and improve prostate diagnostics. Segmentation is a vital part of the prostate image analysis pipeline, and deep neural networks are now the tool of choice to automate this task. In this work, we benchmark various deep neural networks for 3D prostate segmentation using four different publicly available datasets and one private dataset. We show that popular networks such as U-Net trained on one dataset typically generalise poorly when tested on others due to data heterogeneity. Aiming to address this issue, we propose a novel deep-learning architecture for prostate whole-gland segmentation in T2-weighted MRI images that exploits various techniques such as pyramid pooling, concurrent spatial and channel squeeze and excitation, and deep supervision. Our extensive experiments demonstrate that it performs superiorly without requiring special adaptation to any specific dataset.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_11.html">Anomaly-Aware 3D Segmentation of Knee Magnetic Resonance Images</a>
    </span>
    <span class="authors"> Boyeong Woo, Craig Engstrom, Jurgen Fripp, Stuart Crozier, Shekhar S. Chandra</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Blt5-qTxdKo">pdf</a></li><li><a href="https://openreview.net/forum?id=Blt5-qTxdKo">reviews</a></li></ul><span class="abstract">
      Automated segmentation of 3D medical images involves numerous challenges including factors such a lack of large image datasets for training in machine learning approaches, differences in image characteristics within and across imaging technologies and anatomical variations across individuals. Further challenges arise in clinical investigations when images contain incidental or coexisting anomalies alongside the primary pathoanatomy under examination. Therefore, successful automated segmentation of objects in the presence of such anomalies represents an important task in medical image analysis. In this work, we show how popular U-Net-based neural networks can be used for detecting anomalies in the cancellous bone of the knee from 3D magnetic resonance (MR) images in patients with varying grades of osteoarthritis (OA). We also show that the extracted information can be utilised for downstream tasks such as parallel segmentation of anatomical structures along with associated anomalies such as bone marrow lesions (BMLs). For anomaly detection, a U-Net-based model was adopted to inpaint the region of interest in images so that the anomalous regions can be replaced with close to normal appearances. The difference between the original image and the inpainted image was then used to highlight the anomalies. The extracted information was then used to improve the segmentation of bones and cartilages; in particular, the anomaly-aware segmentation mechanism provided a significant reduction in surface distance error in the segmentation of knee MR images containing severe anomalies within the distal femur. Furthermore, all of these U-Net-based models were fully volumetric convolutional neural networks, allowing for efficient 3D image processing.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_12.html">Explainability Guided COVID-19 Detection in CT Scans</a>
    </span>
    <span class="authors"> Ameen Ali Ali, Tal Shaharabany, Lior Wolf</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=KWucjFOxEb2">pdf</a></li><li><a href="https://openreview.net/forum?id=KWucjFOxEb2">reviews</a></li></ul><span class="abstract">
      Radiological examination of chest CT is an effective method for screening COVID-19 cases. In this work, we overcome three challenges in the automation of this process: (i) the limited number of supervised positive cases, (ii) the lack of region-based supervision, and (iii) variability across acquisition sites. These challenges are met by incorporating a recent augmentation solution called SnapMix and a new patch embedding technique, and by performing a test-time stability analysis. The three techniques are complementary and are all based on utilizing the heatmaps produced by the Class Activation Mapping (CAM) explainability method. Compared to the current state of the art, we obtain an increase of five percent in the F1 score on a site with a relatively high number of cases and a gap twice as large for a site with much fewer training images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_13.html">Practical uncertainty quantification for brain tumor segmentation</a>
    </span>
    <span class="authors"> Moritz Fuchs, Camila Gonzalez, Anirban Mukhopadhyay</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Srl3-HnY14U">pdf</a></li><li><a href="https://openreview.net/forum?id=Srl3-HnY14U">reviews</a></li></ul><span class="abstract">
      Despite U-Nets being the de-facto standard for medical image segmentation, researchers have identified shortcomings of U-Nets, such as overconfidence and poor out-of-distribution generalization. Several methods for uncertainty quantification try to solve such problems by relying on well-known approximations such as Monte-Carlo Drop-Out, Probabilistic U-Net, and Stochastic Segmentation Networks. We introduce a novel multi-headed Variational U-Net. The proposed approach combines the global exploration capabilities of deep ensembles with the out-of-distribution robustness of Variational Inference. An efficient training strategy and an expressive yet general design ensure superior uncertainty quantification within a reasonable compute requirement. We thoroughly analyze the performance and properties of our approach on the publicly available BRATS2018 dataset. Further, we test our model on four commonly observed distribution shifts. The proposed approach has good uncertainty calibration and is robust to out-of-distribution shifts.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_14.html">Automatic planning of liver tumor thermal ablation using deep reinforcement learning</a>
    </span>
    <span class="authors"> Krishna Chaitanya, Chloe Audigier, Laura Elena Balascuta, Tommaso Mansi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ehsvFoQaz-W">pdf</a></li><li><a href="https://openreview.net/forum?id=ehsvFoQaz-W">reviews</a></li></ul><span class="abstract">
      Thermal ablation is a promising minimally invasive intervention to treat liver tumors. It requires a meticulous planning phase where the electrode trajectory from the skin surface to the tumor inside the liver as well as the ablation protocol are defined to reach a complete tumor ablation while considering multiple clinical constraints such as avoiding too much damage to healthy tissue. The planning is usually done manually based on 2D views of pre-operative CT images and can be extremely challenging for large or irregularly shaped tumors. Conventional optimization methods have been proposed to automate this complex task, but they suffer from high computation time.  To alleviate this drawback, we propose to leverage a deep reinforcement learning (DRL) approach to find the optimal electrode trajectory that satisfies all the clinical constraints and does not require any labels in training. Here, we define a custom environment as the 3D mask with tumor, surrounding organs, skin labels along with an electrode line and ablation zone. An agent, represented by a neural network, interacts with the custom environment by displacing the electrode and therefore can learn an optimal policy. The reward assignment is done based on the clinical constraints. To explore discrete and continuous action-based approaches with double deep Q networks and proximal policy optimization (PPO), respectively. We perform an evaluation on the publicly available liver tumor segmentation (LITs) challenge dataset. We obtain solutions that satisfy all clinical constraints comparable to the conventional method. The DRL method does not need any post-processing steps, allowing a mean inference time of 13.3 seconds per subject compared to the conventional optimization method&apos;s mean time of 135 seconds. Moreover, the best DRL method (PPO) yields a valid solution irrespective of the tumor location within the liver that demonstrates its robustness.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_15.html">Learning Shape Reconstruction from Sparse Measurements with Neural Implicit Functions</a>
    </span>
    <span class="authors"> Tamaz Amiranashvili, David Lüdke, Hongwei Li, bjoern menze, Stefan Zachow</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=UuHtdwRXkzw">pdf</a></li><li><a href="https://openreview.net/forum?id=UuHtdwRXkzw">reviews</a></li></ul><span class="abstract">
      Reconstructing anatomical shapes from sparse or partial measurements relies on prior knowledge of shape variations that occur within a given population. Such shape priors are learned from example shapes, obtained by segmenting volumetric medical images. For existing models, the resolution of a learned shape prior is limited to the resolution of the training data. However, in clinical practice, volumetric images are often acquired with highly anisotropic voxel sizes, e.g.\ to reduce image acquisition time in MRI or radiation exposure in CT imaging. The missing shape information between the slices prohibits existing methods to learn a high-resolution shape prior. We introduce a method for high-resolution shape reconstruction from sparse measurements without relying on high-resolution ground truth for training. Our method is based on neural implicit shape representations and learns a continuous shape prior only from highly anisotropic segmentations. Furthermore, it is able to learn from shapes with a varying field of view and can reconstruct from various sparse input configurations. We demonstrate its effectiveness on two anatomical structures: vertebra and femur, and successfully reconstruct high-resolution shapes from sparse segmentations, using as few as three orthogonal slices.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_16.html">SMU-Net: Style matching U-Net for brain tumor segmentation with missing modalities</a>
    </span>
    <span class="authors"> Reza Azad, Nika Khosravi, Dorit Merhof</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=X5H_eVaqtb">pdf</a></li><li><a href="https://openreview.net/forum?id=X5H_eVaqtb">reviews</a></li></ul><span class="abstract">
      Gliomas are one of the most prevalent types of primary brain tumors, accounting for more than 30\% of all cases and they develop from the glial stem or progenitor cells. In theory, the majority of brain tumors could well be identified exclusively by the use of Magnetic Resonance Imaging (MRI). Each MRI modality delivers distinct information on the soft tissue of the human brain and integrating all of them would provide comprehensive data for the accurate segmentation of the glioma, which is crucial for the patient&apos;s prognosis, diagnosis, and determining the best follow-up treatment. Unfortunately, MRI is prone to artifacts for a variety of reasons, which might result in missing one or more MRI modalities. Various strategies have been proposed over the years to synthesize the missing modality or compensate for the influence it has on automated segmentation models. However, these methods usually fail to model the underlying missing information. In this paper, we propose a style matching U-Net (SMU-Net) for brain tumour segmentation on MRI images. Our co-training approach utilizes a content and style-matching mechanism to distill the informative features from the full-modality network into a missing modality network. To do so, we encode both full-modality and missing-modality data into a latent space, then we decompose the representation space into a style and content representation.  Our style matching module adaptively recalibrates the representation space by learning a matching function to transfer the informative and textural features from full-modality path into a missing-modality path. Moreover, by modelling the mutual information, our content module surpasses the less informative features and re-calibrates the representation space based on discriminative semantic features. The evaluation process on the Brats 2018 dataset shows the significance of the proposed method on the missing modality scenario.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_17.html">Efficient tool segmentation for endoscopic videos in the wild</a>
    </span>
    <span class="authors"> Clara Tomasini, Iñigo Alonso, Luis Riazuelo, Ana C Murillo</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=DPkb7gxt6gZ">pdf</a></li><li><a href="https://openreview.net/forum?id=DPkb7gxt6gZ">reviews</a></li></ul><span class="abstract">
      In recent years, deep learning methods have become the most effective approach for tool segmentation in endoscopic images, achieving the state of the art on the available public benchmarks. However, these methods present some challenges that hinder their direct deployment in real world scenarios. This work explores how to solve two of the most common challenges: real-time and memory restrictions and false positives in frames with no tools. To cope with the first case, we show how to adapt an efficient general purpose semantic segmentation model. Then, we study how to cope with the common issue of only training on images with at least one tool. Then, when images of endoscopic procedures without tools are processed, there are a lot of false positives. To solve this, we propose to add an extra classification head that performs binary frame classification, to identify frames with no tools present. Finally, we present a thorough comparison of this approach with current state of the art on different benchmarks, including real medical practice recordings, demonstrating similar accuracy with much lower computational requirements.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_18.html">Holistic Modeling in Medical Image Segmentation Using Spatial Recurrence</a>
    </span>
    <span class="authors"> João B. S. Carvalho, João Santinha, Đorđe Miladinović, Carlos Cotrini, Joachim M. Buhmann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=avqFDNyt0Dj">pdf</a></li><li><a href="https://openreview.net/forum?id=avqFDNyt0Dj">reviews</a></li></ul><span class="abstract">
      In clinical practice, regions of interest in medical imaging (MI) often need to be identified through a process of precise image segmentation. For MI segmentation to generalize, we need two components: to identify continuous and local descriptions, but at the same time to develop a holistic representation of the image that captures long-range spatial dependencies. Unfortunately, we demonstrate that the start of the art does not achieve the latter. In particular, it does not provide a modeling that yields a global, contextual model. To improve accuracy, and enable holistic modeling, we introduce a novel deep neural network architecture endowed with spatial recurrence. The implementation relies on gated recurrent units that directionally traverse the feature map, greatly increasing each layers receptive field and explicitly modeling non-adjacent, contextual relationships between pixels. Our method is evaluated in four different segmentations tasks: nuclei segmentation in microscopy images, colorectal polyp segmentation in colonoscopy videos, liver segmentation in abdominal CT scans, and aorta artery segmentation in thoracic CT scans. Our experiments demonstrate an average increase in performance of 4.72 Dice points and 0.68 Hausdorff distance units when compared with commonly used architectures.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_19.html">Are 2.5D approaches superior to 3D deep networks in whole brain segmentation?</a>
    </span>
    <span class="authors"> Saikat Roy, David Kügler, Martin Reuter</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Ob62JPB_CDF">pdf</a></li><li><a href="https://openreview.net/forum?id=Ob62JPB_CDF">reviews</a></li></ul><span class="abstract">
      Segmentation of 3D volumes with a large number of labels, small convoluted structures, and lack of contrast between various structural boundaries is a difficult task. While recent methodological advances across many segmentation tasks are dominated by 3D architectures, currently the strongest performing method for whole brain segmentation is FastSurferCNN, a 2.5D approach. To shed light on the nuanced differences between 2.5D and various 3D approaches, we perform a thorough and fair comparison and suggest a spatially-ensembled 3D architecture. Interestingly, we observe training memory intensive 3D segmentation on full-view images does not outperform the 2.5D approach. A shift to training on patches even while evaluating on full-view solves these limitations of both memory and performance limitations at the same time. We demonstrate significant performance improvements over state-of-the-art 3D methods on both Dice Similarity Coefficient and especially average Hausdorff Distance measures across five datasets. Finally, our validation across variations of neurodegenerative disease states and scanner manufacturers, shows we outperform the previously leading 2.5D approach FastSurferCNN demonstrating robust segmentation performance in realistic settings.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_L_20.html">Confidence Histograms for Model Reliability Analysis and Temperature Calibration</a>
    </span>
    <span class="authors"> Farina Kock, Felix Thielke, Grzegorz Chlebus, Hans Meine</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=p2f6ROn1h02">pdf</a></li><li><a href="https://openreview.net/forum?id=p2f6ROn1h02">reviews</a></li></ul><span class="abstract">
      Proper estimation of uncertainty may help the adoption of deep learning-based solutions in clinical practice, when out-of-distribution situations can be reliably detected and measurements can take error bounds into account. Therefore, a variety of approaches have been proposed already, with varying requirements and computational effort. Uncertainty estimation is complicated by the fact that typical neural networks are overly confident; this effect is particularly prominent with the Dice loss, which is commonly used for image segmentation. On the other hand, various methods for model calibration have been proposed to reduce the discrepancy between classifier confidence and the observed accuracy.  In this work, we focus on the simple network calibration method of introducing a &apos;temperature&apos; parameter for the softmax operation. This approach is not only appealing because of its mathematical simplicity, it also appears to be well-suited for countering the main distortion of the classifier output confidence levels. Finally, it comes at literally zero extra cost, because the necessary multiplications can be integrated into the previous layer&apos;s weights after calibration, and a scalar temperature does not affect the classification at all.  Our contributions are as follows: We thoroughly evaluate the confidence behavior of several models with different architectures, different numbers of output classes, different loss functions, and different segmentation tasks. In order to do so, we propose an efficient intermediate representation and some adaptations of reliability diagrams to semantic segmentation. We investigate different calibration measures and their optimal temperatures for these diverse models.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_L_21.html">Learning to Automatically Generate Accurate ECG Captions</a>
    </span>
    <span class="authors"> Mathieu Guido Geert Bartels, Ivona Najdenkoska, Rutger van de Leur, Arjan Sammani, Karim Taha, David M Knigge, Pieter A Doevendans, Marcel Worring, René van Es</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Y-kXbPYtzsg">pdf</a></li><li><a href="https://openreview.net/forum?id=Y-kXbPYtzsg">reviews</a></li></ul><span class="abstract">
      The electrocardiogram (ECG) is an affordable, non-invasive and quick method to gain essential information about the electrical activity of the heart. Interpreting ECGs is a time-consuming process even for experienced cardiologists, which motivates the current usage of rule-based methods in clinical practice to automatically describe ECGs. However, in comparison with descriptions created by experts, ECG-descriptions generated by such rule-based methods show considerable limitations. Inspired by image captioning methods, we instead propose a data-driven approach for ECG description generation. We introduce a label-guided Transformer model, and show that it is possible to automatically generate relevant and readable ECG descriptions with a data-driven captioning model. We incorporate prior ECG labels into our model design, and show this improves the overall quality of generated descriptions. We find that training these models on free-text annotations of ECGs - instead of the clinically-used computer generated ECG descriptions - greatly improves performance. Moreover, we perform a human expert evaluation study of our best system, which shows that our data-driven approach improves upon existing rule-based methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short1-1"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_1.html">Position Classifier: Rethinking Position Encoding on Chest X-ray Diseases Identification</a>
    </span>
    <span class="authors"> Yu Wen Fang, Fang-Yi Su, Jung-Hsien Chiang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=EpQzz2J4Ft">pdf</a></li><li><a href="https://openreview.net/forum?id=EpQzz2J4Ft">reviews</a></li></ul><span class="abstract">
      The patch-based method of chest X-ray interpretation often suffers from the loss of infor
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_2.html">Classification and Segmentation of Vulvovaginal Candidiasis in Microscopic Leucorrhea Images Based on Combined Deep Learning Model</a>
    </span>
    <span class="authors"> Yiyao Ma, yifei xu, Wei Li</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=_wSgnVQJnN8">pdf</a></li><li><a href="https://openreview.net/forum?id=_wSgnVQJnN8">reviews</a></li></ul><span class="abstract">
      Vulvovaginal Candidiasis (VVC) is a common and serious gynecological disease. Early diagnosis and treatment are of great significance to women&apos;s health. However, most hospitals still use manual diagnosis method, which is not only inefficient but also unstable. This paper proposes a VVC image classification and recognition method based on computer vision and deep learning. Our models can greatly reduce the workload of doctors and improve detection efficiency and stability.After testing on 480 samples, our model has reached 92\% accuracy, 93\% recall and 97\%AUC with 23M parameters. The overall performance is superior to the best baseline model that we obtain 93\% accuracy, 92\% recall and 96\%AUC with 56M parameters. Besides, we are the first known paper to propose detection targets for pathogenic bacteria, using different colored rectangles to encircle different types of bacteria. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_3.html">SinusNet: Label-Free Segmentation of Maxillary Sinus Lesion in CBCT Images</a>
    </span>
    <span class="authors"> DaEl Kim, Su Yang, Seryong Kang, Jin Kim, Soyoung Chun, MinHyuk Choi, Won-Jin Yi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=YrcmnyRKnyi">pdf</a></li><li><a href="https://openreview.net/forum?id=YrcmnyRKnyi">reviews</a></li></ul><span class="abstract">
      To alleviate the workload of data annotation, we propose a label-free approach (SinusNet) for the segmentation of maxillary sinus lesions in CBCT images via learning the anomaly features from diverse synthetic lesions within the normal maxillary sinus. Our SinusNet achieved average F1 of 80.9 ± 11.6%, precision of 82.7 ± 9.1%, and recall of 80.1 ± 15.0%, respectively, and comparable performance with those of previous supervised approaches.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_4.html">Deeply supervised network for white matter hyperintensities segmentation with transfer learning</a>
    </span>
    <span class="authors"> Yilei Wu, Fang Ji, Yao Feng Chong, Li-Hsian Christopher Chen, Juan Helen Zhou</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=KbXNnCCXN-i">pdf</a></li><li><a href="https://openreview.net/forum?id=KbXNnCCXN-i">reviews</a></li></ul><span class="abstract">
      White matter hyperintensities (WMH) are brain white matter lesions commonly found in the elderly. Due to its association with cerebrovascular and neurodegenerative diseases, quantifying WMH volume is critical for many neurological applications. Previous segmentation approaches using 2D U-Net potentially omit the learning of 3D spatial contextual information. This paper proposes a deeply supervised 3D U-Net-like network with transfer learning to perform WMH segmentation in fluid attenuation inversion recovery (FLAIR) magnetic resonance images (MRI). We leveraged a pretrained network constructed by predicting brain age from structural MRIs. The proposed method achieved a Dice score of 82.3 on the MICCAI WMH Challenge training dataset and 75.3 on another independent testing dataset, outperforming other state-of-the-art methods. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_5.html">Prostate Cancer Diagnosis and Grading in Whole Slide Images of Core Needle Biopsies</a>
    </span>
    <span class="authors"> Nitin Singhal, Nilanjan Chattopadhyay, Pranab Samanta, Saikiran Bonthu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=w2UnVmH3PN">pdf</a></li><li><a href="https://openreview.net/forum?id=w2UnVmH3PN">reviews</a></li></ul><span class="abstract">
      Gleason grading is a risk stratification procedure for prostate cancer that is subjective and based on the reporting pathologist&apos;s experience and skill. Deep Learning (DL) algorithms have showed potential in improving Gleason grading objectivity and efficiency. On Whole Slide Images (WSI) from a source other than training data, however, DL networks show domain shift and poor performance. Using a novel training process that learns domain agnostic features, we propose a DL approach for segmenting and grading epithelial tissue. When utilised as an aid for core needle biopsy (CNB) evaluation, our DL approach has the potential to increase grading consistency and accuracy, leading in better patient outcomes.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_6.html">Learning Robust Representation for Laryngeal Cancer Classification in Vocal Folds from Narrow Band Images</a>
    </span>
    <span class="authors"> Debayan Bhattacharya, Finn Behrendt, Axelle Felicio-Briegel, Veronika Volgger, Dennis Eggert, Christian Betz, Alexander Schlaefer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=nJd70UxI5hH">pdf</a></li><li><a href="https://openreview.net/forum?id=nJd70UxI5hH">reviews</a></li></ul><span class="abstract">
      Narrow Band Imaging (NBI) is increasingly being used in laryngology because it increases the visibility of mucosal vascular patterns which serve as important visual markers to detect premalignant, dysplastic, and malignant lesions.  To this end, deep learning methods have been used to automatically detect and classify the lesions from NBI endoscopic videos. However, the heterogeneity of the lesions, illumination changes due to phlegm on the mucosa, and imaging artifacts such as blurriness make inter-patient endoscopic videos exhibit diverging image distributions.  Therefore, learning representations that are robust to image distribution changes can be beneficial and improve the generalizing capability of the convolutional neural network  (CNN).  To this end,  we propose a  dual branch  CNN  that learns robust representations by combining deep narrow band features and wavelet scattering transform features of the narrow band images to classify vocal cord NBI images into malignant and benign classes.  We show the generalizing capability of our learnt representation by training our neural network using two different losses:  cross-entropy (CE) loss and supervised contrastive (SupCon) loss. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_7.html">Classification of visibility in multi-stain microscopy images</a>
    </span>
    <span class="authors"> Jonathan Ganz, Christof Bertram, Robert Klopfleisch, Samir Jabari, Katharina Breininger, Marc Aubreville</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=-GsA-mUVmm">pdf</a></li><li><a href="https://openreview.net/forum?id=-GsA-mUVmm">reviews</a></li></ul><span class="abstract">
      Annotating mitotic figures (MF) in hematoxylin and eosin (H&amp;E) stained slides is an error- prone task that can lead to low inter-rater concordance. Immunohistochemical staining against phospho-histone H3 (PHH3) can lead to higher concordance but, at the same time, to generally higher mitotic figure counts. By annotating MF in PHH3-stained specimen and transferring them to an H&amp;E- re-stained version of the same slide, the high specificity of PHH3 can be used to create high-quality data sets for H&amp;E images. Since considerably more MF can be recognized only in PHH3, this in turn leads to the introduction of label noise. To overcome this problem, we present an attention-based dual-stain classifier which is designed to discriminate MF based on their visibility in H&amp;E. Additionally, we present a data augmentation approach that focuses especially on presenting a large variability of cell pairs to the attention network. The combination of the two methods leads to a weighted accuracy of 0.740 in discriminating H&amp;E-identifiable from non-identifiable MF. Therefore, by automatically discriminating the visibility of MF in H&amp;E slides, PHH3-guided annotation can be used to generate a more reliable ground truth for MF in H&amp;E.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_8.html">Gleason grading of prostate cancer using artificial intelligence: lessons learned from the PANDA challenge</a>
    </span>
    <span class="authors"> Kimmo Kartasalo, Peter Ström, Martin Eklund, Wouter Bulten, Hans Pinckaers, Geert Litjens, Po-Hsuan Cameron Chen, Kunal Nagpal, Pekka Ruusuvuori</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=rg2xsj5Lm3">pdf</a></li><li><a href="https://openreview.net/forum?id=rg2xsj5Lm3">reviews</a></li></ul><span class="abstract">
      Assessing prostate biopsies is crucial for the clinical management of patients with suspected prostate cancer, but is associated with complications such as inter-observer variability. The PANDA challenge aimed at mitigating these issues through development and rigorous validation of image analysis algorithms for the task. In this short paper, we summarize the key insights gained from PANDA from the viewpoints of algorithm development and challenge organisation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_9.html">Physical Color Calibration of Digital Pathology Scanners for Deep Learning Based Diagnosis of Prostate Cancer</a>
    </span>
    <span class="authors"> Xiaoyi Ji, Richard Salmon, Nita Mulliqi, Henrik Olsson, Lars Egevad, Pekka Ruusuvuori, Martin Eklund, Kimmo Kartasalo</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=aYBUqtibfRT">pdf</a></li><li><a href="https://openreview.net/forum?id=aYBUqtibfRT">reviews</a></li></ul><span class="abstract">
      Variation in whole slide image (WSI) across different scanners poses a problem for deep learning algorithms. We apply a color calibration slide to standardize WSIs from different sites and evaluate the effect of calibration on a deep learning model for prostate cancer diagnosis. We show that calibration can significantly improve the accuracy of the model.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_10.html">Deep Learning for Automatic Segmentation of Background Parenchymal Enhancement in Breast MRI.</a>
    </span>
    <span class="authors"> Sylwia Nowakowska, Karol Borkowski, Carlotta Ruppert, Patryk Hejduk, Alexander Ciritsis, Anna Landsmann, Magda Macron, Nicole Berger, Andreas Boss, Cristina Rossi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6WMpziPQwnT">pdf</a></li><li><a href="https://openreview.net/forum?id=6WMpziPQwnT">reviews</a></li></ul><span class="abstract">
      Contrast-enhanced breast MRI plays a crucial role in the care of women at high risk of developing breast cancer. Contrast agent uptake in the breast tissue, i.e., Background Parenchymal Enhancement (BPE), may be an indicator of a higher risk of developing breast cancer and may limit the detectability of lesions. Not only the degree, but also the area of enhancement are elements of importance in the decision-making process in each case. However, they rely on the visual assessment of the reader and thus suffer from poor reliability and reproducibility. In this study, we have developed and evaluated a deep learning (DL) multiclass algorithm for segmentation of both: the BPE area and the non-enhancing tissue. For training, validation, and testing 3441 slices were used. The mean Dice Similarity Coefficient (DSCmean) for the test set amounted to 0.76. Our results show that accurate BPE segmentation is feasible with DL for all classes of enhancement. Such an algorithm may be implemented as part of a pipeline for precise BPE classification or may find direct clinical application in the management of high-risk patients in breast MRI.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_11.html">SwinFPN: Leveraging Vision Transformers for 3D Organs-At-Risk Detection</a>
    </span>
    <span class="authors"> Bastian Wittmann, Suprosanna Shit, Fernando Navarro, Jan C. Peeken, Stephanie E. Combs, bjoern menze</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=yiIz7DhgRU5">pdf</a></li><li><a href="https://openreview.net/forum?id=yiIz7DhgRU5">reviews</a></li></ul><span class="abstract">
      Current state-of-the-art detection algorithms operating on 2D natural images utilize the relation modeling capability of vision transformers to increase detection performance. However, the feasibility of adapting vision transformers for the 3D medical object detection task remains largely unexplored. To this end, we attempt to leverage vision transformers for organs-at-risk detection and propose a novel feature extraction backbone, dubbed SwinFPN, which exploits the concept of shifted window-based self-attention. We combine SwinFPN with Retina U-Net&apos;s head networks and report superior detection performances. Code for SwinFPN will be available in our medical vision transformer library https://github.com/bwittmann/transoar.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_12.html">Segmentation of post-operative glioblastoma</a>
    </span>
    <span class="authors"> Ragnhild Holden Helland, David Bouget, Alexandros Ferles, Roelant S. Eijgelaar, Ole Solheim, Philip C. De Witt Hamer, Ingerid Reinertsen</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=IlIx-gSpZEo">pdf</a></li><li><a href="https://openreview.net/forum?id=IlIx-gSpZEo">reviews</a></li></ul><span class="abstract">
      Extent Of Resection (EOR) after surgery is one of the main prognostic factors for patients diagnosed with glioblastoma. The current standard method for estimating EOR is subject to high inter- and intra-rater variability, and an automated method for segmentation of residual tumor in early post-operative MRI could lead to a more accurate estimation of EOR.  In this study we trained neural networks for segmentation of residual tumor tissue in early post-operative MRI. We introduce a new dataset for this task, consisting of data from 645 patients from 13 hospitals in Europe and the US. The segmentation performance of the best model is similar to that of human expert raters, and the results be used to classify cases of gross total resection and residual tumor with high recall and precision.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_13.html">Masked Autoencoders Pre-training in Multiple Instance Learning for Whole Slide Image Classification</a>
    </span>
    <span class="authors"> Jianpeng An, Yunhao Bai, Huazhen Chen, Zhongke Gao, Geert Litjens</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=rV5gzFDn5PF">pdf</a></li><li><a href="https://openreview.net/forum?id=rV5gzFDn5PF">reviews</a></li></ul><span class="abstract">
      End-to-end learning with whole-slide digital pathology images is challenging due to their size, which is in the order of gigapixels. In this paper, we propose a novel weakly-supervised learning strategy that combines masked autoencoders (MAE) with multiple instance learning (MIL). We use the output tokens of a self-supervised, pre-trained MAE as instances and design a token selection module to reduce the impact of global average pooling. We evaluate our framework on the assessment of whole-slide image classification on Camelyon16 dataset, showing improved performance compared to the state-of-the-art CLAM algorithm.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_14.html">Automated tool to quantitatively assess bone disease on Whole-Body Diffusion Weighted Imaging for patients with Advanced Prostate Cancer</a>
    </span>
    <span class="authors"> Antonio Candito, Matthew D Blackledge, Richard Holbrey, Dow-Mu Koh</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=5oPy4t-2iKE">pdf</a></li><li><a href="https://openreview.net/forum?id=5oPy4t-2iKE">reviews</a></li></ul><span class="abstract">
      An automated tool has been developed to assess bone disease on Whole-Body Diffusion Weighted Imaging (WBDWI). The tool segments areas of suspected bone disease on the high b-value sequences, transfers the ROIs obtained onto the derived Apparent Diffusion Coefficient (ADC) map and estimates the median global ADC (gADC) and the Total Diffusion Volume (TDV).
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_15.html">Looking for abnormalities using asymmetrical information from bilateral mammograms</a>
    </span>
    <span class="authors"> XIN WANG, Yuan Gao, Tianyu Zhang, Luyi Han, Regina Beets-Tan, Ritse Mann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=FsGMbJwz4jG">pdf</a></li><li><a href="https://openreview.net/forum?id=FsGMbJwz4jG">reviews</a></li></ul><span class="abstract">
      Radiologists commonly compare the bilateral mammograms to detect asymmetric abnormalities. While fibroglandular tissue is normally quite symmetrically distributed, lesions in one breast and will only rarely have a counterpart in the corresponding area of the opposite breast. Motivated by this experience, we explore a model that can learn to detect asymmetrical information from bilateral mammograms and then find the abnormal areas, similar to what a radiologist does. This can increase model performance and interpretability. We evaluate the proposed methods on the popular INBreast dataset and show improved performance in abnormal classification and weakly supervised segmentation tasks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_16.html">On the pitfalls of deep image segmentation for lightsheet microscopy</a>
    </span>
    <span class="authors"> Rami Al-Maskari, Johannes C. Paetzold, Izabela Horvath, Ali Erturk, bjoern menze</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=3Krfu84W-Wx">pdf</a></li><li><a href="https://openreview.net/forum?id=3Krfu84W-Wx">reviews</a></li></ul><span class="abstract">
      Fluorescence light sheet microscopy (LSM) of tissue cleared samples enables holistic 3D imaging of the human brain and the full murine body. While this novel imaging method creates high resolution scans and has led to an abundance of high-profile publications in the last 5 years, analysing them is not trivial and comes with complex obstacles. In this paper we present a review and discussion of our groups previous works to present best practices on both animal and human scans and guidelines to overcome these obstacles
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_17.html">Scoliosis Measurement on DXA Scans Using a Combined Deep Learning and Spinal Geometry Approach</a>
    </span>
    <span class="authors"> Emmanuelle Bourigault, Amir Jamaludin, Timor Kadir, Andrew Zisserman</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=4enF5ipqKJQ">pdf</a></li><li><a href="https://openreview.net/forum?id=4enF5ipqKJQ">reviews</a></li></ul><span class="abstract">
      We propose improvements to an automated method for scoliosis measurement. Our main novelty is the use of a spline to better model the curve of the spine, and we employ pseudo- labelling to re-train the segmentation step to mitigate the domain gap when adapting to a new dataset. We obtain promising results with a good fit of our smoothed curve to approximate the spinal midpoints in severe scoliosis cases, and obtain good agreement against human ground-truth. This work is relevant for improving the severity grading of scoliosis and potentially aiding in the treatment management of scoliosis.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/A_S_18.html">Non-stationary deep lifting with application to acute brain infarct segmentation</a>
    </span>
    <span class="authors"> Nadja Gruber, Markus Haltmeier, Annemieke ter Telgte, Johannes Schwab, Elke Gizewski, Malik Galijasevic</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=pgoioZJ6y9A">pdf</a></li><li><a href="https://openreview.net/forum?id=pgoioZJ6y9A">reviews</a></li></ul><span class="abstract">
      We present a deep learning based method for segmenting acute brain infarcts in MRI images using a novel input enhancement strategy combined with a suitable non-stationary loss. The hybrid framework allows incorporating knowledge of clinicians to mimic the diagnostic patterns of experts. More specifically, our strategy consists of an interaction of non-local input transforms that highlight features which are additionally penalized by the non-stationary loss. For brain infarct segmentation, expert knowledge refers to the quasi-symmetry property of healthy brains, whereas in other applications one may include different anatomical priors. In addition, we use a network architecture merging information from the two complementary MRI maps DWI and ADC. We perform experiments on a dataset consisting of DWI and ADC images from 100 patients to demonstrate the applicability of proposed method. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/A_S_19.html">Strategies for Meta-Learning with Diverse Tasks</a>
    </span>
    <span class="authors"> Stefano Woerner, Christian F. Baumgartner</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=SNWV4Qlk53G">pdf</a></li><li><a href="https://openreview.net/forum?id=SNWV4Qlk53G">reviews</a></li></ul><span class="abstract">
      A major limitation of deep learning for medical applications is the scarcity of labelled data. Meta-learning, which leverages principles learned from previous tasks for new tasks, has the potential to mitigate this data scarcity. However, most meta-learning methods assume idealised settings with homogeneous task definitions. The most widely used family of meta-learning methods, those based on Model-Agnostic Meta-Learning (MAML), require a constant network architecture and therefore a fixed number of classes per classification task. Here, we extend MAML to more realistic settings in which the number of classes can vary by adding a new classification layer for each new task. Specifically, we investigate various initialisation strategies for these new layers. We identify a number of such strategies that substantially outperform the naive default (Kaiming) initialisation scheme.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral1-2"></a><h3>Oral Session 1.2: Explainable AI - 13:20 - 14:00 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/B1.html">FBNETGEN: Task-aware GNN-based fMRI Analysis via Functional Brain Network Generation</a>
    </span>
    <span class="authors"> Xuan Kan, Hejie Cui, Joshua Lukemire, Ying Guo, Carl Yang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=oWFphg2IKon">pdf</a></li><li><a href="https://openreview.net/forum?id=oWFphg2IKon">reviews</a></li></ul><span class="abstract">
      Functional magnetic resonance imaging (fMRI) is one of the most commonly used imaging modalities to investigate brain functions. Recent studies in neuroscience stress the great potential of functional brain networks constructed from fMRI data for clinical predictions. Traditional functional brain networks, however, are noisy and unaware of downstream prediction tasks, while also incompatible with the recent powerful deep learning models of graph neural networks (GNNs). In order to fully unleash the power of GNNs in network-based fMRI analysis, we develop FBNETGEN, a task-aware and interpretable fMRI analysis framework via deep brain network generation. In particular, we formulate (1) prominent region of interest (ROI) features extraction, (2) brain networks generation, and (3) clinical predictions with GNNs in an end-to-end trainable model under the guidance of particular prediction tasks. Along with the process, the key novel component is the graph generator which learns to transform raw time-series features into task-oriented brain networks. Our learnable graphs also provide unique interpretations by highlighting prediction-related brain regions. Comprehensive experiments on two datasets, i.e., the recently released and currently largest publicly available fMRI dataset Adolescent Brain Cognitive Development (ABCD), and the widely-used dataset PNC, prove the superior effectiveness and interpretability of FBNETGEN. The implementation is available at https://github.com/Wayfear/FBNETGEN.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/B2.html">Self-supervised learning for analysis of temporal and morphological drug effects in cancer cell imaging data </a>
    </span>
    <span class="authors"> Andrei Dmitrenko, Mauro Miguel Masiero, Nicola Zamboni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ulJpSvIwFdU">pdf</a></li><li><a href="https://openreview.net/forum?id=ulJpSvIwFdU">reviews</a></li></ul><span class="abstract">
      In this work, we propose two novel methodologies to study temporal and morphological phenotypic effects caused by different experimental conditions using imaging data. As a proof of concept, we apply them to analyze drug effects in 2D cancer cell cultures. We train a convolutional autoencoder on 1M images dataset with random augmentations and multi-crops to use as feature extractor. We systematically compare it to the pretrained state-of-the-art models. We further use the feature extractor in two ways. First, we apply distance-based analysis and dynamic time warping to cluster temporal patterns of 31 drugs. We identify clusters allowing annotation of drugs as having cytotoxic, cytostatic, mixed or no effect. Second, we implement an adversarial/regularized learning setup to improve classification of 31 drugs and visualize image regions that contribute to the improvement. We increase top-3 classification accuracy by 8% on average and mine examples of morphological feature importance maps. We provide the feature extractor and the weights to foster transfer learning applications in biology. We also discuss utility of other pretrained models and applicability of our methods to other types of biomedical data. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/B3.html">Surface Vision Transformers: Attention-Based Modelling applied to Cortical Analysis</a>
    </span>
    <span class="authors"> Simon Dahan, Abdulah Fawaz, Logan Zane John Williams, Chunhui Yang, Timothy S. Coalson, Matthew Glasser, A David Edwards, Daniel Rueckert, Emma Claire Robinson</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=mpp843Bsf-">pdf</a></li><li><a href="https://openreview.net/forum?id=mpp843Bsf-">reviews</a></li></ul><span class="abstract">
      The extension of convolutional neural networks (CNNs) to non-Euclidean geometries has led to multiple frameworks for studying manifolds. Many of those methods have shown design limitations resulting in poor modelling of long-range associations, as the generalisation of convolutions to irregular surfaces is non-trivial. Motivated by the success of attention-modelling in computer vision, we translate convolution-free vision transformer approaches to surface data, to introduce a domain-agnostic architecture to study any surface data projected onto a spherical manifold. Here, surface patching is achieved by representing spherical data as a sequence of triangular patches, extracted from a subdivided icosphere. A transformer model encodes the sequence of patches via successive multi-head self-attention layers while preserving the sequence resolution. We validate the performance of the proposed Surface Vision Transformer (SiT) on the task of phenotype regression from cortical surface metrics derived from the Developing Human Connectome Project (dHCP). Experiments show that the SiT generally outperforms surface CNNs, while performing comparably on registered and unregistered data, suggesting the network is capable of achieving transformation invariance.  Analysis of transformer attention maps further illustrates the learning of long-range associations between distant cortical regions and offer strong potential to characterise subtle cognitive developmental patterns.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster1-2"></a><h3>Poster Session 1.2 - Onsite 11:00 - 12:00, Virtual 15:20 - 16:20 (UTC+2)</h3>
<a id="long1-2"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_L_1.html">KeyMorph: Robust Multi-modal Affine Registration via Unsupervised Keypoint Detection</a>
    </span>
    <span class="authors"> Evan M Yu, Alan Q. Wang, Adrian V Dalca, Mert R. Sabuncu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=OrNzjERFybh">pdf</a></li><li><a href="https://openreview.net/forum?id=OrNzjERFybh">reviews</a></li></ul><span class="abstract">
      Registration is a fundamental task in medical imaging, and recent machine learning methods have become the state-of-the-art. However, these approaches are often not interpretable, lack robustness to large misalignments, and do not incorporate symmetries of the problem. In this work, we propose KeypointMorph, an unsupervised end-to-end learning-based image registration framework that relies on automatically detecting corresponding keypoints. Our core insight is straightforward: matching keypoints between images can be used to obtain the optimal transformation via a differentiable closed-form expression. We use this observation to drive the unsupervised learning of anatomically-consistent keypoints from images. This not only leads to substantially more robust registration but also yields better interpretability, since the keypoints reveal which parts of the image are driving the final alignment. Moreover, KeypointMorph can be designed to be equivariant under image translations and/or symmetric with respect to the input image ordering. We demonstrate the proposed framework in solving 3D affine registration of multi-modal brain MRI scans. Remarkably, we show that this strategy leads to consistent keypoints, even across modalities. We demonstrate registration accuracy that surpasses current state-of-the-art methods, especially in the context of large displacements.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_2.html">FBNETGEN: Task-aware GNN-based fMRI Analysis via Functional Brain Network Generation</a>
    </span>
    <span class="authors"> Xuan Kan, Hejie Cui, Joshua Lukemire, Ying Guo, Carl Yang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=oWFphg2IKon">pdf</a></li><li><a href="https://openreview.net/forum?id=oWFphg2IKon">reviews</a></li></ul><span class="abstract">
      Functional magnetic resonance imaging (fMRI) is one of the most commonly used imaging modalities to investigate brain functions. Recent studies in neuroscience stress the great potential of functional brain networks constructed from fMRI data for clinical predictions. Traditional functional brain networks, however, are noisy and unaware of downstream prediction tasks, while also incompatible with the recent powerful deep learning models of graph neural networks (GNNs). In order to fully unleash the power of GNNs in network-based fMRI analysis, we develop FBNETGEN, a task-aware and interpretable fMRI analysis framework via deep brain network generation. In particular, we formulate (1) prominent region of interest (ROI) features extraction, (2) brain networks generation, and (3) clinical predictions with GNNs in an end-to-end trainable model under the guidance of particular prediction tasks. Along with the process, the key novel component is the graph generator which learns to transform raw time-series features into task-oriented brain networks. Our learnable graphs also provide unique interpretations by highlighting prediction-related brain regions. Comprehensive experiments on two datasets, i.e., the recently released and currently largest publicly available fMRI dataset Adolescent Brain Cognitive Development (ABCD), and the widely-used dataset PNC, prove the superior effectiveness and interpretability of FBNETGEN. The implementation is available at https://github.com/Wayfear/FBNETGEN.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_3.html">VORTEX: Physics-Driven Data Augmentations Using Consistency Training for Robust Accelerated MRI Reconstruction</a>
    </span>
    <span class="authors"> Arjun D Desai, Beliz Gunel, Batu Ozturkler, Harris Beg, Shreyas Vasanawala, Brian Hargreaves, Christopher Re, John M. Pauly, Akshay Chaudhari</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=WjwUeGh0yMK">pdf</a></li><li><a href="https://openreview.net/forum?id=WjwUeGh0yMK">reviews</a></li></ul><span class="abstract">
      Deep neural networks have enabled improved image quality and fast inference times for various inverse problems, including accelerated magnetic resonance imaging (MRI) reconstruction. However, such models require extensive fully-sampled ground truth datasets, which are difficult to curate and are sensitive to distribution drifts. In this work, we propose applying physics-driven data augmentations for consistency training that leverage our domain knowledge of the forward MRI data acquisition process and MRI physics to achieve improved data efficiency and robustness to clinically-relevant distribution drifts. Our approach, termed VORTEX, (1) demonstrates strong improvements over supervised baselines with and without data augmentation in robustness to signal-to-noise ratio change and motion corruption in data-limited regimes; (2) considerably outperforms state-of-the-art purely image-based data augmentation techniques and self-supervised reconstruction methods on both in-distribution and out-of-distribution data; and (3) enables composing heterogeneous image-based and physics-driven data augmentations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_L_4.html">Learned Half-Quadratic Splitting Network for MR Image Reconstruction</a>
    </span>
    <span class="authors"> Bingyu Xin, Timothy S Phan, Leon Axel, Dimitris N. Metaxas</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=h7rXUbALijU">pdf</a></li><li><a href="https://openreview.net/forum?id=h7rXUbALijU">reviews</a></li></ul><span class="abstract">
      Magnetic Resonance (MR) image reconstruction from highly undersampled $k$-space data is critical in accelerated MR imaging (MRI) techniques. In recent years, deep learning-based methods have shown great potential in this task. This paper proposes a learned half-quadratic splitting algorithm for MR image reconstruction and implements the algorithm in an unrolled deep learning network architecture. We compare the performance of our proposed method on a public cardiac MR dataset against  DC-CNN and LPDNet, and our method outperforms other methods in both quantitative results and qualitative results with fewer model parameters and faster reconstruction speed. Finally, we enlarge our model to achieve superior reconstruction quality, and the improvement is $1.76$ dB and $2.74$ dB over LPDNet in peak signal-to-noise ratio on $5  imes$ and $10   imes$ acceleration, respectively. Code for our method is publicly available at https://github.com/hellopipu/HQS-Net.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_L_5.html">TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces</a>
    </span>
    <span class="authors"> Andrew Hoopes, Juan Eugenio Iglesias, Bruce Fischl, Douglas Greve, Adrian V Dalca</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=-JiHeZNDY3a">pdf</a></li><li><a href="https://openreview.net/forum?id=-JiHeZNDY3a">reviews</a></li></ul><span class="abstract">
      Mesh-based reconstruction of the cerebral cortex is a fundamental component in brain image analysis. Classical, iterative pipelines for cortical modeling are robust but often time-consuming, mostly due to expensive procedures that involve topology correction and spherical mapping. Recent attempts to address reconstruction with machine learning methods have accelerated some components in these pipelines, but they still require slow processing steps to enforce topological constraints to comply with known anatomical structure. In this work, we introduce a novel learning-based strategy, TopoFit, which rapidly fits a topologically-correct surface to the white-matter tissue boundary. We design a joint network with image and graph convolutions and an efficient symmetric distance loss to learn to predict accurate deformations that map a template mesh to subject-specific anatomy. This technique encompasses the work of current mesh correction, fine-tuning, and inflation steps and, as a result, offers a $150  imes$ faster solution to cortical surface reconstruction compared to traditional approaches. We demonstrate that TopoFit is robust to common failure modes, such as white-matter tissue hypointensities, and is $1.8    imes$ more accurate than current state-of-the-art deep-learning strategy. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_6.html">Negative Evidence Matters in Interpretable Histology Image Classification</a>
    </span>
    <span class="authors"> Soufiane Belharbi, Marco Pedersoli, Ismail Ben Ayed, Luke McCaffrey, Eric Granger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=FF6XuIyeF6V">pdf</a></li><li><a href="https://openreview.net/forum?id=FF6XuIyeF6V">reviews</a></li></ul><span class="abstract">
      Using only global annotations such as the image class labels, weakly-supervised learning methods allow CNN  classifiers to jointly classify an image, and yield the regions of interest associated with the predicted class. However, without any guidance at the pixel level, such methods may yield inaccurate regions. This problem is known to be more challenging with histology images than with natural ones, since objects are less salient, structures have more variations, and foreground and background regions have stronger similarities. Therefore, all the methods in computer vision literature for visual interpretation of CNNs may not directly apply.  In this work, we propose a simple yet efficient method based on a composite loss function that leverages  information from the fully negative samples. Our new loss function contains two complementary terms: the first exploits positive evidence collected from the CNN classifier, while the second leverages the fully negative samples from the training dataset. In particular, we equip a pre-trained classifier with a decoder that allows refining the regions of interest. The same classifier is exploited to collect both the positive and negative evidence at the pixel level to train the decoder.  This enables to take advantages of the fully negative samples that occurs naturally in the data, without any additional supervision signals and using only the image class as supervision. Compared to several recent related methods, over the public benchmark GlaS for colon cancer and a   Camelyon16 patch-based benchmark for breast cancer using three different backbones, we show the substantial improvements introduced by our method. Our results shows the benefits of using both negative and positive evidence, ie, the one obtained from a classifier and the one naturally available in datasets.  We provide an ablation study of both terms. Our code is publicly available.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_7.html">Segmentation-Consistent Probabilistic Lesion Counting</a>
    </span>
    <span class="authors"> Julien Schroeter, Chelsea Myers-Colet, Douglas Arnold, Tal Arbel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kwcxym1kMtf">pdf</a></li><li><a href="https://openreview.net/forum?id=kwcxym1kMtf">reviews</a></li></ul><span class="abstract">
      Lesion counts are important indicators of disease severity, patient prognosis, and treatment efficacy, yet counting as a task in medical imaging is often overlooked in favor of segmentation. This work introduces a novel continuously differentiable function that maps lesion segmentation predictions to lesion count probability distributions in a consistent manner. The proposed end-to-end approach—which consists of voxel clustering, lesion-level voxel probability aggregation, and Poisson-binomial counting—is non-parametric and thus offers a robust and consistent way to augment lesion segmentation models with post hoc counting capabilities. Experiments on Gadolinium-enhancing lesion counting demonstrate that our method outputs accurate and well-calibrated count distributions that capture meaningful uncertainty information. They also reveal that our model is suitable for multi-task learning of lesion segmentation, is efficient in low data regimes, and is robust to adversarial attacks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_L_8.html">SynthMap: a generative model for synthesis of 3D datasets for quantitative MRI parameter mapping of myelin water fraction</a>
    </span>
    <span class="authors"> Serge Vasylechko, Simon Keith Warfield, Sila Kurugol, Onur Afacan</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=qWkGHtDCATs">pdf</a></li><li><a href="https://openreview.net/forum?id=qWkGHtDCATs">reviews</a></li></ul><span class="abstract">
      We present a generative model for synthesis of large scale 3D datasets for quantitative MRI parameter mapping of myelin water fraction (MWF). Training robust neural networks for estimation of quantitative MRI parameters requires large amounts of data. Conventional approaches to tackling data scarcity use spatial augmentations, which may not capture a broad range of possible variations when only a very small initial dataset is available. Furthermore, conventional non linear least squares (NNLS) based methods for MWF estimation are highly sensitive to noise, which means that high quality ground truth MWF parameters are not available for supervised training. Instead of using the noisy NNLS based estimates of MWF parameters from limited real data, we propose to leverage the biophysical model that describes how the MRI signals arise from the underlying tissue parameters to synthetically generate a wide variety of high quality data of the corresponding signals and corresponding parameters for training any CNN based architecture. Our model samples parameter values from a range of naturally occurring prior values for each tissue type. To capture spatial variation, the generative signal decay model is combined with a generative spatial model conditioned on generic tissue segmentations. We demonstrate that our synthetically trained neural network provides superior accuracy over conventional NNLS based methods under the constraints of naturally occuring noise as well as on synthetic low SNR images. Our source code is available at: https://github.com/sergeicu/synthmap
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_9.html">Deep Learning Radiographic Assessment of Pulmonary Edema: Training with Serum Biomarkers</a>
    </span>
    <span class="authors"> Justin Huynh, Samira Masoudi, Abraham Noorbakhsh, Amin Mahmoodi, kyle Hasenstab, Micheal Pazzani, Albert Hsiao</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=NyxXpTbHUCJ">pdf</a></li><li><a href="https://openreview.net/forum?id=NyxXpTbHUCJ">reviews</a></li></ul><span class="abstract">
      A major obstacle faced when developing convolutional neural networks (CNNs) for medical imaging is the acquisition of training labels: most current approaches rely on manually prescribed labels from physicians, which are time consuming and labor intensive to attain. Clinical biomarkers, often measured alongside medical images and used in diagnostic workup, may provide a rich set of data that can be collected retrospectively and utilized to train diagnostic models. In this work, we focused on the blood serum biomarkers BNP and BNPP, indicative of acute heart failure (HF) and cardiogenic pulmonary edema, paired with the chest X-ray imaging modality. We investigated the potential for inferring BNP and BNPP from chest radiographs. For this purpose, a CNN was trained using 28090 radiographs to automatically infer BNP and BNPP, and achieved strong performance ($AUC=0.903$, $r=0.787$). Since radiographic features of pulmonary edema may not be visible on low resolution images, we also assessed the impact of image resolution on model learning and performance, comparing CNNs trained at five image sizes ($64    imes64$ to $1024    imes1024$). With comparable AUC values obtained at different resolutions, our experiments using three activation mapping techniques (saliency, Grad-CAM, XRAI) revealed considerable in-lung attention growth with increased resolution. The highest resolution models focus attention on the lungs, necessary for radiographic diagnosis of pulmonary edema. Our results emphasize the need to utilize radiographs of near-native resolution for optimal CNN performance, not fully captured by summary metrics like AUC.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_L_10.html">Implicit Neural Representations for Deformable Image Registration</a>
    </span>
    <span class="authors"> Jelmer M. Wolterink, Jesse C. Zwienenberg, Christoph Brune</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=BP29eKzQBu3">pdf</a></li><li><a href="https://openreview.net/forum?id=BP29eKzQBu3">reviews</a></li></ul><span class="abstract">
      Deformable medical image registration has in past years been revolutionized by deep learning with convolutional neural networks. These methods surpass conventional image registration techniques in speed but not in accuracy. Here, we present an alternative approach to leveraging neural networks for image registration. Instead of using a neural network to predict the transformation between images, we optimize a neural network to represent this continuous transformation. Using recent insights from differentiable rendering, we show how such an implicit deformable image registration (IDIR) model can be naturally combined with regularization terms based on standard automatic differentiation techniques. We demonstrate the effectiveness of this model on 4D chest CT registration in the DIR-LAB data set and find that a single three-layer multi-layer perceptron with periodic activation functions outperforms all published deep learning-based methods, without any folding and without the need for training data. The model is flexible enough to be extended to include different losses, regularizers, and optimization schemes and is implemented using standard deep learning libraries.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_11.html">Self-supervised learning for analysis of temporal and morphological drug effects in cancer cell imaging data</a>
    </span>
    <span class="authors"> Andrei Dmitrenko, Mauro Miguel Masiero, Nicola Zamboni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ulJpSvIwFdU">pdf</a></li><li><a href="https://openreview.net/forum?id=ulJpSvIwFdU">reviews</a></li></ul><span class="abstract">
      In this work, we propose two novel methodologies to study temporal and morphological phenotypic effects caused by different experimental conditions using imaging data. As a proof of concept, we apply them to analyze drug effects in 2D cancer cell cultures. We train a convolutional autoencoder on 1M images dataset with random augmentations and multi-crops to use as feature extractor. We systematically compare it to the pretrained state-of-the-art models. We further use the feature extractor in two ways. First, we apply distance-based analysis and dynamic time warping to cluster temporal patterns of 31 drugs. We identify clusters allowing annotation of drugs as having cytotoxic, cytostatic, mixed or no effect. Second, we implement an adversarial/regularized learning setup to improve classification of 31 drugs and visualize image regions that contribute to the improvement. We increase top-3 classification accuracy by 8% on average and mine examples of morphological feature importance maps. We provide the feature extractor and the weights to foster transfer learning applications in biology. We also discuss utility of other pretrained models and applicability of our methods to other types of biomedical data. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_12.html">Improving Explainability of Disentangled Representations using Multipath-Attribution Mappings</a>
    </span>
    <span class="authors"> Lukas Klein, João B. S. Carvalho, Mennatallah El-Assady, Paolo Penna, Joachim M. Buhmann, Paul F Jaeger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=3uQ2Z0MhnoE">pdf</a></li><li><a href="https://openreview.net/forum?id=3uQ2Z0MhnoE">reviews</a></li></ul><span class="abstract">
      Explainable AI aims to render model behavior understandable by humans, which can be seen as an intermediate step in extracting causal relations from correlative patterns. Due to the high risk of possible fatal decisions in image-based clinical diagnostics, it is necessary to integrate explainable AI into these safety-critical systems. Current explanatory methods typically assign attribution scores to pixel regions in the input image, indicating their importance for a model&apos;s decision. However, they fall short when explaining why a visual feature is used. We propose a framework that utilizes interpretable disentangled representations for downstream-task prediction. Through visualizing the disentangled representations, we enable experts to investigate possible causation effects by leveraging their domain knowledge. Additionally, we deploy a multi-path attribution mapping for enriching and validating explanations. We demonstrate the effectiveness of our approach on a synthetic benchmark suite and two medical datasets. We show that the framework not only acts as a catalyst for causal relation extraction but also enhances model robustness by enabling shortcut detection without the need for testing under distribution shifts. Code available at github.com/***.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_L_13.html">Surface Vision Transformers: Attention-Based Modelling applied to Cortical Analysis</a>
    </span>
    <span class="authors"> Simon Dahan, Abdulah Fawaz, Logan Zane John Williams, Chunhui Yang, Timothy S. Coalson, Matthew Glasser, A David Edwards, Daniel Rueckert, Emma Claire Robinson</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=mpp843Bsf-">pdf</a></li><li><a href="https://openreview.net/forum?id=mpp843Bsf-">reviews</a></li></ul><span class="abstract">
      The extension of convolutional neural networks (CNNs) to non-Euclidean geometries has led to multiple frameworks for studying manifolds. Many of those methods have shown design limitations resulting in poor modelling of long-range associations, as the generalisation of convolutions to irregular surfaces is non-trivial. Motivated by the success of attention-modelling in computer vision, we translate convolution-free vision transformer approaches to surface data, to introduce a domain-agnostic architecture to study any surface data projected onto a spherical manifold. Here, surface patching is achieved by representing spherical data as a sequence of triangular patches, extracted from a subdivided icosphere. A transformer model encodes the sequence of patches via successive multi-head self-attention layers while preserving the sequence resolution. We validate the performance of the proposed Surface Vision Transformer (SiT) on the task of phenotype regression from cortical surface metrics derived from the Developing Human Connectome Project (dHCP). Experiments show that the SiT generally outperforms surface CNNs, while performing comparably on registered and unregistered data, suggesting the network is capable of achieving transformation invariance.  Analysis of transformer attention maps further illustrates the learning of long-range associations between distant cortical regions and offer strong potential to characterise subtle cognitive developmental patterns.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_L_14.html">Vision Transformers Enable Fast and Robust Accelerated MRI</a>
    </span>
    <span class="authors"> Kang Lin, Reinhard Heckel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=cNX6LASbv6">pdf</a></li><li><a href="https://openreview.net/forum?id=cNX6LASbv6">reviews</a></li></ul><span class="abstract">
      The Vision Transformer, when trained or pre-trained on datasets consisting of millions of images, gives excellent accuracy for image classification tasks and offers computational savings relative to convolutional neural networks. Motivated by potential accuracy gains and computational savings, we study Vision Transformers for accelerated magnetic resonance image reconstruction. We show that, when trained on the fastMRI dataset, a popular dataset for accelerated MRI only consisting of thousands of images, a Vision Transformer tailored to image reconstruction yields on par reconstruction accuracy with the U-net while enjoying higher throughput and less memory consumption. Furthermore, as Transformers are known to perform best with large-scale pre-training, but MRI data is costly to obtain, we propose a simple yet effective pre-training, which solely relies on big natural image datasets, such as ImageNet. We show that pre-training the Vision Transformer drastically improves training data efficiency for accelerated MRI, and increases robustness towards anatomy shifts. In the regime where only 100 MRI training images are available, the pre-trained Vision Transformer achieves significantly better image quality than pre-trained convolutional networks and the current state-of-the-art. Our code is available at url{https://github.com/MLI-lab/transformers_for_imaging}.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_L_15.html">A Flexible Meta-Learning Model for Image Registration</a>
    </span>
    <span class="authors"> Frederic Kanter, Jan Lellmann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=DVvXkperT3t">pdf</a></li><li><a href="https://openreview.net/forum?id=DVvXkperT3t">reviews</a></li></ul><span class="abstract">
      We propose a trainable architecture for affine image registration to produce robust starting points for conventional image registration methods. Learning-based methods for image registration often require networks with many parameters and heavily engineered cost functions and thus are complex and computationally expensive. Despite their success in recent years, these methods often lack the accuracy of classical iterative image registration and struggle with large deformations. On the other hand, iterative methods depend on good initial estimates and tuned hyperparameters. We tackle this problem by combining effective shallow networks and classical optimization algorithms using strategies from the field of meta-learning. The architecture presented in this work incorporates only first-order gradient information of the given registration problems, making it highly flexible and particularly well-suited as an initialization step for classical image registration.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_L_16.html">Warmstart Approach for Accelerating Deep Image Prior Reconstruction in Dynamic Tomography</a>
    </span>
    <span class="authors"> Tobias Knopp, Mirco Grosser</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=aWD0kzMmyD_">pdf</a></li><li><a href="https://openreview.net/forum?id=aWD0kzMmyD_">reviews</a></li></ul><span class="abstract">
      Deep image prior (DIP) has been successfully used in the field of tomography to obtain high-quality images from under-sampled and noisy measurements. The key advantage of DIP compared to conventional deep-learning based image reconstruction techniques is that it requires no training data and thus can be used in a flexible manner without incorporating domain specific knowledge. The downside of DIP is that it shifts the training step to reconstruction time where usually fast algorithms are required to reduced the latency between acquisition and the display of the reconstructed image. In this work we tackle this problem for dynamic tomography scenarios in which a large number of temporally resolved images are taken over time. By initializing the DIP network using a previous frame of the time series, it is possible to significantly reduce the overall reconstruction time. To cope with abrupt changes in the captured time-series, we propose to use an adaptive restart method having the ability to switch between warm- and coldstart depending on the amount of inter-frame changes.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short1-2"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_1.html">Leveraging Uncertainty for Deep Interpretable Classification and Weakly-Supervised  Segmentation of Histology Images</a>
    </span>
    <span class="authors"> Soufiane Belharbi, Jérôme Rony, Jose Dolz, Ismail Ben Ayed, Luke McCaffrey, Eric Granger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=wrz7c--ACPC">pdf</a></li><li><a href="https://openreview.net/forum?id=wrz7c--ACPC">reviews</a></li></ul><span class="abstract">
      Trained using only image class label, deep weakly supervised methods allow image classification and ROI segmentation for interpretability. Despite their success on natural images, they face several challenges over histology data where ROI are visually similar to background making models vulnerable to high pixel-wise false positives. These methods lack mechanisms for modeling explicitly non-discriminative regions which raises false-positive rates. We propose novel regularization terms, which enable the model to seek both non-discriminative and discriminative regions, while discouraging unbalanced segmentations and using only image class label. Our method is composed of two networks: a localizer that yields segmentation mask, followed by a classifier. The training loss pushes the localizer to build a segmentation mask that holds most discrimiantive regions while simultaneously modeling background regions. Comprehensive experiments  over two histology datasets showed the merits of our method in reducing false positives and accurately segmenting ROI.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_2.html">Representing 3D Ultrasound with Neural Fields</a>
    </span>
    <span class="authors"> Ang Nan Gu, Purang Abolmaesumi, Christina Luong, Kwang Moo Yi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=1EDRk-CyQou">pdf</a></li><li><a href="https://openreview.net/forum?id=1EDRk-CyQou">reviews</a></li></ul><span class="abstract">
      3D Ultrasound (3D-US) is a powerful imaging modality, but the high storage requirement and low spatial resolution challenge wider adoption. Recent advancements in Neural Fields suggest a potential for efficient storage and construction of 3D-US data. In this work, we show how to effectively represent 3D-US data with Neural Fields, where we first learn the 2D slices of the 3D ultrasound data and expand to 3D. This two-stage representation learning improves the quality of 3D-US in terms of Peak Signal-to-Noise Ratio (PSNR) to 31.84dB from 28.7dB, a significant improvement directly noticeable to the human eye.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_3.html">The do&apos;s and don&apos;ts of reinforcement learning for tractography</a>
    </span>
    <span class="authors"> Antoine Theberge, Christian Desrosiers, Pierre-marc Jodoin, Maxime Descoteaux</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=H7xbw-1MVPg">pdf</a></li><li><a href="https://openreview.net/forum?id=H7xbw-1MVPg">reviews</a></li></ul><span class="abstract">
      Tractography is the process of virtually reconstructing the white matter structure of the brain in a non-invasive manner. To tackle the various known problems of tractography, deep learning has been proposed, but the lack of well curated diverse datasets makes neural networks incapable of generalizing well on unseen data. Recently, deep reinforcement learning (RL) has been shown to effectively learn the tractography procedure without reference streamlines. While the performances reported were competitive, the proposed framework is complex and little is  known on the role and impact of its multiple parts. In this work, we thoroughly explore the different components of the proposed framework through seven experiments on two datasets and shed light on their impact. Our goal is to guide researchers eager to explore the possibilities of deep RL for tractography by exposing what works and what does not work with this category of approach. We find that directionality is crucial for the agents to learn the tracking procedure and that the input signal and the seeding strategy offer a trade-offs in connectivity vs. volume.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_4.html">Scale-Agnostic Super-Resolution in MRI using Feature-Based Coordinate Networks</a>
    </span>
    <span class="authors"> Dave Van Veen, Rogier Van der Sluijs, Batu Ozturkler, Arjun D Desai, Christian Bluethgen, Robert D. Boutin, Marc H. Willis, Gordon Wetzstein, David B. Lindell, Shreyas Vasanawala, John M. Pauly, Akshay Chaudhari</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=DRz8TyVQPVi">pdf</a></li><li><a href="https://openreview.net/forum?id=DRz8TyVQPVi">reviews</a></li></ul><span class="abstract">
      We propose using a coordinate network as a decoder for MRI super-resolution. The continuous signal representation of coordinate networks enables this approach to be scale-agnostic, i.e. training over a continuous range of scales and querying at arbitrary resolutions. We evaluate the benefits of denoising for coordinate networks and also compare our method to a convolutional decoder using image quality metrics and a radiologist study.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_5.html">Medical Image Quality Assurance using Deep Learning</a>
    </span>
    <span class="authors"> Dženan Zukić, Anne Haley, Curtis Lisle, James Klo, Kilian M. Pohl, Hans J Johnson, Aashish Chaudhary</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=dBxvjWJTVW-">pdf</a></li><li><a href="https://openreview.net/forum?id=dBxvjWJTVW-">reviews</a></li></ul><span class="abstract">
      We present an open-source web tool for quality control of distributed imaging studies. To minimize the amount of human time and attention spent reviewing the images, we created a neural network to provide an automatic assessment. This steers reviewers&apos; attention to potentially problematic cases, reducing the likelihood of missing image quality issues. We test our approach using 5-fold cross validation on a set of 5217 magnetic resonance images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_6.html">Evaluating graph fairness in transductive learning</a>
    </span>
    <span class="authors"> Fernanda Lenita Ribeiro, Valentina Shumovskaia, Thomas Davies, Ira Ktena</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=RojT1Dh9bzE">pdf</a></li><li><a href="https://openreview.net/forum?id=RojT1Dh9bzE">reviews</a></li></ul><span class="abstract">
      Recent work on neuroimaging has demonstrated significant benefits of using population graphs to capture non-imaging information in the prediction of neurodegenerative and neurodevelopmental disorders. These non-imaging attributes may not only contain demographic information about the individuals, e.g. age or sex, but also the acquisition site, as imaging protocols might significantly differ across sites in large-scale studies. In addition, recent studies have highlighted the need to investigate potential biases in the classifiers devised using large-scale datasets, which might be imbalanced in terms of one or more sensitive attributes. This can be exacerbated when employing these attributes in a population graph to explicitly introduce inductive biases to the machine learning model and lead to disparate predictive performance across sub-populations. In this work, we explore the impact of stratification strategies and graph structures on the fairness of a semi-supervised classifier that relies on a population graph for the prediction of autism-spectrum disorder.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_7.html">A glimpse of ClinicaDL, an open-source software for reproducible deep learning in neuroimaging</a>
    </span>
    <span class="authors"> Elina Thibeau-Sutre, Mauricio Díaz, Ravi Hassanaly, Olivier Colliot, Ninon Burgos</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gsqiNMdPSYK">pdf</a></li><li><a href="https://openreview.net/forum?id=gsqiNMdPSYK">reviews</a></li></ul><span class="abstract">
      This paper presents ClinicaDL, a deep learning software for neuroimaging processing. Its aim is to provide a concrete solution to methodological flaws often found in our field (the difficult use of neuroimaging data sets, data leakage and insufficient reproducibility), but also to raise awareness and discuss these issues with our community. The corresponding journal paper was recently accepted in Computer Methods and Programs in Biomedicine.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_8.html">Clustered-CAM: Visual Explanations for Deep Convolutional Networks for Thyroid Nodule Ultrasound Image Classification</a>
    </span>
    <span class="authors"> Ali Eskandari, Hongbo Du, ALAA ALZOUBI</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=wwpkJsAiIjH">pdf</a></li><li><a href="https://openreview.net/forum?id=wwpkJsAiIjH">reviews</a></li></ul><span class="abstract">
      Explaining the CNN classification decision is crucial for the system acceptance in critical applications such as tumour recognition in 2D Ultrasound images. Generating saliency maps that highlight the image regions contributing to the final CNN decision is one of the most common techniques. In this paper, we propose a clustering-based approach to group similar feature maps before assigning importance scores to produce a more accurate and less sensitive visual explanation for CNN models for thyroid nodule classification in US images. Our study with a dataset of 864 ultrasound images shows that the Clustered-CAM achieved a lower average drop and higher percent increase in confidence comparing to the-state-of-the-art techniques. We demonstrate that Clustered-CAM is an effective and promising approach for visualising the CNN model decisions for thyroid nodule recognition.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_9.html">On the performance of learned and fixed-framelet shrinkage networks for low-dose CT denoising</a>
    </span>
    <span class="authors"> Luis Albert Zavala Mondragon, Peter H.N. de With, Fons van der Sommen</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=WGLqD0zHXy9">pdf</a></li><li><a href="https://openreview.net/forum?id=WGLqD0zHXy9">reviews</a></li></ul><span class="abstract">
      The recently introduced wavelet shrinkage networks (WSNs) are models with a performance close to state-of-the-art CT denoising CNNs, but they are faster and have less parameters. Here, we compare elements of two WSNs. The DHSN2 where the encoding-decoding (ED) path is composed by fixed convolution filters/framelets and the noise reduction is achieved through a CNN in the skip connection. Alternatively, the LWFSN where the ED path is learned and denoising is achieved by an ensemble of semi-hard thresholds. Although both models have been used for CT denoising, heterogeneities in data partitioning, training strategies and overall design, do not allow for direct evaluation of the benefits of having a trainable ED path and using a more elaborated design of a shrinkage CNN. This paper compares these issues by evaluating WSNs under common conditions. Our results show that the configuration with the best trade-off between performance and total trainable parameters is the combination of a learned framelet in the ED path with a simple thresholding layer in the skip connection. In addition, we observe that the CNN with fixed ED improves the most from using a CNN in the skip connection, but a careful design is required of the intermediate CNN to avoid extreme increases in trainable parameters
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_10.html">Primal-Dual UNet for Sparse View Cone Beam Computed Tomography Volume Reconstruction</a>
    </span>
    <span class="authors"> Philipp Ernst, Soumick Chatterjee, Georg Rose, Andreas Nürnberger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=RVKcDeJ2fCi">pdf</a></li><li><a href="https://openreview.net/forum?id=RVKcDeJ2fCi">reviews</a></li></ul><span class="abstract">
      In this paper, the Primal-Dual UNet for sparse view CT reconstruction is modified to be applicable to cone beam projections and perform reconstructions of entire volumes instead of slices. Experiments show that the PSNR of the proposed method is increased by 10dB compared to the direct FDK reconstruction and almost 3dB compared to the modified original Primal-Dual Network when using only 23 projections. The presented network is not optimized wrt. memory consumption or hyperparameters but merely serves as a proof of concept and is limited to low resolution projections and volumes.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_11.html">Field Strength Agnostic Cardiac MR Image Segmentation</a>
    </span>
    <span class="authors"> Seb Harrevelt, Yasmina Al Khalil, Sina Amirrajab, Josien P.W. Pluim, Marcel Breeuwer, Alexander Raaijmakers</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=92wsWX2o70">pdf</a></li><li><a href="https://openreview.net/forum?id=92wsWX2o70">reviews</a></li></ul><span class="abstract">
      To train a field strength agnostic cardiac segmentation network, we propose two novel augmentation techniques that allow us to transform 3T images to synthetic 7T images: by i) simulating $B_1$ distribution to approximate the 7T bias field and ii) style transfer using an unpaired 3T-to-7T GAN model. Data augmentation with these two methods improved the average Dice score over all classes by 22% and 25% respectively, on our 7T test dataset. Furthermore, the average performance on a 1.5T and 3T dataset were maintained.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_12.html">A Python application programming interface for accessing Philips iSyntax whole slide images for computational pathology</a>
    </span>
    <span class="authors"> Nita Mulliqi, Kimmo Kartasalo, Henrik Olsson, Xiaoyi Ji, Lars Egevad, Martin Eklund, Pekka Ruusuvuori</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=bPNitiwp0nP">pdf</a></li><li><a href="https://openreview.net/forum?id=bPNitiwp0nP">reviews</a></li></ul><span class="abstract">
      Digital pathology has demonstrated its impact in improving diagnostics and prognostics in the field of pathology, through the utilization of deep learning algorithms. However, equipment from different scanner vendors used for digitizing the glass slides impose challenges for researchers due to non-interoperability between their proprietary formats. We have previously published OpenPhi (Open PatHology Interface), a Python Application Programming Interface providing seamless access to the iSyntax format of the Philips Ultra Fast Scanner, and in this short paper, we summarise its key features.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_13.html">Deep learning–based synthesis of hyperpolarized gas MRI ventilation from 3D multi-inflation proton MRI</a>
    </span>
    <span class="authors"> Joshua Russell Astley, Alberto M Biancardi, Helen Marshall, Laurie J Smith, Paul JC Hughes, Guilhem J Collier, Matthew Q Hatton, Jim M Wild, Bilal Tahir</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=K6XpQxGhFtf">pdf</a></li><li><a href="https://openreview.net/forum?id=K6XpQxGhFtf">reviews</a></li></ul><span class="abstract">
      Hyperpolarized (HP) gas MRI allows visualization and quantification of regional lung ventilation; however, there is limited clinical uptake due to the requirement for highly specialized equipment and exogenous contrast agents. Alternative, non-contrast, model-based proton ($^1$H)-MRI surrogates of ventilation, which correlate moderately with HP gas MRI, have been proposed. Recently, deep learning (DL)-based methods have been used for the synthesis of HP gas MRI from free-breathing $^1$H-MRI for a single 2D section. Here, we developed and evaluated a multi-channel 3D DL method that combines modeling and data-driven approaches to synthesize HP gas MRI ventilation scans from multi-inflation $^1$H-MRI.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_S_14.html">Do we really need all these preprocessing steps in brain MRI segmentation?</a>
    </span>
    <span class="authors"> Ekaterina Kondrateva, Polina Druzhinina, Anvar Kurmukov</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7ub0rd8h_Ie">pdf</a></li><li><a href="https://openreview.net/forum?id=7ub0rd8h_Ie">reviews</a></li></ul><span class="abstract">
      Magnetic resonance imaging (MRI) data is heterogeneous due to the differences in device manufacturers, scanning protocols, and inter-subject variability. Although preprocessing pipeline standardizes image appearance, its influence on the quality of image segmentation on deep neural networks (DNN) has never been rigorously studied. Here we report a comprehensive study of multimodal MRI brain cancer image segmentation on TCIA-GBM open-source dataset. Our results that the most popular standardization steps add no value to artificial neural network performance; moreover, preprocessing can hamper model performance. We show that the only essential transformation for accurate analysis is the unification of voxel spacing across the dataset.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_S_15.html">Can Transformers capture long-range displacements better than CNNs?</a>
    </span>
    <span class="authors"> Paraskevas Pegios, Steffen Czolbe</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=OnzEVyHwPnz">pdf</a></li><li><a href="https://openreview.net/forum?id=OnzEVyHwPnz">reviews</a></li></ul><span class="abstract">
      Convolutional Neural Networks (CNNs) are well-established in medical imaging tackling various tasks. %including image registration.  However, their performance is limited due to their incapacity to capture long spatial correspondences within images. Recently proposed deep-learning-based registration methods try to overcome this limitation by assuming that transformers are better at modeling long-range displacements thanks to the nature of the self-attention mechanism. Even though existing transformers are already considered state-of-the-art in image registration, there is no extensive validation of the key premise. In this work, we test this hypothesis by evaluating the target registration error as a function of the displacement. Our findings show that transformers outperform CNNs on a public dataset of lung 3D CT images with large displacements. Yet, the performance difference stems from transformers registering small displacements with higher accuracy. Contrary to previous beliefs, we find no evidence to support the hypothesis that transformers register long displacements better than CNNs. Additionally, our experiments provide insights on how to train vision transformers effectively for image registration on small datasets with less than 50 image pairs.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/B_S_16.html">Robustness Against Out of Distribution Video Frames in Online Surgical Workflow Recognition with Temporal Convolutional Networks</a>
    </span>
    <span class="authors"> Amirhossein Bayat, Kadir Kirtac, Salih karagoz, Julien Schwerin, Michael Stenzel, Marco Smit, Florian Aspart</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=yfnDR7kiGQI">pdf</a></li><li><a href="https://openreview.net/forum?id=yfnDR7kiGQI">reviews</a></li></ul><span class="abstract">
      The automatic recognition of surgical phase based on laparoscopic videos is a pre-requisite to diverse AI application on surgeries. Online surgical phase recognition is commonly achieved using two-stages models combining (i) a spatial feature extraction at the frame level with a (ii) temporal model.  Yet, this online surgical phase recognition is a challenging task in real-world scenarios.  For example, the camera might be temporally extracted of the body during surgeries (e.g., to be cleaned). The Out-of-body (OOB) phases have out-of-distribution spatial features and have unpredictable occurrence which affect the temporal model performance. We propose a simple, yet effective, mechanism to robustify our temporal model against OOB phases.  Our solution leverages the two-stages structure of surgical phase model predictions. We train and test our model on a large scale real-world dataset of laparoscopic cholecystectomy videos and show the effectiveness of our approach.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_17.html">Dual Branch Prior-SegNet: CNN for Interventional CBCT using Planning Scan and Auxiliary Segmentation Loss</a>
    </span>
    <span class="authors"> Philipp Ernst, Suhita Ghosh, Georg Rose, Andreas Nürnberger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=uhv14tCLmoB">pdf</a></li><li><a href="https://openreview.net/forum?id=uhv14tCLmoB">reviews</a></li></ul><span class="abstract">
      This paper proposes an extension to the Dual Branch Prior-Net for sparse view interventional CBCT reconstruction incorporating a high quality planning scan. An additional head learns to segment interventional instruments and thus guides the reconstruction task. The prior scans are misaligned by up to +-5deg in-plane during training. Experiments show that the proposed model, Dual Branch Prior-SegNet, significantly outperforms any other evaluated model by &gt;2.8dB PSNR. It also stays robust wrt. rotations of up to +-5.5deg.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_18.html">The effect of intra-scan motion on AI reconstructions in MRI</a>
    </span>
    <span class="authors"> Laurens Beljaards, Nicola Pezzotti, Christophe Schülke, Matthias J. P. van Osch, Marius Staring</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=y7BbSh__-UZ">pdf</a></li><li><a href="https://openreview.net/forum?id=y7BbSh__-UZ">reviews</a></li></ul><span class="abstract">
      MRI can be accelerated via (AI-based) reconstruction by undersampling k-space. Current methods typically ignore intra-scan motion, although even a few millimeters of motion can introduce severe blurring and ghosting artifacts that necessitate reacquisition. In this short paper we investigate the effects of rigid-body motion on AI-based reconstructions. Leveraging the Bloch equations we simulate motion corrupted MRI acquisitions with a linear interleaved scanning protocol including spin history effects, and investigate i) the effect on reconstruction quality, and ii) if this corruption can be mitigated by introducing motion-corrupted data during training. We observe an improvement from 0.819 to 0.867 in terms of SSIM when motion-corrupted brain data is included during training, demonstrating that training with motion-corrupted data can partially compensate for motion corruption. Inclusion of spin-history effects did not influence the results.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/B_S_19.html">Efficient Exploitation of Image Repetitions in MR Reconstruction</a>
    </span>
    <span class="authors"> Fasil Gadjimuradov, Thomas Benkert, Marcel Dominik Nickel, Andreas Maier</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7CnEuy4_Iwv">pdf</a></li><li><a href="https://openreview.net/forum?id=7CnEuy4_Iwv">reviews</a></li></ul><span class="abstract">
      Parallel imaging with multiple receiver coils has become a standard in many MRI applications. Methods based on Deep Learning (DL) were shown to allow higher acceleration factors than conventional methods. In the case of diffusion-weighted imaging (DWI) where multiple repetitions of a slice are acquired, a DL-based reconstruction method should ideally make use of available redundancies. Based on the concept of Deep Sets which outlines a generic approach for operating on set-structured data, this work investigates the benefits of joint reconstruction of image repetitions in DWI. Evaluations show that, compared to separate processing of repetitions, reconstructions can be improved both qualitatively and quantitatively by incorporating simple and computationally inexpensive operations into an existing DL architecture.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/B_S_20.html">Learning Registration Models with Differentiable Gauss-Newton Optimisation</a>
    </span>
    <span class="authors"> Mattias P Heinrich</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=2aqkrhzUPyF">pdf</a></li><li><a href="https://openreview.net/forum?id=2aqkrhzUPyF">reviews</a></li></ul><span class="abstract">
      We propose to capture large deformations in few iterations by learning a registration model with differentiable Gauss-Newton and compact CNNs that predict displacement gradients and a suitable residual function. By incorporating a sparse Laplacian regulariser, structural / semantic representations and weak label-supervision we achieve state-of-the-art performance for abdominal CT registration.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral1-3"></a><h3>Oral Session 1.3: Registration - 16:20 - 17:20 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/C1.html">KeyMorph: Robust Multi-modal Affine Registration via Unsupervised Keypoint Detection</a>
    </span>
    <span class="authors"> Evan M Yu, Alan Q. Wang, Adrian V Dalca, Mert R. Sabuncu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=OrNzjERFybh">pdf</a></li><li><a href="https://openreview.net/forum?id=OrNzjERFybh">reviews</a></li></ul><span class="abstract">
      Registration is a fundamental task in medical imaging, and recent machine learning methods have become the state-of-the-art. However, these approaches are often not interpretable, lack robustness to large misalignments, and do not incorporate symmetries of the problem. In this work, we propose KeypointMorph, an unsupervised end-to-end learning-based image registration framework that relies on automatically detecting corresponding keypoints. Our core insight is straightforward: matching keypoints between images can be used to obtain the optimal transformation via a differentiable closed-form expression. We use this observation to drive the unsupervised learning of anatomically-consistent keypoints from images. This not only leads to substantially more robust registration but also yields better interpretability, since the keypoints reveal which parts of the image are driving the final alignment. Moreover, KeypointMorph can be designed to be equivariant under image translations and/or symmetric with respect to the input image ordering. We demonstrate the proposed framework in solving 3D affine registration of multi-modal brain MRI scans. Remarkably, we show that this strategy leads to consistent keypoints, even across modalities. We demonstrate registration accuracy that surpasses current state-of-the-art methods, especially in the context of large displacements.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/C2.html">Implicit Neural Representations for Deformable Image Registration</a>
    </span>
    <span class="authors"> Jelmer M. Wolterink, Jesse C. Zwienenberg, Christoph Brune</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=BP29eKzQBu3">pdf</a></li><li><a href="https://openreview.net/forum?id=BP29eKzQBu3">reviews</a></li></ul><span class="abstract">
      Deformable medical image registration has in past years been revolutionized by deep learning with convolutional neural networks. These methods surpass conventional image registration techniques in speed but not in accuracy. Here, we present an alternative approach to leveraging neural networks for image registration. Instead of using a neural network to predict the transformation between images, we optimize a neural network to represent this continuous transformation. Using recent insights from differentiable rendering, we show how such an implicit deformable image registration (IDIR) model can be naturally combined with regularization terms based on standard automatic differentiation techniques. We demonstrate the effectiveness of this model on 4D chest CT registration in the DIR-LAB data set and find that a single three-layer multi-layer perceptron with periodic activation functions outperforms all published deep learning-based methods, without any folding and without the need for training data. The model is flexible enough to be extended to include different losses, regularizers, and optimization schemes and is implemented using standard deep learning libraries.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/C3.html">TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces</a>
    </span>
    <span class="authors"> Andrew Hoopes, Juan Eugenio Iglesias, Bruce Fischl, Douglas Greve, Adrian V Dalca</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=-JiHeZNDY3a">pdf</a></li><li><a href="https://openreview.net/forum?id=-JiHeZNDY3a">reviews</a></li></ul><span class="abstract">
      Mesh-based reconstruction of the cerebral cortex is a fundamental component in brain image analysis. Classical, iterative pipelines for cortical modeling are robust but often time-consuming, mostly due to expensive procedures that involve topology correction and spherical mapping. Recent attempts to address reconstruction with machine learning methods have accelerated some components in these pipelines, but they still require slow processing steps to enforce topological constraints to comply with known anatomical structure. In this work, we introduce a novel learning-based strategy, TopoFit, which rapidly fits a topologically-correct surface to the white-matter tissue boundary. We design a joint network with image and graph convolutions and an efficient symmetric distance loss to learn to predict accurate deformations that map a template mesh to subject-specific anatomy. This technique encompasses the work of current mesh correction, fine-tuning, and inflation steps and, as a result, offers a $150  imes$ faster solution to cortical surface reconstruction compared to traditional approaches. We demonstrate that TopoFit is robust to common failure modes, such as white-matter tissue hypointensities, and is $1.8    imes$ more accurate than current state-of-the-art deep-learning strategy. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/C4.html">A Flexible Meta-Learning Model for Image Registration</a>
    </span>
    <span class="authors"> Frederic Kanter, Jan Lellmann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=DVvXkperT3t">pdf</a></li><li><a href="https://openreview.net/forum?id=DVvXkperT3t">reviews</a></li></ul><span class="abstract">
      We propose a trainable architecture for affine image registration to produce robust starting points for conventional image registration methods. Learning-based methods for image registration often require networks with many parameters and heavily engineered cost functions and thus are complex and computationally expensive. Despite their success in recent years, these methods often lack the accuracy of classical iterative image registration and struggle with large deformations. On the other hand, iterative methods depend on good initial estimates and tuned hyperparameters. We tackle this problem by combining effective shallow networks and classical optimization algorithms using strategies from the field of meta-learning. The architecture presented in this work incorporates only first-order gradient information of the given registration problems, making it highly flexible and particularly well-suited as an initialization step for classical image registration.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<h2>Thursday 7th July</h2>
<p><a id="oral2-1"></a><h3>Oral Session 2.1: Domain Adaptation and Model Generalization - 09:40 - 10:40 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/D1.html">OptTTA: Learnable Test-Time Augmentation for Source-Free Medical Image Segmentation Under Domain Shift</a>
    </span>
    <span class="authors"> Devavrat Tomar, Guillaume Vray, Jean-Philippe Thiran, Behzad Bozorgtabar</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=B6HdQaY_iR">pdf</a></li><li><a href="https://openreview.net/forum?id=B6HdQaY_iR">reviews</a></li></ul><span class="abstract">
      As distribution shifts are inescapable in realistic clinical scenarios due to inconsistencies in imaging protocols, scanner vendors, and across different centers, well-trained deep models incur a domain generalization problem in unseen environments. Despite a myriad of model generalization techniques to circumvent this issue, their broad applicability is impeded as (i) source training data may not be accessible after deployment due to privacy regulations, (ii) the availability of adequate test domain samples is often impractical, and (iii) such model generalization methods are not well-calibrated, often making unreliable overconfident predictions. This paper proposes a novel learnable test-time augmentation, namely OptTTA, tailored specifically to alleviate large domain shifts for the source-free medical image segmentation task. OptTTA enables efficiently generating augmented views of test input, resembling the style of private source images and bridging a domain gap between training and test data. Our proposed method explores optimal learnable test-time augmentation sub-policies that provide lower predictive entropy and match the source model&apos;s internal batch normalization statistics without requiring access to training source samples. Thorough evaluation and ablation studies on challenging multi-center and multi-vendor MRI datasets of three anatomies have demonstrated the performance superiority of OptTTA over prior-arts test-time augmentation and model adaptation methods. Additionally, the generalization capabilities and effectiveness of OptTTA are evaluated in terms of aleatoric uncertainty and model calibration analyses. Our PyTorch code implementation is publicly available at https://github.com/devavratTomar/OptTTA.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/D2.html">Domain adaptation through anatomical constraints for 3d human pose estimation under the cover</a>
    </span>
    <span class="authors"> Alexander Bigalke, Lasse Hansen, Jasper Diesel, Mattias P Heinrich</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=iCTU7EQipC">pdf</a></li><li><a href="https://openreview.net/forum?id=iCTU7EQipC">reviews</a></li></ul><span class="abstract">
      Domain adaptation has the potential to overcome the expensive or even infeasible labeling of target data by transferring knowledge from a labeled source domain. In this work, we address domain adaptation in the context of point cloud-based 3D human pose estimation, whose clinical applicability is severely limited by a lack of labeled training data. Unlike the mainstream approach of domain-invariant feature learning, we propose to guide the learning process in the target domain through weak supervision, based on prior knowledge about human anatomy. We embed this prior knowledge into a novel loss function that encourages network predictions to match the statistics of an anatomically plausible skeleton. Specifically, we formulate three loss functions that penalize asymmetric limb lengths, implausible joint angles, and implausible bone lengths. We evaluate the method on a public lying pose dataset (SLP), adapting from uncovered patients in the source to covered patients in the target domain. Our method outperforms diverse state-of-the-art domain adaptation techniques and improves the baseline model by 25% while reducing the gap to a fully supervised model by 52%. Source code is available at https://github.com/multimodallearning/da-3dhpe-anatomy.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/D3.html">Signal Domain Learning Approach for Optoacoustic Image Reconstruction from Limited View Data</a>
    </span>
    <span class="authors"> Anna Klimovskaia, Berkan Lafci, Firat Ozdemir, Neda Davoudi, Xose Luis Dean-Ben, Fernando Perez-Cruz, Daniel Razansky</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=9NOyrfUBtx1">pdf</a></li><li><a href="https://openreview.net/forum?id=9NOyrfUBtx1">reviews</a></li></ul><span class="abstract">
      Multi-spectral optoacoustic tomography (MSOT) relies on optical excitation of tissues with subsequent detection of the generated ultrasound waves. Optimal image quality in MSOT is achieved by detection of signals from a broad tomographic view. However, due to physical constraints and other cost-related considerations, most imaging systems are implemented with probes having limited tomographic coverage around the imaged object, such as linear array transducers often employed for clinical ultrasound (US) imaging. MSOT image reconstruction from limited-view data results in arc-shaped image artifacts and disrupted shape of the vascular structures. Deep learning methods have previously been used to recover MSOT images from incomplete tomographic data, albeit poor performance was attained when training with data from simulations or other imaging modalities. We propose a two-step method consisting of i) style transfer for domain adaptation between simulated and experimental MSOT signals, and ii) supervised training on simulated data to recover missing tomographic signals in realistic clinical data. The method is shown capable of correcting images reconstructed from sub-optimal probe geometries using only signal domain data without the need for training with ground truth full-view images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/D4.html">Domain Generalization for Retinal Vessel Segmentation with Vector Field Transformer</a>
    </span>
    <span class="authors"> Dewei Hu, Hao Li, Han Liu, Ipek Oguz</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=mB_V8ThxY8Z">pdf</a></li><li><a href="https://openreview.net/forum?id=mB_V8ThxY8Z">reviews</a></li></ul><span class="abstract">
      Domain generalization has become a heated topic in the literature of deep learning. It has great impact on medical image analysis as the inconsistency of data distribution is prevalent in most of the medical data modalities due to the image acquisition techniques. In this study, we investigate a novel pipeline that generalizes the retinal vessel segmentation across color fundus photography and OCT angiography images. We hypothesize that the scaled minor eigenvector of the Hessian matrix can sufficiently represent the vessel by vector flow. This vector field can be regarded as a common domain for different modalities as it is very similar even for data that follows vastly different intensity distributions. We describe two additional contributions of our work. First, we leverage the uncertainty in the latent space of the auto-encoder to synthesize enhanced vessel maps to augment the training data. Then we propose a transformer network to extract features from the vector field. In comprehensive experiments, we show that our model can work in cross-modality fashion.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster2-1"></a><h3>Poster Session 2.1 - Onsite 15:20 - 16:20 , Virtual 11:00 - 12:00 (UTC+2)</h3>
<a id="long2-1"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_L_1.html">Breathing Freely: Self-supervised Liver T1rho Mapping from A Single T1rho-weighted Image</a>
    </span>
    <span class="authors"> Chaoxing Huang, Yurui Qian, Jian Hou, Baiyan Jiang, Queenie Chan, Vincent Wong, Winnie Chiu Wing Chu, Weitian Chen</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=x5GYGP2cPI9">pdf</a></li><li><a href="https://openreview.net/forum?id=x5GYGP2cPI9">reviews</a></li></ul><span class="abstract">
      Quantitative $T1rho$ imaging is a promising technique for assessment of chronic liver disease. The standard approach requires acquisition of multiple $T1rho$-weighted images of the liver to quantify $T1rho$ relaxation time. The quantification accuracy can be affected by respiratory motion if the subjects cannot hold the breath during the scan.  To tackle this problem, we propose a self-supervised mapping method by taking only one $T1rho$-weighted image to do the mapping. Our method takes into account of signal scale  variations in MR  scan when performing $T1rho$ quantification. Preliminary experimental results show that our method can achieve  better mapping performance than the traditional fitting method, particularly in free-breathing scenarios. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/C_L_2.html">Unsupervised Domain Adaptation through Shape Modeling for Medical Image Segmentation</a>
    </span>
    <span class="authors"> Yuan Yao, Fengze Liu, Zongwei Zhou, Yan Wang, Wei Shen, Alan Yuille, Yongyi Lu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=CwXCs6HObSw">pdf</a></li><li><a href="https://openreview.net/forum?id=CwXCs6HObSw">reviews</a></li></ul><span class="abstract">
      Shape information is a strong and useful prior in segmenting organs in medical image. However, most current deep learning based segmentation algorithms don&apos;t take shape information into consideration, which can lead to bias towards texture. We aim at modeling shape explicitly and use it to help medical image segmentation. Previous methods proposed variational autoencoder (VAE) based models to learn the distribution of shape for a certain organ, and used it to automatically evaluate the quality of a segmentation prediction by fitting it into the learned shape distribution. Based on which we aim at incorporating VAE into current segmentation pipelines. Specifically, we propose a new unsupervised domain adaptation pipeline based on a pseudo loss and a VAE reconstruction loss under a teacher-student learning paradigm. Both losses are optimized simultaneously and in return, boosts the segmentation task performance. Extensive experiments on three public Pancreas segmentation datasets as well as one in-house Pancreas segmentation dataset demonstrate the effectiveness of our method in challenging unsupervised domain adaptation scenario for medical image segmentation. We hope this work will advance shape analysis and geometric learning in medical imaging.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_L_3.html">PILLET-GAN: Pixel-Level Lesion Traversal Generative Adversarial Network for Pneumonia Localization</a>
    </span>
    <span class="authors"> Hyunwoo Kim, Hanbin Ko, Jungjun Kim</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kFDD80TdDLs">pdf</a></li><li><a href="https://openreview.net/forum?id=kFDD80TdDLs">reviews</a></li></ul><span class="abstract">
      The study of pneumonia localization focus on the problem of accurate lesion localization in the thoracic X-ray image. It is crucial to provide precisely localized regions to users. It can lay out the basis of the model decision by comparing the X-ray image between the &apos;Healthy&apos; and &apos;Disease&apos; classes. In particular, for the medical image analysis, it is essential not only to make a correct prediction for the disease but also to provide evidence to support accurate predictions. Many generative adversarial networks (GAN) based approaches are employed to show the pixel-level changes via domain translation technique to address this issue. Although previous research tried to improve localization performance by understanding the domain&apos;s attributes for better image translation, it remains challenging to capture the specific category&apos;s pixel-level changes. For this reason, we focus on the stage of understanding of category attributes. We propose a Pixel-Level Lesion Traversal Generative Adversarial Network (PILLET-GAN) that mines spatial features for the category via spatial attention technique and fuses them into an original feature map extracted from the generator for better domain translation. Our experimental results show that PILLET-GAN achieves superior performance compared to the state-of-the-art models on qualitative and quantitative results on the RSNA-pneumonia dataset.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_L_4.html">Is it Possible to Predict MGMT Promoter Methylation from Brain Tumor MRI Scans using Deep Learning Models?</a>
    </span>
    <span class="authors"> Numan Saeed, Shahad Emad Hardan, Kudaibergen Abutalip, Mohammad Yaqub</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=4V7YQVC7Kru">pdf</a></li><li><a href="https://openreview.net/forum?id=4V7YQVC7Kru">reviews</a></li></ul><span class="abstract">
      Glioblastoma is a common brain malignancy that tends to occur in older adults and is almost always lethal. The effectiveness of chemotherapy, being the standard treatment for most cancer types, can be improved if a particular genetic sequence in the tumor known as MGMT promoter is methylated. However, to identify the state of the MGMT promoter, the conventional approach is to perform a biopsy for genetic analysis, which is time and effort consuming. A couple of recent publications proposed a connection between the MGMT promoter state and the MRI scans of the tumor and hence suggested the use of deep learning models for this purpose. Therefore, in this work, we use one of the most extensive datasets, BraTS 2021, to study the potency of employing deep learning solutions, including 2D and 3D CNN models and vision transformers. After conducting a thorough analysis of the model&apos;s performance, we concluded that there seems to be no connection between the MRI scans and the state of the MGMT promoter.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_L_5.html">MR Image Super Resolution By Combining Feature Disentanglement CNNs and Vision Transformers</a>
    </span>
    <span class="authors"> Dwarikanath Mahapatra, Zongyuan Ge</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=_GUu3Rf8Gy">pdf</a></li><li><a href="https://openreview.net/forum?id=_GUu3Rf8Gy">reviews</a></li></ul><span class="abstract">
      State of the art magnetic resonance (MR) image super-resolution methods (ISR) leverage limited contextual information due to the use of CNNs, which learn interactions over  a small neighborhood. On the other hand Vision transformers (ViT) have the ability to learn much more global contextual information, which is especially relevant for MR ISR since they provide additional information to generate superior quality HR images. We propose to combine local information of CNNs and global information from ViTs for image super resolution and output super resolved images that have superior quality than those produced by state of the art methods. Additionally, we incorporate extra constraints through multiple novel loss functions that preserve structure and texture information from the low resolution to high resolution images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/C_L_6.html">OptTTA: Learnable Test-Time Augmentation for Source-Free Medical Image Segmentation Under Domain Shift</a>
    </span>
    <span class="authors"> Devavrat Tomar, Guillaume Vray, Jean-Philippe Thiran, Behzad Bozorgtabar</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=B6HdQaY_iR">pdf</a></li><li><a href="https://openreview.net/forum?id=B6HdQaY_iR">reviews</a></li></ul><span class="abstract">
      As distribution shifts are inescapable in realistic clinical scenarios due to inconsistencies in imaging protocols, scanner vendors, and across different centers, well-trained deep models incur a domain generalization problem in unseen environments. Despite a myriad of model generalization techniques to circumvent this issue, their broad applicability is impeded as (i) source training data may not be accessible after deployment due to privacy regulations, (ii) the availability of adequate test domain samples is often impractical, and (iii) such model generalization methods are not well-calibrated, often making unreliable overconfident predictions. This paper proposes a novel learnable test-time augmentation, namely OptTTA, tailored specifically to alleviate large domain shifts for the source-free medical image segmentation task. OptTTA enables efficiently generating augmented views of test input, resembling the style of private source images and bridging a domain gap between training and test data. Our proposed method explores optimal learnable test-time augmentation sub-policies that provide lower predictive entropy and match the source model&apos;s internal batch normalization statistics without requiring access to training source samples. Thorough evaluation and ablation studies on challenging multi-center and multi-vendor MRI datasets of three anatomies have demonstrated the performance superiority of OptTTA over prior-arts test-time augmentation and model adaptation methods. Additionally, the generalization capabilities and effectiveness of OptTTA are evaluated in terms of aleatoric uncertainty and model calibration analyses. Our PyTorch code implementation is publicly available at https://github.com/devavratTomar/OptTTA.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/C_L_7.html">Domain adaptation through anatomical constraints for 3d human pose estimation under the cover</a>
    </span>
    <span class="authors"> Alexander Bigalke, Lasse Hansen, Jasper Diesel, Mattias P Heinrich</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=iCTU7EQipC">pdf</a></li><li><a href="https://openreview.net/forum?id=iCTU7EQipC">reviews</a></li></ul><span class="abstract">
      Domain adaptation has the potential to overcome the expensive or even infeasible labeling of target data by transferring knowledge from a labeled source domain. In this work, we address domain adaptation in the context of point cloud-based 3D human pose estimation, whose clinical applicability is severely limited by a lack of labeled training data. Unlike the mainstream approach of domain-invariant feature learning, we propose to guide the learning process in the target domain through weak supervision, based on prior knowledge about human anatomy. We embed this prior knowledge into a novel loss function that encourages network predictions to match the statistics of an anatomically plausible skeleton. Specifically, we formulate three loss functions that penalize asymmetric limb lengths, implausible joint angles, and implausible bone lengths. We evaluate the method on a public lying pose dataset (SLP), adapting from uncovered patients in the source to covered patients in the target domain. Our method outperforms diverse state-of-the-art domain adaptation techniques and improves the baseline model by 25% while reducing the gap to a fully supervised model by 52%. Source code is available at https://github.com/multimodallearning/da-3dhpe-anatomy.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_L_8.html">Transformer-based out-of-distribution detection for clinically safe segmentation</a>
    </span>
    <span class="authors"> Mark S Graham, Petru-Daniel Tudosiu, Paul Wright, Walter Hugo Lopez Pinaya, James Teo, Jean-Marie U-King-Im, Yee Mah, Rolf H. Jäger, David Werring, Parashkev Nachev, Sebastien Ourselin, M. Jorge Cardoso</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=En7660i-CLJ">pdf</a></li><li><a href="https://openreview.net/forum?id=En7660i-CLJ">reviews</a></li></ul><span class="abstract">
      In a clinical setting it is essential that deployed image processing systems are robust to the full range of inputs they might encounter and, in particular, do not make confidently wrong predictions. The most popular approach to safe processing is to train networks that can provide a measure of their uncertainty, but these tend to fail for inputs that are far outside the training data distribution. Recently, generative modelling approaches have been proposed as an alternative; these can quantify the likelihood of a data sample explicitly, filtering out any out-of-distribution (OOD) samples before further processing is performed. In this work, we focus on image segmentation and evaluate several approaches to network uncertainty in the far-OOD and near-OOD cases for the task of segmenting haemorrhages in head CTs. We find all of these approaches are unsuitable for safe segmentation as they provide confidently wrong predictions when operating OOD. We propose performing full 3D OOD detection using a VQ-GAN to provide a compressed latent representation of the image and a transformer to estimate the data likelihood. Our approach successfully identifies images in both the far- and near-OOD cases. We find a strong relationship between image likelihood and the quality of a model&apos;s segmentation, making this approach viable for filtering images unsuitable for segmentation.  To our knowledge, this is the first time transformers have been applied to perform OOD detection on 3D image data.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_L_9.html">On learning adaptive acquisition policies for undersampled multi-coil MRI reconstruction</a>
    </span>
    <span class="authors"> Tim Bakker, Matthew J. Muckley, Adriana Romero-Soriano, Michal Drozdzal, Luis Pineda</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=eAkOp9Oet5y">pdf</a></li><li><a href="https://openreview.net/forum?id=eAkOp9Oet5y">reviews</a></li></ul><span class="abstract">
      Most current approaches to undersampled multi-coil MRI reconstruction focus on learning the reconstruction model for a fixed, equidistant acquisition trajectory. In this paper, we study the problem of joint learning of the reconstruction model together with acquisition policies. To this end, we extend the End-to-End Variational Network with learnable acquisition policies that can adapt to different data points. We validate our model on a coil-compressed version of the large scale undersampled multi-coil astMRI dataset using two undersampling factors: $4  imes$ and $8    imes$. Our experiments show that we are able to outperform the learnable non-adaptive and handcrafted equidistant strategies for both acceleration factors, with an observed improvement up to $\sim 3\%$ in SSIM, suggesting that potentially-adaptive $k$-space acquisition trajectories can improve reconstructed image quality for larger acceleration factors. However, and perhaps surprisingly, our best performing policies learn to be explicitly non-adaptive.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_L_10.html">Angular Super-Resolution in Diffusion MRI with a 3D Recurrent Convolutional Autoencoder</a>
    </span>
    <span class="authors"> Matthew Lyon, Mauricio A Álvarez, Paul Armitage</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=U6HJMtAgW-N">pdf</a></li><li><a href="https://openreview.net/forum?id=U6HJMtAgW-N">reviews</a></li></ul><span class="abstract">
      High resolution diffusion MRI (dMRI) data is often constrained by limited scanning time in clinical settings, thus restricting the use of downstream analysis techniques that     would otherwise be available. In this work we develop a 3D recurrent convolutional neural     network (RCNN) capable of super-resolving dMRI volumes in the angular (q-space)     domain. Our approach formulates the task of angular super-resolution as a patch-wise regression     using a 3D autoencoder conditioned on target b-vectors. Within the network we use a     convolutional long short term memory (ConvLSTM) cell to model the relationship between     q-space samples. We compare model performance against a baseline spherical harmonic     interpolation and a 1D variant of the model architecture. We show that the 3D model has the     lowest error rates across different subsampling schemes and b-values. The relative performance     of the 3D RCNN is greatest in the very low angular resolution domain. Code for this project is     available at \href{https://github.com/mattlyon93/dMRI-RCNN}{github.com/mattlyon93/dMRI-RCNN}.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_L_11.html">Explainable Weakly-Supervised Cell Nuclei Segmentation by Canonical Shape Learning and Transformation</a>
    </span>
    <span class="authors"> Pedro Costa, Alex Gaudio, Aurélio Campilho, Jaime S Cardoso</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=k7JurYNOhQA">pdf</a></li><li><a href="https://openreview.net/forum?id=k7JurYNOhQA">reviews</a></li></ul><span class="abstract">
      Microscopy images have been increasingly analyzed quantitatively in biomedical research. Segmenting individual cell nucleus is an important step as many research studies involve counting cells and analysing their shape.  We propose a novel weakly supervised instance segmentation method that is trained with image segmentation masks only.  Our system is composed of 2 models: an  implicit shape Multi-Layer Perceptron (MLP) that learns the shape of the nuclei in canonical coordinates; and 2) an encoder that predicts the parameters of the affine transformation to deform the canonical shape into the correct location, scale and orientation in the image. Our system is explainable, as the implicit shape MLP learns that the canonical shape of the cell nuclei is a circle, and interpretable as the output of the encoder are parameters of affine transformations. We obtain image segmentation performance close to DeepLabV3 and, additionally, obtain an F1-score$_{IoU=0.5}$ of $68.47\%$ at the instance segmentation task, even though the system was trained with image segmentations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short2-1"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_S_1.html">Evaluation beyond y and p(y)</a>
    </span>
    <span class="authors"> Thijs Kooi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=eU4xqygla-Q">pdf</a></li><li><a href="https://openreview.net/forum?id=eU4xqygla-Q">reviews</a></li></ul><span class="abstract">
      Academic papers and challenges focus mostly on metrics that measure how well a model&apos;s output p(y) approximates labels y. However, a high performance based on these metrics is not a sufficient condition for a practically useful model. Looking into the complexity of a model both in terms of hardware and software can shed more light on the practical merit. This short paper discusses several measures for medical AI system that do not focus solely on labels and predictions. We encourage the research community to consider these metrics more often.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_S_2.html">Stress Testing Vision Transformers Using Common Histopathological Artifacts</a>
    </span>
    <span class="authors"> Geetank Raipuria, Nitin Singhal</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=HpPRDevDYDY">pdf</a></li><li><a href="https://openreview.net/forum?id=HpPRDevDYDY">reviews</a></li></ul><span class="abstract">
      Artifacts on digitized Whole Slide Images like blur, tissue fold, and foreign particles have been demonstrated to degrade the performance of deep convolutional neural networks (CNNs). For prospective deployment of deep learning models in computational histopathology, it is essential that the models are robust to common artifacts. In this work, we stress test multi-head self-attention based Vision Transformer models using 10 common artifacts and compare the performance to CNNs. We discovered that Transformers are substantially more robust to artifacts in histopathological images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_3.html">AI at the forefront of the eye: Triaging tool for confocal microscopy images of human cornea</a>
    </span>
    <span class="authors"> Vlada Rozova, Kh Tohidul Islam, Laura E Downie, Holly Chinnery, Karin Verspoor</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=zOClNUtqKTB">pdf</a></li><li><a href="https://openreview.net/forum?id=zOClNUtqKTB">reviews</a></li></ul><span class="abstract">
      Corneal confocal microscopy is used in both ophthalmology and neurology to identify and monitor the immunological and neural effects of ocular and systemic diseases. However, its use in research and clinical settings is limited by the lack of reliable, time-efficient methods to process acquired data. A typical imaging session yields a stack of images varying in quality and field of view that require careful filtering prior to further analysis. Here, we present a framework for automated quality assessment and selection of distinct human corneal confocal microscopy images suitable for downstream analysis.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_4.html">Three-Dimensional Medical Image Synthesis with Denoising Diffusion Probabilistic Models</a>
    </span>
    <span class="authors"> Zolnamar Dorjsembe, Sodtavilan Odonchimed, Furen Xiao</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Oz7lKWVh45H">pdf</a></li><li><a href="https://openreview.net/forum?id=Oz7lKWVh45H">reviews</a></li></ul><span class="abstract">
      Denoising diffusion probabilistic models (DDPM) have recently shown superior performance in image synthesis and have been extensively studied in various image processing tasks. In this work, we propose a 3D-DDPM for generating three-dimensional (3D) medical images. Different from previous studies, to the best of our knowledge, this work presents the first attempt to investigate the DDPM to enable 3D medical image synthesis. We investigated the generation of high-resolution magnetic resonance images (MRI) of brain tumors. The proposed method is evaluated through experiments on a semi-public dataset, with both quantitative and qualitative tests showing promising results.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="xtai poster">
    <span class="title">
      <a href="papers/C_S_5.html">Sentinel lymph node status prediction using self-attention networks and contrastive learning from routine histology images of primary tumours</a>
    </span>
    <span class="authors"> Carlos Hernandez-Perez, Veronica Vilaplana, Josep Malvehy, Marc Combalia</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=_zznzJjuaIS">pdf</a></li><li><a href="https://openreview.net/forum?id=_zznzJjuaIS">reviews</a></li></ul><span class="abstract">
      Deep learning-based computational pathology approaches are becoming increasingly prominent in histopathology image analysis. However, these images typically come with drawbacks that hamper automatic analysis, which include: labeled sample scarcity or the extremely large size of the images (ranging from $10^7$ to $10^{12}$ pixels). Nonetheless, they have proven to be a powerful tool for diagnosis and risk prevention. One such prevention is reducing the number of patients who undergo surgeries that do not benefit them. This study develops a pipeline for predicting sentinel lymph node (SLN) metastasis non-invasively from digitised Whole Slide Images (WSI) of primary melanoma tumours. Furthermore, we combine the use of a weakly supervised architecture with self-supervised contrastive pre-training. We experimentally demonstrate that 1) the use of self-attention improves sentinel lymph node status prediction and 2) self-supervised contrastive learning improves the quality of the learned representations compared to a standard ImageNet pre-training, which boosts the model&apos;s performance.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_6.html">Novel Deep Learning Approach to Derive Cytokeratin Expression and Epithelium Segmentation from DAPI</a>
    </span>
    <span class="authors"> Felix Jakob Segerer, Katharina Nekolla, Lorenz Rognoni, Ansh Kapil, Markus Schick, Helen Angell, Günter Schmidt</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=fzhKWLjJZok">pdf</a></li><li><a href="https://openreview.net/forum?id=fzhKWLjJZok">reviews</a></li></ul><span class="abstract">
      Generative Adversarial Networks (GANs) are state of the art for image synthesis. Here, we present dapi2ck, a novel GAN-based approach to synthesize cytokeratin (CK) staining from immunofluorescent (IF) DAPI staining of nuclei in non-small cell lung cancer (NSCLC) images. We use the synthetic CK to segment epithelial regions, which, compared to expert annotations, yield equally good results as segmentation on stained CK. Considering the limited number of markers in a multiplexed IF (mIF) panel, our approach allows to replace CK by another marker addressing the complexity of the tumor micro-environment (TME) to facilitate patient selection for immunotherapies. In contrast to stained CK, dapi2ck does not suffer from issues like unspecific CK staining or loss of tumoral CK expression.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/C_S_7.html">Automated Multibeat Tissue Doppler Echocardiography Analysis Using Deep Neural Networks</a>
    </span>
    <span class="authors"> Elisabeth Sarah Lane, Jevgeni Jevsikov, Niti Dhutia, Matthew J Shun-shin, Darrel P Francis, Massoud Zolgharni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6rJ2vWLD7P-">pdf</a></li><li><a href="https://openreview.net/forum?id=6rJ2vWLD7P-">reviews</a></li></ul><span class="abstract">
      Tissue Doppler Imaging is an essential echocardiographic technique for the non-invasive assessment of myocardial blood velocity. Interpretation by trained experts is time-consuming and disruptive to workflow. This study presents an automated deep learning model, trained and tested on Doppler strips of arbitrary length, capable of rapid beat detection and Cartesian coordinate localisation of peak velocities with accuracy indistinguishable from human experts, but with greater speed. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_8.html">SHAPR Predicts 3D Cell Shapes from 2D Microscopic Images</a>
    </span>
    <span class="authors"> Dominik Waibel, Niklas Kiermeyer, Scott Atwell, Ario Sadafi, Matthias Meier, Carsten Marr</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=NPww3kw8Af">pdf</a></li><li><a href="https://openreview.net/forum?id=NPww3kw8Af">reviews</a></li></ul><span class="abstract">
      Reconstructing shapes of three-dimensional (3D) objects from two-dimensional (2D) images is a challenging spatial reasoning task for both our brain and computer vision algorithms.  We focus on solving this inverse problem with a novel deep learning SHApe PRediction autoencoder (SHAPR), and showcase its potential on 2D confocal microsopy images of single cells and nuclei.  Our findings indicate that SHAPR reconstructs 3D shapes of red blood cells from 2D images more accurately than naive stereological models and significantly increases the feature-based classification of red blood cell types.  Applying  it to 2D images of spheroidal aggregates of densely grown human induced pluripotent stem cells, we observe that SHAPR learns fundamental shape properties of cell nuclei and allows for prediction-based 3D morphometry.  SHAPR can help to optimize and up-scale image-based high-throughput applications by reducing imaging time and data storage.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/C_S_9.html">Image-to-image translation trained on unrelated histopathology data helps for Domain Generalization</a>
    </span>
    <span class="authors"> Marin Scalbert, Maria Vakalopoulou, Florent Couzinie-Devy</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Ps_PWSvJkOI">pdf</a></li><li><a href="https://openreview.net/forum?id=Ps_PWSvJkOI">reviews</a></li></ul><span class="abstract">
      Histopathology Whole Slide Images (WSIs) present large illumination or color variations due to protocol variability (scanner, staining). This can strongly harm the generalization performances of deep learning algorithms. To address this problem, we propose to train a multi-domain image-to-image translation (I2IT) model on WSIs from The Cancer Genome Atlas Program (TCGA) and use it for data augmentation. Using TCGA WSIs from different cancer types has several advantages: our data augmentation method can be used for tasks where data is small, the I2IT model does not need to be relearned for each task and the variability of TCGA protocols is high leading to better robustness. The method efficiency is assessed on the Camelyon17 WILDS dataset where we outperform sophisticated data augmentations and domain generalization methods. Results also confirms that training the I2IT model on unrelated histopathology data is much more efficient for generalization than training it on the training data of the domain generalization (DG) task.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_10.html">DDoS-UNet: Incorporating temporal information using Dynamic Dual-channel UNet for enhancing super-resolution of dynamic MRI</a>
    </span>
    <span class="authors"> Soumick Chatterjee, Chompunuch Sarasaen, Georg Rose, Andreas Nürnberger, Oliver Speck</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=S7S6gPtbKU4">pdf</a></li><li><a href="https://openreview.net/forum?id=S7S6gPtbKU4">reviews</a></li></ul><span class="abstract">
      Dynamic MRI is an essential tool for interventions to visualise movements or changes in the target organ. However, such MRI acquisition with high temporal resolution suffers from limited spatial resolution - also known as the spatio-temporal trade-off. Several approaches, including deep learning based super-resolution approaches, have been proposed to mitigate this trade-off. Nevertheless, such an approach typically aims to super-resolve each time-point separately, treating them as individual volumes. This research addresses the problem by creating a deep learning model that attempts to learn spatial and temporal relationships. The performance was tested with 3D dynamic data that was undersampled to different in-plane levels. The proposed network achieved an average SSIM value of 0.951±0.017 while reconstructing the lowest resolution data (i.e. only 4% of the k-space acquired), resulting in a theoretical acceleration factor of 25.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_11.html">Super-resolution microbubble localization in unprocessed ultrasound RF signals using a 1D dilated CNN</a>
    </span>
    <span class="authors"> Nathan Blanken, Jelmer M. Wolterink, Hervé Delingette, Christoph Brune, Michel Versluis, Guillaume Lajoinie</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=8XQ4kJsbSx">pdf</a></li><li><a href="https://openreview.net/forum?id=8XQ4kJsbSx">reviews</a></li></ul><span class="abstract">
      We present a super-resolution ultrasound approach based on direct deconvolution of single-channel ultrasound radio-frequency (RF) signals with a one-dimensional dilated convolutional neural network (CNN). Data are generated with a physics-based simulator that simulates the echoes from a dense cloud of monodisperse microbubbles and captures the full, nonlinear response of resonant, lipid-coated microbubbles. The network is trained with a novel dual-loss function, which features elements of both a classification loss and a regression loss and improves the detection-localization characteristics of the output. The potential of the presented approach to super-resolution ultrasound imaging is demonstrated with a delay-and-sum reconstruction with deconvolved ultrasound data. The resulting image shows an order-of-magnitude gain in axial resolution compared to a delay-and-sum reconstruction with unprocessed element data.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_12.html">Super-Resolution for Ultra High-Field MR Images</a>
    </span>
    <span class="authors"> Qi Wang, Julius Steiglechner, Tobias Lindig, Benjamin Bender, Klaus Scheffler, Gabriele Lohmann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=EFiFV2MSNEB">pdf</a></li><li><a href="https://openreview.net/forum?id=EFiFV2MSNEB">reviews</a></li></ul><span class="abstract">
      Segmenting ultra high-field MR images is an important first step in many applications. Segmentation methods based on machine learning have been shown to be valuable tools for this purpose. However, for ultra high-field MR images ($&gt;
$ 7 Tesla), a lack of training data is a problem. Therefore, in this work, we propose to use super-resolution for augmenting the training set. Specifically, we describe an efficient super-resolution model based on Generative Adversarial Network(GAN). It produces synthetic images that simulate MR data at ultra high isotropic resolutions of $0.6$ mm. We present the first results that show an improvement in segmentation accuracy of imaging data   acquired at a 9.4 Tesla MRI scanner.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_13.html">Super-resolution of portable low-field MRI in real scenarios: integration with denoising and domain adaptation</a>
    </span>
    <span class="authors"> Sonia Laguna, Riana Schleicher, Benjamin Billot, Pamela Schaefer, Brenna McKaig, Joshua N. Goldstein, Kevin N. Sheth, Matthew S. Rosen, W. Taylor Kimberly, Juan Eugenio Iglesias</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=pinw0Gcot4T">pdf</a></li><li><a href="https://openreview.net/forum?id=pinw0Gcot4T">reviews</a></li></ul><span class="abstract">
      Portable low-field MRI has the potential to revolutionize neuroimaging, by enabling point-of-care imaging and affordable scanning in underserved areas. The lower resolution and signal-to-noise ratio of these scans preclude image analysis with existing tools. Super-resolution (SR) methods can overcome this limitation, but: (i) training with downsampled high-field scans fails to generalize; and (ii) training with paired low/high-field data is hard due to the lack of perfectly aligned images. Here, we present an architecture that combines denoising, SR and domain adaptation modules to tackle this problem. The denoising and SR components are pretrained in a supervised fashion with large amounts of existing high-resolution data, whereas unsupervised learning is used for domain adaptation and end-to-end finetuning. We present preliminary results on a dataset of 11 low-field scans. The results show that our method enables segmentation with existing tools, which yield ROI volumes that correlate strongly with those derived from high-field scans (ρ &gt; 0.8).
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="rs poster">
    <span class="title">
      <a href="papers/C_S_14.html">Mesh-based 3D Reconstruction from Bi-planar Radiographs</a>
    </span>
    <span class="authors"> Moritz Jokeit, Ji Hyun Kim, Jess Gerrit Snedeker, Mazda Farshad, Jonas Widmer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=pR6qMzFbJQX">pdf</a></li><li><a href="https://openreview.net/forum?id=pR6qMzFbJQX">reviews</a></li></ul><span class="abstract">
      Reconstruction of 3D surfaces from sparse 2D data is a challenging problem that attracted increasing attention also in the medical field where image acquisition is expensive and the patients often bear high radiation doses (CT, fluoroscopy). Further, advances in computer-guided surgical assistant systems and preoperative planning necessitate fast 3D reconstruction from scarce image data. Recent learning-based approaches showed notable success in reconstructing primitive objects leveraging abundant artificial data sets. However, quality 3D data in the clinical context is often scarce. This motivates the exploitation of domain knowledge in form of anatomical shape priors to simplify the reconstruction problem. Further, mesh-sensitive applications (e.g., finite element analysis of implant design) greatly benefit from pre-defined mesh topologies. Thus, we propose a concept for the implementation and training of a learning-based patient-specific 3D reconstruction from bi-planar radiographs based on altering anatomical template meshes.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral2-2"></a><h3>Oral Session 2.2: Unsupervised and Representation Learning - 13:20 - 14:00 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/E1.html">Self-Supervised Representation Learning for High-Content Screening</a>
    </span>
    <span class="authors"> Daniel Siegismund, Mario Wieser, Stephan Heyse, Stephan Steigele</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=XIofcluPNu">pdf</a></li><li><a href="https://openreview.net/forum?id=XIofcluPNu">reviews</a></li></ul><span class="abstract">
      Biopharma drug discovery requires a set of approaches to find, produce, and test the safety of drugs for clinical application. A crucial part involves image-based screening of cell culture models where single cells are stained with appropriate markers to visually distinguish between disease and healthy states. In practice, such image-based screening experiments are frequently performed using highly scalable and automated multichannel microscopy instruments. This automation enables parallel screening against large panels of marketed drugs with known function. However, the large data volume produced by such instruments hinders a systematic inspection by human experts, which consequently leads to an extensive and biased data curation process for supervised phenotypic endpoint classification. To overcome this limitation, we propose a novel approach for learning an embedding of phenotypic endpoints, without any supervision. We employ the concept of archetypal analysis, in which pseudo-labels are extracted based on biologically reasonable endpoints. Subsequently, we use a self-supervised triplet network to learn a phenotypic embedding which is used for visual inspection and top-down assay quality control. Extensive experiments on two industry-relevant assays demonstrate that our method outperforms state-of-the-art unsupervised and supervised approaches. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/E2.html">Denoising Autoencoders for Unsupervised Anomaly Detection in Brain MRI</a>
    </span>
    <span class="authors"> Antanas Kascenas, Nicolas Pugeault, Alison Q O&apos;Neil</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Bm8-t_ggzPD">pdf</a></li><li><a href="https://openreview.net/forum?id=Bm8-t_ggzPD">reviews</a></li></ul><span class="abstract">
      Pathological brain lesions exhibit diverse appearance in brain images, making it difficult to design specialized detection solutions due to the lack of comprehensive data and annotations. Thus, in this work we tackle unsupervised anomaly detection, using only healthy data for training with the aim of detecting unseen anomalies at test time. Many current approaches employ autoencoders with restrictive architectures (i.e. containing information bottlenecks) that tend to give poor reconstructions of not only the anomalous but also the normal parts of the brain. Instead, we investigate classical denoising autoencoder models that do not require bottlenecks and can employ skip connections to give high resolution fidelity. We design a simple noise generation method of upscaling low-resolution noise that enables high-quality reconstructions, reducing false positive noise in reconstruction errors. We find that with appropriate noise generation, denoising autoencoder reconstruction errors generalize to hyperintense lesion segmentation and can reach state of the art performance for unsupervised tumor detection in brain MRI data, beating more complex methods such as variational autoencoders. We believe this provides a strong and easy-to-implement baseline for further research into unsupervised anomaly detection.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/E3.html">Interpretable Prediction of Lung Squamous Cell Carcinoma Recurrence With Self-supervised Learning</a>
    </span>
    <span class="authors"> Weicheng Zhu, Carlos Fernandez-Granda, Narges Razavian</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=QBg9YNm26FF">pdf</a></li><li><a href="https://openreview.net/forum?id=QBg9YNm26FF">reviews</a></li></ul><span class="abstract">
      Lung squamous cell carcinoma (LSCC) has a high recurrence and metastasis rate. Factors influencing recurrence and metastasis are currently unknown and there are no distinct histopathological or morphological features indicating the risks of recurrence and metastasis in LSCC. Our study focuses on the recurrence prediction of LSCC based on H&amp;E-stained histopathological whole-slide images (WSI). Due to the small size of LSCC cohorts in terms of patients with available recurrence information, standard end-to-end learning with various convolutional neural networks for this task tends to overfit. Also, the predictions made by these models are hard to interpret. Histopathology WSIs are typically very large and are therefore processed as a set of smaller tiles. In this work, we propose a novel conditional self-supervised learning (SSL) method to learn representations of WSI at the tile level first, and leverage clustering algorithms to identify the tiles with similar histopathological representations. The resulting representations and clusters from self-supervision are used as features of a survival model for recurrence prediction at the patient level. Using two publicly available datasets from TCGA and CPTAC, we show that our LSCC recurrence prediction survival model outperforms both LSCC pathological stage-based approach and machine learning baselines such as multiple instance learning. The proposed method also enables us to explain the recurrence histopathological risk factors via the derived clusters. This can help pathologists derive new hypotheses regarding morphological features associated with LSCC recurrence.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster2-2"></a><h3>Poster Session 2.2 - Onsite 11:00 - 12:00, Virtual 15:20 - 16:20 (UTC+2)</h3>
<a id="long2-2"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_1.html">Speckle and Shadows: Ultrasound-specific Physics-based Data Augmentation Applied to Kidney Segmentation</a>
    </span>
    <span class="authors"> Rohit Singla, Cailin Ringstrom, Ricky Hu, Victoria Lessoway, Janice Reid, Chris Nguan, Robert Rohling</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=E_KsfOoVf9D">pdf</a></li><li><a href="https://openreview.net/forum?id=E_KsfOoVf9D">reviews</a></li></ul><span class="abstract">
      Data augmentation techniques are frequently used to prevent overfitting, enhance generalizability, and overcome limited amounts of data. This data-oriented approach commonly includes domain-agnostic techniques of geometric transformations, colour space changes, and generative adversarial networks. However, leveraging domain-specific traits in aug- mentations may yield further improvements. We propose three new contributions to ultrasound augmentation: zoom, artificial shadowing, and speckle parameter maps. We first present zoom, a modification on scale which maintains the ultrasound beam shape. We then characterize acoustic shadows within abdominal ultrasound images, and formulate a method to introduce artificial shadows in a realistic manner into existing images. Finally, we transform B-mode ultrasound images into speckle parameter maps based on the Nakagami distribution to represent spatial structures not obvious in conventional B-mode. The three augmentations are evaluated in training a fully supervised network and a contrastive learning network for multi-class intra-organ semantic segmentation. Our preliminary results demonstrate the benefit of using zoom and speckle maps as augmentation, and the challenges presented by acoustic shadowing, in segmentation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_2.html">Bridging the Gap: Point Clouds for Merging Neurons in Connectomics</a>
    </span>
    <span class="authors"> Jules Berman, Dmitri Chklovskii, Jingpeng Wu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=lHDVYDy5S9l">pdf</a></li><li><a href="https://openreview.net/forum?id=lHDVYDy5S9l">reviews</a></li></ul><span class="abstract">
      In the field of Connectomics, a primary problem is that of 3D neuron segmentation. Although deep learning-based methods have achieved remarkable accuracy, errors still exist, especially in regions with image defects. One common type of defect is that of consecutive missing image sections. Here, data is lost along some axis, and the resulting neuron segmentations are split across the gap. To address this problem, we propose a novel method based on point cloud representations of neurons. We formulate the problem as a classification problem and train CurveNet, a state-of-the-art point cloud classification model, to identify which neurons should be merged. We show that our method not only performs strongly but also scales reasonably to gaps well beyond what other methods have attempted to address. Additionally, our point cloud representations are highly efficient in terms of data, maintaining high performance with an amount of data that would be unfeasible for other methods. We believe that this is an indicator of the viability of using point cloud representations for other proofreading tasks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_3.html">Omni-Seg: A Single Dynamic Network for Multi-label Renal Pathology Image Segmentation using Partially Labeled Data</a>
    </span>
    <span class="authors"> Ruining Deng, Quan Liu, Can Cui, Zuhayr Asad, Haichun Yang, Yuankai Huo</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=v-z4Zxkt9Ex">pdf</a></li><li><a href="https://openreview.net/forum?id=v-z4Zxkt9Ex">reviews</a></li></ul><span class="abstract">
      Computer-assisted quantitative analysis on Giga-pixel pathology images has provided a new avenue in precision medicine. The innovations have been largely focused on cancer pathology (i.e., tumor segmentation and characterization). In non-cancer pathology, the learning algorithms can be asked to examine more comprehensive tissue types simultaneously, as a multi-label setting. The prior arts typically needed to train multiple segmentation networks in order to match the domain-specific knowledge for heterogeneous tissue types (e.g., glomerular tuft, glomerular unit, proximal tubular, distal tubular, peritubular capillaries, and arteries). In this paper, we propose a dynamic single segmentation network (Omni-Seg) that learns to segment multiple tissue types using partially labeled images (i.e., only one tissue type is labeled for each training image) for renal pathology.  By learning from ~150,000 patch-wise pathological images from six tissue types, the proposed Omni-Seg network achieved superior segmentation accuracy and less resource consumption when compared to the previous the multiple-network and multi-head design. In the testing stage, the proposed method obtains &apos;completely labeled&apos; tissue segmentation results using only &apos;partially labeled&apos; training images. The source code is available at https://github.com/ddrrnn123/Omni-Seg.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_4.html">Label conditioned segmentation</a>
    </span>
    <span class="authors"> Tianyu Ma, Benjamin C. Lee, Mert R. Sabuncu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ML3EIKhFMaW">pdf</a></li><li><a href="https://openreview.net/forum?id=ML3EIKhFMaW">reviews</a></li></ul><span class="abstract">
      Semantic segmentation is an important task in computer vision that is often tackled with convolutional neural networks (CNNs). A CNN learns to produce pixel-level predictions through training on pairs of images and their corresponding ground-truth segmentation labels.  For segmentation tasks with multiple classes, the standard approach is to use a network that computes a multi-channel probabilistic segmentation map, with each channel representing one class.  In applications where the image grid size (e.g., when it is a 3D volume) and/or the number of labels is relatively large, the standard (baseline) approach can become prohibitively expensive for our computational resources. In this paper, we propose a simple yet effective method to address this challenge. In our approach, the segmentation network produces a single-channel output, while being conditioned on a single class label, which determines the output class of the network.  Our method, called label conditioned segmentation (LCS), can be used to segment images with a very large number of classes, which might be infeasible for the baseline approach.  We also demonstrate in the experiments that label conditioning can improve the accuracy of a given backbone architecture, likely, thanks to its parameter efficiency.  Finally, as we show in our results, an LCS model can produce previously unseen fine-grained labels during inference time, when only coarse labels were available during training. We provide all of our code here: https://github.com/tym002/Label-conditioned-segmentation
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_5.html">CAiD: Context-Aware Instance Discrimination for Self-supervised Learning in Medical Imaging</a>
    </span>
    <span class="authors"> Mohammad Reza Hosseinzadeh Taher, Fatemeh Haghighi, Michael Gotway, Jianming Liang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=PNAdmb_Ujf">pdf</a></li><li><a href="https://openreview.net/forum?id=PNAdmb_Ujf">reviews</a></li></ul><span class="abstract">
      Recently, self-supervised instance discrimination methods have achieved significant success in learning visual representations from unlabeled natural images. However, given the marked differences between natural and medical images, the efficacy of instance-based objectives, focusing on the most discriminative global feature in the image (i.e., cycle in bicycle), remains unknown in medical imaging. Our preliminary analysis showed that high global similarity of medical images in terms of anatomy hampers instance discrimination methods in capturing a set of distinct features, negatively impacting their performance on medical downstream tasks. To alleviate this limitation, we have developed a simple yet effective self-supervised framework, called Context-Aware instance Discrimination (CAiD). CAiD aims to improve instance discrimination learning by providing finer and more discriminative information encoded from diverse local context of unlabeled medical images. We conduct a systematic analysis to investigate the utility of the learned features from a three-pronged perspective: (i) generalizability and transferability, (ii) separability in the embedding space, and (iii) reusability. Our extensive experiments demonstrate that CAiD (1) enriches representations learned from existing instance discrimination methods; (2) delivers more discriminative features by adequately capturing finer contextual information from individual medial images; and (3) improves reusability of low/mid-level features compared to standard instance discriminative methods. As open science, all codes and pre-trained models are available on our GitHub page: https://github.com/JLiangLab/CAiD.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_L_6.html">SZLoc: A Multi-resolution Architecture for Automated Epileptic Seizure Localization from Scalp EEG</a>
    </span>
    <span class="authors"> Jeff Craley, Emily Johnson, Christophe C Jouny, David Hsu, Raheel Ahmed, Archana Venkataraman</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=yGgZ3iPrkJT">pdf</a></li><li><a href="https://openreview.net/forum?id=yGgZ3iPrkJT">reviews</a></li></ul><span class="abstract">
      We propose an end-to-end deep learning framework for epileptic seizure localization from scalp electroencephalography (EEG). Our architecture, SZLoc, extracts multi-resolution information via local (single channel) and global (cross-channel) CNN encodings. These interconnected representations are fused using a transformer layer. Leveraging its multi-resolution outputs, SZLoc derives three clinically interpretable outputs: electrode-level seizure activity, seizure onset zone localization, and identification of the EEG signal intervals that contribute to the final localization. From an optimization standpoint, we formulate a novel multi-task ensemble of loss functions to train SZLoc using inexact spatial and temporal labels of seizure onset. In this manner, SZLoc automatically learns phenomena at finer resolutions than the training labels. We validate our SZLoc framework and training paradigm on a clinical EEG dataset of 34 focal epilepsy patients. As compared to other deep learning baseline models, SZLoc achieves robust inter-patient seizure localization performance. We also demonstrate generalization of SZLoc to a second cohort of 16 epilepsy patients with different seizure characteristics and recorded at a different site. Taken together, SZLoc extends beyond the traditional paradigm of seizure detection by providing clinically relevant seizure localization information from coarse and inexact training labels.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_7.html">TorchXRayVision: A library of chest X-ray datasets and models</a>
    </span>
    <span class="authors"> Joseph Paul Cohen, Joseph D Viviano, Paul Bertin, Paul Morrison, Parsa Torabian, Matteo Guarrera, Matthew P. Lungren, Akshay Chaudhari, Rupert Brooks, Mohammad Hashir, Hadrien Bertrand</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=_5iri84DJmE">pdf</a></li><li><a href="https://openreview.net/forum?id=_5iri84DJmE">reviews</a></li></ul><span class="abstract">
      TorchXRayVision is an open source software library for working with chest X-ray datasets and deep learning models. It provides a common interface and common pre-processing chain for a wide set of publicly available chest X-ray datasets. In addition, a number of classification and representation learning models with different architectures, trained on different data combinations, are available through the library to serve as baselines or feature extractors.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_8.html">Interpretable Prediction of Lung Squamous Cell Carcinoma Recurrence With Self-supervised Learning</a>
    </span>
    <span class="authors"> Weicheng Zhu, Carlos Fernandez-Granda, Narges Razavian</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=QBg9YNm26FF">pdf</a></li><li><a href="https://openreview.net/forum?id=QBg9YNm26FF">reviews</a></li></ul><span class="abstract">
      Lung squamous cell carcinoma (LSCC) has a high recurrence and metastasis rate. Factors influencing recurrence and metastasis are currently unknown and there are no distinct histopathological or morphological features indicating the risks of recurrence and metastasis in LSCC. Our study focuses on the recurrence prediction of LSCC based on H&amp;E-stained histopathological whole-slide images (WSI). Due to the small size of LSCC cohorts in terms of patients with available recurrence information, standard end-to-end learning with various convolutional neural networks for this task tends to overfit. Also, the predictions made by these models are hard to interpret. Histopathology WSIs are typically very large and are therefore processed as a set of smaller tiles. In this work, we propose a novel conditional self-supervised learning (SSL) method to learn representations of WSI at the tile level first, and leverage clustering algorithms to identify the tiles with similar histopathological representations. The resulting representations and clusters from self-supervision are used as features of a survival model for recurrence prediction at the patient level. Using two publicly available datasets from TCGA and CPTAC, we show that our LSCC recurrence prediction survival model outperforms both LSCC pathological stage-based approach and machine learning baselines such as multiple instance learning. The proposed method also enables us to explain the recurrence histopathological risk factors via the derived clusters. This can help pathologists derive new hypotheses regarding morphological features associated with LSCC recurrence.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_9.html">Learning Strategies for Contrast-agnostic Segmentation via SynthSeg for Infant MRI data</a>
    </span>
    <span class="authors"> Ziyao Shang, Md Asadullah Turja, Eric Feczko, Audrey Houghton, Amanda Rueter, Lucille A Moore, Kathy Snider, Timothy Hendrickson, Paul Reiners, Sally Stoyell, Omid Kardan, Monica Rosenberg, Jed T Elison, Damien A Fair, Martin Andreas Styner</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=MOYTPAvLluZ">pdf</a></li><li><a href="https://openreview.net/forum?id=MOYTPAvLluZ">reviews</a></li></ul><span class="abstract">
      Longitudinal studies of infants&apos; brains are essential for research and clinical detection of Neurodevelopmental Disorders. However, for infant brain MRI scans, effective deep learning-based  segmentation frameworks exist only within small age intervals due the large image intensity and contrast changes that take place in the early postnatal stages of development. However, using different segmentation frameworks or models at different age intervals within the same longitudinal data set would cause segmentation inconsistencies and age-specific biases. Thus, an age-agnostic segmentation model for infants&apos; brains is needed. In this paper, we present &apos;Infant-SynthSeg&apos;, an extension of the contrast-agnostic SynthSeg segmentation framework applicable to MRI data of infant at ages within the first year of life. Our work mainly focuses on extending learning strategies related to synthetic data generation and augmentation, with the aim of creating a method that employs training data capturing features unique to infants&apos; brains during this early-stage development. Comparison across different learning strategy settings, as well as a more-traditional contrast-aware deep learning model (NN-Unet) are presented. Our experiments show that our trained Infant-SynthSeg models show consistently high segmentation performance on MRI scans of infant brains throughout the first year of life. Furthermore, as the model is trained on ground truth labels at different ages, even labels that are not present at certain ages (such as cerebellar white matter at 1 month) can be appropriately segmented via Infant-SynthSeg across the whole age range. Finally, while Infant-SynthSeg shows consistent segmentation performance across the first year of life, it is outperformed by age-specific deep learning models trained for a specific narrow age range.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_10.html">Detecting Out-of-Distribution via an Unsupervised Uncertainty Estimation for Prostate Cancer Diagnosis</a>
    </span>
    <span class="authors"> Jingya Liu, Bin Lou, Mamadou Diallo, Tongbai Meng, Heinrich von Busch, Robert Grimm, Yingli Tian, Dorin Comaniciu, Ali Kamen, David Winkel, henkjan huisman, Angela Tong, Tobias Penzkofer, Ivan Shabunin, Moon Hyung Choi, Pengyi Xing, Dieter Szolar, Steven Shea, Fergus Coakley, Mukesh Harisinghani</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=WDRcTpj5WfF">pdf</a></li><li><a href="https://openreview.net/forum?id=WDRcTpj5WfF">reviews</a></li></ul><span class="abstract">
      Artificial intelligence-based prostate cancer (PCa) detection models have been widely explored to assist clinical diagnosis. However, these trained models may generate erroneous results specifically on datasets that are not within training distribution. In this paper, we propose an approach to tackle this so-called out-of-distribution (OOD) data problem. Specifically, we devise an end-to-end unsupervised framework to estimate uncertainty values for cases analyzed by a previously trained PCa detection model. Our PCa detection model takes the inputs of bpMRI scans and through our proposed approach we identify OOD cases that are likely to generate degraded performance due to the data distribution shifts. The proposed OOD framework consists of two parts. First, an autoencoder-based reconstruction network is proposed, which learns discrete latent representations of in-distribution data. Second, the uncertainty is computed using perceptual loss that measures the distance between original and reconstructed images in the feature space of a pre-trained PCa detection network. The effectiveness of the proposed framework is evaluated on seven independent data collections with a total of 1,432 cases. The performance of pre-trained PCa detection model is significantly improved by excluding cases with high uncertainty.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_11.html">Memory-efficient Segmentation of Volumetric High-resolution MicroCT Images</a>
    </span>
    <span class="authors"> Yuan Wang, Laura Blackie, Irene Miguel-Aliaga, Wenjia Bai</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ecOY_ywB3UB">pdf</a></li><li><a href="https://openreview.net/forum?id=ecOY_ywB3UB">reviews</a></li></ul><span class="abstract">
       In recent years, 3D convolutional neural networks have become the dominant approach for volumetric medical image segmentation. However, compared to their 2D counterparts, 3D networks introduce substantially more training parameters and higher requirement for the GPU memory. This has become a major limiting factor for designing and training 3D networks for high-resolution volumetric images. In this work, we propose a novel memory-efficient network architecture for 3D high-resolution image segmentation. The network incorporates both global and local features via a two-stage U-net-based cascaded framework and at the first stage, a memory-efficient U-net (meU-net) is developed. The features learnt at the two stages are connected via post-concatenation, which further improves the information flow. The proposed segmentation method is evaluated on an ultra high-resolution microCT dataset with typically 250 million voxels per volume. Experiments show that it outperforms state-of-the-art 3D segmentation methods in terms of both segmentation accuracy and memory efficiency.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_12.html">Learning Morphological Feature Perturbations for Calibrated Semi-Supervised Segmentation</a>
    </span>
    <span class="authors"> Moucheng Xu, Yukun Zhou, Chen Jin, Stefano B Blumberg, Frederick Wilson, Neil Oxtoby, Marius De Groot, Daniel C. Alexander, Joseph Jacob</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=OL6tAasXCmi">pdf</a></li><li><a href="https://openreview.net/forum?id=OL6tAasXCmi">reviews</a></li></ul><span class="abstract">
      In this paper, we propose MisMatch, a novel consistency-driven semi-supervised segmentation framework which produces predictions that are invariant to learnt feature perturbations. MisMatch consists of an encoder and a two decoders. One decoder learns positive attention to the foreground regions of interest (RoI) on unlabelled images thereby generating dilated features of the foreground. The other decoder learns negative attention to the foreground on the same unlabelled images thereby generating eroded features of the foreground. We then apply a consistency regularisation on the paired predictions. MisMatch outperforms state-of-the-art semi-supervised methods on a CT-based pulmonary vessel segmentation task and a MRI-based brain tumour segmentation task. We also show that the effectiveness of MisMatch comes from better model calibration than its supervised learning counterpart. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_13.html">Diffusion Models for Implicit Image Segmentation Ensembles</a>
    </span>
    <span class="authors"> Julia Wolleb, Robin Sandkuehler, Florentin Bieder, Philippe Valmaggia, Philippe C. Cattin</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=QNLR05X6uW">pdf</a></li><li><a href="https://openreview.net/forum?id=QNLR05X6uW">reviews</a></li></ul><span class="abstract">
      Diffusion models have shown impressive performance for generative modelling of images. In this paper, we present a novel semantic segmentation method based on diffusion models. By modifying the training and sampling scheme, we show that diffusion models can perform lesion segmentation of medical images. To generate an image specific segmentation, we train the model on the ground truth segmentation, and use the image as a prior during training and in every step during the sampling process. With the given stochastic sampling process, we can generate a distribution of segmentation masks. This property allows us to compute pixel-wise uncertainty maps of the segmentation, and allows an implicit ensemble of segmentations that increases the segmentation performance. We evaluate our method on the BRATS2020 dataset for brain tumor segmentation. Compared to state-of-the-art segmentation models, our approach yields good segmentation results and, additionally, detailed uncertainty maps.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_14.html">Comparing representations of biological data learned with different AI paradigms, augmenting and cropping strategies</a>
    </span>
    <span class="authors"> Andrei Dmitrenko, Mauro Miguel Masiero, Nicola Zamboni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=RPR7hjLYTyU">pdf</a></li><li><a href="https://openreview.net/forum?id=RPR7hjLYTyU">reviews</a></li></ul><span class="abstract">
      Recent advances in computer vision and robotics enabled automated large-scale biological image analysis. Various machine learning approaches have been successfully applied to phenotypic profiling. However, it remains unclear how they compare in terms of biological feature extraction. In this study, we propose a simple CNN architecture and implement weakly-supervised, self-supervised, unsupervised and regularized learning of image representations. We train 16 deep learning setups on the 770k cancer cell images dataset under identical conditions, using different augmenting and cropping strategies. We compare the learned representations by evaluating multiple metrics for each of three downstream tasks: i) distance-based similarity analysis of known drugs, ii) classification of drugs versus controls, iii) clustering within cell lines. We also compare training times and memory usage. Among all tested setups, multi-crops and random augmentations generally improved performance across tasks, as expected. Strikingly, self-supervised models showed competitive performance being up to 11 times faster to train. Regularized learning required the most of memory and computation to deliver arguably the most informative features. We observe that no single combination of augmenting and cropping strategies consistently resulted in top performance across tasks and recommend prospective research directions.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_15.html">Denoising Autoencoders for Unsupervised Anomaly Detection in Brain MRI</a>
    </span>
    <span class="authors"> Antanas Kascenas, Nicolas Pugeault, Alison Q O&apos;Neil</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Bm8-t_ggzPD">pdf</a></li><li><a href="https://openreview.net/forum?id=Bm8-t_ggzPD">reviews</a></li></ul><span class="abstract">
      Pathological brain lesions exhibit diverse appearance in brain images, making it difficult to design specialized detection solutions due to the lack of comprehensive data and annotations. Thus, in this work we tackle unsupervised anomaly detection, using only healthy data for training with the aim of detecting unseen anomalies at test time. Many current approaches employ autoencoders with restrictive architectures (i.e. containing information bottlenecks) that tend to give poor reconstructions of not only the anomalous but also the normal parts of the brain. Instead, we investigate classical denoising autoencoder models that do not require bottlenecks and can employ skip connections to give high resolution fidelity. We design a simple noise generation method of upscaling low-resolution noise that enables high-quality reconstructions, reducing false positive noise in reconstruction errors. We find that with appropriate noise generation, denoising autoencoder reconstruction errors generalize to hyperintense lesion segmentation and can reach state of the art performance for unsupervised tumor detection in brain MRI data, beating more complex methods such as variational autoencoders. We believe this provides a strong and easy-to-implement baseline for further research into unsupervised anomaly detection.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_16.html">SPA: Shape-Prior Variational Autoencoders for Unsupervised Brain Pathology Segmentation</a>
    </span>
    <span class="authors"> Cosmin I. Bercea, Benedikt Wiestler, Daniel Rueckert, Shadi Albarqouni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=mB_V8ThxY8Z">pdf</a></li><li><a href="https://openreview.net/forum?id=mB_V8ThxY8Z">reviews</a></li></ul><span class="abstract">
      Deep unsupervised representation learning for brain pathology segmentation is of great interest for medical imaging, as it does not require extensive annotations for training and allows the detection of unseen pathologies. While recent approaches proposed to model the distribution of healthy brain Magnetic Resonance Imaging (MRI) using variational autoencoders, we propose to model the pixel distribution of the healthy brain by introducing a shape-prior based on the brain tissue distribution.  To this end, we propose Shape-Prior variational Autoencoders (SPA) to disentangle the generative factors of brain MRI, namely cerebrospinal fluid (CSF), gray matter (GM), and white matter (WM). Our method obtains interpretable latent representations, providing pixel-wise tissue probability maps. We evaluated the proposed method on MRIs of 538 patients from six data-sets containing demyelinating lesions, small vessel disease, and tumors. Experimental results indicate that our method is capable of disentangling the generative brain MR factors and avoiding the reconstruction of anomalous regions, leading to better lesion detection performance.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_17.html">i3Deep: Efficient 3D interactive segmentation with the nnU-Net</a>
    </span>
    <span class="authors"> Karol Gotkowski, Camila Gonzalez, Isabel Jasmin Kaltenborn, Ricarda Fischbach, Andreas Bucher, Anirban Mukhopadhyay</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=R420Pr5vUj3">pdf</a></li><li><a href="https://openreview.net/forum?id=R420Pr5vUj3">reviews</a></li></ul><span class="abstract">
      3D interactive segmentation is highly relevant in reducing the annotation time for experts. However, current methods often achieve only small segmentation improvements per interaction as lightweight models are a requirement to ensure near-realtime usage. Models with better predictive performance such as the nnU-Net cannot be employed for interactive segmentation due to their high computational demands, which result in long inference times. To solve this issue, we propose the 3D interactive segmentation framework i3Deep. Slices are selected through uncertainty estimation in an offline setting and afterwards corrected by an expert. The slices are then fed to a refinement nnU-Net, which significantly improves the global 3D segmentation from the local corrections. This approach bypasses the issue of long inference times by moving expensive computations into an offline setting that does not include the expert. For three different anatomies, our approach reduces the workload of the expert by 80.3%, while significantly improving the Dice by up to 39.5%, outperforming other state-of-the-art methods by a clear margin. Even on out-of-distribution data i3Deep is able to improve the segmentation by 19.3%.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_18.html">An Analysis of the Impact of Annotation Errors on the Accuracy of Deep Learning for Cell Segmentation</a>
    </span>
    <span class="authors"> Șerban Vădineanu, Daniel Pelt, Oleh Dzyubachyk, Joost Batenburg</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=C4B46ZS7MSB">pdf</a></li><li><a href="https://openreview.net/forum?id=C4B46ZS7MSB">reviews</a></li></ul><span class="abstract">
      Recent studies have shown that there can be high inter- and intra-observer variability when creating annotations for biomedical image segmentation. To mitigate the effects of manual annotation variability when training machine learning algorithms, various methods have been developed. However, little work has been done on actually assessing the impact of annotation errors on machine learning-based segmentation. For the task of cell segmentation, our work aims to bridge this gap by providing a thorough analysis of three types of potential annotation errors. We tackle the limitation of previous studies that lack a golden standard ground truth by performing our analysis on two synthetically-generated data sets with perfect labels, while also validating our observations on manually-labeled data. Moreover, we discuss the influence of the annotation errors on the results of three different network architectures: UNet, SegNet, and MSD. We find that UNet shows the overall best robustness for all data sets on two categories of errors, especially when the severity of the error is low, while MSD generalizes well even when a large proportion of the cell labels is missing during training. Moreover, we observe that special care should be taken to avoid wrongly labeling large objects when the target cells have small footprints.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_L_19.html">Deep Learning for Model Correction in Cardiac Electrophysiological Imaging</a>
    </span>
    <span class="authors"> Victoriya Kashtanova, Ibrahim Ayed, Andony Arrieula, Mark Potse, patrick gallinari, Maxime Sermesant</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7MW9oh7MDKp">pdf</a></li><li><a href="https://openreview.net/forum?id=7MW9oh7MDKp">reviews</a></li></ul><span class="abstract">
      Imaging the electrical activity of the heart can be achieved with invasive catheterisation however the resulting data is sparse and noisy. Mathematical modelling of cardiac electrophysiology can help the analysis but solving the associated mathematical systems can become unfeasible. It is often computationally demanding, for instance when solving for different patient conditions. We present a new framework to model the dynamics of cardiac electrophysiology at lower cost. It is based on the integration of a low-fidelity physical model and a learning component implemented here via neural networks. The latter acts as a complement to the physical part, and handles all quantities and dynamics that the simplified physical model neglects. We demonstrate that this framework allows us to reproduce the dynamics of the complex transmembrane potential and to correctly identify the relevant physical parameters, even when only partial measurements are available. This combined model-based and data-driven approach could improve cardiac electrophysiological imaging and provide predictive tools.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_20.html">Robust Multi-Organ Nucleus Segmentation Using a Locally Rotation Invariant Bispectral U-Net</a>
    </span>
    <span class="authors"> Valentin Oreiller, Julien Fageot, Vincent Andrearczyk, John O. Prior, Adrien Depeursinge</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=paGzvj2t_x">pdf</a></li><li><a href="https://openreview.net/forum?id=paGzvj2t_x">reviews</a></li></ul><span class="abstract">
      Locally Rotation Invariant (LRI) operators have shown great potential to analyze biomedical textures where discriminative patterns appear at random positions and orientations.  We build LRI operators through the local projection of the image on circular harmonics followed by the computation of the bispectrum, which is LRI by design. This formulation allows to avoid the discretization of the orientations and does not require any criterion to locally align the descriptors. This operator is used in a convolutional layer resulting in LRI Convolutional Neural Networks (LRI CNN). To evaluate the relevance of this approach, we use it to segment cellular nuclei in histopathological images. We compare the proposed bispectral LRI layer against a standard convolutional layer in a U-Net architecture. While they perform equally in terms of F-score, the LRI CNN provides more robust segmentation with respect to orientation, even when rotational data augmentation is used. This robustness is essential when the relevant pattern may vary in orientation, which is often the case in medical images.  Keywords: Locally Rotation Invariant, Convolutional Neural Network, Deep Learning, Segmentation, Bispectrum.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_L_21.html">Video-based Computer-aided Laparoscopic Bleeding Management: a Space-time Memory Neural Network with Positional Encoding and Adversarial Domain Adaptation</a>
    </span>
    <span class="authors"> Navid Rabbani, Callyane Seve, Nicolas Bourdel, Adrien Bartoli</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kmV0i37vuCy">pdf</a></li><li><a href="https://openreview.net/forum?id=kmV0i37vuCy">reviews</a></li></ul><span class="abstract">
      One of the main challenges in laparoscopic procedures is handling intraoperative bleeding. We propose video-based Computer-aided Laparoscopic Bleeding Management (CALBM) for early detection and management of intraoperative bleeding. Our system performs the online video-based segmentation of bleeding sources and displays them to the surgeon. It hinges on an improved space-time memory network, which we train from real and semi-synthetic data, using adversarial domain adaptation. Our system improves the IoU and F-Score from 69.97% to 73.40% and 50.23% to 58.09% in comparison to the baseline space-time memory network. It is far better than the prior CALBM systems based on still images, which we reimplemented with DeepLabV3+, reaching an  IoU and F-Score of 65.86% and 43.19%. The improvement is also supported by user evaluation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_L_22.html">MRI bias field correction with an implicitly trained CNN.</a>
    </span>
    <span class="authors"> Attila Tibor Simko, Tommy Löfstedt, Anders Garpebring, Tufve Nyholm, Joakim Jonsson</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=LbHd47ij5s">pdf</a></li><li><a href="https://openreview.net/forum?id=LbHd47ij5s">reviews</a></li></ul><span class="abstract">
      In magnetic resonance imaging (MRI), bias fields are difficult to correct since they are inherently unknown. They cause intra-volume intensity inhomogeneities which limit the performance of subsequent automatic medical imaging tasks, e.g. tissue-based segmentation. Since the ground truth is unavailable, training a supervised machine learning solution requires approximating the bias fields, which limits the resulting method.  We introduce implicit training which sidesteps the inherent lack of data and allows the training of machine learning solutions without ground truth. We describe how training a model implicitly for bias field correction allows using non-medical data for training, achieving a highly generalized model. The implicit approach was compared to a more traditional training on medical data. Both models were compared to an optimized N4ITK method, with evaluations on six datasets.  The implicitly trained model improved the homogeneity of all encountered medical data, and it generalized better for a range of anatomies, than the model trained traditionally. The model achieves a significant speed-up over an optimized N4ITK method---by a factor of 100, and it also requires no parameters to tune.  For tasks such as bias field correction---where ground truth is generally not available, but the characteristics of the corruption are known---implicit training promises to be a fruitful alternative for highly generalized solutions.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short2-2"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_1.html">Anatomically Constrained Semi-supervised Learning for Echocardiography Segmentation</a>
    </span>
    <span class="authors"> Thierry Judge, Arnaud Judge, Pierre-marc Jodoin</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gG1xKNXo6Y">pdf</a></li><li><a href="https://openreview.net/forum?id=gG1xKNXo6Y">reviews</a></li></ul><span class="abstract">
      Deep convolutional neural networks (CNNs) have had great success for medical imaging segmentation. Many methods attained nearly perfect Dice scores, sometimes within inter-expert variability. However, CNNs require large amounts of labeled data and are not immune to producing anatomically implausible results, especially when applied to ultrasound images.  In this paper, we propose a method that tackles both of these problems simultaneously.  Our method optimizes anatomical segmentation metrics on both labeled and unlabeled data using a training scheme analogous to adversarial training.  Our method allows the optimization of several hand-made non-differentiable metrics for any segmentation model and drastically reduces the number of anatomical errors.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_2.html">Attention-based Dynamic Subspace Learners</a>
    </span>
    <span class="authors"> Sukesh Adiga Vasudeva, Jose Dolz, Herve Lombaert</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=IHRUUHMeXcJ">pdf</a></li><li><a href="https://openreview.net/forum?id=IHRUUHMeXcJ">reviews</a></li></ul><span class="abstract">
      Deep metric learning methods are widely used to learn similarities in the data. Most methods use a single metric learner, which is inadequate to handle the variety of object attributes such as color, shape, or artifacts in the images. Multiple metric learners could focus on these object attributes. However, it requires a number of learners to be found empirically for each new dataset. This work presents a Dynamic Subspace Learners to dynamically exploit multiple learners by removing the need of knowing apriori the number of learners and aggregating new subspace learners during training. Furthermore, the interpretability of such subspace learning is enforced by integrating an attention module into our method, providing a visual explanation of the embedding features. Our method achieves competitive results with the performances of multiple learners baselines and significantly improves over the classification network in clustering and retrieval tasks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_3.html">Building representations of different brain areas through hierarchical point cloud networks</a>
    </span>
    <span class="authors"> Joy M Jackson, Ran Liu, Eva L Dyer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=3GeifJ_GCg0">pdf</a></li><li><a href="https://openreview.net/forum?id=3GeifJ_GCg0">reviews</a></li></ul><span class="abstract">
      Understanding how the microstructure varies across different brain regions is critical for disease modeling and brain registration. However, current deep learning approaches that work on image data directly may unintentionally focus on textures or other sources of noise in the data and fail to capture meaningful information about the underlying microstructures of interest. In this work, we propose a deep learning method that aims to build salient representations of microstructures inside neuroimage data by working on point cloud representations. We developed a hierarchical PointNet to process extracted 3D point clouds of brain anatomy to solve a brain region classification task. We validate our method on a micron-scale neuroimaging dataset, where we generated point clouds from both pixel-level segmentations and simple edge detection methods. In both cases, we show that point cloud-based models achieve better stability and performance when compared to 3D convolutional networks trained on the same brain region classification task. Our results in using &apos;noisier&apos; data from simple filtering operations provides initial evidence that point cloud representations could be a lightweight and data-efficient approach for brain parcellation. Keywords: Neuroanatomy, Point Cloud, Deep Learning, PointNet, Brain Parcellation
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_S_4.html">Improving the Self-Supervised Pretext Task for Histopathologic Subtype Classification</a>
    </span>
    <span class="authors"> Ruiwen Ding, Anil Yadav, Erika Rodriguez, Ana Cristina Araujo Lemos da Silva, William Hsu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7QWzEwByMXq">pdf</a></li><li><a href="https://openreview.net/forum?id=7QWzEwByMXq">reviews</a></li></ul><span class="abstract">
      In computational pathology, fully-supervised convolutional neural networks have been shown to perform well on tasks such as histology segmentation and classification but require large amounts of expert-annotated labels. In this work, we propose a self-supervised learning pretext task that utilizes the multi-resolution nature of whole slide images to reduce labeling effort. Given a pair of image tiles cropped at different magnification levels, our model predicts whether one tile is contained in the other. We hypothesize that this task induces the model to learn to distinguish different structures presented in the images, thus benefiting the downstream classification. The potential of our method was shown in downstream classification of lung adenocarcinoma histologic subtypes using H&amp;E-images from the National Lung Screening Trial.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_5.html">Metrics Reloaded - A new recommendation framework for biomedical image analysis validation</a>
    </span>
    <span class="authors"> Annika Reinke</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=24kBqy8rcB_">pdf</a></li><li><a href="https://openreview.net/forum?id=24kBqy8rcB_">reviews</a></li></ul><span class="abstract">
      Meaningful performance assessment of biomedical image analysis algorithms depends on objective and appropriate performance metrics. There are major shortcomings in the current state of the art. Yet, so far limited attention has been paid to practical pitfalls associated when using particular metrics for image analysis tasks. Therefore, a number of international initiatives have collaborated to offer researchers with guidance and tools for selecting performance metrics in a problem-aware manner. In our proposed framework, the characteristics of the given biomedical problem are first captured in a problem fingerprint, which identifies properties related to domain interests, the target structure(s), the input datasets, and algorithm output. A problem category-specific mapping is applied in the second step to match fingerprints to metrics that reflect domain requirements. Based on input from experts from more than 60 institutions worldwide, we believe our metric recommendation framework to be useful to the MIDL community and to enhance the quality of biomedical image analysis algorithm validation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_6.html">Adaptive Gradient Triplet Loss with Automatic Margin Learning for Forensic Medical Image Matching</a>
    </span>
    <span class="authors"> Khanh Nguyen, Hoang Huy Nguyen, Aleksei Tiulpin</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=LgO9mFejtNN">pdf</a></li><li><a href="https://openreview.net/forum?id=LgO9mFejtNN">reviews</a></li></ul><span class="abstract">
      This paper tackles the challenge of forensic medical image matching (FMIM) using deep neural networks (DNNs). We investigate Triplet loss (TL), which is probably the most well-known loss for this problem. TL aims to enforce closeness between similar and enlarge the distance between dissimilar data points in the image representation space extracted by a DNN. Although TL has been shown to perform well, it still has limitations, which we identify and analyze in this work. Specifically, we first introduce AdaTriplet -- an extension of TL that aims to adapt loss gradients according to the levels of difficulty of negative samples. Second, we also introduce AutoMargin -- a technique to adjust hyperparameters of margin-based losses such as TL and AdaTriplet dynamically during training. The performance of our loss is evaluated on a new large-scale benchmark for FMIM, which we have constructed from the Osteoarthritis Initiative cohort. The codes allowing replication of our results have been made publicly available at url{https:github.comOulu-IMEDSAdaTriplet}.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_7.html">Fully Automated Thrombus Segmentation on CT Images of Patients with Acute Ischemic Stroke</a>
    </span>
    <span class="authors"> Mahsa Mojtahedi, Manon Kappelhof, Elena Ponomareva, Henk van Voorst, Efstratios Gavves, Bart J. Emmer, Charles B. Majoie, Henk Marquering</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=zEB9D8vhNf">pdf</a></li><li><a href="https://openreview.net/forum?id=zEB9D8vhNf">reviews</a></li></ul><span class="abstract">
      Thrombus imaging characteristics are associated with treatment success and functional outcomes in stroke patients. However, assessing these characteristics based on manual annotations is labor intensive and subject to observer bias. Therefore, we aimed to create an automated pipeline for consistent and fast full thrombus segmentation. We first found the occlusion location using StrokeViewer LVO and created a bounding box around it. We trained dual modality U-Net based convolutional neural networks (CNNs) to subsequently segment the thrombus inside this bounding box. Segmentation results have high spatial accuracy with manual delineations and can therefore be used to determine thrombus characteristics and potentially benefit decision making in clinical practice.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_S_8.html">Toward complete colorectal tumor resection using intraoperative ultrasound and ensemble learning</a>
    </span>
    <span class="authors"> Freija Geldof, Stijn Pruijssers, Lynn-Jade S. Jong, Dinusha Veluponnar, Theo Ruers, Behdad Dashtbozorg</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Lz_HgXzGAWk">pdf</a></li><li><a href="https://openreview.net/forum?id=Lz_HgXzGAWk">reviews</a></li></ul><span class="abstract">
      Cancer surgery is characterized by a delicate balance between radical tumor resection and sparing healthy tissue and critical anatomical structures. The trouble of recognizing tissue structures during surgery may either lead to resection too close to the tumor resulting in tumor-positive resection margins or too wide resection around the tumor with potential damage to vital anatomical structures. Ultrasound is a widely available and non-invasive imaging technique which can be used for surgical guidance by continuous real-time tissue recognition during surgery, however, interpretation of US images requires training and experience. One of the notorious challenges in medical image analysis is the scarcity of labeled data. To address this issue, we introduce a deep ensemble learning framework for colorectal tumor detection in ultrasound images using models which are pre-trained for tumor segmentation in breast ultrasound images. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_9.html">A multi-channel deep learning approach for lung cavity estimation using hyperpolarized gas and proton MRI</a>
    </span>
    <span class="authors"> Joshua Russell Astley, Alberto M Biancardi, Helen Marshall, Paul JC Hughes, Guilhem J Collier, Laurie J Smith, James Eaden, Jim M Wild, Bilal Tahir</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=-10ClNgdEO">pdf</a></li><li><a href="https://openreview.net/forum?id=-10ClNgdEO">reviews</a></li></ul><span class="abstract">
      Hyperpolarized (HP) gas MRI enables quantification of regional lung ventilation via clinical biomarkers such as the ventilation defect percentage (VDP). VDP is computed from segmentations derived from spatially co-registered functional HP gas MRI and structural proton ($^1$H)-MRI; although these scans are acquired at similar inflation levels, misalignments are frequent, requiring a lung cavity estimation (LCE). Here, we propose a multi-channel deep learning method for generating LCEs using HP gas and $^1$H-MRI. We compare the performance of the proposed method to single-channel alternatives.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_S_10.html">End-to-end learning for detecting MYC translocations</a>
    </span>
    <span class="authors"> Stephan Dooper, Geert Litjens</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gGry8j6l2zB">pdf</a></li><li><a href="https://openreview.net/forum?id=gGry8j6l2zB">reviews</a></li></ul><span class="abstract">
      Recent developments have improved whole-slide image classification to the point where the entire slide can be analyzed using only weak labels, whilst retaining both local and global context. In this paper, we use an end-to-end whole-slide image classification approach using weak labels to classify MYC translocations in slides of diffuse large B-cell lymphoma. Our model is able to achieve an AUC of 0.8012, which indicates the possibility of learning relevant features for MYC translocations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_11.html">Automated Oral Epithelial Dysplasia Grading Using Neural Networks and Feature Analysis</a>
    </span>
    <span class="authors"> Neda Azarmehr, Adam Shephard, Hanya Mahmood, Nasir Rajpoot, Syed Ali Khurram</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ABl-dIO4g74">pdf</a></li><li><a href="https://openreview.net/forum?id=ABl-dIO4g74">reviews</a></li></ul><span class="abstract">
      Oral epithelial dysplasia (OED) is a precancerous lesion, histologically graded as mild, moderate or severe. The manual histological diagnosis of OED is time-consuming and subjective. We explore a customised Neural Architecture Search (NAS) technique to optimise an efficient architecture for full epithelium and individual nuclei segmentation in pathology whole slide images (WSIs). Results show the NAS-derived model outperforms all state-of-the-art networks. Accurate nuclear segmentation allows us to extract morphometric features. We propose a random forest model, using these features, to differentiate between OED grades.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_12.html">Capturing Inter-Slice Dependencies of 3D Brain MRI-Scans for Unsupervised Anomaly Detection</a>
    </span>
    <span class="authors"> Finn Behrendt, Marcel Bengs, Debayan Bhattacharya, Julia Krüger, Roland Opfer, Alexander Schlaefer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=db8wDgKH4p4">pdf</a></li><li><a href="https://openreview.net/forum?id=db8wDgKH4p4">reviews</a></li></ul><span class="abstract">
      The increasing workloads for radiologists in clinical practice lead to the need for an automatic support tool for anomaly detection in brain MRI-scans. While supervised learning methods can detect and localize lesions in brain MRI-scans, the need for large, balanced data sets with pixel-level annotations limits their use. In contrast, unsupervised anomaly detection (UAD) models only require healthy brain data for training.  Despite the inherent 3D structure of brain MRI-scans, most UAD studies focus on slice-wise processing. In this work, we capture the inter-slice dependencies of the human brain using recurrent neural networks (RNN) and transformer-based self-attention mechanisms together with variational autoencoders (VAE). We show that by this we can improve both reconstruction quality and UAD performance while the number of parameters remain similar to the 2D approach where the slices are processed individually.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_13.html">Self- and Cross-attention based Transformer for left ventricle segmentation in 4D flow MRI</a>
    </span>
    <span class="authors"> Xiaowu Sun, Li-Hsin Cheng, Rob J. van der Geest</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gDocX1Js4zN">pdf</a></li><li><a href="https://openreview.net/forum?id=gDocX1Js4zN">reviews</a></li></ul><span class="abstract">
      The conventional quantitative analysis of 4D flow MRI relies on the co-registered cine MRI. In this work, we proposed a self- and cross-attention based Transformer to segment the left ventricle directly from the 4D flow MRI and evaluated our method on a large dataset using various metrics. The results demonstrate that self- and cross-attention improve the segmentation performance, achieving a mean Dice of 82.41$\%$, ASD of 4.51 mm, left ventricle ejection fraction (LVEF) error of 7.96$\%$ and kinetic energy (KE) error of 1.34 $\mu$J$/$ml.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_14.html">A Semi-Supervised Deep Learning Approach for Multi-Stain Foreground Segmentation in Digital Pathology</a>
    </span>
    <span class="authors"> Agathe de Vulpian, Valentina di Proietto, Gauthier Roy, Saima Ben Hadj, Rutger RH Fick</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6uw53DAsjNG">pdf</a></li><li><a href="https://openreview.net/forum?id=6uw53DAsjNG">reviews</a></li></ul><span class="abstract">
      The analysis of whole computational pathology slides can often be accelerated by excluding background areas from the analysis. Deep learning has proven to be superior to signal processing techniques to robustly recover the foreground in HE Images. However, naively generalizing this technique to the wide variability of histological stains used in practice would require annotations in all stain domains. To avoid this, we propose a method which leverages tissue annotation from a single stain to perform foreground segmentation in slides with other non-annotated stains.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/D_S_15.html">Multi-task learning to improve performance consistency in mammogram classification</a>
    </span>
    <span class="authors"> Mickael Tardy, Diana Mateus</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=q7yGMPLDkx4">pdf</a></li><li><a href="https://openreview.net/forum?id=q7yGMPLDkx4">reviews</a></li></ul><span class="abstract">
      Breast cancer is the most prevalent cancer amongst women. Its regular screening, often based on mammograms, significantly reduces the mortality. Deep learning has shown good performances in coping with screening-generated imaging data, however there are still open questions related to the imbalance, noisiness, and heterogeneity of the data. We propose to address these challenges with Multi-Task Learning, combining tasks such as classification, regression, segmentation, and reconstruction. Our approach allows to obtain consistent performances of AUC $pprox 0.80$ across different vendors (including those unknown during training) on the primary breast cancer classification task, while fulfilling well secondary tasks including an $F_1$ score of $0.96$ on 4-class vendor classification, and $F_1$ score of 0.64 on 4-class density classification.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_16.html">Maximizing Segmentation Quality of Under-sampled Motion Corrupted Cardiac Cine-MRI Using an End-to-End Deep Learning Model</a>
    </span>
    <span class="authors"> Ahmed Adly, Ruud Van Sloun, Kerstin Hammernik, Jose Caballero, Daniel Rueckert, Nicola Pezzotti</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=oZvqfAczKji">pdf</a></li><li><a href="https://openreview.net/forum?id=oZvqfAczKji">reviews</a></li></ul><span class="abstract">
      Assessing cardiac health by measuring the cardiac function, for example using volume and ejection fractions, in cine magnetic resonance imaging is an essential step to assess the severity of cardiovascular diseases. However, motion artifacts caused by the difficulties the patients may have in either breath-holding or remaining still during acquisition, make the estimation of the segmentations required to compute the metrics above difficult, which in turn will undermine the quality of the estimated metrics. In this paper, we propose an end-to-end deep learning model that is optimized for two different tasks: reconstruction and segmentation. This is achieved by implementing a joint model that can achieve high segmentation accuracy while leveraging a fast acquisition by acting on under-sampled k-space data, under the assumption that some random motion occurs during cine cardiac MRI acquisition. Moreover, our joint model is able to reconstruct high quality images coupled with motion correction.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_17.html">Self-supervised learning of mammograms with pathology aware</a>
    </span>
    <span class="authors"> Yuan Gao, XIN WANG, Tianyu Zhang, Luyi Han, Regina Beets-Tan, Ritse Mann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=zTn0kYfsgkJ">pdf</a></li><li><a href="https://openreview.net/forum?id=zTn0kYfsgkJ">reviews</a></li></ul><span class="abstract">
      Screening mammography is recognized as an effective method to diagnose breast cancer (BC). However, for extremely dense breasts, there is a higher chance to induce misdiagnosing. To suppress misdiagnosis from radiologists in mammography reading, computer-aided diagnosis (CAD) based on imaging has been widely researched and applied. These CAD tools increasingly have deeper layers design aiming for better performance, but this may decrease robustness particularly in dense breast. Therefore, to benefit BC identification in the context of supervision from rare annotated datasets, we propose a self-supervised learning framework to normalize mammograms into pathology aware (PA) style, which is in line with the pathological local enhancement characteristic, and prove the value of PA mammogram for the downstream tasks. Experimental results on INBreast and CBIS-DDSM datasets suggest that our method can achieve better performance in both normal and dense breasts for classification and segmentation tasks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/D_S_18.html">Multi-Modality Microscopy Image Style Augmentation for Nuclei Segmentation</a>
    </span>
    <span class="authors"> Sophia J Wagner, Ye Liu, Tingying Peng</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gmXYdr0e5OR">pdf</a></li><li><a href="https://openreview.net/forum?id=gmXYdr0e5OR">reviews</a></li></ul><span class="abstract">
      Annotating microscopy images for nuclei segmentation is laborious and time-consuming. To leverage the few existing annotations, also across multiple modalities, we propose a microscopy-style augmentation technique based on a generative adversarial network (GAN). Unlike other style transfer methods, it can not only deal with different cell assay types and lighting conditions but also with different imaging modalities, such as bright-field and fluorescence microscopy. Using disentangled representations for content and style, we can preserve the structure of the original image while altering its style during augmentation. We evaluate our data augmentation on the 2018 Data Science Bowl dataset, consisting of various cell assays, lighting conditions, and imaging modalities. With our style augmentation, the segmentation accuracy of the two top-ranked Mask R-CNN-based nuclei segmentation algorithms in the competition increases significantly. Thus, our augmentation technique renders the downstream task more robust to the test data heterogeneity and helps counteract class imbalance without resampling of minority classes.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_19.html">A Fully Automated Multi-Scale Pipeline for Oral Epithelial Dysplasia Grading and Outcome Prediction</a>
    </span>
    <span class="authors"> Adam Shephard, Neda Azarmehr, Raja Muhammad Saad Bashir, SHAN E AHMED RAZA, Hanya Mahmood, Syed Ali Khurram, Nasir Rajpoot</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=G4h5aDsi5zl">pdf</a></li><li><a href="https://openreview.net/forum?id=G4h5aDsi5zl">reviews</a></li></ul><span class="abstract">
      Oral epithelial dysplasia (OED) is a premalignant histopathological diagnosis given to lesions of the oral cavity, characterised by changes to the nuclear morphometry and the epithelial layers. In this work, we have finetuned HoVer-Net+ for the simultaneous segmentation of nuclei and the epithelial layers in heamatoxylin and eosin (H&amp;E) stained whole slide images (WSIs). We then employed a multi-scale attention-based multiple instance learning architecture for the prediction of OED status, grade, recurrence and malignant transformation. The impressive results have demonstrated the potential of such methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_20.html">Influence of Loss Function on Left Ventricular Volume and Ejection Fraction Estimation in Deep Neural Networks</a>
    </span>
    <span class="authors"> Preshen Naidoo, Eman I Alajrami, Elisabeth Sarah Lane, Jevgeni Jevsikov, Matthew J Shun-shin, Darrel P Francis, Massoud Zolgharni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=46uz5RvpI7h">pdf</a></li><li><a href="https://openreview.net/forum?id=46uz5RvpI7h">reviews</a></li></ul><span class="abstract">
      Quantification of the left ventricle shape is crucial in evaluating cardiac function from 2D echocardiographic images. This study investigates the applicability of established loss functions when optimising the U-Net model for 2D echocardiographic left ventricular segmentation. Our results indicate loss functions are a significant component for optimal left ventricle volume measurements when established segmentation metrics could be imperceptible.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="seg poster">
    <span class="title">
      <a href="papers/D_S_21.html">Search for temporal cell segmentation robustness in phase-contrast microscopy videos</a>
    </span>
    <span class="authors"> Estibaliz Gómez-de-Mariscal, Hasini Jayatilaka, Özgün Cicek, Thomas Brox, Denis Wirtz, Arrate Munoz-Barrutia</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=QzZE_PJi49u">pdf</a></li><li><a href="https://openreview.net/forum?id=QzZE_PJi49u">reviews</a></li></ul><span class="abstract">
      This work presents a deep learning-based workflow to segment cancer cells embedded in $3$D collagen matrices and imaged with phase-contrast microscopy under low magnification and strong background noise conditions. Due to the experimental and imaging setup, cell and protrusion appearance change largely from frame to frame. We use transfer learning and recurrent convolutional long-short term memory units to exploit the temporal information and provide temporally stable results. Our results show that the proposed approach is robust to weight initialization and training data sampling. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral2-3"></a><h3>Oral Session 2.3: Segmentation II - 16:20 - 17:20 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/F1.html">Memory-efficient Segmentation for Volumetric High-resolution MicroCT Images</a>
    </span>
    <span class="authors"> Yuan Wang, Laura Blackie, Irene Miguel-Aliaga, Wenjia Bai</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ecOY_ywB3UB">pdf</a></li><li><a href="https://openreview.net/forum?id=ecOY_ywB3UB">reviews</a></li></ul><span class="abstract">
      In recent years, 3D convolutional neural networks have become the dominant approach for volumetric medical image segmentation. However, compared to their 2D counterparts, 3D networks introduce substantially more training parameters and higher requirement for the GPU memory. This has become a major limiting factor for designing and training 3D networks for high-resolution volumetric images. In this work, we propose a novel memory-efficient network architecture for 3D high-resolution image segmentation. The network incorporates both global and local features via a two-stage U-net-based cascaded framework and at the first stage, a memory-efficient U-net (meU-net) is developed. The features learnt at the two stages are connected via post-concatenation, which further improves the information flow. The proposed segmentation method is evaluated on an ultra high-resolution microCT dataset with typically 250 million voxels per volume. Experiments show that it outperforms state-of-the-art 3D segmentation methods in terms of both segmentation accuracy and memory efficiency.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/F2.html">Learning Morphological Feature Perturbations for Calibrated Semi-Supervised Segmentation</a>
    </span>
    <span class="authors"> Moucheng Xu, Yukun Zhou, Chen Jin, Stefano B Blumberg, Frederick Wilson, Marius De Groot, Daniel C. Alexander, Neil Oxtoby, Joseph Jacob</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=OL6tAasXCmi">pdf</a></li><li><a href="https://openreview.net/forum?id=OL6tAasXCmi">reviews</a></li></ul><span class="abstract">
      In this paper, we propose MisMatch, a novel consistency-driven semi-supervised segmentation framework which produces predictions that are invariant to learnt feature perturbations. MisMatch consists of an encoder and a two decoders. One decoder learns positive attention to the foreground regions of interest (RoI) on unlabelled images thereby generating dilated features of the foreground. The other decoder learns negative attention to the foreground on the same unlabelled images thereby generating eroded features of the foreground. We then apply a consistency regularisation on the paired predictions. MisMatch outperforms state-of-the-art semi-supervised methods on a CT-based pulmonary vessel segmentation task and a MRI-based brain tumour segmentation task. We also show that the effectiveness of MisMatch comes from better model calibration than its supervised learning counterpart.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/F3.html">Label conditioned segmentation</a>
    </span>
    <span class="authors"> Tianyu Ma, Benjamin C. Lee, Mert R. Sabuncu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ML3EIKhFMaW">pdf</a></li><li><a href="https://openreview.net/forum?id=ML3EIKhFMaW">reviews</a></li></ul><span class="abstract">
      Semantic segmentation is an important task in computer vision that is often tackled with convolutional neural networks (CNNs). A CNN learns to produce pixel-level predictions through training on pairs of images and their corresponding ground-truth segmentation labels. For segmentation tasks with multiple classes, the standard approach is to use a network that computes a multi-channel probabilistic segmentation map, with each channel representing one class. In applications where the image grid size (e.g., when it is a 3D volume) and/or the number of labels is relatively large, the standard (baseline) approach can become prohibitively expensive for our computational resources. In this paper, we propose a simple yet effective method to address this challenge. In our approach, the segmentation network produces a single-channel output, while being conditioned on a single class label, which determines the output class of the network. Our method, called label conditioned segmentation (LCS), can be used to segment images with a very large number of classes, which might be infeasible for the baseline approach. We also demonstrate in the experiments that label conditioning can improve the accuracy of a given backbone architecture, likely, thanks to its parameter efficiency. Finally, as we show in our results, an LCS model can produce previously unseen fine-grained labels during inference time, when only coarse labels were available during training. We provide all of our code here: https://github.com/tym002/Label-conditioned-segmentation
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/F4.html">Video-based Computer-aided Laparoscopic Bleeding Management: a Space-time Memory Neural Network with Positional Encoding and Adversarial Domain Adaptation</a>
    </span>
    <span class="authors">Navid Rabbani, Callyane Seve, Nicolas Bourdel, Adrien Bartoli</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kmV0i37vuCy">pdf</a></li><li><a href="https://openreview.net/forum?id=kmV0i37vuCy">reviews</a></li></ul><span class="abstract">
      One of the main challenges in laparoscopic procedures is handling intraoperative bleeding. We propose video-based Computer-aided Laparoscopic Bleeding Management (CALBM) for early detection and management of intraoperative bleeding. Our system performs the online video-based segmentation of bleeding sources and displays them to the surgeon. It hinges on an improved space-time memory network, which we train from real and semi-synthetic data, using adversarial domain adaptation. Our system improves the IoU and F-Score from 69.97% to 73.40% and 50.23% to 58.09% in comparison to the baseline space-time memory network. It is far better than the prior CALBM systems based on still images, which we reimplemented with DeepLabV3+, reaching an IoU and F-Score of 65.86% and 43.19%. The improvement is also supported by user evaluation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<h2>Friday 8th July</h2>
<p><a id="oral3-1"></a><h3>Oral Session 3.1: Trustworthy AI - 09:40 - 10:40 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/G1.html">Transformer-based out-of-distribution detection for clinically safe segmentation</a>
    </span>
    <span class="authors"> Mark S Graham, Petru-Daniel Tudosiu, Paul Wright, Walter Hugo Lopez Pinaya, Jean-Marie U-King-Im, Yee Mah, James Teo, Rolf H. Jäger, David Werring, Parashkev Nachev, Sebastien Ourselin, M. Jorge Cardoso</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=En7660i-CLJ">pdf</a></li><li><a href="https://openreview.net/forum?id=En7660i-CLJ">reviews</a></li></ul><span class="abstract">
      In a clinical setting it is essential that deployed image processing systems are robust to the full range of inputs they might encounter and, in particular, do not make confidently wrong predictions. The most popular approach to safe processing is to train networks that can provide a measure of their uncertainty, but these tend to fail for inputs that are far outside the training data distribution. Recently, generative modelling approaches have been proposed as an alternative; these can quantify the likelihood of a data sample explicitly, filtering out any out-of-distribution (OOD) samples before further processing is performed. In this work, we focus on image segmentation and evaluate several approaches to network uncertainty in the far-OOD and near-OOD cases for the task of segmenting haemorrhages in head CTs. We find all of these approaches are unsuitable for safe segmentation as they provide confidently wrong predictions when operating OOD. We propose performing full 3D OOD detection using a VQ-GAN to provide a compressed latent representation of the image and a transformer to estimate the data likelihood. Our approach successfully identifies images in both the far- and near-OOD cases. We find a strong relationship between image likelihood and the quality of a model&apos;s segmentation, making this approach viable for filtering images unsuitable for segmentation.  To our knowledge, this is the first time transformers have been applied to perform OOD detection on 3D image data.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/G2.html">VORTEX: Physics-Driven Data Augmentations Using Consistency Training for Robust Accelerated MRI Reconstruction</a>
    </span>
    <span class="authors"> Arjun D Desai, Beliz Gunel, Batu Ozturkler, Harris Beg, Shreyas Vasanawala, Brian Hargreaves, Christopher Re, John M. Pauly, Akshay Chaudhari</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=WjwUeGh0yMK">pdf</a></li><li><a href="https://openreview.net/forum?id=WjwUeGh0yMK">reviews</a></li></ul><span class="abstract">
      Deep neural networks have enabled improved image quality and fast inference times for various inverse problems, including accelerated magnetic resonance imaging (MRI) reconstruction. However, such models require extensive fully-sampled ground truth datasets, which are difficult to curate and are sensitive to distribution drifts. In this work, we propose applying physics-driven data augmentations for consistency training that leverage our domain knowledge of the forward MRI data acquisition process and MRI physics to achieve improved data efficiency and robustness to clinically-relevant distribution drifts. Our approach, termed VORTEX, (1) demonstrates strong improvements over supervised baselines with and without data augmentation in robustness to signal-to-noise ratio change and motion corruption in data-limited regimes; (2) considerably outperforms state-of-the-art purely image-based data augmentation techniques and self-supervised reconstruction methods on both in-distribution and out-of-distribution data; and (3) enables composing heterogeneous image-based and physics-driven data augmentations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/G3.html">Segmentation-Consistent Probabilistic Lesion Counting</a>
    </span>
    <span class="authors"> Julien Schroeter, Chelsea Myers-Colet, Douglas Arnold, Tal Arbel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=kwcxym1kMtf">pdf</a></li><li><a href="https://openreview.net/forum?id=kwcxym1kMtf">reviews</a></li></ul><span class="abstract">
      Lesion counts are important indicators of disease severity, patient prognosis, and treatment efficacy, yet counting as a task in medical imaging is often overlooked in favor of segmentation. This work introduces a novel continuously differentiable function that maps lesion segmentation predictions to lesion count probability distributions in a consistent manner. The proposed end-to-end approach—which consists of voxel clustering, lesion-level voxel probability aggregation, and Poisson-binomial counting—is non-parametric and thus offers a robust and consistent way to augment lesion segmentation models with post hoc counting capabilities. Experiments on Gadolinium-enhancing lesion counting demonstrate that our method outputs accurate and well-calibrated count distributions that capture meaningful uncertainty information. They also reveal that our model is suitable for multi-task learning of lesion segmentation, is efficient in low data regimes, and is robust to adversarial attacks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/G4.html">An Analysis of the Impact of Annotation Errors on the Accuracy of Deep Learning for Cell Segmentation</a>
    </span>
    <span class="authors"> Șerban Vădineanu, Daniel Pelt, Oleh Dzyubachyk, Joost Batenburg</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=C4B46ZS7MSB">pdf</a></li><li><a href="https://openreview.net/forum?id=C4B46ZS7MSB">reviews</a></li></ul><span class="abstract">
      Recent studies have shown that there can be high inter- and intra-observer variability when creating annotations for biomedical image segmentation. To mitigate the effects of manual annotation variability when training machine learning algorithms, various methods have been developed. However, little work has been done on actually assessing the impact of annotation errors on machine learning-based segmentation. For the task of cell segmentation, our work aims to bridge this gap by providing a thorough analysis of three types of potential annotation errors. We tackle the limitation of previous studies that lack a golden standard ground truth by performing our analysis on two synthetically-generated data sets with perfect labels, while also validating our observations on manually-labeled data. Moreover, we discuss the influence of the annotation errors on the results of three different network architectures: UNet, SegNet, and MSD. We find that UNet shows the overall best robustness for all data sets on two categories of errors, especially when the severity of the error is low, while MSD generalizes well even when a large proportion of the cell labels is missing during training. Moreover, we observe that special care should be taken to avoid wrongly labeling large objects when the target cells have small footprints.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster3-1"></a><h3>Poster Session 3.1:  Onsite 15:20 - 16:20 , Virtual 11:00 - 12:00 (UTC+2)</h3>
<a id="long3-1"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_L_1.html">Semi-Supervised Medical Image Segmentation via Cross Teaching between CNN and Transformer</a>
    </span>
    <span class="authors"> Xiangde Luo, Minhao Hu, Tao Song, Guotai Wang, Shaoting Zhang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=KUmlnqHrAbE">pdf</a></li><li><a href="https://openreview.net/forum?id=KUmlnqHrAbE">reviews</a></li></ul><span class="abstract">
      Recently, deep learning with Convolutional Neural Networks (CNNs) and Transformers has shown encouraging results in fully supervised medical image segmentation. However, it is still challenging for them to achieve good performance with limited annotations for training. In this work, we present a very simple yet efficient framework for semi-supervised medical image segmentation by introducing the cross teaching between CNN and Transformer. Specifically, we simplify the classical deep co-training from consistency regularization to cross teaching, where the prediction of a network is used as the pseudo label to supervise the other network directly end-to-end. Considering the difference in learning paradigm between CNN and Transformer, we introduce the Cross Teaching between CNN and Transformer rather than just using CNNs. Experiments on a public benchmark show that our method outperforms eight existing semi-supervised learning methods just with a simpler framework. Notably, this work may be the first attempt to combine CNN and transformer for semi-supervised medical image segmentation and achieve promising results on a public benchmark. The code will be released at: https://github.com/HiLab-git/SSL4MIS.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_2.html">Towards IID representation learning and its application on biomedical data</a>
    </span>
    <span class="authors"> Jiqing Wu, Inti Zlobec, Maxime W Lafarge, Yukun He, Viktor Koelzer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=qKZH_U-tn9P">pdf</a></li><li><a href="https://openreview.net/forum?id=qKZH_U-tn9P">reviews</a></li></ul><span class="abstract">
      Due to the heterogeneity of real-world data, the widely accepted independent and identically distributed (IID) assumption has been criticized in recent studies on causality. In this paper, we argue that instead of being a questionable assumption,  IID is a fundamental task-relevant property that needs to be learned. We elaborate on how a variety of different causal questions can be reformulated to learning a task-relevant function that induces IID, which we term IID representation learning.  For proof of concept, we examine the IID representation learning on Out-of-Distribution (OOD) generalization tasks. Concretely, by utilizing the representation obtained via the learned function that induces IID, we conduct prediction of molecular characteristics (molecular prediction) on two biomedical datasets with real-world distribution shifts introduced by a) preanalytical variation and b) sampling protocol. To enable reproducibility and for comparison to the state-of-the-art (SOTA) methods, this is done by following the OOD benchmarking guidelines recommended from WILDS. Compared to the SOTA baselines supported in WILDS, the results confirm the superior performance of IID representation learning on OOD tasks. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_3.html">Unsupervised Pre-training Improves Tooth Segmentation in 3-Dimensional Intraoral Mesh Scans</a>
    </span>
    <span class="authors"> Xiaoxuan He, Hualiang Wang, Haoji Hu, Jianfei Yang, Yang Feng, Gaoang Wang, Zuozhu Liu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=5JEnrPnpbI7">pdf</a></li><li><a href="https://openreview.net/forum?id=5JEnrPnpbI7">reviews</a></li></ul><span class="abstract">
      Accurate tooth segmentation in 3-Dimensional (3D) intraoral scanned (IOS) mesh data is an essential step for many practical dental applications.  Recent research highlights the success of deep learning based methods for end-to-end 3D tooth segmentation, yet most of them are only trained or validated with a small dataset as annotating 3D IOS dental surfaces requires complex pipelines and intensive human efforts. In this paper, we propose a novel method to boost the performance of 3D tooth segmentation leveraging large-scale unlabeled IOS data. Our tooth segmentation network is first pre-trained with an unsupervised learning framework and point-wise contrastive learning loss on the large-scale unlabeled dataset and subsequently fine-tuned on a small labeled dataset. With the same amount of annotated samples, our method can achieve a mIoU of 89.38\%, significantly outperforming the supervised counterpart. Moreover, our method can achieve better performance with only 40\% of the annotated samples as compared to the fully supervised baselines. To the best of our knowledge, we present the first attempt of unsupervised pre-training for 3D tooth segmentation, demonstrating its strong potential in reducing human efforts for annotation and verification. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/E_L_4.html">Diffeomorphic Image Registration using Lipschitz Continuous Residual Networks.</a>
    </span>
    <span class="authors"> Ankita Joshi, Yi Hong</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=AREzZY5zASj">pdf</a></li><li><a href="https://openreview.net/forum?id=AREzZY5zASj">reviews</a></li></ul><span class="abstract">
      Image registration is an essential task in medical image analysis.We propose two novel unsupervised diffeomorphic image registration networks, which use deep Residual Networks(ResNets) as numerical approximations of the underlying continuous diffeomorphic setting governed by ordinary differential equations (ODEs), viewed as an Eulerian discretization scheme. While considering the ODE-based parameterizations of diffeomorphisms, we consider both stationary and non-stationary (time varying) velocity fields as the driving velocities to solve the ODEs, which gives rise to our two proposed architectures for diffeomorphic registration. We also employ Lipschitz-continuity on the Residual Networks in both architectures to define the admissible Hilbert space of velocity fields as a Reproducing Kernel Hilbert Spaces (RKHS) and regularize the smoothness of the velocity fields. We apply both registration networks to align and segment the OASIS brain MRI dataset.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_5.html">Self-Supervised Representation Learning for High-Content Screening</a>
    </span>
    <span class="authors"> Daniel Siegismund, Mario Wieser, Stephan Heyse, Stephan Steigele</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=XIofcluPNu">pdf</a></li><li><a href="https://openreview.net/forum?id=XIofcluPNu">reviews</a></li></ul><span class="abstract">
      Biopharma drug discovery requires a set of approaches to find, produce, and test the safety of drugs for clinical application. A crucial part involves image-based screening of cell culture models where single cells are stained with appropriate markers to visually distinguish between disease and healthy states. In practice, such image-based screening experiments are frequently performed using highly scalable and automated multichannel microscopy instruments. This automation enables parallel screening against large panels of marketed drugs with known function. However, the large data volume produced by such instruments hinders a systematic inspection by human experts, which consequently leads to an extensive and biased data curation process for supervised phenotypic endpoint classification. To overcome this limitation, we propose a novel approach for learning an embedding of phenotypic endpoints, without any supervision. We employ the concept of archetypal analysis, in which pseudo-labels are extracted based on biologically reasonable endpoints. Subsequently, we use a self-supervised triplet network to learn a phenotypic embedding which is used for visual inspection and top-down assay quality control. Extensive experiments on two industry-relevant assays demonstrate that our method outperforms state-of-the-art unsupervised and supervised approaches. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_6.html">Self-Supervised Transformers for fMRI representation</a>
    </span>
    <span class="authors"> Itzik Malkiel, Gony Rosenman, Lior Wolf, Talma Hendler</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=0ZNbiLvTPem">pdf</a></li><li><a href="https://openreview.net/forum?id=0ZNbiLvTPem">reviews</a></li></ul><span class="abstract">
      We present TFF, which is a Transformer framework for the analysis of functional Magnetic Resonance Imaging (fMRI) data. TFF employs a two-phase training approach. First, self-supervised training is applied to a collection of fMRI scans, where the model is trained to reconstruct 3D volume data. Second, the pre-trained model is fine-tuned on specific tasks, utilizing ground truth labels. Our results show state-of-the-art performance on a variety of fMRI tasks, including age and gender prediction, as well as schizophrenia recognition. Our code for the training, network architecture, and results is attached as supplementary material.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_7.html">Position Regression for Unsupervised Anomaly Detection</a>
    </span>
    <span class="authors"> Florentin Bieder, Julia Wolleb, Robin Sandkuehler, Philippe C. Cattin</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=myJkK4u93g">pdf</a></li><li><a href="https://openreview.net/forum?id=myJkK4u93g">reviews</a></li></ul><span class="abstract">
      In recent years, anomaly detection has become an essential field in medical image analysis.  Most current anomaly detection methods for medical images are based on image reconstruction.  In this work, we propose a novel anomaly detection approach based on coordinate regression.  Our method estimates the position of patches within a volume, and is trained only on data of healthy subjects.  During inference, we can detect and localize anomalies by considering the error of the position estimate of a given patch.  We apply our method to 3D CT volumes and evaluate it on patients with intracranial haemorrhages and cranial fractures. The results show that our method performs well in detecting these anomalies.  Furthermore, we show that our method requires less memory than comparable approaches that involve image reconstruction.  This is highly relevant for processing large 3D volumes, for instance, CT or MRI scans. The code will be publicly available.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_8.html">On the Pitfalls of Using the Residual as Anomaly Score</a>
    </span>
    <span class="authors"> Felix Meissen, Benedikt Wiestler, Georgios Kaissis, Daniel Rueckert</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ZsoHLeupa1D">pdf</a></li><li><a href="https://openreview.net/forum?id=ZsoHLeupa1D">reviews</a></li></ul><span class="abstract">
      Many current state-of-the-art methods for anomaly detection in medical images rely on calculating a residual image between a potentially anomalous input image and its (&apos;healthy&apos;) reconstruction. As the reconstruction of the unseen anomalous region should be erroneous, this yields large residuals as a score to detect anomalies in medical images. However, this assumption does not take into account residuals resulting from imperfect reconstructions of the machine learning models used. Such errors can easily overshadow residuals of interest and therefore strongly question the use of residual images as scoring function. Our work explores this fundamental problem of residual images in detail. We theoretically define the problem and thoroughly evaluate the influence of intensity and texture of anomalies against the effect of imperfect reconstructions in a series of experiments.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_L_9.html">Orientation Estimation of Abdominal Ultrasound Images with Multi-Hypotheses Networks</a>
    </span>
    <span class="authors"> Timo Horstmann, Oliver Zettinig, Wolfgang Wein, Raphael Prevost</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=1gsauv2B7Ar">pdf</a></li><li><a href="https://openreview.net/forum?id=1gsauv2B7Ar">reviews</a></li></ul><span class="abstract">
      Ultrasound imaging can provide valuable information to clinicians during interventions, in particular when fused with other modalities. Multi-modal image registration algorithms however require a somewhat accurate initialization, which is particularly difficult to estimate for ultrasound images as their orientation is arbitrary and their content ambiguous (limited field of view, artifacts, etc.). In this work, we train neural networks to predict the absolute orientation of ultrasound frames, but also to produce a confidence for each prediction. This allows us to select only the most confident frames in the clip. Our networks are trained to produce multiple hypotheses using a simple yet overlooked meta-loss that is specifically designed to capture the ambiguity of the input data.  We show on several abdominal ultrasound datasets that multi-hypotheses networks provide better uncertainty estimates than Monte-Carlo dropout while being more efficient than network ensembling. Generic, easy to implement and able to quantify both data ambiguity and out-of-distribution samples, they represent a preferable alternative to traditional baselines for uncertainty estimation. Our method produces on a clinical test estimates within $20^{\circ}$ of the true orientation, which we can use to improve the accuracy of a subsequent registration algorithm down to less than $10^{\circ}$.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_10.html">Cell Anomaly Localisation using Structured Uncertainty Prediction Networks</a>
    </span>
    <span class="authors"> Boyko Vodenicharski, Samuel McDermott, K M Webber, Viola Introini, Richard Bowman, Pietro Cicuta, Ivor J A Simpson, Neill D. F. Campbell</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=-RLCTAvUxuf">pdf</a></li><li><a href="https://openreview.net/forum?id=-RLCTAvUxuf">reviews</a></li></ul><span class="abstract">
      This paper proposes an unsupervised approach to anomaly detection in bright-field or fluorescence cell microscopy, where our goal is to localise malaria parasites. This is achieved by building a generative model (a variational autoencoder) that describes healthy cell images, where we additionally model the structure of the predicted image uncertainty, rather than assuming pixelwise independence in the likelihood function. This provides a &apos;whitened&apos; residual representation, where the anticipated structured mistakes by the generative model are reduced, but distinctive structures that did not occur in the training distribution, e.g. parasites are highlighted. We employ the recently published Structured Uncertainty Prediction Networks approach to enable tractable learning of the uncertainty structure. Here, the residual covariance matrix is efficiently approximated using a sparse Cholesky parameterisation. We demonstrate that our proposed approach is more effective for detecting real and synthetic structured image perturbations compared to diagonal Gaussian likelihoods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_L_11.html">Weakly-supervised learning for image-based classification of primary melanomas into genomic immune subgroups</a>
    </span>
    <span class="authors"> Lucy Godson, Navid Alemi, Jeremie Nsengimana, Graham Cook, Emily L Clarke, Darren Treanor, D Timothy Bishop, Julia A Newton-Bishop, Ali Gooya</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=_ZUu2wpDDVv">pdf</a></li><li><a href="https://openreview.net/forum?id=_ZUu2wpDDVv">reviews</a></li></ul><span class="abstract">
      Determining early-stage prognostic markers and stratifying patients for effective treatment are two key challenges for improving outcomes for melanoma patients. Previous studies have used tumour transcriptome data to stratify patients into immune subgroups, which were associated with differential melanoma specific survival and potential treatment strategies. However, acquiring transcriptome data is a time-consuming and costly process. Moreover, it is not routinely used in the current clinical workflow. Here we attempt to overcome this by developing deep learning models to classify gigapixel H&amp;E stained pathology slides, which are well established in clinical workflows, into these immune subgroups. Previous subtyping approaches have employed supervised learning which requires fully annotated data, or have only examined single genetic mutations in melanoma patients. We leverage a multiple-instance learning approach, which only requires slide-level labels and uses an attention mechanism to highlight regions of high importance to the classification. Moreover, we show that pathology-specific self-supervised models generate better representations compared to pathology-agnostic models for improving our model performance, achieving a mean AUC of 0.76 for classifying histopathology images as high or low immune subgroups. We anticipate that this method may allow us to find new biomarkers of high importance and could act as a tool for clinicians to infer the immune landscape of tumours and stratify patients, without needing to carry out additional expensive genetic tests.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short3-1"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_S_1.html">SIHeDA-Net: Sensor to Image Heterogeneous Domain Adaptation Network</a>
    </span>
    <span class="authors"> Ishikaa Lunawat, Vignesh S, S P Sharan</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=zVzeKdlCMWX">pdf</a></li><li><a href="https://openreview.net/forum?id=zVzeKdlCMWX">reviews</a></li></ul><span class="abstract">
      The main advantage of wearable devices lies in enabling them to be tracked without external infrastructure. However, unlike vision (cameras), there is a dearth of large-scale training data to develop robust ML models for wearable devices. SIHeDA-Net (Sensor-Image Heterogeneous Domain Adaptation) uses training data from public images of American Sign Language (ASL) that can be used for inferences on sensors even with errors by bridging the domain gaps through latent space transfer.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/E_S_2.html">Continuous benchmarking in medical image registration - review of the current state of the Learn2Reg challenge</a>
    </span>
    <span class="authors"> Lasse Hansen, Alessa Hering, Christoph Großbröhmer, Mattias P Heinrich</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6JdGvJhKZgp">pdf</a></li><li><a href="https://openreview.net/forum?id=6JdGvJhKZgp">reviews</a></li></ul><span class="abstract">
      Image registration is a fundamental medical image analysis task, and a wide variety of approaches have been proposed. However, only a few studies have comprehensively compared medical image registration approaches on a wide range of clinically relevant tasks, in part because of the lack of availability of such diverse data. This limits the development of registration methods, the adoption of research advances into practice, and a fair benchmark across competing approaches. The Learn2Reg challenge addresses these limitations by providing a multi-task medical image registration benchmark for comprehensive characterisation of deformable registration algorithms. We established an easily accessible framework for training and validation of 3D registration methods, which so far enabled the compilation of results of over 65 individual method submissions from more than 20 unique teams. We used a complementary set of metrics, including robustness, accuracy, plausibility, and runtime, enabling unique insight into the current state-of-the-art of medical image registration. In this abstract for the MIDL community we want to 1) give a shortest (graphical) overview of the Learn2Reg Challenge, 2) present key results and outcomes of past editions and 3) outline limitations and resulting ongoing work.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_S_3.html">A Generative Model Reveals the Influence of Patient Attributes on Fundus Images</a>
    </span>
    <span class="authors"> Sarah Müller, Lisa M. Koch, Hendrik Lensch, Philipp Berens</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=u9idZRTwmWR">pdf</a></li><li><a href="https://openreview.net/forum?id=u9idZRTwmWR">reviews</a></li></ul><span class="abstract">
      Screening for ophthalmic diseases routinely relies on retinal fundus images. These images are highly heterogeneous and little is known about how patient attributes such as age and ethnicity contribute to the variability in appearance. As the image variation due to such factors may ultimately confound automated image interpretation using deep learning models, understanding the influence of patient attributes on retinal fundus images is key for reliable AI applications in ophthalmology. Here, we draw on recent advances in generative modeling and present a population model of retinal fundus images which is capable of generating highly realistic images and allows for an analysis of how the patient attributes age and ethnicity are organized in the latent space of the generative model.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_S_4.html">Weak labels for deep-learning-based detection of brain aneurysms from MR angiography scans</a>
    </span>
    <span class="authors"> Tommaso Di Noto, Guillaume Marie, Sebastien Tourbier, Yasser Alemán-Gómez, Oscar Esteban, Guillaume Saliou, Meritxell Bach Cuadra, Patric Hagmann, Jonas Richiardi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=27w4JsiZnn8">pdf</a></li><li><a href="https://openreview.net/forum?id=27w4JsiZnn8">reviews</a></li></ul><span class="abstract">
      Unruptured Intracranial Aneurysms (UIAs) are focal dilatations in cerebral arteries. If overlooked, UIAs can rupture and lead to subarachnoid hemorrhages. Deep Learning (DL) models currently reach state-of-the-art performances for the automated detection of UIAs in Magnetic Resonance Angiography. However, there are still a few missing pieces to create robust DL models that can generalize across sites and be used during clinical practice. On one hand, the need for voxel-wise annotations from medical experts is hindering the creation of large datasets. On the other hand, multi-site validations are unfeasible since there exists to date only one open-access dataset. In this work, we summarize a full paper that we recently submitted to a journal and whose main contributions are the following: (a) a DL training approach that leverages fast-to-create weak labels and (b) the release of a second open-access dataset (the largest in the community) to foster model generalization.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_S_5.html">Physically Informed Neural Network for Non-Invasive Arterial Input Function Estimation In Dynamic PET Imaging</a>
    </span>
    <span class="authors"> Matteo Ferrante, Marianna Inglese, Ludovica Brusaferri, Alexander Whitehead, Marco Loggia, Nicola Toschi</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=a2a8LnYcqID">pdf</a></li><li><a href="https://openreview.net/forum?id=a2a8LnYcqID">reviews</a></li></ul><span class="abstract">
      The invasive measurement of the AIF for the full quantification of dynamic PET data limits its widespread use in clinical research studies. Current methods which estimate the AIF from imaging data are prone to large errors, even when based on NNs. This work aims to estimate the AIF from dynamic PET images using physically informed deep neural networks. To this end, we employ 3D convolutions where we exploit the different channels to encode time-dependent information, and exploit depthwise separable convolutional layers to significantly reduce parameter count. We find that the incorporation of prior knowledge in the form of differentiable equations allows accurate estimation of the AIF. This allows kinetic modeling which leads to good estimates of the distribution volume. This work can pave the way for removing the large invasivity constraint that currently limits quantitative PET applications.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_S_6.html">Domain Shift as a Confounding Variable in Unsupervised Pathology Detection</a>
    </span>
    <span class="authors"> Felix Meissen, Ioannis Lagogiannis, Georgios Kaissis, Daniel Rueckert</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6tsAzh_tnyF">pdf</a></li><li><a href="https://openreview.net/forum?id=6tsAzh_tnyF">reviews</a></li></ul><span class="abstract">
      Unsupervised Pathology Detection (UPD) has recently received considerable attention in medical image diagnosis. However, the lack of publicly available benchmark datasets for UPD makes researchers fall back on datasets that were originally created for other tasks. These datasets may exhibit domain shift that acts as a confounding variable, fooling observers into believing that the models excel at detecting pathologies, while a significant part of the model&apos;s performance is detecting the domain shift. In this short paper, we show on the example of the Hyper-Kvasir dataset, how confounding variables can dramatically skew the actual performance of pathology detection methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/E_S_7.html">Fast deformable image registration uncertainty estimation for contour propagation in daily adaptive proton therapy</a>
    </span>
    <span class="authors"> Andreas Smolders, Florian Amstutz, Ye Zhang, Damien Charles Weber, Tony Lomax, Francesca Albertini</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6b60oHnnST4">pdf</a></li><li><a href="https://openreview.net/forum?id=6b60oHnnST4">reviews</a></li></ul><span class="abstract">
      In daily adaptive proton therapy, deformable image registration (DIR) can be used to propagate manually delineated contours from a reference CT to the daily CT for plan reoptimization. However, the ill-posedness of DIR implies uncertainty on the DIR hyperparameters, which results in uncertainty in the displacement field. In this work, a fast deep learning method is developed to predict the uncertainty associated with a DIR result without the need for Monte-Carlo (MC) sampling. It is shown that this results in a significant time reduction compared to MC whilst leading to similar probabilistic contours.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_S_8.html">Constrative Learning for Kidney Transplant Analysis using MRI data and Deep Convolutional Networks</a>
    </span>
    <span class="authors"> Leo Milecki, Vicky Kalogeiton, Sylvain Bodard, Dany Anglicheau, Jean-Michel Correas, Marc-Olivier Timsit, Maria Vakalopoulou</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=fLUyt7-mWwI">pdf</a></li><li><a href="https://openreview.net/forum?id=fLUyt7-mWwI">reviews</a></li></ul><span class="abstract">
      In this work, we propose contrastive learning schemes based on a 3D Convolutional Neural Network (CNN) to generate meaningful representations for kidney transplants associated with different relevant clinical information. To deal with the problem of a limited amount of data, we investigate various two-stream schemes pre-trained in a contrastive manner, where we use the cosine embedding loss to learn to discriminate pairs of inputs. Our universal 3D CNN models identify low dimensional manifolds for representing Dynamic Contrast-Enhanced Magnetic Resonance Imaging series from four different follow-up exams after the transplant surgery. Feature visualization analysis highlights the relevance of our proposed contrastive pre-trainings and therefore their significance in the study of chronic dysfunction mechanisms in renal transplantation, setting the path for future research in this area. The code is available at https://github.com/leomlck/renal_transplant_imaging.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="reg poster">
    <span class="title">
      <a href="papers/E_S_9.html">Reference-less SSIM Regression for Detection and Quantification of Motion Artefacts in Brain MRIs</a>
    </span>
    <span class="authors"> Alessandro Sciarra, Soumick Chatterjee, Max Dünnwald, Giuseppe Placidi, Andreas Nürnberger, Oliver Speck, Steffen Oeltze-Jafra</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=24cqMfboXhH">pdf</a></li><li><a href="https://openreview.net/forum?id=24cqMfboXhH">reviews</a></li></ul><span class="abstract">
      Motion artefacts in magnetic resonance images can critically affect diagnosis and the quantification of image degradation due to their presence is required. Usually, image quality assessment is carried out by experts such as radiographers, radiologists and researchers. However, subjective evaluation requires time and is strongly dependent on the experience of the rater. In this work, an automated image quality assessment based on the structural similarity index regression through ResNet models is presented. The results show that the trained models are able to regress the SSIM values with high level of accuracy. When the predicted SSIM values were grouped into 10 classes and compared against the ground-truth motion classes, the best weighted accuracy of 89±2% was observed with RN-18 model, trained with contrast augmentation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="lnl poster">
    <span class="title">
      <a href="papers/E_S_10.html">The effect of skull-stripping on transfer learning for 3D MRI models: ADNI data</a>
    </span>
    <span class="authors"> Polina Druzhinina, Ekaterina Kondrateva</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=IS1yeyiAFZS">pdf</a></li><li><a href="https://openreview.net/forum?id=IS1yeyiAFZS">reviews</a></li></ul><span class="abstract">
      In recent years, with the improvement of data collection and preprocessing, as well as the development of deep learning algorithms, there have been more opportunities for applying artificial intelligence to different areas, including neuroimaging. Various model learning pipelines are emerging to study the degree of cognitive impairment in diseases such as Alzheimer&apos;s disease (AD). In this study, we explore knowledge transfer for the stability of the 3D computer vision models (CNN) for the classification of AD on ADNI data. To assess the model performance, and the quality of learned patterns and examine the ways of models overfitting we utilize conventional 3DCNN interpretation methods and swap tests. We imply that skull-stripping and knowledge transfer strategies can significantly impact the robustness and reproducibility of learned patterns, and suggest applying swap tests to ensure the model stability.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_S_11.html">Self-supervised Methods for Ugly Duckling Detection in Wide Field Images</a>
    </span>
    <span class="authors"> Vullnet Useini, Nicolaus Andratschke, Stephanie Tanadini-Lang, Quentin Lohmeyer, Ralph P. Braun, Javier Barranco Garcia</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=oIQdSU6T-9J">pdf</a></li><li><a href="https://openreview.net/forum?id=oIQdSU6T-9J">reviews</a></li></ul><span class="abstract">
      Screening skin lesions is a very time-consuming process in which the dermatologist examines hundreds of lesions all over the patient&apos;s body in a limited period of time. The decision as to which lesions should be further examined is made based on the &apos;ugly duckling&apos; sign. The dermatologist compares all lesions on the same patient and identifies those that are different from the average-looking lesions. Deep learning algorithms have been shown to be efficient tools for detecting outliers in large image datasets. In this study, we propose a self-supervised approach for lesion clustering and outlier detection to identify and suggest lesions of interest for each individual patient.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_S_12.html">Handcrafted Histological Transformer (H2T): A Brief Introduction</a>
    </span>
    <span class="authors"> Dang Quoc Vu, Kashif Rajpoot, SHAN E AHMED RAZA, Nasir Rajpoot</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=N_rvbWWQNsR">pdf</a></li><li><a href="https://openreview.net/forum?id=N_rvbWWQNsR">reviews</a></li></ul><span class="abstract">
      Recently, deep neural networks (DNNs) have been proposed to derive unsupervised WSI representations; these are attractive as they rely less on expert annotation which is cumbersome. However, a major trade-off is that higher predictive power generally comes at the cost of interpretability, posing a challenge to their clinical use where transparency in decision-making is generally expected. To address this challenge, we present a handcrafted framework based on DNN for constructing holistic WSI-level representations.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="url poster">
    <span class="title">
      <a href="papers/E_S_13.html">Semantic analysis of real endoscopies with unsupervised learned descriptors</a>
    </span>
    <span class="authors"> O. León Barbed, Cristina Oriol, Pablo Azagra Millán, Ana C Murillo</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=aQchDrGRkM-">pdf</a></li><li><a href="https://openreview.net/forum?id=aQchDrGRkM-">reviews</a></li></ul><span class="abstract">
      This work explores automatic analysis of medical procedure recordings, in particular, endoscopies. Regular medical practice recordings are noisy and challenging to process, so a quick and automatic overview of their content is essential. We show how advances in unsupervised representation learning can be applied to real medical data, obtaining rich descriptors to perform automatic semantic analysis of these recordings.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral3-2"></a><h3>Oral Session 3.2: Computer Aided Detection and Diagnosis - 13:20 - 14:00 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/H1.html">Regularizing Brain Age Prediction via Gated Knowledge Distillation</a>
    </span>
    <span class="authors"> Yanwu Yang, Guo Xutao, Chenfei Ye, Yang Xiang, Ting Ma</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=nxA2bZff3iQ">pdf</a></li><li><a href="https://openreview.net/forum?id=nxA2bZff3iQ">reviews</a></li></ul><span class="abstract">
      The brain age has been proven to be a phenotype of relevance to cognitive performance and brain disease. Recently, brain age estimation accuracy has been greatly improved by using deep learning. However, deep neural networks with millions of parameters may incur overfitting and suffer from poor generalizations, especially for insufficient brain imaging data. This paper presents a novel regularization method that penalizes the predictive distribution using knowledge distillation and introduces additional knowledge to reinforce the learning process. During knowledge distillation, we propose a gated distillation mechanism to enable the student model to attentively learn meaningful knowledge from the teacher model, given the assumption that a teacher might not always be correct. Moreover, to enhance the capability of knowledge transfer, the hint representation similarity is also adopted to regularize the model for training. Our evaluation on a cohort of 3655 subjects from four public datasets with ages range of 16-92, demonstrates that our proposed method improves the prediction performance over a series of well-established models, where the mean absolute error of the estimated ages is reduced to 2.129 years.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/H2.html">Personalized Prediction of Future Lesion Activity and Treatment Effect in Multiple Sclerosis from Baseline MRI</a>
    </span>
    <span class="authors"> Joshua D. Durso-Finley, Jean-Pierre René Falet, Brennan Nichyporuk, Douglas Arnold, Tal Arbel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Jc8lyRwRs90">pdf</a></li><li><a href="https://openreview.net/forum?id=Jc8lyRwRs90">reviews</a></li></ul><span class="abstract">
      Precision medicine for chronic diseases such as multiple sclerosis (MS) involves choosing a treatment that best balances efficacy and side effects for the individual patients. Making  this choice as early as possible would be important, as delays in finding an effective therapy can lead to irreversible disability accrual. To this end, we present the first multi-head, deep neural network model for individualized treatment decisions from baseline magnetic resonance imaging (MRI) (with clinical information if available) for MS patients which (a) predicts future new and enlarging T2 weighted (NE-T2) lesion counts on follow-up MRI on multiple treatments and (b) estimates the conditional average treatment effect (CATE), as defined by the predicted future suppression of NE-T2 lesions, between different treatment options relative to placebo. Our model is validated on a large, proprietary, federated dataset of 1817 multi-sequence MRIs acquired from MS patients during four multi-centre randomized clinical trials. Our framework achieves high average precision in the binarized regression of future NE-T2 lesions on five different treatments, can reliably identify heterogeneous treatment effects, and provides a personalized treatment recommendation that accounts for treatment-associated risk.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/H3.html">Survival Analysis for Idiopathic Pulmonary Fibrosis using CT Images and Incomplete Clinical Data</a>
    </span>
    <span class="authors"> Ahmed H. Shahin, Joseph Jacob, Daniel C. Alexander, David Barber</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=YWDmiiJ4hYP">pdf</a></li><li><a href="https://openreview.net/forum?id=YWDmiiJ4hYP">reviews</a></li></ul><span class="abstract">
      Idiopathic Pulmonary Fibrosis (IPF) is an inexorably progressive fibrotic lung disease with a variable and unpredictable rate of progression. CT scans of the lungs inform clinical assessment of IPF patients and contain pertinent information related to disease progression. In this work, we propose a multi-modal method that uses neural networks and memory banks to predict the survival of IPF patients using clinical and imaging data. The majority of clinical IPF patient records have missing data (e.g. missing lung function tests). To this end, we propose a probabilistic model that captures the dependencies between the observed clinical variables and imputes missing ones. This principled approach to missing data imputation can be naturally combined with a deep survival analysis model. We show that the proposed framework yields significantly better survival analysis results than baselines in terms of concordance index and integrated Brier score. Our work also provides insights into novel image-based biomarkers that are linked to mortality.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>
<p><a id="poster3-2"></a><h3>Poster Session 3.2: Onsite 11:00 - 12:00, Virtual 15:20 - 16:20 (UTC+2)</h3>
<a id="long3-2"></a><h3>Long Papers</h3></p>
<div class="papers">
<ul>
<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_1.html">MedSelect: Selective Labeling for Medical Image Classification Using Meta-Learning</a>
    </span>
    <span class="authors"> Akshay Smit, Damir Vrabac, Yujie He, Andrew Y. Ng, Andrew Beam, Pranav Rajpurkar</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=GgLjvwvB8yF">pdf</a></li><li><a href="https://openreview.net/forum?id=GgLjvwvB8yF">reviews</a></li></ul><span class="abstract">
      We propose a selective labeling method using meta-learning for medical image interpretation in the setting of limited labeling resources. Our method, MedSelect, consists of a trainable deep learning model that uses image embeddings  to select   images to label, and a non-parametric classifier that uses cosine similarity to classify unseen images. We demonstrate that MedSelect learns an effective selection strategy outperforming baseline selection strategies across seen and unseen medical conditions for chest X-ray interpretation. We also perform an analysis of the selections performed by MedSelect comparing the distribution of latent embeddings and clinical features, and find significant differences compared to the strongest performing baseline. Our method is broadly applicable across medical imaging tasks where labels are expensive to acquire.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_2.html">MAF-Net: Multi-branch Anchor-Free Detector for Polyp Localization and Classification in Colonoscopy</a>
    </span>
    <span class="authors"> Xinzi Sun, Dechun Wang, Qilei Chen, Jing Ni, Shuijiao Chen, Xiaowei Liu, Yu Cao, Benyuan Liu</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=smSjbVJvPfN">pdf</a></li><li><a href="https://openreview.net/forum?id=smSjbVJvPfN">reviews</a></li></ul><span class="abstract">
      Colorectal polyps are abnormal tissues growing on the intima of the colon or rectum with a high risk of developing into colorectal cancer, the third leading cause of cancer death world- wide. The most common types of colorectal polyps include inflammatory, hyperplastic, and adenomatous polyps. Adenomatous polyps are the most dangerous type of polyp with the potential to become cancerous. Therefore, the prevention of colorectal cancer heavily de- pends on the identification and removal of adenomatous polyps. In this paper, we propose a novel framework to assist physicians to localize, identify, and remove adenomatous polyps in colonoscopy. The framework consists of an anchor-free polyp detection branch for de- tecting and localizing polyps and a classification branch for global feature extraction and pathology prediction. Furthermore, we propose a foreground attention module to generate local features from the foreground subnet in the detection branch, which are combined with the global feature in the classification branch to enhance the pathology prediction performance. We collect a dataset that contains 6,059 images with 6,827 object-level an- notations. This dataset is the first large-scale polyp pathology dataset with both object segmentation annotations and pathology labels. Experiment results show that our proposed framework outperforms traditional CNN-based classifiers on polyp pathology classification and anchor-based detectors on polyp detection and localization.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_L_3.html">Domain Generalization for Retinal Vessel Segmentation with Vector Field Transformer</a>
    </span>
    <span class="authors"> Dewei Hu, Hao Li, Han Liu, Ipek Oguz</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=mB_V8ThxY8Z">pdf</a></li><li><a href="https://openreview.net/forum?id=mB_V8ThxY8Z">reviews</a></li></ul><span class="abstract">
      Domain generalization has become a heated topic in the literature of deep learning. It has great impact on medical image analysis as the inconsistency of data distribution is prevalent in most of the medical data modalities due to the image acquisition techniques. In this study, we investigate a novel pipeline that generalizes the retinal vessel segmentation across color fundus photography and OCT angiography images. We hypothesize that the scaled minor eigenvector of the Hessian matrix can sufficiently represent the vessel by vector flow. This vector field can be regarded as a common domain for different modalities as it is very similar even for data that follows vastly different intensity distributions. We describe two additional contributions of our work. First, we leverage the uncertainty in the latent space of the auto-encoder to synthesize enhanced vessel maps to augment the training data. Then we propose a transformer network to extract features from the vector field. In comprehensive experiments, we show that our model can work in cross-modality fashion.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_L_4.html">Hierarchical Optimal Transport for Comparing Histopathology Datasets</a>
    </span>
    <span class="authors"> Anna Yeaton, Rahul G Krishnan, Rebecca Mieloszyk, David Alvarez-Melis, Grace Huynh</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=gADV7sV4CMo">pdf</a></li><li><a href="https://openreview.net/forum?id=gADV7sV4CMo">reviews</a></li></ul><span class="abstract">
      Scarcity of labeled histopathology data limits the applicability of deep learning methods to under-profiled cancer types and labels. Transfer learning allows researchers to overcome the limitations of small datasets by pre-training machine learning models on larger datasets similar to the small target dataset. However, similarity between datasets is often determined heuristically. In this paper, we propose a principled notion of distance between histopathology datasets based on a hierarchical generalization of optimal transport distances. Our method does not require any training, is agnostic to model type, and preserves much of the hierarchical structure in histopathology datasets imposed by tiling. We apply our method to H&amp;E stained slides from The Cancer Genome Atlas from six different cancer types. We show that our method outperforms a baseline distance in a cancer-type prediction task. Our results also show that our optimal transport distance predicts difficulty of transferability in a tumor vs. normal prediction setting.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_5.html">Personalized Prediction of Future Lesion Activity and Treatment Effect in Multiple Sclerosis from Baseline MRI</a>
    </span>
    <span class="authors"> Joshua D. Durso-Finley, Jean-Pierre René Falet, Brennan Nichyporuk, Douglas Arnold, Tal Arbel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Jc8lyRwRs90">pdf</a></li><li><a href="https://openreview.net/forum?id=Jc8lyRwRs90">reviews</a></li></ul><span class="abstract">
      Precision medicine for chronic diseases such as multiple sclerosis (MS) involves choosing a treatment that best balances efficacy and side effects for the individual patients. Making  this choice as early as possible would be important, as delays in finding an effective therapy can lead to irreversible disability accrual. To this end, we present the first multi-head, deep neural network model for individualized treatment decisions from baseline magnetic resonance imaging (MRI) (with clinical information if available) for MS patients which (a) predicts future new and enlarging T2 weighted (NE-T2) lesion counts on follow-up MRI on multiple treatments and (b) estimates the conditional average treatment effect (CATE), as defined by the predicted future suppression of NE-T2 lesions, between different treatment options relative to placebo. Our model is validated on a large, proprietary, federated dataset of 1817 multi-sequence MRIs acquired from MS patients during four multi-centre randomized clinical trials. Our framework achieves high average precision in the binarized regression of future NE-T2 lesions on five different treatments, can reliably identify heterogeneous treatment effects, and provides a personalized treatment recommendation that accounts for treatment-associated risk.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_6.html">LILE: Look In-Depth before Looking Elsewhere -- A Dual Attention Network using Transformers for Cross-Modal Information Retrieval in Histopathology Archives</a>
    </span>
    <span class="authors"> Danial Maleki, Hamid Tizhoosh</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ZmsElUaQ0Xm">pdf</a></li><li><a href="https://openreview.net/forum?id=ZmsElUaQ0Xm">reviews</a></li></ul><span class="abstract">
      The volume of available data has grown dramatically in recent years in many applications. Furthermore, the age of networks that used multiple modalities separately has practically ended. Therefore, enabling bidirectional cross-modality data retrieval capable of processing has become a requirement for many domains and disciplines of research. This is especially true in the medical field, as data comes in a multitude of types, including various types of images and reports as well as molecular data. Most contemporary works apply cross attention to highlight the essential elements of an image or text in relation to the other modalities and try to match them together. However, regardless of their importance in their own modality, these approaches usually consider features of each modality equally. In this study, self-attention as an additional loss term will be proposed to enrich the internal representation provided into the cross attention module.   This work suggests a novel architecture with a new loss term to help represent images and texts in the joint latent space. Experiment results on two benchmark datasets, i.e. MS-COCO and ARCH, show the effectiveness of the proposed method.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_7.html">Attention-Guided Prostate Lesion Localization and Grade Group Classification with Multiple Instance Learning</a>
    </span>
    <span class="authors"> Ekaterina Redekop, Karthik V. Sarma, Adam Kinnaird, Anthony Sisk, Steven S. Raman, Leonard S. Marks, William Speier, Corey W. Arnold</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=QDJhkKy5x4q">pdf</a></li><li><a href="https://openreview.net/forum?id=QDJhkKy5x4q">reviews</a></li></ul><span class="abstract">
      Prostate lesion localization is a component of the prostate magnetic resonance imaging (MRI) routine evaluation. Localization is essential for targeted biopsy by enabling registration with real-time ultrasound. Most previous work on prostate cancer localization was focused on classification or segmentation assuming availability of radiological annotations. In this work we propose to use unsipervised attention-based multiple instance learning (MIL) method in an application for the prediction and localization of clinically significant prostate cancer. We train our model end-to-end with only image-level labels instead of relying on expensive pixel-level annotations. We extend MIL method by operating both on patches and the whole size image to learn local and global features which further improves classification and localization performance. To better leverage the relationships between multi-modal data we use an architecture with multiple encoding paths, where each path processing one image modality respectively. The model was developed on dataset containing 986 multiparametric prostate MRI and achieved 0.75 ± 0.03 AUROC using 3-fold cross-validation in prostate cancer Grade Group classification.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_8.html">CAD-RADS Scoring using Deep Learning and Task-Specific Centerline Labeling</a>
    </span>
    <span class="authors"> Felix Denzinger, Michael Wels, Oliver Taubmann, Mehmet Akif Gülsün, Max Schöbinger, Florian André, Sebastian Buß, Johannes Görich, Michael Suehling, Andreas Maier, Katharina Breininger</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=vVPMifME8b">pdf</a></li><li><a href="https://openreview.net/forum?id=vVPMifME8b">reviews</a></li></ul><span class="abstract">
      With coronary artery disease (CAD) persisting to be one of the leading causes of death worldwide, interest in supporting physicians with algorithms to speed up and improve diagnosis is high. In clinical practice, the severeness of CAD is often assessed with a coronary CT angiography (CCTA) scan and manually graded with the CAD-Reporting and Data System (CAD-RADS) score.  The clinical questions this score assesses are whether a patient has CAD or not (rule-out) and whether he has severe CAD or not (hold-out). In this work, we reach new state-of-the-art performance for automatic CAD-RADS scoring from CCTA. We propose using severity-based label encoding, test time augmentation (TTA) and model ensembling for a task-specific deep learning architecture. Furthermore, we introduce a novel task- and model-specific, heuristic coronary segment labeling, which subdivides coronary trees into consistent parts across patients. It is fast, robust, and easy to implement. We were able to raise the previously reported area under the receiver operating characteristic curve (AUC) from 0.914 to 0.942 in the rule-out and from 0.921 to 0.950 in the hold-out task respectively.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_L_9.html">Hidden in Plain Sight: Subgroup Shifts Escape OOD Detection</a>
    </span>
    <span class="authors"> Lisa M. Koch, Christian M. Schürch, Arthur Gretton, Philipp Berens</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=aZgiUNye2Cz">pdf</a></li><li><a href="https://openreview.net/forum?id=aZgiUNye2Cz">reviews</a></li></ul><span class="abstract">
      The safe application of machine learning systems in healthcare relies on valid performance claims. Such  claims are typically established in a clinical validation setting designed to be as close as possible to the intended use, but inadvertent domain or population shifts remain a fundamental problem. In particular, subgroups may be differently represented in the data distribution in the validation  compared to the application setting. For example, algorithms trained on population cohort data spanning all age groups may be predominantly applied in elderly people. While these data are not &apos;out-of distribution&apos;, changes in the prevalence of different subgroups may have considerable impact on algorithm performance or will at least render original performance claims invalid. Both are serious problems for safely deploying machine learning systems. In this paper, we demonstrate the fundamental limitations of individual example out-of-distribution detection for such scenarios, and show that subgroup shifts can be detected on a population-level instead. We formulate population-level shift detection in the framework of statistical hypothesis testing and show that recent state-of-the-art statistical tests can be effectively applied to subgroup shift detection in a synthetic scenario as well as real histopathology images. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_L_10.html">Signal Domain Learning Approach for Optoacoustic Image Reconstruction from Limited View Data</a>
    </span>
    <span class="authors"> Anna Klimovskaia, Berkan Lafci, Firat Ozdemir, Neda Davoudi, Xose Luis Dean-Ben, Fernando Perez-Cruz, Daniel Razansky</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=9NOyrfUBtx1">pdf</a></li><li><a href="https://openreview.net/forum?id=9NOyrfUBtx1">reviews</a></li></ul><span class="abstract">
      Multi-spectral optoacoustic tomography (MSOT) relies on optical excitation of tissues with subsequent detection of the generated ultrasound waves. Optimal image quality in MSOT is achieved by detection of signals from a broad tomographic view. However, due to physical constraints and other cost-related considerations, most imaging systems are implemented with probes having limited tomographic coverage around the imaged object, such as linear array transducers often employed for clinical ultrasound (US) imaging. MSOT image reconstruction from limited-view data results in arc-shaped image artifacts and disrupted shape of the vascular structures. Deep learning methods have previously been used to recover MSOT images from incomplete tomographic data, albeit poor performance was attained when training with data from simulations or other imaging modalities. We propose a two-step method consisting of i) style transfer for domain adaptation between simulated and experimental MSOT signals, and ii) supervised training on simulated data to recover missing tomographic signals in realistic clinical data. The method is shown capable of correcting images reconstructed from sub-optimal probe geometries using only signal domain data without the need for training with ground truth full-view images.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_11.html">Differentiable Boundary Point Extraction for Weakly Supervised Star-shaped Object Segmentation</a>
    </span>
    <span class="authors"> Robin Camarasa, Hoel Kervadec, Daniel Bos, Marleen de Bruijne</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=whpBn0oadz">pdf</a></li><li><a href="https://openreview.net/forum?id=whpBn0oadz">reviews</a></li></ul><span class="abstract">
      Although Deep Learning is the new gold standard in medical image segmentation, the annotation burden limits its expansion to clinical practice.  We also observe a mismatch between annotations required by deep learning methods designed with pixel-wise optimization in mind and clinically relevant annotations designed for biomarkers extraction (diameters, counts, etc.). Our study proposes a first step toward bridging this gap, optimizing vessel segmentation based on its diameter annotations. To do so we propose to extract boundary points from a star-shaped segmentation in a differentiable manner. This differentiable extraction allows reducing annotation burden as instead of the pixel-wise segmentation only the two annotated points required for diameter measurement are used for training the model. Our experiments show that training based on diameter is efficient; produces state-of-the-art weakly supervised segmentation; and performs reasonably compared to full supervision. 
oindent Our code is publicly available:url{https:anonymous.4open.sciencerBoundary-Point-Extraction-F163}
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_12.html">Interpretable and Interactive Deep Multiple Instance Learning for Dental Caries Classification in Bitewing X-rays</a>
    </span>
    <span class="authors"> Benjamin Bergner, Csaba Rohrer, Aiham Taleb, Martha Duchrau, Guilherme De Leon, Jonas Almeida Rodrigues, Falk Schwendicke, Joachim Krois, Christoph Lippert</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=NpHKh4YlQ0D">pdf</a></li><li><a href="https://openreview.net/forum?id=NpHKh4YlQ0D">reviews</a></li></ul><span class="abstract">
      We propose a simple and efficient image classification architecture based on deep multiple instance learning, and apply it to the challenging task of caries detection in dental radiographs. Technically, our approach contributes in two ways: First, it outputs a heatmap of local patch classification probabilities despite being trained with weak image-level labels. Second, it is amenable to learning from segmentation labels to guide training. In contrast to existing methods, the human user can faithfully interpret predictions and interact with the model to decide which regions to attend to. Experiments are conducted on a large clinical dataset of \sim$38k bitewings ($\sim$316k teeth), where we achieve competitive performance compared to various baselines. When guided by an external caries segmentation model, a significant improvement in classification and localization performance is observed.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_L_13.html">Unsupervised Domain Adaptation for Medical Image Segmentation via Self-Training of Early Features</a>
    </span>
    <span class="authors"> Rasha Sheikh, Thomas Schultz</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=wc9qnxw35tS">pdf</a></li><li><a href="https://openreview.net/forum?id=wc9qnxw35tS">reviews</a></li></ul><span class="abstract">
      U-Net models provide a state-of-the-art approach for medical image segmentation, but their accuracy is often reduced when training and test images come from different domains, such as different scanners. Recent work suggests that, when limited supervision is available for domain adaptation, early U-Net layers benefit the most from a refinement. This motivates our proposed approach for self-supervised refinement, which does not require any manual annotations, but instead refines early layers based on the richer, higher-level information that is derived in later layers of the U-Net. This is achieved by adding a segmentation head for early features, and using the final predictions of the network as pseudo-labels for refinement. This strategy reduces detrimental effects of imperfection in the pseudo-labels, which are unavoidable given the domain shift, by retaining their probabilistic nature and restricting the refinement to early layers. Experiments on two medical image segmentation tasks confirm the effectiveness of this approach, and compare favorably to a baseline method for unsupervised domain adaptation.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_14.html">Structural Networks for Brain Age Prediction</a>
    </span>
    <span class="authors"> Oscar Pina, Irene Cumplido-Mayoral, Raffaele Cacciaglia, José María González‐de‐Echávarri, Juan Domingo Gispert, Veronica Vilaplana</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Uf8Ow26cpU">pdf</a></li><li><a href="https://openreview.net/forum?id=Uf8Ow26cpU">reviews</a></li></ul><span class="abstract">
      Biological networks have gained considerable attention within the Deep Learning community because of the promising framework of Graph Neural Networks (GNN), neural models that operate in complex networks. In the context of neuroimaging, GNNs have successfully been employed for functional MRI processing but their application to ROI-level structural MRI (sMRI) remains mostly unexplored. In this work we analyze the implementation of these geometric models with sMRI by building graphs of ROIs (ROI graphs) using tools from Graph Signal Processing literature and evaluate their performance in a downstream supervised task, age prediction. We first make a qualitative and quantitative comparison of the resulting networks obtained with common graph topology learning strategies. In a second stage, we train GNN-based models for brain age prediction. Since the order of every ROI graph is exactly the same and each vertex is an entity by itself (a ROI), we evaluate whether including ROI information during message-passing or global pooling operations is beneficial and compare the performance of GNNs against a Fully-Connected Neural Network baseline. The results show that ROI-level information is needed during the global pooling operation in order to achieve competitive results. However, no relevant improvement has been detected when it is incorporated during the message passing. These models achieve a MAE of 4.27 in hold-out test data, which is a performance very similar to the baseline, suggesting that the inductive bias included with the obtained graph connectivity is relevant and useful to reduce the dimensionality of the problem.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_15.html">Survival Analysis for Idiopathic Pulmonary Fibrosis using CT Images and Incomplete Clinical Data</a>
    </span>
    <span class="authors"> Ahmed H. Shahin, Joseph Jacob, Daniel C. Alexander, David Barber</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=YWDmiiJ4hYP">pdf</a></li><li><a href="https://openreview.net/forum?id=YWDmiiJ4hYP">reviews</a></li></ul><span class="abstract">
      Idiopathic Pulmonary Fibrosis (IPF) is an inexorably progressive fibrotic lung disease with a variable and unpredictable rate of progression. CT scans of the lungs inform clinical assessment of IPF patients and contain pertinent information related to disease progression. In this work, we propose a multi-modal method that uses neural networks and memory banks to predict the survival of IPF patients using clinical and imaging data. The majority of clinical IPF patient records have missing data (e.g. missing lung function tests). To this end, we propose a probabilistic model that captures the dependencies between the observed clinical variables and imputes missing ones. This principled approach to missing data imputation can be naturally combined with a deep survival analysis model. We show that the proposed framework yields significantly better survival analysis results than baselines in terms of concordance index and integrated Brier score. Our work also provides insights into novel image-based biomarkers that are linked to mortality.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_L_16.html">A Modular Deep Learning Pipeline for Cell Culture Analysis: Investigating the Proliferation of Cardiomyocytes</a>
    </span>
    <span class="authors"> Lars Leyendecker, Julius Haas, Tobias Piotrowski, Maik Frye, Cora Becker, Bernd K. Fleischmann, Michael Hesse, Robert H. Schmitt</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=hTil-xs1xNq">pdf</a></li><li><a href="https://openreview.net/forum?id=hTil-xs1xNq">reviews</a></li></ul><span class="abstract">
      Cardiovascular disease is a leading cause of death in the Western world. The exploration of strategies to enhance the regenerative capacity of the mammalian heart is therefore of great interest. One approach is the treatment of isolated transgenic mouse cardiomyocytes (CMs) with potentially cell cycle-inducing substances and assessment if this results in atypical cell cycle activity or authentic cell division. This requires the tedious and cost intensive manual analysis of microscopy images. Advances in recent years have led to the increasing use of deep learning (DL) algorithms in cell biological image analysis. While developments in image or single-cell classification are well advanced, multi-cell classification in crowded image scenarios remains a challenge. This is reinforced by typically smaller dataset sizes in such laboratory-specific analyses. In this paper, we propose a modular DL-based image analysis pipeline for multi-cell classification of mononuclear and binuclear CMs in confocal microscopy imaging data. We trisect the pipeline structure into preprocessing, modelling and postprocessing. We perform semantic segmentation to extract general image features, which are further analyzed in postprocessing. We benchmark 18 encoder-decoder model architectures, perform hyperparameter optimization, and conduct 127 experiments to evaluate dataset-related effects. The results show that our approach has great potential for automating specific cell culture analyses even with small datasets.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_17.html">ECONet: Efficient Convolutional Online Likelihood Network for Scribble-based Interactive Segmentation</a>
    </span>
    <span class="authors"> Muhammad Asad, Lucas Fidon, Tom Vercauteren</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=9xtE2AgD_Cc">pdf</a></li><li><a href="https://openreview.net/forum?id=9xtE2AgD_Cc">reviews</a></li></ul><span class="abstract">
      Automatic segmentation of lung lesions associated with COVID-19 in CT images requires large amount of annotated volumes. Annotations mandate expert knowledge and are time-intensive to obtain through fully manual segmentation methods. Additionally, lung lesions have large inter-patient variations, with some pathologies having similar visual appearance as healthy lung tissues. This poses a challenge when applying existing semi-automatic interactive segmentation techniques for data labelling. To address these challenges, we propose an efficient convolutional neural networks (CNNs) that can be learned online while the annotator provides scribble-based interaction. To accelerate learning from only the samples labelled through user-interactions, a patch-based approach is used for training the network. Moreover, we use weighted cross-entropy loss to address the class imbalance that may result from user-interactions. During online inference, the learned network is applied to the whole input volume using a fully convolutional approach. We compare our proposed method with state-of-the-art and show that it outperforms existing methods on the task of annotating lung lesions associated with COVID-19, achieving 16% higher Dice score while reducing execution time by 3$    imes$ and requiring 9000 lesser scribbles-based labelled voxels. Due to the online learning aspect, our approach adapts quickly to user input, resulting in high quality segmentation labels. Source code will be made available upon acceptance. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="del poster">
    <span class="title">
      <a href="papers/F_L_18.html">EfficientCellSeg: Efficient Volumetric Cell Segmentation Using Context Aware Pseudocoloring</a>
    </span>
    <span class="authors"> Royden Wagner, Karl Rohr</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=KnJsGdhx1kH">pdf</a></li><li><a href="https://openreview.net/forum?id=KnJsGdhx1kH">reviews</a></li></ul><span class="abstract">
      Volumetric cell segmentation in fluorescence microscopy images is important to study a wide variety of cellular processes. Applications range from the analysis of cancer cells to behavioral studies of cells in the embryonic stage. Like in other computer vision fields, most recent methods use either large convolutional neural networks (CNNs) or vision transformer models (ViTs). Since the number of available 3D microscopy images is typically limited in applications, we take a different approach and introduce a small CNN for volumetric cell segmentation. Compared to previous CNN models for cell segmentation, our model is efficient and has an asymmetric encoder-decoder structure with very few parameters in the decoder. Training efficiency is further improved via transfer learning. In addition, we introduce Context Aware Pseudocoloring to exploit spatial context in z-direction of 3D images while performing volumetric cell segmentation slice-wise. We evaluated our method using different 3D datasets from the Cell Segmentation Benchmark of the Cell Tracking Challenge. Our segmentation method achieves top-ranking results while our CNN model has an up to 25x lower number of parameters than other top-ranking methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="short3-2"></a><h3>Short Papers</h3></p>
<div class="papers">
<ul>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_1.html">Transfer Learning Promotes Robust Parametric Mapping of Diffusion Encoded MR Fingerprinting</a>
    </span>
    <span class="authors"> Alan Finkelstein, Congyu Liao, Xiaozhi Cao, Jianhui Zhong</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=pCusj-HT_bi">pdf</a></li><li><a href="https://openreview.net/forum?id=pCusj-HT_bi">reviews</a></li></ul><span class="abstract">
      MR fingerprinting (MRF) is a framework to simultaneously quantify multiple tissue properties. Acquisition parameters are varied pseudo-randomly and each signal evolution is matched with a dictionary of simulated entries. However, dictionary methods are computationally and memory intensive. Deep learners (DL) are capable of mapping complex MRF signal evolutions to a quantitative parametric space, reducing the computational requirements and reconstruction time; yet fail to perform as well in the setting of noise. Drawing from natural language processing (NLP) we proposed a transfer learning (TL) model to improve MRF parametric estimates with realistic noise levels. The weights of a network trained on clean data are used to instantiate the weights of a noisy model. The model is constrained to learn noise invariant features, by freezing the last layer. Signal evolutions were modeled using a recurrent neural network (RNN) to reconstruct T1, T2, and the apparent diffusion coefficient (ADC). Compared to a model trained with noise, but without TL our approached resulted in a 15% reduction in mean squared error (MSE). Monte Carlo simulations performed at varying SNR (10-60 dB) showed our method yielded losses comparable to the clean model at higher SNRs and proved more robust in the setting of noise at lower SNRs.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_2.html">Automatic Extraction of Spinopelvic Parameters Using Deep Learning to Detect Landmarks as Objects</a>
    </span>
    <span class="authors"> AliAsghar MohammadiNasrabadi, William McNally, Gemah Moammer, John McPhee</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=1WGmOnOjJU-">pdf</a></li><li><a href="https://openreview.net/forum?id=1WGmOnOjJU-">reviews</a></li></ul><span class="abstract">
      Surgeons measure spinopelvic parameters from X-ray images to evaluate spinopelvic alignment preoperatively for surgical planning. Automatic extraction of these parameters not only saves time but also provides consistent measurements, avoiding human error. In this paper, we introduce a new approach to automatic spinopelvic parameter extraction, which considers landmarks as objects. The landmarks are extracted using a deep learning object detection algorithm that can address the drawbacks of heatmap-based regression. The model is evaluated using two datasets totalling 1000 lateral spinal and pelvic X-ray images. Acceptable accuracy is achieved when comparing the reference manual parameter measurements with those obtained automatically by our prediction model.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_3.html">Source-Free Domain Adaptation for Image Segmentation</a>
    </span>
    <span class="authors"> Mathilde Bateson, Hoel Kervadec, Jose Dolz, Herve Lombaert, Ismail Ben Ayed</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=JfGn-feo88D">pdf</a></li><li><a href="https://openreview.net/forum?id=JfGn-feo88D">reviews</a></li></ul><span class="abstract">
      Domain adaptation (DA) tackles the performance drop observed when applying a model on target data from a different domain than the training one. However, most common DA techniques require concurrent access to the input images of both the source and target domains, which is often impossible for privacy concerns. We introduce a source-free domain adaptation for image segmentation, leveraging a prior-aware entropy minimization. We validate on spine, prostate and cardiac segmentation problems.  Our method yields comparable results to several state-of-the-art adaptation techniques, despite having access to much less information. Our framework can be used in many segmentation problems, and our code is publicly available at url{https://github.com/mathilde-b/SFDA}
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_4.html">Predicting Thrombectomy Recanalization from CT Imaging Using Deep Learning Models</a>
    </span>
    <span class="authors"> Haoyue Zhang, Jennifer Polson, Eric J Yang, Kambiz Nael, William Speier, Corey W. Arnold</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=6K7FJWUmSiF">pdf</a></li><li><a href="https://openreview.net/forum?id=6K7FJWUmSiF">reviews</a></li></ul><span class="abstract">
      For acute ischemic stroke (AIS) patients with large vessel occlusions, clinicians must decide if the benefit of mechanical thrombectomy (MTB) outweighs the risks and potential complications following an invasive procedure. Pre-treatment computed tomography (CT) and angiography (CTA) are widely used to characterize occlusions in the brain vasculature. If a patient is deemed eligible, a modified treatment in cerebral ischemia (mTICI) score will be used to grade how well blood flow is reestablished throughout and following the MTB procedure. An estimation of the likelihood of successful recanalization can support treatment decision-making. In this study, we proposed a fully automated prediction of a patient&apos;s recanalization score using pre-treatment CT and CTA imaging. We designed a spatial cross attention network (SCANet) that utilizes vision transformers to localize to pertinent slices and brain regions. Our top model achieved an average cross-validated ROC-AUC of 77.33 ± 3.9%. This is a promising result that supports future applications of deep learning on CT and CTA for the identification of eligible AIS patients for MTB.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_5.html">Graph Attention Network for Prostate Cancer Lymph Node Invasion Prediction</a>
    </span>
    <span class="authors"> Maxence Larose, Nawar Touma, Nicolas Raymond, Danahé LeBlanc, Fatemeh Rasekh, Bertrand Neveu, Hélène Hovington, Martin Vallières, Frédéric Pouliot, Louis Archambault</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=zIpx-MISaIA">pdf</a></li><li><a href="https://openreview.net/forum?id=zIpx-MISaIA">reviews</a></li></ul><span class="abstract">
      This work proposes the use of a graph attention network (GAT) model combining radiomics and clinical data to improve the performance and interpretability of lymph node invasion (LNI) prediction in high-grade prostate cancer (PCa). Experiments were conducted using an in-house dataset of 170 high-grade PCa (Gleason $\geq8$), each with FDG-PET/CT images acquired prior to prostatectomy. To ensure interpretable connections between patients, the graph structure was constructed by merging the most important radiomic shape-based CT feature and first-order intensity-based PET feature to the clinically relevant features. The performance of the GAT model was compared to random forest (RF) and support vector machine (SVM) classifiers. On the 30 patients test set, the models reached {AUC=0.765, bACC= 0.705}, {AUC=0.748, bACC=0.66} and {AUC=0.725,bACC=0.725} for the GAT, RF and SVM models respectively. Even though SVM achieved higher balanced accuracy than GAT, the predictions made by the latter are more interpretable through the graph structure and attention mechanism.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_6.html">Focal loss improves repeatability of deep learning models</a>
    </span>
    <span class="authors"> Syed Rakin Ahmed, Andreanne Lemay, Katharina V Hoebel, Jayashree Kalpathy-cramer</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7Cov6FwmOP1">pdf</a></li><li><a href="https://openreview.net/forum?id=7Cov6FwmOP1">reviews</a></li></ul><span class="abstract">
      Deep learning models for clinical diagnosis, prognosis and treatment need to be trustworthy and robust for clinical deployment, given that model predictions often directly inform a subsequent course of action, where individual patient lives are at stake. Central to model robustness is repeatability, or the ability of a model to generate near-identical predictions under identical conditions. In this work, we optimize focal loss as a cost function to improve repeatability of model predictions on two clinically significant classification tasks: knee osteoarthritis grading and breast density classification, with and without the presence of Monte Carlo (MC) Dropout. We discover that in all experimental instances, focal loss improves repeatability of the resulting models, an effect compounded in the presence of MC Dropout.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_7.html">Efficient Transfer Learning for Cardiac landmark Localization Using Rotational Entropy</a>
    </span>
    <span class="authors"> Samira Masoudi, Kevin Blansit, Naeim Bahrami, Albert Hsiao</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=tOzkTcofcnN">pdf</a></li><li><a href="https://openreview.net/forum?id=tOzkTcofcnN">reviews</a></li></ul><span class="abstract">
      Transfer learning is a common technique to address model generalization among different sources, which requires additional annotated data.  Herein, we proposed a novel strategy to select new data to be annotated for transfer learning of a landmark localization model, minimizing the time and effort for annotation and thus model generalization. A CNN model was initially trained using 1.5T images to localize the apex and mitral valve on the long axis cardiac MR images. Model performance on 3T images was reported poor, necessitating transfer learning to 3T images.    extit{Rotational entropy}, was introduced not only as a surrogate of model performance but as a metric which could be used to prioritize the most informative cases for transfer learning.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_8.html">Energy Efficiency of Quantized Neural Networks in Medical Imaging</a>
    </span>
    <span class="authors"> Priyanshu Sinha, Sai Sreya Tummala, Saptarshi Purkayastha, Judy Gichoya</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=laP9b5P22kZ">pdf</a></li><li><a href="https://openreview.net/forum?id=laP9b5P22kZ">reviews</a></li></ul><span class="abstract">
      The main goal of this paper is to compare the energy efficiency of quantized neural networks to perform medical image analysis on different processors and neural network architectures. Deep neural networks have demonstrated outstanding performance in medical image analysis but require high computation and power usage. In our work, we review the power usage and temperature of processors when running Resnet and Unet architectures to perform image classification and segmentation respectively. We compare Edge TPU, Jetson Nano, Apple M1, Nvidia Quadro P6000 and Nvidia A6000 to infer using full-precision FP32 and quantized INT8 models. The results will be useful for designers and implementers of medical imaging AI on hand-held or edge computing devices.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_9.html">3D convolutional neural networks for outcome prediction in glioblastoma using methionine PET and T1w MRI</a>
    </span>
    <span class="authors"> Iram Shahzadi, Annekatrin Seidlitz, Alex Zwanenburg, Bettina Beuthien-Baumann, Ivan Platzek, Jörg Kotzerke, Michael Baumann, Mechthild Krause, Steffen Löck</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=BLXlChVgVb5">pdf</a></li><li><a href="https://openreview.net/forum?id=BLXlChVgVb5">reviews</a></li></ul><span class="abstract">
      For treatment personalization of patients with glioblastoma, we investigate three different 3D convolutional neural networks (3D-CNN) for predicting time to recurrence (TTR) and overall survival (OS) from postoperative [11C] methionine PET (MET-PET) and gadolinium-enhanced T1-weighted magnetic resonance imaging (T1c-w MRI). The 3D-DenseNet model on MET-PET integrated with age and MGMT status achieved the best performance on independent test data (Concordance-Index: TTR=0.68, OS=0.65) with significant patient stratification (p-value: TTR=0.017, OS=0.039). After prospective validation, these models may be considered for treatment personalization.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_10.html">Convolutional neural networks predict the linear energy transfer for proton-beam radiotherapy of patients with brain tumours</a>
    </span>
    <span class="authors"> Sebastian Starke, Jan Eulitz, Alex Zwanenburg, Esther G.C. Troost, Mechthild Krause, Armin Lühr, Steffen Löck</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=ue4_3NG344g">pdf</a></li><li><a href="https://openreview.net/forum?id=ue4_3NG344g">reviews</a></li></ul><span class="abstract">
      Proton therapy is a promising option for cancer treatment, even though its radiobiological properties are not yet fully considered in clinical practice. In this context, the relative biological effectiveness (RBE) of protons is the most important quantity, which is strongly related to their linear energy transfer (LET). LET distributions can be provided by commercial treatment-planning systems based on Monte Carlo simulations. However, such systems require a considerable amount of computational resources, are not yet available in every proton-therapy centre and may not be applicable to assess retrospective patient data. Here, we provide proof-of-concept for inferring LET distributions using convolutional neural networks (CNN) based on proton therapy radiation dose distributions and treatment-planning computed tomography (CT). We further evaluate established models for estimating treatment-related side effects after proton therapy of brain tumours and observe good agreement between CNN and MC based outputs.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_11.html">A vertebral compression fracture score based on deep generative contextual modeling</a>
    </span>
    <span class="authors"> Michel Botros, Matthieu Rutten, Twan van Laarhoven, Nikolas Lessmann</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=g0L9efmf56G">pdf</a></li><li><a href="https://openreview.net/forum?id=g0L9efmf56G">reviews</a></li></ul><span class="abstract">
      Grading of vertebral compression fractures most commonly relies on a semi-quantitative grading scale that defines fractures as height loss of the vertebral body. This paper presents an alternative approach that instead considers the three-dimensional shape of the vertebral body and expresses the abnormality of the shape on a scale from 0 to 100. The abnormality is expressed relative to the expected healthy shape, which is predicted by a deep generative model that is provided with contextual information, namely shape and orientation of surrounding vertebrae.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_12.html">Toward Automatic Tumor-Stroma Ratio Assessment for Survival Analysis in Colorectal Cancer</a>
    </span>
    <span class="authors"> Christian Abbet, Linda Studer, Inti Zlobec, Jean-Philippe Thiran</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=PMQZGFtItHJ">pdf</a></li><li><a href="https://openreview.net/forum?id=PMQZGFtItHJ">reviews</a></li></ul><span class="abstract">
      In this paper, we present a fully automated system for tumor-stroma ratio scoring in line with current recommendations for pathologists, based on tumor and tumor-adjacent stroma tissue detection. In order to evaluate the scoring system, we perform survival analysis on 221 whole slide images from colorectal cancer patients. We find that the whole slide-level and region of interest-level tumor-stroma ratio are statistically significant predictors of overall survival.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_13.html">Stain Isolation-based Guidance for Improved Stain Translation</a>
    </span>
    <span class="authors"> Nicolas Brieu, Felix J. Segerer, Ansh Kapil, Philipp Wortmann, Günter Schmidt</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=Sml87FSoVqh">pdf</a></li><li><a href="https://openreview.net/forum?id=Sml87FSoVqh">reviews</a></li></ul><span class="abstract">
      Unsupervised and unpaired domain translation using generative adversarial neural networks, and more precisely CycleGAN, is state of the art for the stain translation of histopathology images. It often, however, suffers from the presence of cycle-consistent but non structure-preserving errors. We propose an alternative approach to the set of methods which, relying on segmentation consistency, enable the preservation of pathology structures. Focusing on immunohistochemistry (IHC) and multiplexed immunofluorescence (mIF), we introduce a simple yet effective guidance scheme as a loss function that leverages the consistency of stain translation with stain isolation. Qualitative and quantitative experiments show the ability of the proposed approach to improve translation between the two domains
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_14.html">Towards more efficient tumor follow-up assessment using AI assistance</a>
    </span>
    <span class="authors"> Alessa Hering, Felix Peisen, Jan Hendrik Moltz</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=4chzvY0rrV">pdf</a></li><li><a href="https://openreview.net/forum?id=4chzvY0rrV">reviews</a></li></ul><span class="abstract">
          Measurement of metastatic tumors on longitudinal computer tomography (CT) scans is essential to evaluate the efficacy of cancer treatment. Manual measurements for the diameter-based RECIST (Response Evaluation Criteria In Solid Tumors) criteria are often time-consuming and error-prone. However, those criteria and the execution of the measurements undergo continuous changes. Lesion segmentation assistance based on artificial intelligence (AI) might significantly speed up response evaluation and help to handle the ever-growing mass of image-based staging and follow-up evaluations. Various technical papers investigate the segmentation accuracy of AI algorithms. While these technical measures give a first impression of the performance, they do not yet tell us whether we can add value to the assessment of cancer patients. As a first step to quantify this, the goal of the presented reader study was to compare the workflow of reading follow-up examinations with and without AI assistance to evaluate the impact of the proposed AI-assisted workflow. Our findings support our research hypothesis of an assisted workflow which is superior with respect to processing time and non-inferior with respect to accuracy compared to the manual workflow.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="damg poster">
    <span class="title">
      <a href="papers/F_S_15.html">A Simple but Effective Training Process for the Few-shot Prediction Task of Early Rheumatoid Arthritis from MRI</a>
    </span>
    <span class="authors"> Yanli Li, Denis P. Shamonin, Tahereh Hassanzadeh, Monique Reijnierse, Annette H.M. van der Helm-van Mil, Berend Stoel</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=8fk23e6ftYP">pdf</a></li><li><a href="https://openreview.net/forum?id=8fk23e6ftYP">reviews</a></li></ul><span class="abstract">
      Predicting rheumatoid arthritis (RA) in an early-stage based on MRI can help initiate timely treatment and therefore halt the progression of the disease and increase the possibility of recovery. Deep learning methods are in general highly suitable for this type of labeling tasks. However, applying this approach to RA detection faces challenges from the lack of a large number of samples, difficulty in distinguishing patterns of RA from imaging artifacts, and a wide anatomical variation, leading to the failure of transfer learning based on pre-trained models. In this paper, a pre- and post-training method for this fewshot task is proposed. Based on the clinical MRI data, this method was validated through cross-validation, achieving a significant improvement in AUC, F1 score, and accuracy to the baseline deep learning models. Since these pre- and post-training strategies are intuitive, effective and easy to implement, they can also contribute to other challenging few-shot medical tasks.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_16.html">Improving CCE video review time with a model based on frame similarity</a>
    </span>
    <span class="authors"> Pere Gilabert, Santi Seguí</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=3lLvO8-a3EE">pdf</a></li><li><a href="https://openreview.net/forum?id=3lLvO8-a3EE">reviews</a></li></ul><span class="abstract">
      Many advances have been made in the detection of pathologies through the use of the Colon Capsule Endoscopy (CCE), a non-invasive procedure that allows physicians to view the entire interior of a patient&apos;s digestive system without the need for sedation. In this article we focus on the subsequent process, assuming that we already have a good model to detect a pathology (polyps in this case) and see how to improve the video review process by re-sorting the high score frames. With a simple sorting method, we obtain a 7% improvement compared to the linear method where the frames are reviewed in decreasing order of score. This accuracy boost occurs in the first 100 frames, which allows the videos to be reviewed more quickly and efficiently.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_17.html">Automated L3-based sarcopenia quantification in CT scans</a>
    </span>
    <span class="authors"> Othmane Laousy, Guillaume Chassagnon, Nikos Paragios, Marie-Pierre Revel, Maria Vakalopoulou</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=7-uT3eV0pI">pdf</a></li><li><a href="https://openreview.net/forum?id=7-uT3eV0pI">reviews</a></li></ul><span class="abstract">
      Sarcopenia refers to a skeletal muscle disorder that results in gradual and widespread muscle loss. Single-slice sarcopenia quantification is done with the localization of a vertebra first, followed by muscle segmentation.  In this paper, we present a fully automated sarcopenia assessment pipeline for CT scans, relying on powerful deep learning based techniques. Our framework consists of two steps, one that solves the detection of the appropriate CT slice using reinforcement learning and one that addresses the segmentation of the abdominal muscle mass together with the total quantification of its area.  Our pipeline has been evaluated on 100 patients, including different CT scan protocols, and reports an overall quantification performance smaller than the interobserver, indicating its potential for clinical practice.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_18.html">Pulmonary Embolus Detection with Dual-Energy CT Data Augmentation</a>
    </span>
    <span class="authors"> Cornelia Hofsäß, Roman Johannes Gertz, Tanja Lossau, Jens-Peter M. Zemke, Tobias Klinder, Alexander C. Bunck, Hannes Nickisch</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=3shWnvRa0P">pdf</a></li><li><a href="https://openreview.net/forum?id=3shWnvRa0P">reviews</a></li></ul><span class="abstract">
      3D segmentation U-Nets are trained for pulmonary embolus detection on three different data sets. We investigate the impact of the training data set on the generalization capabilities and use dual-energy CT data augmentation to increase performance.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_19.html">Automated Analysis of Mitral Inflow Doppler using Convolutional Neural Networks</a>
    </span>
    <span class="authors"> Jevgeni Jevsikov, Elisabeth Sarah Lane, Catherine C Stowell, Matthew J Shun-shin, Darrel P Francis, Massoud Zolgharni</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=SBrZSeeIo6N">pdf</a></li><li><a href="https://openreview.net/forum?id=SBrZSeeIo6N">reviews</a></li></ul><span class="abstract">
      Doppler echocardiography is commonly used for functional assessment of heart valves such as mitral valve. Currently, the measurements are made manually which is a laborious and subjective process. We have demonstrated the feasibility of using neural networks to fully automate the process of mitral valve inflow measurements. Experiments show that the automated system yields comparable performance to the experts.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
<li><div class="cad poster">
    <span class="title">
      <a href="papers/F_S_20.html">Two-Year Overall Survival Prediction in Non–Small-Cell Lung Cancer Patients Using Pre-Treatment Computed Tomography Images and Deep Neural Networks: A Multicentric Study</a>
    </span>
    <span class="authors"> zahra Khodabakhshi, Habib Zaidi, Isaac Shiri, Nicolaus Andratschke, stephanie Tanadini-Lang</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=GqWakgLuMOn">pdf</a></li><li><a href="https://openreview.net/forum?id=GqWakgLuMOn">reviews</a></li></ul><span class="abstract">
      Introduction:  Prognostic models for cancer patients may improve decision making to personalize management of cancer patients. In the current study, we propose a deep learning-based predictive model for Non–Small-Cell Lung Cancer patients. We developed a combined 2D and 3D model to include all 3D tumour information in CT images without losing spatial information.  Method: In the current study, we enrolled 363 histopathological proven Patients from 5 different centres gathered from TCIA. In current study we aimed to predict 2 year overall survival, for this purpose continues value of survival times (calculated from start of the treatment) were dichotomized by 2-year cut-off point. We excluded right-censored patients (alive patients with follow up less than 2 years). We extracted each tumour separately based on bounding box We applied largest bounding box on each tumour separately considering the centre of mass of each lesion. Finally, we extracted a tumour region with size of 128×128×Z which Z is different for each different patient. We implemented 2D networks to construct  3D combination CNNs network. Feature extraction was performed in each 2D slices separately using same architecture and then final layer of network were averaged to train in 3D volume of tumor. Different architecture of networks including simple Xception, VGG, ResNet, Inception, and DensNet were implemented in this approach.  Data of three centre (257) were used for train/validation and two centres were hold for external test set (106 patients). The predictive power of each model was assessed by using the area under the receiver operating characteristic (AUC - ROC), precision, recall, and accuracy. DeLong tests were performed on AUC to compare different models. Results: We set up a study to predict two year overall survival in NSCLC patients using deep neural networks. In term of accuracy, VGG had highest performance of 0.75. In term of precision and recall Xception and VGG had highest value of 0.77 and 0.83, respectively. Considering all four parameters, VGG had highest performance with precision, recall, AUC, and accuracy of 0.72, 0.83, 0.78, and 0.75, respectively . There was no statistically significant difference between different models (delong test p-value &gt;0.05).   Conclusion:. In current study we proposed end-to-end prognostic modelling in NSCLC using deep neural networks and pre-treatment CT images. Notwithstanding high variability across different datasets including geographic, ethnicity and CT scanner, image acquisition and image reconstruction, proposed models performed very well on different centres. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></li>
</ul>
</div>
<p><a id="oral3-3"></a><h3>Oral Session 3.3: Data Efficient Learning - 16:20 - 17:20 (UTC+2)</h3></p>
<div class="papers">
<ul>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/I1.html">MedSelect: Selective Labeling for Medical Image Classification Using Meta-Learning</a>
    </span>
    <span class="authors"> Damir Vrabac, Akshay Smit, Yujie He, Andrew Y. Ng, Andrew Beam, Pranav Rajpurkar</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=GgLjvwvB8yF">pdf</a></li><li><a href="https://openreview.net/forum?id=GgLjvwvB8yF">reviews</a></li></ul><span class="abstract">
      We propose a selective labeling method using meta-learning for medical image interpretation in the setting of limited labeling resources. Our method, MedSelect, consists of a trainable deep learning model that uses image embeddings  to select   images to label, and a non-parametric classifier that uses cosine similarity to classify unseen images. We demonstrate that MedSelect learns an effective selection strategy outperforming baseline selection strategies across seen and unseen medical conditions for chest X-ray interpretation. We also perform an analysis of the selections performed by MedSelect comparing the distribution of latent embeddings and clinical features, and find significant differences compared to the strongest performing baseline. Our method is broadly applicable across medical imaging tasks where labels are expensive to acquire.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/I2.html">Differentiable Boundary Point Extraction for Weakly Supervised Star-shaped Object Segmentation</a>
    </span>
    <span class="authors"> Robin Camarasa, Hoel Kervadec, Daniel Bos, Marleen de Bruijne</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=whpBn0oadz">pdf</a></li><li><a href="https://openreview.net/forum?id=whpBn0oadz">reviews</a></li></ul><span class="abstract">
      Although Deep Learning is the new gold standard in medical image segmentation, the annotation burden limits its expansion to clinical practice.  We also observe a mismatch between annotations required by deep learning methods designed with pixel-wise optimization in mind and clinically relevant annotations designed for biomarkers extraction (diameters, counts, etc.). Our study proposes a first step toward bridging this gap, optimizing vessel segmentation based on its diameter annotations. To do so we propose to extract boundary points from a star-shaped segmentation in a differentiable manner. This differentiable extraction allows reducing annotation burden as instead of the pixel-wise segmentation only the two annotated points required for diameter measurement are used for training the model. Our experiments show that training based on diameter is efficient; produces state-of-the-art weakly supervised segmentation; and performs reasonably compared to full supervision. 
oindent Our code is publicly available:url{https:anonymous.4open.sciencerBoundary-Point-Extraction-F163}
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div></p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/I3.html">ECONet: Efficient Convolutional Online Likelihood Network for Scribble-based Interactive Segmentation</a>
    </span>
    <span class="authors"> Muhammad Asad, Lucas Fidon, Tom Vercauteren</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=9xtE2AgD_Cc">pdf</a></li><li><a href="https://openreview.net/forum?id=9xtE2AgD_Cc">reviews</a></li></ul><span class="abstract">
      Automatic segmentation of lung lesions associated with COVID-19 in CT images requires large amount of annotated volumes. Annotations mandate expert knowledge and are time-intensive to obtain through fully manual segmentation methods. Additionally, lung lesions have large inter-patient variations, with some pathologies having similar visual appearance as healthy lung tissues. This poses a challenge when applying existing semi-automatic interactive segmentation techniques for data labelling. To address these challenges, we propose an efficient convolutional neural networks (CNNs) that can be learned online while the annotator provides scribble-based interaction. To accelerate learning from only the samples labelled through user-interactions, a patch-based approach is used for training the network. Moreover, we use weighted cross-entropy loss to address the class imbalance that may result from user-interactions. During online inference, the learned network is applied to the whole input volume using a fully convolutional approach. We compare our proposed method with state-of-the-art and show that it outperforms existing methods on the task of annotating lung lesions associated with COVID-19, achieving 16% higher Dice score while reducing execution time by 3$    imes$ and requiring 9000 lesser scribbles-based labelled voxels. Due to the online learning aspect, our approach adapts quickly to user input, resulting in high quality segmentation labels. Source code will be made available upon acceptance. 
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
<li>
<p><div class="None poster">
    <span class="title">
      <a href="papers/I4.html">EfficientCellSeg: Efficient Volumetric Cell Segmentation Using Context Aware Pseudocoloring</a>
    </span>
    <span class="authors"> Royden Wagner, Karl Rohr</span>
    <ul class="links">
      <li><a class="toggle_visibility" data-selector=".abstract" data-level="3">abstract</a></li><li><a href="https://openreview.net/pdf?id=KnJsGdhx1kH">pdf</a></li><li><a href="https://openreview.net/forum?id=KnJsGdhx1kH">reviews</a></li></ul><span class="abstract">
      Volumetric cell segmentation in fluorescence microscopy images is important to study a wide variety of cellular processes. Applications range from the analysis of cancer cells to behavioral studies of cells in the embryonic stage. Like in other computer vision fields, most recent methods use either large convolutional neural networks (CNNs) or vision transformer models (ViTs). Since the number of available 3D microscopy images is typically limited in applications, we take a different approach and introduce a small CNN for volumetric cell segmentation. Compared to previous CNN models for cell segmentation, our model is efficient and has an asymmetric encoder-decoder structure with very few parameters in the decoder. Training efficiency is further improved via transfer learning. In addition, we introduce Context Aware Pseudocoloring to exploit spatial context in z-direction of 3D images while performing volumetric cell segmentation slice-wise. We evaluated our method using different 3D datasets from the Cell Segmentation Benchmark of the Cell Tracking Challenge. Our segmentation method achieves top-ranking results while our CNN model has an up to 25x lower number of parameters than other top-ranking methods.
      <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span></div> </p>
</li>
</ul>
</div>