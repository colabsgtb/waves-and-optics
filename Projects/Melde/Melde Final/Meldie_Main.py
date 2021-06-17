#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
variable = pd.read_csv("Melde_Final_For_LSF.csv")
New = variable.to_numpy()
#print(New)
X = variable["x"]
Y = variable["y"]
X_Long = variable["x_long"]
Y_Long = variable["y_long"]
m = variable["mass per unit length"]

n1,n2 = New.shape
#print(n1,n2)
if len(X) == len(Y) and n1 >3:
    
    sigma_xy = np.sum(X*Y)
    sigma_x = np.sum(X)
    sigma_y = np.sum(Y)
    sigma_x_sq = np.sum(X*X)
    sigma_x_whole_sq = np.sum(X)**2
    slope = (n1*sigma_xy - sigma_x*sigma_y)/(n1*sigma_x_sq - sigma_x_whole_sq)
    intercept = (sigma_x_sq * sigma_y - sigma_x * sigma_xy) / (n1 * sigma_x_sq - sigma_x**2)
    Frequency = np.sqrt(1/(slope*0.497910448))
    ycal = slope*X + intercept
    print("Slope for Transverse motion is ",slope)
    print("Intercept for Transverse motion is ",intercept)
    print("Frequency in Transverse motion is ",Frequency)
    print("Final Frequency = ",np.sqrt(1/(slope*0.497910448)))
#Curve Fitting
for i in X:
    for j in Y:
        plot1 = plt.figure(1)
        plt.scatter(X,Y)
        plt.plot(X,ycal)
        plt.title("Curve Fitting for Transverse Standing Waves")
        plt.xlabel("Tension")
        plt.ylabel("$\lambda^2$")
if len(X) == len(Y) and n1 >3:
    sigma_xy = np.sum(X_Long*Y_Long)
    sigma_x = np.sum(X_Long)
    sigma_y = np.sum(Y_Long)
    sigma_x_sq = np.sum(X_Long*X_Long)
    sigma_x_whole_sq = np.sum(X_Long)**2
    slope = (n1*sigma_xy - sigma_x*sigma_y)/(n1*sigma_x_sq - sigma_x_whole_sq)
    intercept = (sigma_x_sq * sigma_y - sigma_x * sigma_xy) / (n1 * sigma_x_sq - sigma_x**2)
    Frequency = np.sqrt(4/(slope*0.497910448))
    ycal = slope*X + intercept
    print("Slope for Longitudinal motion is", slope)
    print("Intercept for Longitudinal motion is",intercept)
    print("Frequency in Longitudinal motion is ",Frequency)
    print("Final Frequency = ",np.sqrt(4/(slope*0.497910448)))
for i in X_Long:
    for j in Y_Long:
        plot2 = plt.figure(2)
        plt.scatter(X_Long,Y_Long)
        plt.plot(X_Long,ycal)
        plt.title("Curve Fitting for Longitudinal Standing Waves")
        plt.xlabel("Tension")
        plt.ylabel("$\lambda^2$")


# In[ ]:





# In[ ]:





# In[ ]:




