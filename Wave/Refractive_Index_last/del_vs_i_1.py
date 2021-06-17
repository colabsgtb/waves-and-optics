import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
def rad(x):
    return (x * np.pi/180)

def func(i,A,n):
    return i - A + np.arcsin(n * np.sin(A - np.arcsin(np.sin(i)/n)))

def min_dev(y_cal,xlim):
    list = []
    for j in range(len(y_cal)):
        xlim[j]
        if y_cal[j] == np.min(y_cal):
            list.append(xlim[j])
            list.append(np.min(y_cal))
    mini = np.array(list)
    print("\nCoordinates of minima of the graph (x,y):\n",mini)
    print("Angle of minimum deviation from Graph is:\n",min(y_cal)) 
    return mini
    

if __name__ == "__main__":
    datax = np.array([30,35,40,45,50,55,60])
    mean_dev_deg = np.array([47,41,38,37,37,37,39])
    mean_dev_min = np.array([0,0,30,30,15,30,0])
    datay= np.array((mean_dev_deg) + (mean_dev_min/60))
    xlim = np.linspace(30,60,100)
    print(datay) 
    popt, pcov = curve_fit(func,rad(datax),rad(datay))
    print("\nAngle of prism and Refractive index of the prism from fitting:\n",popt,"\n")
    y_cal = np.array(func(rad(xlim),*popt)) * 180/np.pi
    print(y_cal)
    mini = min_dev(y_cal,xlim)
    fig1, ax1 = plt.subplots() 
    plt.style.use("ggplot")
    plt.title("Graph between $\delta$ vs i")
    ax1.set_xlabel('Angle of incidence (i)')
    ax1.set_ylabel('Angle of deviation ($\delta$)')
    ax1.scatter(datax,datay,color = "b",label = "Experimental data")
    ax1.scatter(mini[0],mini[1],c = "g",label = "Minimum deviation point")
    ax1.plot(xlim,np.array(func(rad(xlim),*popt) * 180/np.pi), color = "r",label = "Fitting curve")
    plt.legend()
    plt.show()
