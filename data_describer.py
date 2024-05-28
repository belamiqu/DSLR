import csv
import numpy as np
import pandas as pd
import sys

# def load_csv(filename):
#     dataset = list()
#     with open(filename) as csvfile:
#         reader = csv.reader(csvfile)
#         try:
#             for _ in reader:
#                 row = list()
#                 for value in _:
#                     try:
#                         value = float(value)
#                     except:
#                         if not value:
#                             value = np.nan
#                     row.append(value)
#                 dataset.append(row)
#         except csv.Error as e:
#             print(f'file {filename}, line {reader.line_num}: {e}')
#     return np.array(dataset, dtype=object)

def load_csv(filename):
    dataset = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            processed_row = []
            for value in row:
                try:
                    processed_row.append(float(value))
                except ValueError:
                    processed_row.append(np.nan if value == '' else value)
            dataset.append(processed_row)
    return np.array(dataset, dtype=object)

def read_file(filname):
    try:
        data = pd.read_csv(filname)
    except:
        sys.exit("File doesn't exist")

    """Remove unwanted columns"""   
    data = data.drop(['First Name', 'Last Name', 'Birthday', 'Index'], axis=1)

    """Map 'Best Hand' to numeric values"""

    data['Best Hand'] = data['Best Hand'].map({'Right': 0, 'Left': 1})

    """Fill missing values ​​with the mean of each column, except 'Hogwarts House'"""

    for key in data:
        if (key != "Hogwarts House"):
            data.fillna(value={key: data[key].mean()}, inplace=True)
    return (data)

def count_(X):
    try:
        X = X.astype('float')
        X = X[~np.isnan(X)]
        return len(X)
    except:
        return len(X)

def mean_(X):
    total = 0
    for x in X:
        if np.isnan(x):
            continue
        total = total + x
    return total / len(X)

def std_(X):
    mean = mean_(X)
    total = 0
    for x in X:
        if np.isnan(x):
            continue
        total = total + (x - mean) ** 2
    return (total / len(X)) ** 0.5

def min_(X):
    min_value = X[0]
    for x in X:
        val = x
        if val < min_value:
            min_value = val
    return min_value

def max_(X):
    min_value = X[0]
    for x in X:
        val = x
        if val > min_value:
            min_value = val
    return min_value

def percentile_(X, p):
    X.sort()
    k = (len(X) - 1) * (p / 100)
    f = np.floor(k)
    c = np.ceil(k)

    if f == c:
        return X[int(k)]

    d0 = X[int(f)] * (c - k)
    d1 = X[int(c)] * (k - f)
    return d0 + d1

def describe_data(data):
    description = {
        'Count': [],
        'Mean': [],
        'Std': [],
        'Min': [],
        '25%': [],
        '50%': [],
        '75%': [],
        'Max': []
    }
    
    for column in data.columns:
        if data[column].dtype in [np.float64, np.int64]:
            description['Count'].append(count_(data[column]))
            description['Mean'].append(mean_(data[column]))
            description['Std'].append(std_(data[column]))
            description['Min'].append(min_(data[column]))
            description['25%'].append(percentile_(data[column], 25))
            description['50%'].append(percentile_(data[column], 50))
            description['75%'].append(percentile_(data[column], 75))
            description['Max'].append(max_(data[column]))
        else:
            description['Count'].append(np.nan)
            description['Mean'].append(np.nan)
            description['Std'].append(np.nan)
            description['Min'].append(np.nan)
            description['25%'].append(np.nan)
            description['50%'].append(np.nan)
            description['75%'].append(np.nan)
            description['Max'].append(np.nan)
    
    desc_df = pd.DataFrame(description, index=data.columns)
    return desc_df

