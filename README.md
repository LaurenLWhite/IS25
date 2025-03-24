## Speech reference intervals: an assessment of feasibility in depression symptom severity prediction
This is the repository for...

### Primary authors
- Lauren L. White $^{1, 2}$
- Nicholas Cummins $^{1, 2}$
- Ewan Carr $^{1}$

### Abstract 
Major Depressive Disorder (MDD) is a prevalent mental disorder. Combining speech features and machine learning has promise for predicting MDD, but interpretability is crucial for clinical applications. Reference intervals (RIs) represent a typical range for a speech feature in a population. RIs could increase interpretability and help clinicians identify deviations from norms. They could also replace conventional speech features in machine learning models. However, no work has yet assessed the feasibility of speech RIs in MDD. We generated and compared RIs from three reference datasets varying in size, elicitation prompt, and health information. We then calculated deviations from each RI set for people with MDD to compare performance on a depression symptom severity prediction task. Our RI-based models trained with demographic data performed similarly to each other and equivalent models using conventional features or demographics only, demonstrating the value of RI-derived features.

------

To replicate or develop your own version of the analyses from this paper, you will need to reference this and two other repositories. Some steps are also for the user to complete separately. One of the reference datasets (TCS) and the depression dataset (RADAR-MDD) for this work are not publicly available. Therefore, code is only presented for CLAC and Common Voice, which are publicly available. A synthetic depression dataset with the necessary features has been generated as an example. This synthetic_mdd datsaset is an example dataset _only_. 

The overall steps are outlined in the below figure, then bullet points outline the specific steps and source for this step (i.e. this repository, one of the other repositories, or user).

<img width="468" alt="image" src="https://github.com/user-attachments/assets/4f480a97-dc4d-45cd-b85a-0b7e9a1d3910" />

#### The repositories:
- Botelho: https://github.com/mcatarinatb/reference-speech-characterization
- Cummins: https://github.com/nickcummins41/VoiceSpeechHealth
- White (current): https://github.com/laurenwhite99/IS25

#### Specific steps & sources for each step
1. Pre-processing (user)
2. Feature extraction (Cummins)
3. Outlier removal (Botelho)
4. Sex partitioning (user)
5. Non-parametric RI estimation (Botelho)
6. Deviation score computation (White)
7. Overlap calculation (White)
8. Prediction (White)


### Secondary authors
- Judith Dineley $^{1}$
- Catarina Botelho $^{3}$
- Pauline Conde $^{1}$
- Faith Matcham $^{4}$
- Carolin Oetzmann $^{1}$
- Amos A. Folarin $^{1, 5}$
- George Fairs $^{2}$
- Agnes Norbury $^{2}$
- Stefano Goria $^{2}$
- Srinivasan Vairavan $^{6}$
- Til Wykes $^{1, 5}$
- Richard J.B. Dobson $^{1, 7}$
- Vaibhav A. Narayan $^{8}$
- Matthew Hotopf $^{1, 5}$
- Alberto Abad $^{3, 9}$
- Isabel Trancoso $^{3, 9}$
- The RADAR-CNS Consortium $^{10}$

#### Affiliations
- $^{1}$ Institute of Psychiatry, Psychology, and Neurosceince, King's College London, UK
- $^{2}$ Thymia, London, UK
- $^{3}$ INESC-ID, Portugal
- $^{4}$ School of Psychology, University of Sussex, Falmer, UK
- $^{5}$ South London and Maudsley NHS Foundation Trust, London, UK
- $^{6}$ Janssen Research and Development, LLC, Titusville, NJ, United States
- $^{7}$ Institute of Health Informatics, University College London, UK
- $^{8}$ Davos Alzheimer's Collaborative
- $^{9}$ Instituto Superior Técnico, University of Lisbon, Portugal
- $^{10}$ www.radar-cns.org



### Acknowledgements
The RADAR-CNS project has received funding from the Innovative Medicines Initiative 2 Joint Undertaking under grant agreement No 115902. This Joint Undertaking receives support from the EU’s Horizon 2020 research and innovation programme and EFPIA. This communication reflects the views of the RADAR CNS consortium, and neither IMI nor the EU and EFPIA are liable for any use that may be made of the information contained herein. We thank all RADAR-CNS patient advisory board members for contributing to the device selection procedures and providing invaluable advice throughout the study protocol design. This paper represents independent research funded by the National Institute for Health Research (NIHR) Maudsley Biomedical Research Centre at South London and Maudsley NHS Foundation Trust and King’s College London. The views expressed are those of the author(s) and not necessarily those of the NHS, NIHR, or the Department of Health and Social Care.
