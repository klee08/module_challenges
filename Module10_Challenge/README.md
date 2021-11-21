# Crypto Investments Portfolio Proposal
In order to propose a novel approach to assebmling cryptocurrencies invesmtent portfolio, 
comparing their historical performance and clustering cyptocurrencies into groups based in different time periods by using unsupervised learning:
* Find the Best Value for k Using the Original Data
* Cluster Cryptocurrencies with K-means Using the Original Data
* Optimize Clusters with Principal Component Analysis
* Find the Best Value for k Using the PCA Data
* Cluster the Cryptocurrencies with K-means Using the PCA Data
* Visualize and Compare the Results



# Technologies
using primarily sklearn for the unsupervised learning analysis - 1. KMeans(cluster), 2. PCA(decomposition), 3. Preprocessing(StandardScaler), as well as 
pandas data frame and plot visualization(hvplot) to visualize and compare results.

# Installation Guide
For this project modeule: we need the following dependencies:
Step 1: Install scikit-learn:
```
pip install -U scikit-learn
```
Step 2: Install hvPlot
```
conda install -c pyviz hvplot
 ```
# Usage
To run this project load the jupyter notebook cypto_investments.ipynb and run.
libaray: 
import hvplot.pandas
from path import Path
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
 
# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
