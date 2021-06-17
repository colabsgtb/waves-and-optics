#curvefiiting graph
import matplotlib.pyplot as plt
import csv
import cmath

X1 = []     #tension for transverse
Y1 = []     #lambda_sq for transverse 
X2 = []     #tension for longitudinal
Y2 = []     #lambda_sq for longitudinal

with open('melde_csv.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)       #reading the values from csv file and making list of them.
    next(csv_reader)
    for line in csv_reader:
        X1.append(line[1])
        Y1.append(line[2])
        X2.append(line[3])
        Y2.append(line[4])
        
X11 = []
for i in range(len(X1)):             #to convert elements of list from str into float
    X11.append(float(X1[i]))
    
Y11 = []
for i in range(len(Y1)):
    Y11.append(float(Y1[i]))
    
Y22 = []
for i in range(len(Y2)):
    Y22.append(float(Y2[i]))
               
X22 = []  
for i in range(len(X2)):
    X22.append(float(X2[i]))
    
#fnct for leastsquarefitting and calculations of other constants
    
def lisq(x,y):            
    Y_CAL = []
    E = []
    sum_of_residual = 0
    sum_of_residual_squares = 0
    a=len(x)
    b=len(y)
    a0 = 0
    a1 = 0
    if a==b and a>2:
        sum_xi = 0
        sum_yi = 0
        sum_xisq = 0
        sum_xiyi = 0
        sum_yisq = 0

        for i in range(a):
            sum_xi = sum_xi + x[i]
            sum_yi = sum_yi + y[i]
            sum_xisq = sum_xisq + x[i]**2
            sum_xiyi = sum_xiyi + x[i]*y[i]
            sum_yisq = sum_yisq + y[i]**2

        a0=(sum_xi * sum_yi - a * sum_xiyi)/(sum_xi **2 - a*sum_xisq)              #slope

        a1=(sum_xisq * sum_yi - sum_xi * sum_xiyi)/(a * sum_xisq - sum_xi**2)      #intercept
        
        bxy = sum_xiyi/sum_yisq   #regression coefficient of TENSION on LAMBDA SQUARE
        
        byx = sum_xiyi/sum_xisq   #regression coefficient of LAMBDA SQUARE on TENSION
        
        r = cmath.sqrt(bxy*byx)   #correlation coeffcient
        
        for i in range(a):
            Ycal = x[i]*a0 + a1
            Y_CAL.append(Ycal)
            error = Ycal - y[i]
            E.append(error)
            sum_of_residual += error   #sum of residuals
            sum_of_residual_squares += error**2  #sum of residual squares
        
        SSxx = sum_xisq - ((sum_xi)**2/a)   
        std_slope = cmath.sqrt((sum_of_residual_squares)/(SSxx * (a-2)))  #standard deviation of slope
        std_intercept = cmath.sqrt(((std_slope)**2)*(sum_xisq/a))   #standard deviation of intercept             
        
    else:
        print(" error ! check observations again")

    return a0,a1,r,bxy,byx,sum_of_residual,sum_of_residual_squares,std_slope,std_intercept,Y_CAL,E

slope_1,intercept_1,r1,RC11,RC12,SUM_RES1,SUM_RES_SQ1,STD_SLOPE1,STD_INT1,Y_CAL1,E1 = lisq(X11,Y11)      #for transverse mode
slope_2,intercept_2,r2,RC21,RC22,SUM_RES2,SUM_RES_SQ2,STD_SLOPE2,STD_INT2,Y_CAL2,E2 = lisq(X22,Y22)       #for longitudinal mode

# GRAPH FOR TRANSVERSE MODE
print("\n X AND Y IN BELOW RESULTS , REPRESENTS TENSION AND LAMBDA SQUARE RESPECTIVELY \n")
print("FOR TRANSVERSE MODE : \n","slope is: ",slope_1,"\n intercept is:",intercept_1)
print("the calculated Y for best fit is: \n",Y_CAL1)
print("the errors for  corresponding values of y is: \n",E1,"\n sum of residuals is :",SUM_RES1,"\n sum of residuals square is :",SUM_RES_SQ1)   
print("standard error in slope is :",STD_SLOPE1,"\n standard error in intercept is :",STD_INT1)
print("regression coefficient of x on y is :",RC11,"\n regression coefficient of y on x is :",RC12)
print("correlation coefficient is :",r1)
#graph
plt.title("for transverse mode")
plt.xlabel("Tension")
plt.ylabel("lambda **2 ")
plt.plot(X11,Y11,c = 'r',linewidth = 1.2,label = "experimental")
plt.plot(X11,Y_CAL1,c = 'b',linewidth = 1.2,label = "BESTFITTED")

plt.legend()
plt.scatter(X11,Y11,c='k')
plt.grid()
plt.savefig("curve1")
plt.show()

# GRAPH FOR LONGITUDINAL MODE
print("\n")
print("\n FOR LONGITUDINAL MODE : \n","slope is: ",slope_2,"\n intercept is:",intercept_2)
print("the calculated Y for best fit is: \n",Y_CAL2)
print("the errors for  corresponding values of y is: \n",E2,"\n sum of residuals is :",SUM_RES2,"\n sum of residuals square is :",SUM_RES_SQ2)   
print("standard error in slope is :",STD_SLOPE2,"\n standard error in intercept is :",STD_INT2)
print("regression coefficient of x on y is :",RC21,"\n regression coefficient of y on x is :",RC22)
print("correlation coefficient is :",r2)

#graph
plt.title("for longitudinal mode")
plt.xlabel("Tension")
plt.ylabel("lambda **2 ")
plt.plot(X22,Y22,c = 'r',linewidth = 1.2,label = "experimental")
plt.plot(X22,Y_CAL2,c = 'b',linewidth = 1.2,label = "BESTFITTED")

plt.legend()
plt.scatter(X22,Y22,c='k')
plt.grid()
plt.savefig("curve2")
plt.show()

