"""
Display information for all numerical features
    
"""
import numpy as np
import pandas as pd
import argparse
from data_describer import count_, mean_, std_, min_, percentile_, max_, load_csv, read_file

"""To display dataframe exactly as in the subject . Only numerical values, transposed texts and first four columns of Features"""

# def describe_dataset(data):
#    # Rename the subject columns
#     new_columns = {'Arithmancy': 'Feature 1',
#                    'Astronomy': 'Feature 2',
#                    'Herbology': 'Feature 3',
#                    'Defense Against the Dark Arts': 'Feature 4'}
#     data = data.rename(columns=new_columns)

#     # Select only the first four features
#     selected_features = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']
#     data = data[selected_features]
    
#    # Create a DataFrame to store the statistics
#     stats = pd.DataFrame(index=['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max'])
    
#     for feature in selected_features:
#         column_data = data[feature].dropna().values
#         stats[feature] = [
#             count_(column_data),
#             mean_(column_data),
#             std_(column_data),
#             min_(column_data),
#             percentile_(column_data, 25),
#             percentile_(column_data, 50),
#             percentile_(column_data, 75),
#             max_(column_data)
#         ]
    
#     # Print the transposed DataFrame for the desired format
#     print(stats)

# def describe(filename):
#     data = read_file(filename)
#     describe_dataset(data)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Describe a dataset with basic statistics.")
#     parser.add_argument("dataset", type=str, help="Path to the input dataset CSV file")
#     args = parser.parse_args()
#     describe(args.dataset)

"""To display a dataframe with only numerical values, transposed axes and first four Subjects."""
# import numpy as np
# import pandas as pd
# import argparse
# from data_describer import count_, mean_, std_, min_, percentile_, max_, read_file

# def describe_dataset(data):
#     # Select only the first four features based on original column names
#     selected_features = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts']
#     data = data[selected_features]
    
#     # Create a DataFrame to store the statistics
#     stats = pd.DataFrame(index=['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max'])
    
#     for feature in selected_features:
#         column_data = data[feature].dropna().values
#         stats[feature] = [
#             count_(column_data),
#             mean_(column_data),
#             std_(column_data),
#             min_(column_data),
#             percentile_(column_data, 25),
#             percentile_(column_data, 50),
#             percentile_(column_data, 75),
#             max_(column_data)
#         ]
    
#     # Print the transposed DataFrame for the desired format
#     print(stats)

# def describe(filename):
#     data = read_file(filename)
#     describe_dataset(data)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Describe a dataset with basic statistics.")
#     parser.add_argument("dataset", type=str, help="Path to the input dataset CSV file")
#     args = parser.parse_args()
#     describe(args.dataset)

"""To show the dataframe from a complete csvfile with all types of values ​​and with all subjects"""

def describe(filename):
    dataset = load_csv(filename)
    features = dataset[0]
    dataset = dataset[1:]
    print(
        f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    for i in range(0, len(features)):
        print(f'{features[i]:15.15}', end=' |')
        try:
            data = np.array(dataset[:, i], dtype=float)
            data = data[~np.isnan(data)]
            if not data.any():
                raise Exception()

            print(f'{count_(data):>12.4f}', end=' |')
            print(f'{mean_(data):>12.4f}', end=' |')
            print(f'{std_(data):>12.4f}', end=' |')
            print(f'{min_(data):>12.4f}', end=' |')
            print(f'{percentile_(data, 25):>12.4f}', end=' |')
            print(f'{percentile_(data, 50):>12.4f}', end=' |')
            print(f'{percentile_(data, 75):>12.4f}', end=' |')
            print(f'{max_(data):>12.4f}')
        except:
            print(f'{count_(dataset[:, i]):>12.4f}', end=' |')
            print(f'{"No numerical value to display":>60}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="input dataset")
    args = parser.parse_args()
    describe(args.dataset)
