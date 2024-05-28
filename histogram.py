import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_describer import read_file
import argparse

def split_data_by_house(data, feature):
    houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']
    house_data = {house: data[data['Hogwarts House'] == house][feature].dropna() for house in houses}
    return house_data

def plot_histogram(ax, house_data, feature):
    colors = {'Gryffindor': 'red', 'Slytherin': 'green', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue'}
    for house, data in house_data.items():
        ax.hist(data, bins='auto', facecolor=colors[house], alpha=0.5, label=house)
    ax.set_title(feature)
    ax.legend(frameon=False)

def show_histogramme(data):
    features = [col for col in data.columns if col != 'Hogwarts House']
    fig, axs = plt.subplots(2, 7, figsize=(16, 10))
    axs = axs.flatten()

    for ax, feature in zip(axs, features):
        house_data = split_data_by_house(data, feature)
        plot_histogram(ax, house_data, feature)

    plt.tight_layout()
    plt.show()

def show_most_homogenous_feat(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    house_data = split_data_by_house(data, 'Care of Magical Creatures')
    plot_histogram(ax, house_data, 'Care of Magical Creatures')
    ax.set_title("Most homogenous feature: Care of Magical Creatures")
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help="Dataset to analyze")
    parser.add_argument('-all', action='store_true', help="Plot all histograms", default=False)
    args = parser.parse_args()

    data = read_file(args.file)
    if args.all:
        show_histogramme(data)
    show_most_homogenous_feat(data)

if __name__ == "__main__":
    main()
