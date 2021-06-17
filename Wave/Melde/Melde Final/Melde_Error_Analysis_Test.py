#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
variable = pd.read_csv("Melde_Error_Analysis.csv")
New = variable.to_numpy()
#print(New)
X = variable["x"]
Y = variable["y"]
M = variable["Load M(g)"]
M_String = variable["Mass of string"]
No_Loops = variable["No. of Loops(P)"]
del_M = variable["del_M"]
del_l = variable["del_l"]
M_p = variable["Mass of Pan"]
L_Tr = variable["Length_one _loop_Transverse I = l/P(CM)"]
L_Long = variable["Length of one loop Longitudinal I = l/P(CM)"]
M_unit_length = variable["mass per unit length"]
L_string = variable["Length of string"]
n1,n2 = New.shape
#del_M = 0.01
#del_l = 0.1
#print(n1,n2)
#Error Analysis

for n in range(7):
    for i in M:
        for j in L_Tr:
            log_X = del_M/M + del_M/M_p
            log_Y = 2*del_l/L_Tr
            error_in_M_unit_length = del_M/M_String + del_l/L_string
            error_in_slope = ((n*log_X + n*log_Y) + (log_X + log_Y)) + ((n*2*log_X) + (log_X)*2*n)
            error_in_frequency = 1/2*(error_in_M_unit_length + error_in_slope) 
#print(error_in_slope)
print("Average Error in Mass per unit length ",np.sum(error_in_M_unit_length)/len(L_Tr))
print("Average Error in Slope for transverse motion = ",np.sum(error_in_slope)/len(L_Tr))          
#print(error_in_frequency)
print("Average Error in Frequency for Transverse motion ",np.sum(error_in_frequency)/len(L_Tr))

for n in range(7):
    for i in M:
        for j in L_Long:
            log_X = del_M/M + del_M/M_p
            log_Y = 2*del_l/L_Long
            error_in_M_unit_length = del_M/M_String + del_l/L_string
            error_in_slope = ((n*log_X + n*log_Y) + (log_X + log_Y)) + ((n*2*log_X) + (log_X)*2*n)
            error_in_frequency = 1/2*(error_in_M_unit_length + error_in_slope) 
#print(error_in_slope)
print("Average Error in Slope for Longitudinal motion = ",np.sum(error_in_slope)/len(L_Tr))          
#print(error_in_frequency)
print("Average Error in Frequency for Longitudinal motion ",np.sum(error_in_frequency)/len(L_Tr))


# In[ ]:




