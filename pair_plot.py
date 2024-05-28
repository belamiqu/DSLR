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
    # after see the pair plot, histogram, scatterplot I decide to move up best hand
    # , care of magic creature, charms  and astronomy
    data = data.drop(['Best Hand', 'Care of Magical Creatures', 'Charms', 'Astronomy'], \
                     axis=1)

    sns.pairplot(data, hue="Hogwarts House", height=1, diag_kind='hist')
    plt.tight_layout()  # Adjust the layout
    plt.show()


if __name__ == "__main__":
    main()