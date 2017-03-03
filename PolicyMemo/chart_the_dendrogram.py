import pandas as pd

def read_file(path):
	with open(path, "r") as f:
		for row in f:
			print row
			quit()
		# next(f)
		# df = pd.DataFrame(l.rstrip().split() for l in f)
	# df.shape




if __name__ == "__main__":

	path = "/Users/Emily/Desktop/Harris/Macroeconomics/Data/usa_00005.csv"

	df = pd.read_csv(path)

