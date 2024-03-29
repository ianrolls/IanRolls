# Ian Rolls' Project Repository
Hi, I'm a recent computer science graduate working on some personal projects and looking for work.
This is my personal Repo containing all of my projects. Hope you enjoy! Below is a list with a short description of some of my work. Thanks for checking it out!

PLEASE NOTE: All crowded subdirectories will have README files that should help navigate any confusion.

---

<h3> ML PROJECTS: <br />
*Note - each corresponding folder contains any files and diagrams used. To see the main paper/project, go to the PDF/Python file that has the same name as the folder </h3>

<h4> 1. WineClassification </h4> <br />
We used chemical data and tasting quality ratings on wines to predict wine quality from chemical properties. We developed linear and logistic regression models as well as utilizing L1/L2 regularization techniques (Ridge and LASSO). <br />
<h4> 2. ClothingClassification </h4> <br />
I used the Fashion MNST dataset to classify articles of clothing based on their image. I implemented a Canny edge detector filter for additional feature selection and developed KNN and Logistic Regression models. <br />
<h4> 3. CancerModel </h4> <br />
We used genetic data from ~3000 patients to predict cancer type across 7 cancers. This involved creating a variety of models, including SVM, Random Forest, Linear SVM, SGG, KNN, and a Linear Neural Net. <br />
<h4> 4. BiasesInCreditRiskClassification </h4> <br />
We used loan data to create an accurate classification model for determining if someone is likely to default. We then examined biases within the model using a multiude of different techniques to examine whether machine learning should be applied to real world scenarios. This project involved taking a deep dive into the inner workings of machine learning models, specifically for random forests since that was our most accurate prediction model. We found that even when direct data on gender was not included in a model, that data was implictly contained in other features, meaning even models that have no exposure to demographic features will likely still end up biasing towards certain demographics. <br />

<h4> All 4 ML projects used Python (Pandas, NumPy) for data manipulation and cleaning, the SkLearn library for ML tools, and MatPlotLib/Seaborn for data visualization </h4>

<h4> 5. Mask_CycleGAN </h4> <br />
Davidson Hackathon project which won 1st prize for best use of machine learning. Our group used TensorFlow to create a generative adversarial network that would take an image of someone with a mesk on and generate a face beneath. We used an open source Kaggle dataset containing thousands of images with corresponding photos of people with/without a mask on. Although we werent given proper time and resources to fully train our model, we created an overfitted proof of concept. <br />

---

<h3>OPTIMIZATION PROJECT:</h3>
This project was created for a linear and discrete optimization class, my partner and I used the GurobiPy optimization software to optimize the BART transportation schedule to minimize resource cost while still properly serving every rider who wanted to access the transit network. We were able to find the optimal frequency to run trains along each line given ridership constrants, train inventory contraints, and a base constraint that every station should have a train arriving each 15m.

---

<h3>DATA ANALYSIS/VISUALIZATION PROJECTS</h3>
<h4> 1. "AgingHomeAid.pdf"</h4> <br />
This was a final paper for my Econometrics class, I examined the effect of the aging baby boomer crisis on the cost of home aide. I used world bank data for home aide CPI and % population >65 years old and used a longitudinal panel regression to examine the relationship. I found that technological development offsets the increase labor cost by subsitituting labor-using processes with tech. I used Stata for all data processing, analysis, and visualization. <br />
<h4> 2. "AgingHospitalQuality.pdf"</h4> <br />
Inspired by my first Econometrics paper, I created this poster for an end-of-year research event at my university. I hypothesized that aging populations affected hospital quality in that a hospital in a county with an older population would be more equiped to deal with problems affecting older individuals. I employed a 2-stage least squares model with Average Temperature as the instrumental variable. I used Python to merge and clean hospital-level rating data and county-level population data (as well as other control variable data), Stata for the data analysis and some of the data visualization, and then I used QGIS to create maps to enhance visualization.
