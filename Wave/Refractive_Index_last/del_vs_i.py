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
    return mini
    

if __name__ == "__main__":
    datax = np.array([30,32.5,35,37.5,40,42.5,45,47.5,50,52.5])
    datay = np.array([40.75,39.52,38.1,37.55,37.65,36.95,36.95,37.15,37.77,38.2])
    xlim = np.linspace(30,60,100)

    popt, pcov = curve_fit(func,rad(datax),rad(datay))
    print("\nAngle of prism and Refractive index of the prism from fitting:\n",popt,"\n")
    y_cal = np.array(func(rad(xlim),*popt)) * 180/np.pi
    print(y_cal)
    mini = min_dev(y_cal,xlim)
    
    plt.style.use("ggplot")
    plt.title("Graph between $\delta$ vs i")
    plt.xlabel('Angle of incidence (i)')
    plt.ylabel('Angle of deviation ($\delta$)')
    plt.scatter(datax,datay,color = "b",label = "Experimental data")
    plt.scatter(mini[0],mini[1],c = "g",label = "Minimum deviation point")
    plt.plot(xlim,np.array(func(rad(xlim),*popt) * 180/np.pi), color = "r",label = "Fitting curve")
    plt.legend()
    plt.show()
