# CANCER MODEL

<h4> This folder contains a PDF LaTeX project write-up, "CancerModel.pdf", a zip file containing the data, as well as three Python Notebook files. Their purposes are as such:

1. datashaping.ipynb - This file contains the code to properly unzip and reformat the data. The zip file contains a list of patient folders with their individual genetic data. We created a new datatable and appended each of the individual patient information which results in a dataframe of size (2895, 1883). This data is then stored in the "cancerDataframe.csv" file.
2. cancerModelBinary.ipynb - This file contains the code for the binarized model discribed in the paper. To summarize, instead of displaying reads per million miRNA as a number, we instead label it as a 1 if the frequency falls in the top 20% of all patients and a 0 if the frequency falls in the bottom 80% of all patients.
3. cancerModelNOFS.ipynb - This fine contains the code for the basic model with no additional feature selection (NOFS).

</h4>
