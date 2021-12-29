# 14. Machine Learning Trading Bot
Enhance the existing trading signals with machine learning algorithms that can adapt to new data 
in order to improve the existing algorithmic trading systems and maintain the firm’s competitive advantage in the market
* 1. Establish a Baseline Performance
* 2. Tune the Baseline Trading Algorithm
* 3. Evaluate a New Machine Learning Classifier
* 4. Create an Evaluation Report
_____________________________________________________
# README ANSWERS
1. Establish a Baseline Performance
Write your conclusions about the performance of the baseline trading algorithm in the README.md file that’s associated with your GitHub repository. Support your findings by using the PNG image that you saved in the previous step.
              precision    recall  f1-score   support

        -1.0       0.88      0.14      0.25        49
         1.0       0.65      0.99      0.78        79

    accuracy                           0.66       128
   macro avg       0.76      0.57      0.51       128
weighted avg       0.74      0.66      0.58       128


ANSWER: based on given range 2015-04-02 ~ 2015.07-02 w/ SVM default, accuracy was 66% with low 1.0 precision (65%) and 
low -1.0 recall (14%). Besides short period in late April of 2015, Strategy Return was lower than Actual Return =
The model is not helpful at all to maximize the profit. 

2. Tune the Baseline Trading Algorithm
Step 1: Tune the training algorithm by adjusting the size of the training dataset.
To do so, slice your data into different periods. Rerun the notebook with the updated parameters, and record the results in your README.md file.
1) Shorter - 2 months:
2015-04-02 15:00:00
2015-06-02 15:00:00
              precision    recall  f1-score   support

        -1.0       0.89      0.27      0.41        30
         1.0       0.69      0.98      0.81        49

    accuracy                           0.71        79
   macro avg       0.79      0.62      0.61        79
weighted avg       0.76      0.71      0.66        79

2) longer Period - 9 months:
2015-04-02 15:00:00
2016-01-02 15:00:00
              precision    recall  f1-score   support

        -1.0       0.57      0.21      0.31       239
         1.0       0.56      0.86      0.68       279

    accuracy                           0.56       518
   macro avg       0.56      0.54      0.49       518
weighted avg       0.56      0.56      0.51       518
Answer the following question: What impact resulted from increasing or decreasing the training window?
ANSWER: By changing rolling windows (one or both windows) for 9 months period or longer, it's making accuracy/performance worse

Step 2: Tune the trading algorithm by adjusting the SMA input features.
Adjust one or both of the windows for the algorithm. Rerun the notebook with the updated parameters, and record the results in your README.md file.
# Set the short window and long window
short_window = 5
long_window = 40

2015-04-02 15:00:00
2016-01-02 15:00:00
              precision    recall  f1-score   support

        -1.0       0.57      0.21      0.31       239
         1.0       0.56      0.86      0.68       279

    accuracy                           0.56       518
   macro avg       0.56      0.54      0.49       518
weighted avg       0.56      0.56      0.51       518

ANSWER: By changing rolling windows (one or both windows) for given 3 or 9 months data period, making accuracy/performance worse

### Step 3: Choose the set of parameters that best improved the trading algorithm returns. 
              precision    recall  f1-score   support

        -1.0       0.81      0.35      0.49        49
         1.0       0.70      0.95      0.81        79

    accuracy                           0.72       128
   macro avg       0.76      0.65      0.65       128
weighted avg       0.74      0.72      0.68       128

ANSWER: By chaning SVM kernel from linear to rbf with C=7.0 with 3 month data sample
overall Accuracy including recall and precision was improved slightly from 66% to 72%. 

# Technologies
* 1. StandardScaler removes the mean and scales each feature/variable to unit variance
* 2. SVC classifier model - Supports Vector Machines (SVMs),a set of supervised learning methods used for classification, regression and outliers detection.
  The advantages of support vector machines are:
    - Effective in high dimensional spaces.
    - Still effective in cases where number of dimensions is greater than the number of samples.
    - Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
    - Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
  The disadvantages of support vector machines include:
    - If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
    - SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

* 3. AdaBoost classifier - An AdaBoost classifier is a meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset but where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.
   AdaBoost can be used both for classification and regression problems:
    - For multi-class classification, AdaBoostClassifier implements AdaBoost-SAMME and AdaBoost-SAMME.R
    - For regression, AdaBoostRegressor implements AdaBoost.R2
    
# Installation Guide
For this project modeule: we need the following dependencies:
  pip install --upgrade scikit-learn

# Usage
To run this project load the jupyter notebook forecasting_net_prophet.ipynb and run.
Required libaray: 
* import pandas as pd
* import numpy as np
* from pathlib import Path
* import hvplot.pandas
* import matplotlib.pyplot as plt
* from sklearn import svm
* from sklearn.preprocessing import StandardScaler
* from pandas.tseries.offsets import DateOffset
* from sklearn.metrics import classification_report
* from sklearn.ensemble import AdaBoostClassifier 
# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
