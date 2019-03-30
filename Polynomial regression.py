#Importing the Libraries
      
      import pandas as pd
      import numpy as np
      import matplotlib.pyplot as plt

#Load the dataset
       dataset=pd.read_csv('# your csv file ')
       X= dataset.iloc[].values         # X is a independent variable
       y= dataset.iloc[].values         # y is a dependent variable
     
#Encoding categorical data into numerical if required
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder_X=LabelEncoder()
      
X[categorical column]=labelencoder_X.fit_transform(X[])
      
onehotencoder=OneHotEncoder(categorical_features =[])
      
X=onehotencoder.fit_transform(X).toarray()

#fitting poly_reg to the dataset
  from sklearn.preprocessing import PolynomialFeatures
  poly_reg=PolynomialFeatures(degree=4)
  X_poly=poly_reg.fit_transform(X)

  lin_reg2=LinearRegression()

  lin_reg2.fit(X_poly,y)

Visualising the result
  plt.scatter(X,y,color='red')

  plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color='blue')

  plt.title('')

  plt.xlabel('')

  plt.ylabel('')

  plt.show()
