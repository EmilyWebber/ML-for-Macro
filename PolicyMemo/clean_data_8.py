from __future__ import division
import pandas as pd
import csv
from pandasql import *
from chart_the_dendrogram import plot_dendrogram

pysqldf = lambda q: sqldf(q, globals())

def drop_na_hhincome(df):
	print "Starting off with {} rows".format(df.shape[0])
	df = df[ df["HHINCOME"] != 9999999 ]
	print "Finished up with {} rows".format(df.shape[0])
	return df

def aggregate_columns(df):
	'''
	Computing hhh income / people ratios
	'''
	df["WeightedPeople"] = df["PERNUM"] * df["PERWT"]
	df["WeightedHHIncome"] = df["HHWT"] * df["HHINCOME"]
	df["Ratio"] = df["WeightedPeople"] / df["WeightedHHIncome"]
	return df


if __name__ == "__main__":
	data = "../Data/usa_08.csv"

	df = pd.read_csv(data)

	df = drop_na_hhincome(df)

	df = aggregate_columns(df)

	# try to aggregate to state-specific county level

# df["WeightedPeople"] / df["WeightedHHIncome"]

	ildf = df[ df["STATEICP"] == 21]

	# plot_dendrogram(df[ ["WeightedPeople", "WeightedHHIncome"] ])