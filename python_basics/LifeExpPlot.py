# This is LifeExpPlot.py

# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# reading file
my_file = pd.read_table("gapminder.txt")

# subsetting info

Canada = my_file.loc[my_file['country'] =="Canada", :]

# plotting

Canada.plot.line(x='year',y='lifeExp', label = "Life Expectancy", figsize=(8,6))
plt.suptitle("Life Expectancy in Canada over the years", fontsize = 20)
plt.xlabel("Year", fontsize = 16)
plt.ylabel("Life Expectancy", fontsize = 16)
plt.savefig("PlotLifeExp.png")