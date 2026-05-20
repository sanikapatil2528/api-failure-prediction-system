import matplotlib.pyplot as plt


def plot_metrics(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["cpu"],label="CPU")
    plt.plot(df["latency"],label="Latency")
    plt.plot(df["errors"],label="Errors")
    plt.title("System Behavior Over Time")
    plt.legend()
    plt.show()