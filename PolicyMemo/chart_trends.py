import pandas as pd
import csv
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use("ggplot")

def chart_hhincome_in_us(seventh, others):
	plot_me = {"seventh" : []}
	for o in others:
		plot_me[o] = []

	years = [2002, 2005, 2007, 2009, 2013, 2015]

	for idx, pull in enumerate([9, 10, 11, 12, 13, 14]):
		new_list = []

		if pull == 9:
			path = "/Users/Emily/Downloads/usa_0000{}.csv".format(pull)
		else:
			path = "/Users/Emily/Downloads/usa_000{}.csv".format(pull)

		df = pd.read_csv(path)
		states = df.groupby(["STATEICP"])["HHINCOME"].mean()
		seventh_mean = states[seventh].mean()
		plot_me["seventh"].append(seventh_mean)
		for o in others:
			o_mean = states[o].mean()
			plot_me[o].append(o_mean)


if __name__ == "__main__":

	# IL, IA, MI, WI, IN
	seventh = [21, 31, 23, 25, 22]

	# Florida, Texas, Arizona, Utah, Washington, Colorado, Pennsylvania, Vermont, Maine, New York
	others = [43, 49, 61, 67, 73, 62, 14, 06, 02, 13 ]

	# chart hh income in 7th states against a selection of other states in the country
	chart_hhincome_in_us(seventh, others)