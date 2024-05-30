"""
Show pair plots for all courses
"""

import seaborn as sns
import matplotlib.pyplot as plt
import sys
from data_describer import read_file

def main():
    if (len(sys.argv) <= 1):
        sys.exit("No name file")
    if (len(sys.argv) >= 3):
        sys.exit("too much file")
    data = read_file(sys.argv[1])

    # After see the pair plot, histogram, scatterplot I decide to move up Best hand
    # , Care of magic creature, Transfiguration  and Astronomy

    data = data.drop(['Best Hand', 'Care of Magical Creatures', 'Transfiguration', 'Astronomy'], \
                     axis=1)
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'] 
    sns.pairplot(data, hue="Hogwarts House", height=1, diag_kind='hist')
    plt.tight_layout()  
    plt.show()


if __name__ == "__main__":
    main()