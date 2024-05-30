
from data_describer import load_csv
import numpy as np
import matplotlib.pyplot as plt


def scatter_plot(X, y, legend, xlabel, ylabel):
    plt.scatter(X[:327], y[:327], color='red', alpha=0.5)  # Grynffindor House
    plt.scatter(X[327:856], y[327:856], color='yellow', alpha=0.5)  # Hufflepuff House
    plt.scatter(X[856:1299], y[856:1299], color='blue', alpha=0.5)  # Ravenclaw House
    plt.scatter(X[1299:], y[1299:], color='green', alpha=0.5)  # Slytherin House

    plt.legend(legend, loc='upper right', frameon=False)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()



if __name__ == '__main__':
    
    """
    After looking at the PairPlot graph, you will notice that 
        "Astronomy" and "Defense Against the Dark Arts"
    They are the two most similar characteristics
    """

    dataset = load_csv('dataset_train.csv')
    data = dataset[1:, :]
    data = data[data[:, 1].argsort()]
    
    """"Linear Negative Correlation:when Defense Again.. increases, Astromomy tends to decrease."""

    
    # X = np.array(data[:, 7], dtype=float)  # get the "Astronomy" row data
    # y = np.array(data[:, 9], dtype=float)  # get the "Defense Again ..." row data
    # legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']  # set the "Hogwarts House"'s \
    # # names manually
    # scatter_plot(X, y, legend=legend, xlabel=dataset[0, 7], ylabel=dataset[0, 9])

    """Being bad at magic and good at Flying means 99% that you belong in Grinffindor"""

    X = np.array(data[:, 13], dtype=float)  # get the History of Magics row data
    y = np.array(data[:, 18], dtype=float)  # get the "Flying ..." row data
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']  # set the "Hogwarts House"'s \
    # names manually
    scatter_plot(X, y, legend=legend, xlabel=dataset[0, 13], ylabel=dataset[0, 18])

    """" If they get bad marks in those they belong to 99% to Grynffindor"""

    # X = np.array(data[:, 13], dtype=float)  # get the "History of Magics" row data
    # y = np.array(data[:, 14], dtype=float)  # get the "Transfiguration ..." row data
    # legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']  # set the "Hogwarts House"'s \
    # # names manually
    # scatter_plot(X, y, legend=legend, xlabel=dataset[0, 13], ylabel=dataset[0, 14])

    """Null or weak correlation"""
    # X = np.array(data[:, 6], dtype=float)  # get the "Arithmancy" row data
    # y = np.array(data[:, 16], dtype=float)  # get the "Care of Magical Creatures ..." row data
    # legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']  # set the "Hogwarts House"'s \
    # # names manually
    # scatter_plot(X, y, legend=legend, xlabel=dataset[0, 6], ylabel=dataset[0, 16])
    