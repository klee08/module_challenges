# 13. Neural Network Model that predicts whether applicants will be successful if funded by Alphabet Soup
Use machine learning and neural networks features and technologies in the provided dataset to create a binary classifier model 
that will predict whether an applicant will become a successful business.
* Step 1: Prepare the Data for Use on a Neural Network Model
* Step 2: Compile and Evaluate a Binary Classification Model Using a Neural Network
* Step 3: Optimize the Neural Network Model

# Technologies
* OneHotEncoder: transforms each categorical feature with n_categories possible values into n_categories binary features, with one of them 1, and all others 0
* StandardScaler removes the mean and scales each feature/variable to unit variance
* Sequential model: compile, train and build Neural Network model with a plain stack of layers where each layer has exactly one input tensor and one output tensor for machine 

# Installation Guide
For this project modeule: we need the following dependencies:
  pip install --upgrade tensorflow
  pip install --upgrade scikit-learn

# Usage
To run this project load the jupyter notebook forecasting_net_prophet.ipynb and run.
Required libaray: 
* import tensorflow as tf
* from tensorflow.keras.layers import Dense
* from tensorflow.keras.models import Sequential
* from sklearn.model_selection import train_test_split
* from sklearn.preprocessing import StandardScaler,OneHotEncoder
 
# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
