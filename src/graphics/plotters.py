import matplotlib.pyplot as plt


from typing import Tuple, List, Union, Any, Optional


def plot_bar(
    axis: Tuple[Any, Any],
    figsize: Tuple[int, int],
    title: str,
    labels: List[str],
    is_barh: Optional[bool] = False,
) -> None:
    plt.figure(figsize=figsize)
    (
        plt.barh(axis[0], axis[1], color="blue")
        if is_barh
        else plt.bar(axis[0], axis[1], color="blue")
    )
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_pie(
    axis: Tuple[Any, Any],
    figsize: Tuple[int, int],
    title: str,
) -> None:
    plt.figure(figsize=figsize)
    plt.pie(
        axis[1],
        labels=list(map(lambda x: x.upper(), axis[0])),
        autopct="%1.1f%%",
        startangle=140,
        colors=["pink", "skyblue"],
    )
    plt.title(title)
    plt.axis("equal")
    plt.show()


def plot_hist(
    figsize: Tuple[int, int],
    title: str,
    labels: List[Union[str, int]],
    content: List[int],
) -> None:
    plt.figure(figsize=figsize)
    plt.hist(content, bins=20, edgecolor="black", alpha=0.7)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.tight_layout()
    plt.show()
