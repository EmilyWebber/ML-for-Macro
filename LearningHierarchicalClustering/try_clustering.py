# from the tutorial https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import inconsistent
from scipy.cluster.hierarchy import fcluster



def step_one():
	np.random.seed(4711)
	a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
	b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
	X = np.concatenate((a, b),)
	# print X.shape
	# plt.scatter(X[:,0], X[:,1])
	# plt.show()
	return X

def step_two(X):
	Z = linkage(X, "ward")
	return Z

def check_out_iterations(Z):
	idxs = [33, 68, 62]
	plt.figure(figsize = (10, 8))
	plt.scatter(X[:,0], X[:,1])
	plt.scatter(X[idxs, 0], X[idxs, 1], c="r")
	# plt.show()

	idxs = [15, 69, 41]
	plt.scatter(X[idxs, 0], X[idxs, 1], c="r")
	# plt.show()

def plot_dendrogram(Z):
	plt.figure(figsize=(25,10))
	plt.title("Hierarchical Clustering Dendrogram")
	plt.xlabel("sample index")
	plt.ylabel("distance")
	dendrogram(Z, leaf_rotation=90., leaf_font_size=8.,)
	plt.show()

def plot_truncated_dendrogram(Z):
	plt.title("Hierarchical Clustering Dendrogram (truncated)")
	plt.xlabel("sample index")
	plt.ylabel("distance")
	dendrogram(Z, truncate_mode = "lastp", p=12, show_leaf_counts=False, leaf_rotation=90., leaf_font_size=12., show_contracted=True)
	plt.show()



def plot_dendro(Z):
	plt.title("Hierarchical Clustering Dendrogram (truncated)")
	plt.xlabel("sample index or (cluster size)")
	plt.ylabel("distance")
	dendrogram(Z, truncate_mode="lastp", p=12, leaf_rotation=90., leaf_font_size=12., show_contracted=True)
	plt.show()

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


def plot_fancy(Z):
	fancy_dendrogram(Z, truncate_mode="lastp", p=12, leaf_rotation=90., leaf_font_size=12., show_contracted=True, annotate_above=10)

	plt.show()


def add_a_cutoff(Z, max_d):
	fancy_dendrogram(Z, truncate_mode="lastp", p=12, leaf_rotation=90., leaf_font_size=12., show_contracted=True, annotate_above=10, max_d=max_d)
	plt.show()

def step_three(X):
	c = np.random.multivariate_normal([40, 40], [[20, 1], [1, 30]], size=[200, ])
	d = np.random.multivariate_normal([80, 80], [[30, 1], [1, 30]], size=[200, ])
	e = np.random.multivariate_normal([0, 100], [[100, 1], [1, 100]], size=[200, ])
	X2 = np.concatenate((X, c, d, e))
	plt.scatter(X2[:,0], X2[:,1])
	# plt.show()
	return X2

def step_four(X2):
	Z2 = linkage(X2, "ward")
	plt.figure(figsize=(10, 10))
	fancy_dendrogram(Z2, truncate_mode="lastp", p=30, leaf_rotation=90., leaf_font_size=12., show_contracted=True, annotate_above=40, max_d=170)
	# plt.show()
	return Z2

def elbow(Z2):
	last = Z2[-10:, 2]
	last_rev = last[::-1]
	idxs = np.arange(1, len(last) + 1)
	plt.plot(idxs, last_rev)

	# 2nd derivative of the distances
	acceleration = np.diff(last, 2)
	acceleration_rev = acceleration[::-1]
	plt.plot(idxs[:-2] + 1, acceleration_rev)
	plt.show()

	k = acceleration_rev.argmax() + 2
	print "clusters: ", k

def final_step(X, Z):
	max_d = 50
	clusters = fcluster(Z, max_d, criterion="distance")

	plt.figure(figsize=(10, 8))
	plt.scatter(X[:,0], X[:,1], c=clusters, cmap="prism")
	plt.show()

if __name__ == "__main__":
	X = step_one()

	Z = step_two(X)

	# X2 = step_three(X)

	# Z2 = step_four(X2)

	# elbow(Z2)

	final_step(X, Z)