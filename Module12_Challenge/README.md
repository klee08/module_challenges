# Module 12. Credit Risk Classification
## Overview of the Analysis
1. Explain the purpose of the analysis.
- Build "Credit Risk Classification Model" that helps peer-to-peer lending services compmary to identify the credit worthiness of borrowers
- Since Healthy loans easily outnumber risky loans, using various techniques to train and evaluate models with imbalanced classes

2. Explain what financial information the data was on, and what you needed to predict.
- Given data: Sample Loan Atrributes (such as loansize, income, rate, DTI, total debt, number of opened accoutns) and Loan Status 
- Prediction: Train and Predict Credit Risk (e.g. Risky Loans) based on borrower Loan Attributes 

3. Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
-  Target Values: 
   0: 75,036 Healthy Loans 
   1:  2,500 Risky Loans
   Prediction: identify loan wheather it's healthy or risk (sample answer target: loan_status) 
4. Describe the stages of the machine learning process you went through as part of this analysis.
   1) Split the Data into Training and Testing Sets
   2) Create a Logistic Regression Model and fit the model using training data
   3) Make a predictiion using testing data
   4) Analyze model accuracy, precision, recall by using blanaced accuracy score, confusion matrix and classification report
   5) consider additional technique to overcome the imbalance problem or inaccuracy
   
5. Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).
   1. from sklearn.linear_model import LogisticRegression - Logistic Regression with Sklearn & Scikit: 
   a statistical method/ Machine Learning classification algorithm 
   for predicting binary classes (probability of a categorical dependent variable)
   2. from imblearn.over_sampling import RandomOverSampler - Random Over Sampler:
   In order to outcome imbalanced classes, RandomOverSampler is generating new samples by randomly sampling with
   replacement the current available sample classes

## Results
Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

     * Machine Learning Model 1 Fit with Given Sample data:
                       precision    recall  f1-score   support

               0       1.00      0.99      1.00     18765
               1       0.85      0.91      0.88       619

        accuracy                           0.99     19384
        macro avg       0.92      0.95      0.94     19384
     weighted avg       0.99      0.99      0.99     19384


    * Description of Model 2 Accuracy, Precision, and Recall scores.
Overral balanced accuracy score is 95.2% (Model classicication accurany is 99%) but, high-risk loan level precision[85%(of all predicted 1, 85% actually hisk risk loan) and recall: 91%(of all actual high risk loan, 91% correctly predicted as 1) and f1-score 88%] requires bit improvement (since prediction of high-risk loans is more critical than healthy loan to mitigate the risk). This might be caused by imbalance of the data ( because healthy loans easily outnumber risky loans, many samples of healthy loan while few samples of high riskloan). As a result, the classifier seems overfitting to healthy loan(0) to minimize the error during training. So better to consider additional technique to overcome the imbalance problem    


     * Machine Learning Model 2. Fit with Oversampled data:
                  precision    recall  f1-score   support

               0       1.00      0.99      1.00     18765
               1       0.84      0.99      0.91       619

        accuracy                           0.99     19384
       macro avg       0.92      0.99      0.95     19384
    weighted avg       0.99      0.99      0.99     19384



    * Description of Model 2 Accuracy, Precision, and Recall scores.
Balanced accuracy score was improved to 99% from 95.2% (Model Classification Accuracy is similar 99% level), we see improvement on recall of high-risk loan from 91% to 99% with oversampled data. We have much better recall prediction as 1 of all records are actually high risk loans that would be helpful while precision of 1 has beeen decreased 1% as trade off. so oversample data was helpful to overcome imbalance problem bit and provide the better model to identify the creditworthiness of borrowers


## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
Model #2 Fit with Oversampled data because from calssification report, both balanced accuracy (99% and from 95.2%), recall of high-risk loan has been improved to 99% from 91% that will be help us to indentify borrower credit risk in advance and creditworthiness of borrowers while precision got trade-off 1% lower 

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )
Yes - It's more important to predict 1 (Risky) rather than 0 (Healthy) in order to identify and filter out potential risky borrower in advance 
to reduce the loan portfolio risk and potential loss 

If you do not recommend any of the models, please justify your reasoning.
For the above, linear regression with oversampled data is recommended, but also good to considere additional technique to overcome the imbalance problem  


# Technologies
scikit-learn: Logistic regression model
imbalanced-learn: RandomOverSampler

# Installation Guide
For this project modeule: we need to install Scikit-Learn:
   pip install -U scikit-learn

# Usage
To run this project load the jupyter notebook credit_risk_resampling.ipynb:
Required libaray: 
    import numpy as np
    import pandas as pd
    from pathlib import Path
    from sklearn.metrics import balanced_accuracy_score
    from sklearn.metrics import confusion_matrix
    from imblearn.metrics import classification_report_imbalanced
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import confusion_matrix,classification_report
    from imblearn.over_sampling import RandomOverSampler
    from pathlib import Path
    import pandas as pd
    
# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
