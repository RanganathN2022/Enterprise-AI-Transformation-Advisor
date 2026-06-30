import matplotlib.pyplot as plt


def maturity_chart(maturity):
    """
    Generates a horizontal bar chart for AI maturity assessment.
    """

    labels = list(maturity.keys())
    values = list(maturity.values())

    fig, ax = plt.subplots(figsize=(8, 4))

    bars = ax.barh(labels, values)

    ax.set_xlim(0, 100)

    ax.set_xlabel("Score")
    ax.set_title("Enterprise AI Maturity Assessment")

    # Display percentage values at the end of each bar
    for bar in bars:
        width = bar.get_width()

        ax.text(
            width + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{int(width)}%",
            va="center",
            fontsize=10
        )

    plt.tight_layout()

    return fig

