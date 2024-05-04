
import matplotlib.pyplot as plt
from argparse import ArgumentParser

from data_describer import HogwartsDataDescriber


def histogram(plot: plt,
              df: HogwartsDataDescriber,
              course: str,
              save_path: str):
    """
    Scatter plot for 2 courses
    :param plot: matplotlib.axes._subplots.AxesSubplot
    :param df: HogwartsDataDescriber
    :param course: course name
    :param save_path: path to save the plot
    :return: None
    """
    for house, color in zip(df.houses, df.colors):
        # choose course marks of students belonging to the house
        marks = df[course][df['Hogwarts House'] == house].dropna()

        plot.hist(marks, color=color, alpha=0.5)

    plot.set_title(course)
    plot.legend(df.houses, frameon=False)
    plot.set_xlabel('Marks')
    plot.set_ylabel('Students')

    # Save the plot as a PNG file
    plot.figure.savefig(save_path)


def show_course_marks_distribution(csv_path: str, course: str, save_path: str):
    # obtaining data for plotting
    df = HogwartsDataDescriber.read_csv(csv_path)
    _, ax = plt.subplots()

    histogram(ax, df, course, save_path)
    plt.show()


if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('--data_path',
                        type=str,
                        default='../data/dataset_train.csv',
                        help='Path to dataset_train.csv file')

    parser.add_argument('--course',
                        type=str,
                        default='Care of Magical Creatures',
                        help='Name of the course to plot')

    parser.add_argument('--save_path',
                        type=str,
                        default='plot.png',
                        help='Path to save the plot')

    args = parser.parse_args()

    show_course_marks_distribution(args.data_path, args.course, args.save_path)