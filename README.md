# Ian Rolls' Repo
Hi, I'm a recent computer science graduate working on some personal projects and looking for work.
This is my personal Repo containing all of my projects. Hope you enjoy!

<h2> Project Map </h2>

<h3> ML PROJECTS: <br />
*Note - each corresponding folder contains any files and diagrams used. To see the main paper/project, go to the PDF/Python file that has the same name as the folder </h3>

1. WineClassification - Using chemical data and tasting quality ratings on wines to predict wine quality from chemical properties
  * Created linear and logistic regression models as well as L1/L2 regularization technique (Ridge and LASSO)
2. ClothingClassification - Using the Fashion MNST dataset to classify articles of clothing based on their image
  * Used Canny edge detector filter for additional feature selection and created KNN and Logistic Regression models
3. CancerModel - Using genetic data from ~3000 patients to predict cancer type across 7 cancers
  * Created a variety of models, including SVM, Random Forest, Linear SVM, SGG, KNN, and a Linear Neural Net
4. BiasesInCreditRiskClassification - Using loan data to create an accurate classification model for determining if someone is likely to default. We then examined biases within the model using a multiude of different techniques to examine whether machine learning should be applied to real world scenarios. We found that even when direct data on gender was not included in a model, that data was implictly contained in other features, meaning even models that have no exposure to demographic features will likely still end up biasing towards certain demographics.

<h3>OPTIMIZATION PROJECT:</h3>
This project was created for a linear and discrete optimization class, my partner and I used the GurobiPy optimization software to optimize the BART transportation schedule to minimize resource cost while still properly serving every rider who wanted to access the transit network. We were able to find the optimal frequency to run trains along each line given ridership constrants, train inventory contraints, and a base constraint that every station should have a train arriving each 15m.
