import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import inconsistent
from scipy.cluster.hierarchy import fcluster

def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

def plot_dendrogram(X1):
	Z1 = linkage(X1, "ward")
	plt.figure(figsize=(10, 10))
	fancy_dendrogram(Z1, truncate_mode="lastp", p=30, leaf_rotation=90., leaf_font_size=12., show_contracted=True, annotate_above=40, max_d=170)
	plt.show()



if __name__ == "__main__":

	path = "/Users/Emily/Desktop/Harris/Macroeconomics/Data/usa_00006.csv"

	df = pd.read_csv(path, nrows = 20000)

	X1 =  df.drop("EDUC", axis=1)

	plot_dendrogram(X1)