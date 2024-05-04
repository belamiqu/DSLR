import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris


#Load the iris dataset from scikit-learn
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]
df.head()

df['species'].unique()

df.isnull().sum()