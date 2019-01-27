import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
	
	titanic_data=pd.read_csv('../data/train.csv')
	
	pd.scatter_matrix(titanic_data[["Age", "Fare", "Pclass"]], figsize = (10,10))
	plt.savefig("../latex/figs/figure_1.png")

	t_agenan = titanic_data.loc[np.isnan(titanic_data["Age"])]
	t_agenan_c1 = t_agenan[t_agenan["Pclass"] == 1].index
	t_agenan_c2 = t_agenan[t_agenan["Pclass"] == 2].index
	t_agenan_c3 = t_agenan[t_agenan["Pclass"] == 3].index
	titanic_data.set_value(t_agenan_c1, "Age", 42)
	titanic_data.set_value(t_agenan_c2, "Age", 26.5)
	titanic_data.set_value(t_agenan_c3, "Age", 24)

	pd.scatter_matrix(titanic_data[["Age", "Fare", "Pclass"]], figsize = (10,10))
	plt.savefig("../latex/figs/figure_2.png")

	plt.scatter(titanic_data["Pclass"], titanic_data["Fare"])
	plt.savefig("../latex/figs/figure_3.png")
	[a, b] = np.polyfit(titanic_data["Pclass"], titanic_data["Fare"], deg = 1)

	fig, ax = plt.subplots()
	ax.scatter(titanic_data["Pclass"], titanic_data["Fare"])
	fitline1 = b + (a * titanic_data["Pclass"])
	ax.plot(titanic_data["Pclass"], fitline1, "r--")
	plt.savefig("../latex/figs/figure_4.png")

	plt.scatter(titanic_data["Pclass"], titanic_data["Age"])
	plt.savefig("../latex/figs/figure_5.png")
	[a1, b1] = np.polyfit(titanic_data["Pclass"], titanic_data["Age"], deg = 1)
		
	fig, ax = plt.subplots()
	ax.scatter(titanic_data["Pclass"], titanic_data["Age"])
	fitline2 = b1 + (a1 * titanic_data["Pclass"])
	ax.plot(titanic_data["Pclass"], fitline2, "r--")
	plt.savefig("../latex/figs/figure_6.png")

	plt.scatter(titanic_data["Age"], titanic_data["Fare"])
	plt.savefig("../latex/figs/figure_7.png")
	[a2, b2] = np.polyfit(titanic_data["Age"], titanic_data["Fare"], deg = 1)

	fig, ax = plt.subplots()
	ax.scatter(titanic_data["Age"], titanic_data["Fare"])
	fitline3 = b2 + (a2 * titanic_data["Age"])
	ax.plot(titanic_data["Age"], fitline3, "r--")
	plt.savefig("../latex/figs/figure_8.png")

