"""
Show pair plots for all courses
"""

import seaborn as sns
import matplotlib.pyplot as plt
import sys
from data_describer import read_file


def main():
    if len(sys.argv) <= 1:
        sys.exit("No name file")
    if len(sys.argv) >= 3:
        sys.exit("too much file")
    data = read_file(sys.argv[1])

    # After seeing the pair plot, histogram, scatter plot I decided to include Best Hand,
    # Care of Magical Creatures, Transfiguration, and Astronomy.

    data = data.drop(['Best Hand', 'Care of Magical Creatures', 'Transfiguration', 'Astronomy'], axis=1)
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'] 
    colors = {'Gryffindor': 'red', 'Slytherin': 'green', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue'}
    sns.pairplot(data, hue="Hogwarts House", height=1, diag_kind='hist', palette=colors)
    plt.tight_layout()  
    plt.show()


if __name__ == "__main__":
    main()