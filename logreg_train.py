"""
Script to train one-vs-all logistic regression
It saves models weights in separate files
"""
import numpy as np
import pandas as pd
import argparse
from model import LogisticRegressionOVR
from data_describer import read_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help="datasets to train")
    parser.add_argument('-v', action='store_true', help="visualize cost/iteration", default=False)
    parser.add_argument('-n', action='store', help="number of iteration", type=int, default=30000)
    args = parser.parse_args()

    hptrain = read_file(args.file)
    logreg = LogisticRegressionOVR(data=hptrain, v=args.v, n_iter=args.n, prediction=False)
    weights = logreg.fit()

    """Convert list of tuples to a dictionary"""
    weights_dict = {house: w for (w, house) in weights}

    """Save the weights in an npy file"""
    np.save("weights.npy", weights_dict)

    print(f"Weights saved in 'weights.npy',\nAccuracy: {'{:.2f}'.format(logreg.score() * 100)} %")

    """Convert the weights to a Pandas DataFrame"""
    weights_df = pd.DataFrame(weights, columns=['Feature', 'Weight'])

    """Save the DataFrame to a CSV file"""
    weights_df.to_csv("weights.csv", index=False)