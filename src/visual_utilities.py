from matplotlib import pyplot as plt
from typing import List, Tuple


def plot_bar_chart(dictionary: dict) -> None:
    keys = dictionary.keys()
    values = dictionary.values()

    plt.bar(keys, values)
    plt.show()


def plot_line_graphs(
    x_values: List[int],
    dictionary: dict,
    labels: Tuple[str, str] = ("", ""),
    title: str = "",
):
    line_labels = list(dictionary.keys())
    values = list(dictionary.values())
    for ind, label in enumerate(line_labels):
        plt.plot(x_values, values[ind], label=label)
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.legend()
    plt.show()
