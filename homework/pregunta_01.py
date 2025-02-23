"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de colores, orden y grosores
COLORS = {
    "Television": "dimgray",
    "Newspaper": "grey",
    "Internet": "tab:blue",
    "Radio": "lightgrey",
}

ZORDER = {
    "Television": 1,
    "Newspaper": 1,
    "Internet": 2,
    "Radio": 1,
}

LINEWIDTHS = {
    "Television": 2,
    "Newspaper": 2,
    "Internet": 4,
    "Radio": 2,
}


def load_data(filepath):
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv(filepath, index_col=0)


def annotate_plot(df):
    """Anota los puntos iniciales y finales en el gráfico."""
    for col in df.columns:
        first_year, last_year = df.index[0], df.index[-1]
        plt.scatter(first_year, df[col][first_year], color=COLORS[col], zorder=ZORDER[col])
        plt.text(first_year - 0.2, df[col][first_year], f"{col} {df[col][first_year]}%", ha="right", va="center", color=COLORS[col])

        plt.scatter(last_year, df[col][last_year], color=COLORS[col])
        plt.text(last_year + 0.2, df[col][last_year], f"{df[col][last_year]}%", ha="left", va="center", color=COLORS[col])


def plot_news_data(df):
    """Genera y configura el gráfico de tendencias de noticias."""
    plt.figure()

    for col in df.columns:
        plt.plot(df[col], label=col, color=COLORS[col], zorder=ZORDER[col], linewidth=LINEWIDTHS[col])

    plt.title("How people get their news", fontsize=16)
    plt.xticks(ticks=df.index, labels=df.index, ha="center")

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    annotate_plot(df)
    plt.tight_layout()


def save_plot(output_path):
    """Guarda el gráfico en la ruta especificada."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)


def pregunta_01():
    """Función principal que ejecuta la generación del gráfico."""
    input_file = "files/input/news.csv"
    output_file = "files/plots/news.png"

    df = load_data(input_file)
    plot_news_data(df)
    save_plot(output_file)

pregunta_01
