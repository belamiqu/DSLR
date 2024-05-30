"""
Script to make predictions using a trained logistic regression model and
 saving the predictions to a CSV file for further analysis.
 """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from model import LogisticRegressionOVR
from data_describer import read_file

if __name__ == "__main__":
    hptest = read_file(sys.argv[1])
    weights = np.load(sys.argv[2], allow_pickle=True).item()  

    logreg = LogisticRegressionOVR(data=hptest, prediction=True)
    predicts = logreg.predict(weights)  
    houses = pd.DataFrame({'Index': range(len(predicts)), 'Hogwarts House': predicts})
    houses.to_csv('houses.csv', index=False)
    print("Predictions saved to 'houses.csv'")
