import numpy as np
import pandas as pd

#Read in the data sets 
mydata1 = pd.read_excel("C:\\Users\Brian\Desktop\EECS_731\Project1\Data\People-who-visit-restaurants-in-the-us-2017-by-age.xlsx")
mydata2 = pd.read_excel("C:\\Users\Brian\Desktop\EECS_731\Project1\Data\People-who-visit-restaurants-in-the-us-2018-by-age.xlsx")

#Group the data sets with pandas
grouped = pd.merge(mydata1, mydata2, how = "outer")
#Sort the data sets 
grouped = grouped.sort_values(["Company","Age"])
#Drop a constant column
grouped = grouped.drop(columns=["Country"])
#Display the first 60 results
print(grouped.head(60))
#Display total size of the data set
print(grouped.shape)
