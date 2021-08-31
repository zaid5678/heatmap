import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def generate_heatmap(data):
    sns.set()
    ax = sns.heatmap(data)
    plt.show()

data = pd.DataFrame("filename.csv")

