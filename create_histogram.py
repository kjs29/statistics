import matplotlib.pyplot as plt

def plot_histogram(data, bins=45, title='Histogram', xlabel='Value', ylabel='Frequency'):
    """
    Plots a histogram for the given data.

    Parameters:
    - data: list or array-like, the data to plot.
    - bins: int, the number of bins for the histogram (default is 45).
    - title: str, the title of the histogram (default is 'Histogram').
    - xlabel: str, the label for the x-axis (default is 'Value').
    - ylabel: str, the label for the y-axis (default is 'Frequency').
    """
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()